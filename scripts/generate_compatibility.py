#!/usr/bin/env python3
"""
rashifal.online — One-time compatibility data generator.

Generates a detailed Vedic-flavoured zodiac compatibility analysis for all
12 × 12 = 144 sign combinations and writes the result to
content/compatibility-data.json.

This is NOT part of the daily automation. Run manually once:

    python scripts/generate_compatibility.py

Re-running will overwrite the file. Set the ANTHROPIC_API_KEY env var first.

Output schema (one entry per pair, key is "<id1>_<id2>"):

  {
    "mesh_vrishabh": {
      "score": 72,
      "emotional": 8, "communication": 6, "trust": 7,
      "physical": 8, "values": 7,
      "analysis_hi": "...", "analysis_en": "...",
      "best_hi": ["...", "..."], "best_en": ["...", "..."],
      "challenges_hi": ["...", "..."], "challenges_en": ["...", "..."]
    },
    ...
  }
"""

import json
import os
import sys
import time
import datetime
import pathlib
import urllib.request
import urllib.error

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
MODEL = "claude-sonnet-4-20250514"
CONTENT_DIR = pathlib.Path(__file__).parent.parent / "content"
OUTFILE = CONTENT_DIR / "compatibility-data.json"
SLEEP_BETWEEN_CALLS = 1.0  # seconds — be a polite API citizen

RASHIS = [
    {"id": "mesh",      "name_hi": "मेष",     "name_en": "Aries"},
    {"id": "vrishabh",  "name_hi": "वृषभ",    "name_en": "Taurus"},
    {"id": "mithun",    "name_hi": "मिथुन",   "name_en": "Gemini"},
    {"id": "kark",      "name_hi": "कर्क",    "name_en": "Cancer"},
    {"id": "singh",     "name_hi": "सिंह",    "name_en": "Leo"},
    {"id": "kanya",     "name_hi": "कन्या",   "name_en": "Virgo"},
    {"id": "tula",      "name_hi": "तुला",    "name_en": "Libra"},
    {"id": "vrishchik", "name_hi": "वृश्चिक", "name_en": "Scorpio"},
    {"id": "dhanu",     "name_hi": "धनु",     "name_en": "Sagittarius"},
    {"id": "makar",     "name_hi": "मकर",     "name_en": "Capricorn"},
    {"id": "kumbh",     "name_hi": "कुम्भ",   "name_en": "Aquarius"},
    {"id": "meen",      "name_hi": "मीन",     "name_en": "Pisces"},
]


def call_claude(prompt: str) -> str:
    """Call Claude API and return raw text response."""
    body = json.dumps({
        "model": MODEL,
        "max_tokens": 2500,
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


def parse_json(raw: str):
    clean = raw.strip()
    if clean.startswith("```"):
        clean = clean.split("\n", 1)[1]
    if clean.endswith("```"):
        clean = clean.rsplit("```", 1)[0]
    return json.loads(clean.strip())


def build_prompt(s1, s2):
    return f"""You are an expert Vedic astrologer producing a zodiac compatibility report for {s1['name_en']} ({s1['name_hi']}) and {s2['name_en']} ({s2['name_hi']}).

Be REALISTIC — not every pair is 90%+. Use the elemental, modal and ruling-planet
relationships of these signs to ground the scores. Same-sign pairings have their
own dynamics (familiar but possibly stagnant). Opposite-sign pairings have a
magnetic pull but real friction.

Return ONLY valid JSON (no markdown, no backticks) with this exact structure:

{{
  "score": 72,
  "emotional": 8,
  "communication": 6,
  "trust": 7,
  "physical": 8,
  "values": 7,
  "analysis_hi": "4-5 sentence analysis in Hindi explaining why these signs do or don't match.",
  "analysis_en": "4-5 sentence analysis in English explaining why these signs do or don't match.",
  "best_hi":      ["1 sentence — first strength of this pairing in Hindi", "1 sentence — second strength in Hindi"],
  "best_en":      ["1 sentence — first strength in English", "1 sentence — second strength in English"],
  "challenges_hi":["1 sentence — first challenge in Hindi", "1 sentence — second challenge in Hindi"],
  "challenges_en":["1 sentence — first challenge in English", "1 sentence — second challenge in English"]
}}

Rules:
- score: integer 0-100, realistic. Distribution should resemble a bell curve
  centred around 60-75. Avoid clustering everything above 85.
- All five 1-10 scores: integers, realistic, vary across pairs.
- Tone: warm, grounded, no fatalism. Avoid generic horoscope clichés.
- Each pair must read distinctly — do not repeat the same analysis verbatim
  across pairs."""


def generate_pair(s1, s2):
    prompt = build_prompt(s1, s2)
    raw = call_claude(prompt)
    try:
        return parse_json(raw)
    except json.JSONDecodeError:
        # one retry on parse failure
        time.sleep(2)
        raw = call_claude(prompt)
        return parse_json(raw)


def main():
    if not API_KEY:
        print("✗ ANTHROPIC_API_KEY not set. Aborting.", file=sys.stderr)
        sys.exit(1)

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # Resume support: if the file already exists, load it and skip pairs
    # that were already generated. Lets you re-run after a network blip.
    out = {}
    if OUTFILE.exists():
        try:
            out = json.loads(OUTFILE.read_text(encoding="utf-8"))
            print(f"↻ Resuming — {len(out)} pairs already in {OUTFILE}")
        except Exception:
            out = {}

    total = len(RASHIS) * len(RASHIS)
    counter = 0
    started = time.time()

    for s1 in RASHIS:
        for s2 in RASHIS:
            counter += 1
            key = f"{s1['id']}_{s2['id']}"

            if key in out:
                print(f"  [{counter:>3}/{total}] {key} — already present, skipping")
                continue

            print(f"  [{counter:>3}/{total}] Generating {s1['name_en']} + {s2['name_en']}...", end=" ", flush=True)
            try:
                entry = generate_pair(s1, s2)
                out[key] = entry
                print(f"score={entry.get('score', '?')}")
            except Exception as e:
                print(f"⚠ failed: {e}")
                # Persist partial progress so a re-run can pick up
                OUTFILE.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
                continue

            # Periodically flush to disk
            if counter % 12 == 0:
                OUTFILE.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

            time.sleep(SLEEP_BETWEEN_CALLS)

    # Final write
    payload = {
        "version": 1,
        "generated_at": datetime.datetime.utcnow().isoformat(),
        "pairs": out,
    }
    OUTFILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    elapsed = time.time() - started
    print(f"\n✅ Done — {len(out)}/{total} pairs written to {OUTFILE}")
    print(f"   Elapsed: {elapsed/60:.1f} min")


if __name__ == "__main__":
    main()
