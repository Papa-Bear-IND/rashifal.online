#!/usr/bin/env python3
"""
rashifal.online — Daily Horoscope Content Generator
Calls Claude API to generate unique daily rashifal for all 12 rashis
in both Hindi and English. Outputs JSON files consumed by the site builder.
"""

import json, os, sys, datetime, pathlib, time
import urllib.request, urllib.error

# Force UTF-8 stdout on Windows so emoji/Devanagari prints don't crash
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

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
        "max_tokens": 4000,
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


def _parse_json(raw: str):
    clean = raw.strip()
    if clean.startswith("```"):
        clean = clean.split("\n", 1)[1]
    if clean.endswith("```"):
        clean = clean.rsplit("```", 1)[0]
    return json.loads(clean.strip())


def generate_panchang(date_str: str) -> dict:
    """Call Claude once to produce traditional panchang for the given date."""
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    weekday_en = dt.strftime("%A")
    prompt = f"""You are a traditional Vedic astrologer producing the Hindu panchang for {date_str} ({weekday_en}) for Bhopal, India (IST).

Return ONLY valid JSON (no markdown, no backticks) with this exact structure:
{{
  "tithi": {{"hi": "तिथि नाम (पक्ष सहित)", "en": "Tithi name with paksha"}},
  "nakshatra": {{"hi": "नक्षत्र नाम", "en": "Nakshatra name"}},
  "yoga": {{"hi": "योग नाम", "en": "Yoga name"}},
  "karana": {{"hi": "करण नाम", "en": "Karana name"}},
  "special": {{"hi": "कोई विशेष पर्व/व्रत/योग, अन्यथा खाली", "en": "Any special vrat/observance, else empty"}}
}}

Rules:
- Use authentic, traditional Hindu panchang values for that exact date.
- Be concise — names only, no explanations."""
    raw = call_claude(prompt)
    try:
        return _parse_json(raw)
    except Exception:
        time.sleep(2)
        return _parse_json(call_claude(prompt))


CHINESE_ANIMALS = [
    {"id":"rat",     "hi":"चूहा",     "en":"Rat"},
    {"id":"ox",      "hi":"बैल",      "en":"Ox"},
    {"id":"tiger",   "hi":"बाघ",      "en":"Tiger"},
    {"id":"rabbit",  "hi":"खरगोश",    "en":"Rabbit"},
    {"id":"dragon",  "hi":"ड्रैगन",   "en":"Dragon"},
    {"id":"snake",   "hi":"साँप",     "en":"Snake"},
    {"id":"horse",   "hi":"घोड़ा",    "en":"Horse"},
    {"id":"goat",    "hi":"बकरी",     "en":"Goat"},
    {"id":"monkey",  "hi":"बंदर",     "en":"Monkey"},
    {"id":"rooster", "hi":"मुर्गा",   "en":"Rooster"},
    {"id":"dog",     "hi":"कुत्ता",   "en":"Dog"},
    {"id":"pig",     "hi":"सूअर",     "en":"Pig"},
]


def generate_chinese_daily(date_str: str) -> dict:
    """Generate daily Chinese horoscope for all 12 animals.
    Returns a dict keyed by animal id with hindi/english predictions."""
    out = {}
    for animal in CHINESE_ANIMALS:
        prompt = f"""You are an expert Chinese astrologer writing a daily horoscope.
Generate the daily Chinese horoscope for {animal['en']} ({animal['hi']}) sign for {date_str}.

Return ONLY valid JSON (no markdown, no backticks):
{{
  "hindi": {{
    "prediction": "3-4 sentences in Hindi about today for this Chinese sign — work, relationships, energy.",
    "lucky_number": 7,
    "lucky_color": "लाल",
    "rating": 3.5
  }},
  "english": {{
    "prediction": "3-4 sentences in English about today for this Chinese sign — work, relationships, energy.",
    "lucky_number": 7,
    "lucky_color": "Red",
    "rating": 3.5
  }}
}}

Rules:
- rating is 1.0 to 5.0
- Be specific and varied per sign — do not repeat generic advice
- Tone: warm, hopeful, realistic"""
        try:
            out[animal["id"]] = _parse_json(call_claude(prompt))
        except Exception as e:
            print(f"    ⚠ Chinese {animal['en']} failed: {e}")
            out[animal["id"]] = None
        time.sleep(1)
    return out


def generate_tarot_daily(date_str: str) -> dict:
    """Generate today's tarot card-of-the-day plus a 3-card past/present/future spread."""
    prompt = f"""You are a Tarot reader producing the reading for {date_str}.
Pick one Major Arcana card as Card of the Day and three Major Arcana cards
(can be different from the Card of the Day) as a Past / Present / Future spread.

Return ONLY valid JSON (no markdown, no backticks):
{{
  "card_of_day": {{
    "number": 17,
    "hindi": {{
      "name": "तारा",
      "meaning": "2-3 sentences in Hindi explaining the card's meaning.",
      "advice": "1 sentence advice in Hindi for the day."
    }},
    "english": {{
      "name": "The Star",
      "meaning": "2-3 sentences in English explaining the card's meaning.",
      "advice": "1 sentence advice in English for the day."
    }}
  }},
  "spread": [
    {{
      "position": {{"hi":"अतीत","en":"Past"}},
      "number": 6,
      "hindi": {{"name":"प्रेमी","meaning":"1-2 sentence interpretation in Hindi for the past position."}},
      "english": {{"name":"The Lovers","meaning":"1-2 sentence interpretation in English for the past position."}}
    }},
    {{
      "position": {{"hi":"वर्तमान","en":"Present"}},
      "number": 10,
      "hindi": {{"name":"भाग्य का चक्र","meaning":"1-2 sentence interpretation in Hindi for the present position."}},
      "english": {{"name":"Wheel of Fortune","meaning":"1-2 sentence interpretation in English for the present position."}}
    }},
    {{
      "position": {{"hi":"भविष्य","en":"Future"}},
      "number": 19,
      "hindi": {{"name":"सूर्य","meaning":"1-2 sentence interpretation in Hindi for the future position."}},
      "english": {{"name":"The Sun","meaning":"1-2 sentence interpretation in English for the future position."}}
    }}
  ]
}}

Rules:
- Use only Major Arcana cards (number 0 to 21).
- Pick a different Card of the Day each calendar day — vary across the year.
- Names must be the standard Tarot names in English (e.g. The Fool, The Magician)
  and the standard Hindi equivalents.
- Keep meanings warm, applicable, and free of fatalism."""
    try:
        return _parse_json(call_claude(prompt))
    except Exception as e:
        print(f"    ⚠ Tarot failed: {e}")
        return None


def generate_numerology(date_str: str) -> list:
    """Daily numerology — predictions for mulank 1..9."""
    prompt = f"""Generate daily numerology predictions for {date_str}.
For each root number (mulank) 1 through 9, provide:
- 2-3 sentence prediction in Hindi
- 2-3 sentence prediction in English
- lucky color (Hindi name + English name)
- compatible number (1..9)

Ruling planets: 1=Sun, 2=Moon, 3=Jupiter, 4=Rahu, 5=Mercury, 6=Venus, 7=Ketu, 8=Saturn, 9=Mars.

Return ONLY a valid JSON array (no markdown, no backticks) with exactly 9 entries:
[
  {{
    "number": 1,
    "planet": {{"hi":"सूर्य","en":"Sun"}},
    "hindi": {{"prediction":"...","lucky_color":"लाल","compatible":3}},
    "english":{{"prediction":"...","lucky_color":"Red","compatible":3}}
  }},
  ... (one entry per mulank 1..9)
]"""
    try:
        return _parse_json(call_claude(prompt))
    except Exception as e:
        print(f"    ⚠ Numerology failed: {e}")
        return None


def generate_vastu(date_str: str) -> dict:
    """One Vastu Shastra tip of the day."""
    prompt = f"""Generate one Vastu Shastra tip of the day for {date_str}.
Include the tip's title, a 3-4 sentence detailed tip, the direction it relates to,
and the benefit. In both Hindi and English.

Return ONLY valid JSON (no markdown, no backticks):
{{
  "direction": {{"hi":"उत्तर-पूर्व","en":"North-East"}},
  "hindi": {{
    "title": "...",
    "tip": "3-4 sentence detailed tip in Hindi.",
    "benefit": "1 sentence benefit in Hindi."
  }},
  "english": {{
    "title": "...",
    "tip": "3-4 sentence detailed tip in English.",
    "benefit": "1 sentence benefit in English."
  }}
}}"""
    try:
        return _parse_json(call_claude(prompt))
    except Exception as e:
        print(f"    ⚠ Vastu failed: {e}")
        return None


def generate_gemstone(date_str: str) -> dict:
    """Gemstone of the day, derived from weekday's ruling planet."""
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    # Mon=0..Sun=6 in python; map to gemstone+planet
    table = {
        0: ("Moon", "चंद्र", "Pearl", "मोती"),
        1: ("Mars", "मंगल", "Red Coral", "मूँगा"),
        2: ("Mercury", "बुध", "Emerald", "पन्ना"),
        3: ("Jupiter", "गुरु", "Yellow Sapphire", "पुखराज"),
        4: ("Venus", "शुक्र", "Diamond", "हीरा"),
        5: ("Saturn", "शनि", "Blue Sapphire", "नीलम"),
        6: ("Sun", "सूर्य", "Ruby", "माणिक्य"),
    }
    planet_en, planet_hi, gem_en, gem_hi = table[dt.weekday()]
    weekday_en = dt.strftime("%A")
    prompt = f"""Today is {weekday_en} ({date_str}), ruled by {planet_en} ({planet_hi}).
The gemstone of the day is {gem_en} ({gem_hi}).

Generate a recommendation explaining why it's auspicious today, who should wear it,
who should avoid it, and a short Sanskrit mantra for energizing it.

Return ONLY valid JSON (no markdown, no backticks):
{{
  "planet": {{"hi":"{planet_hi}","en":"{planet_en}"}},
  "gemstone": {{"hi":"{gem_hi}","en":"{gem_en}"}},
  "hindi": {{
    "why": "2-3 sentences in Hindi explaining why this gem is auspicious today.",
    "wear": "1-2 sentences in Hindi naming who benefits from wearing it.",
    "avoid": "1 sentence in Hindi naming who should avoid it.",
    "mantra": "Short Sanskrit mantra in Devanagari to energise the gem."
  }},
  "english": {{
    "why": "2-3 sentences in English explaining why this gem is auspicious today.",
    "wear": "1-2 sentences in English naming who benefits from wearing it.",
    "avoid": "1 sentence in English naming who should avoid it.",
    "mantra": "Same Sanskrit mantra in Devanagari (do not transliterate)."
  }}
}}"""
    try:
        out = _parse_json(call_claude(prompt))
        return out
    except Exception as e:
        print(f"    ⚠ Gemstone failed: {e}")
        return None


def generate_transit(date_str: str) -> dict:
    """One major planetary transit interpretation for today."""
    prompt = f"""Generate today's planetary transit interpretation for {date_str}.
Pick ONE major current transit (which planet is currently transiting which sign)
and explain what it means for the general public. Include its effect on career,
relationships and health. 3-4 sentences in Hindi and English.

Return ONLY valid JSON (no markdown, no backticks):
{{
  "headline": {{
    "hi": "Short 1-line headline in Hindi like 'बुध मेष राशि में — संचार में सावधानी'.",
    "en": "Short 1-line headline in English like 'Mercury in Aries — be careful with communication'."
  }},
  "hindi": {{
    "summary": "3-4 sentence interpretation in Hindi.",
    "career": "1 sentence in Hindi.",
    "relationships": "1 sentence in Hindi.",
    "health": "1 sentence in Hindi."
  }},
  "english": {{
    "summary": "3-4 sentence interpretation in English.",
    "career": "1 sentence in English.",
    "relationships": "1 sentence in English.",
    "health": "1 sentence in English."
  }}
}}"""
    try:
        return _parse_json(call_claude(prompt))
    except Exception as e:
        print(f"    ⚠ Transit failed: {e}")
        return None


def generate_muhurat(date_str: str) -> dict:
    """Auspicious / inauspicious time slots for the day."""
    prompt = f"""Generate auspicious and inauspicious timings for {date_str} (IST, Bhopal).
Include best time for: starting new work, travel, financial transactions,
medical procedures, and the time to avoid (Rahu Kaal based on weekday).

Return ONLY valid JSON (no markdown, no backticks):
{{
  "new_work":   {{"time":"7:30 AM – 9:00 AM","hi":"नए कार्य के लिए","en":"For starting new work"}},
  "travel":     {{"time":"...","hi":"यात्रा के लिए","en":"For travel"}},
  "finance":    {{"time":"...","hi":"धन-लेनदेन के लिए","en":"For financial transactions"}},
  "medical":    {{"time":"...","hi":"चिकित्सा के लिए","en":"For medical procedures"}},
  "avoid":      {{"time":"...","hi":"राहु काल — टालें","en":"Rahu Kaal — avoid"}}
}}

Times must be in 12-hour IST format with AM/PM. Be realistic for the given weekday."""
    try:
        return _parse_json(call_claude(prompt))
    except Exception as e:
        print(f"    ⚠ Muhurat failed: {e}")
        return None


def generate_story(date_str: str) -> dict:
    """Call Claude to produce a short dharmic story for the day."""
    prompt = f"""You are a teacher of dharmic literature. Compose a short story (150-200 words) for {date_str}, drawn from the Ramayan, Mahabharat, Puranas, or other Hindu scriptures.

Return ONLY valid JSON (no markdown, no backticks) with this exact structure:
{{
  "title": {{"hi": "कथा का शीर्षक हिंदी में", "en": "Story title in English"}},
  "text": {{"hi": "150-200 शब्दों की कथा हिंदी में, सरल और भावपूर्ण।", "en": "150-200 word story in English, simple and evocative."}},
  "moral": {{"hi": "1-2 वाक्यों में नैतिक शिक्षा।", "en": "1-2 sentence moral teaching."}}
}}

Rules:
- Pick a different story each day; avoid the most cliché ones.
- Keep tone reverent, warm, and accessible.
- Story text length: 150-200 words in each language."""
    raw = call_claude(prompt)
    try:
        return _parse_json(raw)
    except Exception:
        time.sleep(2)
        return _parse_json(call_claude(prompt))


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
    "prediction": "4-5 sentences of overall daily prediction in Hindi. Be specific, varied, engaging.",
    "love": "2-3 sentences in Hindi about love, romance and relationships for today.",
    "career": "2-3 sentences in Hindi about career, work and business for today.",
    "health": "2-3 sentences in Hindi about physical and mental health for today.",
    "finance": "2-3 sentences in Hindi about money, savings and financial decisions for today.",
    "remedy": "One simple, specific astrological remedy for today in Hindi (e.g. 'आज लाल वस्त्र पहनें' or 'हनुमान चालीसा का पाठ करें').",
    "mantra": {{
      "sanskrit": "A short Sanskrit mantra (Devanagari) relevant to today's planetary ruler.",
      "meaning": "Brief Hindi meaning of the mantra in one sentence."
    }},
    "lucky_number": 7,
    "lucky_color": "लाल",
    "rating": 3.5
  }},
  "english": {{
    "prediction": "4-5 sentences of overall daily prediction in English. Be specific, varied, engaging.",
    "love": "2-3 sentences in English about love, romance and relationships for today.",
    "career": "2-3 sentences in English about career, work and business for today.",
    "health": "2-3 sentences in English about physical and mental health for today.",
    "finance": "2-3 sentences in English about money, savings and financial decisions for today.",
    "remedy": "One simple, specific astrological remedy for today in English (e.g. 'Wear red today' or 'Chant the Hanuman Chalisa this evening').",
    "mantra": {{
      "sanskrit": "The same short Sanskrit mantra in Devanagari, relevant to today's planetary ruler.",
      "meaning": "Brief English meaning of the mantra in one sentence."
    }},
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
- Keep tone warm, hopeful but realistic
- Each category (love/career/health/finance) must give DIFFERENT, specific guidance — do not repeat the overall prediction
- The overall prediction should be a holistic summary, the categories should add fresh detail"""

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

    print("  Generating: Panchang...")
    try:
        panchang = generate_panchang(date_str)
    except Exception as e:
        print(f"    ⚠ Panchang failed: {e}")
        panchang = None
    time.sleep(1)

    print("  Generating: Story of the day...")
    try:
        story = generate_story(date_str)
    except Exception as e:
        print(f"    ⚠ Story failed: {e}")
        story = None
    time.sleep(1)

    print("  Generating: Chinese horoscope (12 animals)...")
    try:
        chinese = generate_chinese_daily(date_str)
    except Exception as e:
        print(f"    ⚠ Chinese horoscope failed: {e}")
        chinese = None
    time.sleep(1)

    print("  Generating: Tarot card of the day + spread...")
    try:
        tarot = generate_tarot_daily(date_str)
    except Exception as e:
        print(f"    ⚠ Tarot failed: {e}")
        tarot = None
    time.sleep(1)

    print("  Generating: Numerology (mulank 1-9)...")
    numerology = generate_numerology(date_str)
    time.sleep(1)

    print("  Generating: Vastu tip of the day...")
    vastu = generate_vastu(date_str)
    time.sleep(1)

    print("  Generating: Gemstone of the day...")
    gemstone = generate_gemstone(date_str)
    time.sleep(1)

    print("  Generating: Transit interpretation...")
    transit = generate_transit(date_str)
    time.sleep(1)

    print("  Generating: Muhurat timings...")
    muhurat_detail = generate_muhurat(date_str)

    # Save daily content
    output = {
        "date": date_str,
        "date_hi": date_hi,
        "weekday_en": weekday_en,
        "weekday_hi": weekday_hi,
        "rashis": all_rashis,
        "panchang": panchang,
        "story": story,
        "chinese": chinese,
        "tarot": tarot,
        "numerology": numerology,
        "vastu": vastu,
        "gemstone": gemstone,
        "transit": transit,
        "muhurat_detail": muhurat_detail,
        "generated_at": datetime.datetime.utcnow().isoformat(),
    }

    outfile = CONTENT_DIR / f"{date_str}.json"
    outfile.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Saved: {outfile}")
    return output


def _period_rashi_loop(prompt_builder, label: str):
    """Helper that runs a per-rashi Claude call and returns a list of entries."""
    out = []
    for rashi in RASHIS:
        print(f"  {label}: {rashi['name_en']} ({rashi['name_hi']})...")
        prompt = prompt_builder(rashi)
        try:
            data = _parse_json(call_claude(prompt))
        except Exception:
            time.sleep(2)
            data = _parse_json(call_claude(prompt))
        out.append({**rashi, **data})
        time.sleep(1)
    return out


def generate_weekly(date_str: str):
    """Weekly rashifal — Monday to Sunday containing date_str."""
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    monday = dt - datetime.timedelta(days=dt.weekday())
    sunday = monday + datetime.timedelta(days=6)
    iso_year, iso_week, _ = dt.isocalendar()
    week_label = f"{monday.strftime('%d %b')} – {sunday.strftime('%d %b %Y')}"

    def prompter(rashi):
        return f"""You are an expert Vedic astrologer writing a weekly horoscope.
Generate the weekly horoscope for {rashi['name_en']} ({rashi['name_hi']}) for the week {week_label}.

Return ONLY valid JSON (no markdown, no backticks):
{{
  "hindi": {{
    "prediction": "5-6 sentences in Hindi covering the whole week, weekly themes, and key days to watch.",
    "key_days": "1-2 sentences in Hindi naming the most auspicious and most challenging days of the week.",
    "love": "2-3 sentences in Hindi for love/relationships this week.",
    "career": "2-3 sentences in Hindi for career/work this week.",
    "health": "2-3 sentences in Hindi for health this week.",
    "finance": "2-3 sentences in Hindi for money this week.",
    "lucky_number": 7,
    "lucky_color": "लाल",
    "rating": 3.5
  }},
  "english": {{
    "prediction": "5-6 sentences in English covering the whole week, weekly themes, and key days to watch.",
    "key_days": "1-2 sentences in English naming the most auspicious and most challenging days.",
    "love": "2-3 sentences in English for love this week.",
    "career": "2-3 sentences in English for career this week.",
    "health": "2-3 sentences in English for health this week.",
    "finance": "2-3 sentences in English for money this week.",
    "lucky_number": 7,
    "lucky_color": "Red",
    "rating": 3.5
  }}
}}

Rules:
- rating 1.0-5.0 (half-star)
- Be specific and varied per rashi
- Mention ruling planet of the week and any major transits"""

    rashis = _period_rashi_loop(prompter, "Weekly")
    output = {
        "period": "weekly",
        "week_label": week_label,
        "iso_year": iso_year,
        "iso_week": iso_week,
        "start": monday.strftime("%Y-%m-%d"),
        "end": sunday.strftime("%Y-%m-%d"),
        "rashis": rashis,
        "generated_at": datetime.datetime.utcnow().isoformat(),
    }
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    outfile = CONTENT_DIR / f"weekly-{iso_year}-W{iso_week:02d}.json"
    outfile.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Saved: {outfile}")
    return output


def generate_monthly(date_str: str):
    """Monthly rashifal for the calendar month containing date_str."""
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    ym = dt.strftime("%Y-%m")
    month_label = dt.strftime("%B %Y")

    def prompter(rashi):
        return f"""You are an expert Vedic astrologer writing a monthly horoscope.
Generate the monthly horoscope for {rashi['name_en']} ({rashi['name_hi']}) for {month_label}.

Return ONLY valid JSON (no markdown, no backticks):
{{
  "hindi": {{
    "prediction": "6-8 sentences in Hindi describing the monthly themes, best week, challenging week, and overall arc.",
    "best_week": "1 sentence in Hindi naming the best week of the month and why.",
    "tough_week": "1 sentence in Hindi naming the toughest week and what to watch.",
    "love": "2-3 sentences in Hindi for love this month.",
    "career": "2-3 sentences in Hindi for career this month.",
    "health": "2-3 sentences in Hindi for health this month.",
    "finance": "2-3 sentences in Hindi for finance this month.",
    "lucky_number": 7,
    "lucky_color": "लाल",
    "rating": 3.5
  }},
  "english": {{
    "prediction": "6-8 sentences in English describing the monthly themes, best week, challenging week, and overall arc.",
    "best_week": "1 sentence in English naming the best week and why.",
    "tough_week": "1 sentence in English naming the toughest week and what to watch.",
    "love": "2-3 sentences in English for love this month.",
    "career": "2-3 sentences in English for career this month.",
    "health": "2-3 sentences in English for health this month.",
    "finance": "2-3 sentences in English for finance this month.",
    "lucky_number": 7,
    "lucky_color": "Red",
    "rating": 3.5
  }}
}}

Rules:
- Mention any major planetary transits (Jupiter, Saturn, eclipses) happening in {month_label}
- Be specific to the rashi"""

    rashis = _period_rashi_loop(prompter, "Monthly")
    output = {
        "period": "monthly",
        "month": ym,
        "month_label": month_label,
        "rashis": rashis,
        "generated_at": datetime.datetime.utcnow().isoformat(),
    }
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    outfile = CONTENT_DIR / f"monthly-{ym}.json"
    outfile.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Saved: {outfile}")
    return output


def generate_yearly(date_str: str):
    """Yearly rashifal for the calendar year containing date_str."""
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    year = dt.year

    def prompter(rashi):
        return f"""You are an expert Vedic astrologer writing a yearly horoscope.
Generate the {year} yearly horoscope for {rashi['name_en']} ({rashi['name_hi']}).

Return ONLY valid JSON (no markdown, no backticks):
{{
  "hindi": {{
    "prediction": "8-10 sentences in Hindi giving the overall arc of {year} for this rashi, including major planetary events.",
    "q1": "1-2 sentences in Hindi about January-March.",
    "q2": "1-2 sentences in Hindi about April-June.",
    "q3": "1-2 sentences in Hindi about July-September.",
    "q4": "1-2 sentences in Hindi about October-December.",
    "love": "2-3 sentences in Hindi for love this year.",
    "career": "2-3 sentences in Hindi for career this year.",
    "health": "2-3 sentences in Hindi for health this year.",
    "finance": "2-3 sentences in Hindi for wealth this year.",
    "lucky_number": 7,
    "lucky_color": "लाल",
    "rating": 3.5
  }},
  "english": {{
    "prediction": "8-10 sentences in English giving the overall arc of {year} for this rashi, including major planetary events.",
    "q1": "1-2 sentences in English about January-March.",
    "q2": "1-2 sentences in English about April-June.",
    "q3": "1-2 sentences in English about July-September.",
    "q4": "1-2 sentences in English about October-December.",
    "love": "2-3 sentences in English for love this year.",
    "career": "2-3 sentences in English for career this year.",
    "health": "2-3 sentences in English for health this year.",
    "finance": "2-3 sentences in English for wealth this year.",
    "lucky_number": 7,
    "lucky_color": "Red",
    "rating": 3.5
  }}
}}

Rules:
- Reference real major transits in {year} (Jupiter sign change, Saturn position, eclipses)
- Be substantive — this is the most prominent reading"""

    rashis = _period_rashi_loop(prompter, "Yearly")
    output = {
        "period": "yearly",
        "year": year,
        "rashis": rashis,
        "generated_at": datetime.datetime.utcnow().isoformat(),
    }
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    outfile = CONTENT_DIR / f"yearly-{year}.json"
    outfile.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Saved: {outfile}")
    return output


if __name__ == "__main__":
    if not API_KEY:
        print("❌ Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    mode = "daily"
    target_date = datetime.date.today().isoformat()
    args = sys.argv[1:]
    if args and args[0] in ("daily", "weekly", "monthly", "yearly", "all"):
        mode = args[0]
        if len(args) > 1:
            target_date = args[1]
    elif args:
        target_date = args[0]

    print(f"🔮 Generating {mode} rashifal for {target_date}...")
    if mode == "daily":
        generate_daily(target_date)
    elif mode == "weekly":
        generate_weekly(target_date)
    elif mode == "monthly":
        generate_monthly(target_date)
    elif mode == "yearly":
        generate_yearly(target_date)
    elif mode == "all":
        generate_daily(target_date)
        generate_weekly(target_date)
        generate_monthly(target_date)
        generate_yearly(target_date)
    print("🎉 Done!")
