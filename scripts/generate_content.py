#!/usr/bin/env python3
"""
rashifal.online — Daily Horoscope Content Generator
Calls Claude API to generate unique daily rashifal for all 12 rashis
in both Hindi and English. Outputs JSON files consumed by the site builder.
"""

import json, os, sys, datetime, pathlib, time
import urllib.request, urllib.error

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-sonnet-4-20250514"
CONTENT_DIR = pathlib.Path(__file__).parent.parent / "content"

RASHIS = [
    {"id": "mesh",      "name_hi": "मेष",     "name_en": "Aries",       "symbol": "♈", "dates": "Mar 21 – Apr 19"},
    {"id": "vrishabh",  "name_hi": "वृषभ",    "name_en": "Taurus",      "symbol": "♉", "dates": "Apr 20 – May 20"},
    {"id": "mithun",    "name_hi": "मिथुन",   "name_en": "Gemini",      "symbol": "♊", "dates": "May 21 – Jun 20"},
    {"id": "kark",      "name_hi": "कर्क",    "name_en": "Cancer",      "symbol": "♋", "dates": "Jun 21 – Jul 22"},
    {"id": "singh",     "name_hi": "सिंह",    "name_en": "Leo",         "symbol": "♌", "dates": "Jul 23 – Aug 22"},
    {"id": "kanya",     "name_hi": "कन्या",   "name_en": "Virgo",       "symbol": "♍", "dates": "Aug 23 – Sep 22"},
    {"id": "tula",      "name_hi": "तुला",    "name_en": "Libra",       "symbol": "♎", "dates": "Sep 23 – Oct 22"},
    {"id": "vrishchik", "name_hi": "वृश्चिक", "name_en": "Scorpio",     "symbol": "♏", "dates": "Oct 23 – Nov 21"},
    {"id": "dhanu",     "name_hi": "धनु",     "name_en": "Sagittarius", "symbol": "♐", "dates": "Nov 22 – Dec 21"},
    {"id": "makar",     "name_hi": "मकर",     "name_en": "Capricorn",   "symbol": "♑", "dates": "Dec 22 – Jan 19"},
    {"id": "kumbh",     "name_hi": "कुम्भ",   "name_en": "Aquarius",    "symbol": "♒", "dates": "Jan 20 – Feb 18"},
    {"id": "meen",      "name_hi": "मीन",     "name_en": "Pisces",      "symbol": "♓", "dates": "Feb 19 – Mar 20"},
]

def call_claude(prompt: str) -> str:
    """Call Claude API and return text response."""
    body = json.dumps({
        "model": MODEL,
        "max_tokens": 2000,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    return data["content"][0]["text"]


def generate_daily(date_str: str):
    """Generate horoscope for all 12 rashis for a given date."""
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # Format date nicely
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    date_hi = dt.strftime("%d %B %Y")
    weekday_en = dt.strftime("%A")
    weekday_map = {
        "Monday": "सोमवार", "Tuesday": "मंगलवार", "Wednesday": "बुधवार",
        "Thursday": "गुरुवार", "Friday": "शुक्रवार", "Saturday": "शनिवार", "Sunday": "रविवार"
    }
    weekday_hi = weekday_map.get(weekday_en, weekday_en)

    all_rashis = []

    for rashi in RASHIS:
        print(f"  Generating: {rashi['name_en']} ({rashi['name_hi']})...")

        prompt = f"""You are an expert Vedic astrologer writing daily horoscope predictions.
Generate the daily horoscope for {rashi['name_en']} ({rashi['name_hi']}) for {date_str} ({weekday_en}).

Return ONLY valid JSON (no markdown, no backticks) with this exact structure:
{{
  "hindi": {{
    "prediction": "4-5 sentences of daily prediction in Hindi. Be specific, varied, and engaging. Mention career, health, relationships, or finance as relevant for today.",
    "lucky_number": 7,
    "lucky_color": "लाल",
    "rating": 3.5
  }},
  "english": {{
    "prediction": "4-5 sentences of daily prediction in English. Be specific, varied, and engaging. Mention career, health, relationships, or finance as relevant for today.",
    "lucky_number": 7,
    "lucky_color": "Red",
    "rating": 3.5
  }}
}}

Rules:
- rating is 1.0 to 5.0 (half-star increments)
- lucky_number is 1-99
- Each day's prediction must be UNIQUE — never repeat generic advice
- Mention the weekday's ruling planet influence naturally
- Keep tone warm, hopeful but realistic"""

        raw = call_claude(prompt)
        # Clean any markdown fencing
        clean = raw.strip()
        if clean.startswith("```"):
            clean = clean.split("\n", 1)[1]
        if clean.endswith("```"):
            clean = clean.rsplit("```", 1)[0]
        clean = clean.strip()

        try:
            prediction = json.loads(clean)
        except json.JSONDecodeError:
            print(f"    ⚠ JSON parse failed, retrying...")
            time.sleep(2)
            raw = call_claude(prompt)
            clean = raw.strip().lstrip("`json\n").rstrip("`").strip()
            prediction = json.loads(clean)

        entry = {**rashi, **prediction}
        all_rashis.append(entry)
        time.sleep(1)  # Rate limit courtesy

    # Save daily content
    output = {
        "date": date_str,
        "date_hi": date_hi,
        "weekday_en": weekday_en,
        "weekday_hi": weekday_hi,
        "rashis": all_rashis,
        "generated_at": datetime.datetime.utcnow().isoformat(),
    }

    outfile = CONTENT_DIR / f"{date_str}.json"
    outfile.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Saved: {outfile}")
    return output


if __name__ == "__main__":
    if not API_KEY:
        print("❌ Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    target_date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    print(f"🔮 Generating rashifal for {target_date}...")
    generate_daily(target_date)
    print("🎉 Done!")
