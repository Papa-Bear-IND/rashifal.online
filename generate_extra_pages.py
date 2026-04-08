#!/usr/bin/env python3
"""Generate astrology tool pages + festival puja/katha pages for rashifal.online"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def page_shell(title_hi, title_en, meta_desc, filename, body_hi, body_en, extra_js=""):
    """Shared page template matching site design."""
    return f"""<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_hi} | {title_en} — Rashifal.online</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="https://rashifal.online/{filename}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Tiro+Devanagari+Hindi:ital@0;1&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{--midnight:#0A0E1A;--charcoal:#131825;--gold:#D4AF37;--gold-light:#E8CC6E;--gold-muted:rgba(212,175,55,0.12);--gold-faint:rgba(212,175,55,0.03);--t-heading:rgba(232,228,218,0.95);--t-body:rgba(200,205,220,0.82);--t-muted:rgba(200,205,220,0.62);--t-faint:rgba(200,205,220,0.36);--b-subtle:rgba(212,175,55,0.06);--b-default:rgba(212,175,55,0.1);--f-serif:'Cormorant Garamond','Tiro Devanagari Hindi',Georgia,serif;--f-sans:'Inter',system-ui,sans-serif;--f-hindi:'Tiro Devanagari Hindi',serif;--glass-bg:rgba(14,18,30,0.55);--glass-blur:blur(16px);--glass-border:1px solid rgba(255,255,255,0.04);--glass-radius:14px}}
html{{scroll-behavior:smooth;font-size:16px}}
body{{background:var(--midnight);color:var(--t-body);font-family:var(--f-sans);line-height:1.7;min-height:100vh;-webkit-font-smoothing:antialiased}}
h1,h2,h3{{font-family:var(--f-serif);color:var(--t-heading);font-weight:600;line-height:1.2}}
.container{{max-width:860px;margin:0 auto;padding:0 1.5rem}}
.nav{{position:sticky;top:0;z-index:50;background:rgba(7,11,20,0.85);backdrop-filter:var(--glass-blur);border-bottom:1px solid var(--b-subtle)}}
.nav-inner{{max-width:1120px;margin:0 auto;padding:0 1.5rem;display:flex;align-items:center;height:56px}}
.nav-brand{{font-family:var(--f-serif);font-size:1.333rem;font-weight:600;color:var(--gold);text-decoration:none;margin-right:auto}}
.nav-links{{display:flex;gap:0.25rem}}
.nav-link{{padding:0.5rem 1rem;font-size:0.875rem;font-weight:500;color:var(--t-muted);text-decoration:none;border-radius:6px}}
.nav-link:hover{{color:var(--t-heading)}}
.hero{{text-align:center;padding:3.5rem 0 2.5rem}}
.hero h1{{font-size:clamp(1.6rem,4vw,2.2rem);color:var(--gold);margin-bottom:0.5rem}}
.hero .sub{{font-size:0.95rem;color:var(--t-muted);max-width:520px;margin:0 auto}}
.card{{background:var(--glass-bg);backdrop-filter:var(--glass-blur);border:var(--glass-border);border-radius:var(--glass-radius);padding:2rem;margin-bottom:1.5rem}}
.card h2{{font-size:1.25rem;margin-bottom:1rem;color:var(--gold-light)}}
.card h3{{font-size:1.05rem;margin-bottom:0.75rem;color:var(--gold-light)}}
.prose{{font-size:1rem;line-height:1.85;color:var(--t-body)}}
.prose.hi{{font-family:var(--f-hindi);line-height:1.95}}
.prose p{{margin-bottom:1rem}}
.prose ul,.prose ol{{margin:1rem 0;padding-left:1.5rem}}
.prose li{{margin-bottom:0.5rem}}
.highlight{{background:linear-gradient(135deg,rgba(212,175,55,0.04),rgba(14,18,30,0.6));border:1px solid rgba(212,175,55,0.08);border-radius:var(--glass-radius);padding:1.5rem;margin:1.5rem 0}}
.highlight p{{color:var(--gold-light);font-style:italic}}
.grid-2{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;margin:1.5rem 0}}
.grid-3{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem;margin:1.5rem 0}}
.info-item{{background:rgba(255,255,255,0.03);border-radius:10px;padding:1rem;text-align:center}}
.info-label{{font-size:0.75rem;color:var(--t-faint);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:0.25rem}}
.info-value{{font-family:var(--f-serif);font-size:1.1rem;color:var(--gold)}}
.lang-sw{{display:flex;border:1px solid var(--b-default);border-radius:6px;overflow:hidden;margin:1rem auto;width:fit-content}}
.lang-b{{padding:0.4rem 1.25rem;font-size:0.875rem;font-weight:500;background:none;border:none;color:var(--t-muted);cursor:pointer;font-family:var(--f-sans)}}
.lang-b.active{{background:var(--gold-muted);color:var(--gold)}}
.en-only{{display:none}}.hi-only{{display:block}}
body.lang-en .en-only{{display:block}}body.lang-en .hi-only{{display:none}}
.back-link{{display:inline-block;margin:2rem 0;font-size:0.875rem;color:var(--t-muted);text-decoration:none}}
.back-link:hover{{color:var(--gold)}}
footer{{text-align:center;padding:3rem 1.5rem 2rem;border-top:1px solid var(--b-subtle);margin-top:2rem;color:var(--t-faint);font-size:0.875rem}}
footer a{{color:var(--gold);text-decoration:none}}
.dynamic-content{{min-height:200px;position:relative}}
.loading{{color:var(--t-faint);font-style:italic}}
@media(max-width:768px){{.nav-links{{display:none}}.grid-2,.grid-3{{grid-template-columns:1fr}}.card{{padding:1.5rem}}.hero{{padding:2.5rem 0 2rem}}}}
</style>
</head>
<body>
<nav class="nav"><div class="nav-inner">
  <a href="index.html" class="nav-brand">Rashifal</a>
  <div class="nav-links">
    <a href="index.html" class="nav-link">Home</a>
    <a href="index.html#horoscopes" class="nav-link">Horoscopes</a>
    <a href="index.html#compatibility" class="nav-link">Compatibility</a>
  </div>
</div></nav>
<div class="container">
  <div class="lang-sw">
    <button class="lang-b active" onclick="setL('hi')">हिन्दी</button>
    <button class="lang-b" onclick="setL('en')">English</button>
  </div>
  <div class="hero">
    <h1 class="hi-only">{title_hi}</h1>
    <h1 class="en-only">{title_en}</h1>
    <p class="sub hi-only">{meta_desc.split('.')[0]}।</p>
    <p class="sub en-only">{meta_desc.split('.')[0]}.</p>
  </div>
  {body_hi}
  {body_en}
  <a href="index.html" class="back-link">&larr; <span class="hi-only">मुखपृष्ठ पर लौटें</span><span class="en-only">Back to homepage</span></a>
</div>
<footer><p>Rashifal.online &middot; 2026 &middot; Bhopal, India</p><p style="margin-top:0.5rem"><a href="privacy.html">Privacy</a> &middot; <a href="terms.html">Terms</a> &middot; <a href="about.html">About</a></p></footer>
<script>
function setL(l){{document.body.classList.toggle('lang-en',l==='en');document.querySelectorAll('.lang-b').forEach(b=>b.classList.toggle('active',b.textContent.includes(l==='hi'?'हिन':'Eng')));localStorage.setItem('rashifal_lang',l)}}
if(localStorage.getItem('rashifal_lang')==='en')setL('en');
{extra_js}
</script>
</body>
</html>"""

# ═══════════════════════════════════════
# ASTROLOGY TOOL PAGES
# ═══════════════════════════════════════

TOOL_PAGES = [
    {
        "file": "chinese-horoscope.html",
        "title_hi": "चीनी राशिफल 2026",
        "title_en": "Chinese Horoscope 2026",
        "meta": "चीनी राशिफल 2026 — अपने चीनी राशि चिन्ह के अनुसार वार्षिक भविष्यफल। Chinese Horoscope 2026 predictions for all 12 animal signs",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>चीनी ज्योतिष क्या है?</h2><div class="prose hi">
<p>चीनी ज्योतिष विश्व की सबसे प्राचीन ज्योतिष पद्धतियों में से एक है, जिसका इतिहास 5,000 वर्षों से भी अधिक पुराना है। यह पद्धति 12 पशु चिन्हों पर आधारित है, जो एक 12 वर्षीय चक्र में घूमते हैं। प्रत्येक व्यक्ति का चीनी राशि चिन्ह उसके जन्म वर्ष के आधार पर निर्धारित होता है।</p>
<p>भारतीय वैदिक ज्योतिष की तरह, चीनी ज्योतिष भी पाँच तत्वों (लकड़ी, अग्नि, पृथ्वी, धातु, जल) और यिन-यांग के सिद्धांत पर आधारित है। 2026 अग्नि घोड़े (Fire Horse) का वर्ष है — यह साहस, ऊर्जा और स्वतंत्रता का प्रतीक है।</p>
</div></div>

<div class="card"><h2>12 चीनी राशि चिन्ह</h2><div class="grid-3">
<div class="info-item"><div class="info-label">चूहा (Rat)</div><div class="info-value">2024, 2012, 2000, 1988</div></div>
<div class="info-item"><div class="info-label">बैल (Ox)</div><div class="info-value">2021, 2009, 1997, 1985</div></div>
<div class="info-item"><div class="info-label">बाघ (Tiger)</div><div class="info-value">2022, 2010, 1998, 1986</div></div>
<div class="info-item"><div class="info-label">खरगोश (Rabbit)</div><div class="info-value">2023, 2011, 1999, 1987</div></div>
<div class="info-item"><div class="info-label">ड्रैगन (Dragon)</div><div class="info-value">2024, 2012, 2000, 1988</div></div>
<div class="info-item"><div class="info-label">साँप (Snake)</div><div class="info-value">2025, 2013, 2001, 1989</div></div>
<div class="info-item"><div class="info-label">घोड़ा (Horse)</div><div class="info-value">2026, 2014, 2002, 1990</div></div>
<div class="info-item"><div class="info-label">बकरी (Goat)</div><div class="info-value">2027, 2015, 2003, 1991</div></div>
<div class="info-item"><div class="info-label">बंदर (Monkey)</div><div class="info-value">2028, 2016, 2004, 1992</div></div>
<div class="info-item"><div class="info-label">मुर्गा (Rooster)</div><div class="info-value">2029, 2017, 2005, 1993</div></div>
<div class="info-item"><div class="info-label">कुत्ता (Dog)</div><div class="info-value">2030, 2018, 2006, 1994</div></div>
<div class="info-item"><div class="info-label">सूअर (Pig)</div><div class="info-value">2031, 2019, 2007, 1995</div></div>
</div></div>

<div class="card"><h2>2026 — अग्नि घोड़े का वर्ष</h2><div class="prose hi">
<p>2026 में अग्नि घोड़े की ऊर्जा पूरे विश्व को प्रभावित करेगी। यह वर्ष तीव्र गति, साहसिक निर्णय और नई शुरुआत का है। घोड़ा चीनी ज्योतिष में स्वतंत्रता, यात्रा और महत्वाकांक्षा का प्रतीक है।</p>
<p>इस वर्ष जो लोग नए व्यवसाय शुरू करना चाहते हैं, यात्रा करना चाहते हैं या जीवन में बड़े परिवर्तन लाना चाहते हैं — उनके लिए अनुकूल समय है। हालांकि अग्नि तत्व के कारण आवेगपूर्ण निर्णयों से बचना चाहिए।</p>
<p>प्रत्येक चीनी राशि चिन्ह पर इस वर्ष का प्रभाव अलग-अलग होगा। चूहा और बंदर राशि वालों के लिए करियर में उन्नति, जबकि बैल और बकरी राशि वालों को धैर्य रखने की आवश्यकता होगी।</p>
</div></div>

<div class="card"><h2>अपना चीनी राशि चिन्ह जानें</h2><div class="prose hi">
<p>अपना चीनी राशि जानने के लिए अपना जन्म वर्ष देखें। ध्यान रखें कि चीनी नव वर्ष जनवरी-फरवरी में शुरू होता है, इसलिए यदि आपका जन्म जनवरी या फरवरी में हुआ है तो पिछले वर्ष का चिन्ह लागू हो सकता है।</p>
<p>उदाहरण: यदि आपका जन्म 1990 में हुआ है तो आपका चिन्ह घोड़ा (Horse) है। 2026 आपका राशि वर्ष (Ben Ming Nian) है — इस वर्ष विशेष सावधानी और लाल रंग के वस्त्र पहनने की सलाह दी जाती है।</p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>What is Chinese astrology?</h2><div class="prose">
<p>Chinese astrology is one of the world's oldest divination systems, with a history spanning over 5,000 years. It is based on a 12-year cycle, with each year represented by an animal sign. Your Chinese zodiac sign is determined by your birth year.</p>
<p>Like Indian Vedic astrology, Chinese astrology incorporates five elements (Wood, Fire, Earth, Metal, Water) and the principle of Yin and Yang. 2026 is the Year of the Fire Horse — symbolizing courage, energy, and independence.</p>
</div></div>

<div class="card"><h2>The 12 Chinese zodiac signs</h2><div class="grid-3">
<div class="info-item"><div class="info-label">Rat</div><div class="info-value">2024, 2012, 2000, 1988</div></div>
<div class="info-item"><div class="info-label">Ox</div><div class="info-value">2021, 2009, 1997, 1985</div></div>
<div class="info-item"><div class="info-label">Tiger</div><div class="info-value">2022, 2010, 1998, 1986</div></div>
<div class="info-item"><div class="info-label">Rabbit</div><div class="info-value">2023, 2011, 1999, 1987</div></div>
<div class="info-item"><div class="info-label">Dragon</div><div class="info-value">2024, 2012, 2000, 1988</div></div>
<div class="info-item"><div class="info-label">Snake</div><div class="info-value">2025, 2013, 2001, 1989</div></div>
<div class="info-item"><div class="info-label">Horse</div><div class="info-value">2026, 2014, 2002, 1990</div></div>
<div class="info-item"><div class="info-label">Goat</div><div class="info-value">2027, 2015, 2003, 1991</div></div>
<div class="info-item"><div class="info-label">Monkey</div><div class="info-value">2028, 2016, 2004, 1992</div></div>
<div class="info-item"><div class="info-label">Rooster</div><div class="info-value">2029, 2017, 2005, 1993</div></div>
<div class="info-item"><div class="info-label">Dog</div><div class="info-value">2030, 2018, 2006, 1994</div></div>
<div class="info-item"><div class="info-label">Pig</div><div class="info-value">2031, 2019, 2007, 1995</div></div>
</div></div>

<div class="card"><h2>2026 — Year of the Fire Horse</h2><div class="prose">
<p>The Fire Horse's energy will influence the entire world in 2026. This is a year of rapid movement, bold decisions, and new beginnings. The Horse in Chinese astrology represents freedom, travel, and ambition.</p>
<p>Those looking to start new businesses, travel, or make major life changes will find favorable conditions. However, the Fire element demands caution against impulsive decisions.</p>
<p>Each Chinese zodiac sign will experience this year differently. Rat and Monkey signs can expect career advancement, while Ox and Goat signs may need extra patience.</p>
</div></div>
</div>"""
    },
    {
        "file": "tarot.html",
        "title_hi": "आज का टैरो कार्ड",
        "title_en": "Daily Tarot Card",
        "meta": "आज का टैरो कार्ड — दैनिक टैरो रीडिंग और मार्गदर्शन। Daily Tarot card reading with interpretation and guidance",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>टैरो क्या है?</h2><div class="prose hi">
<p>टैरो कार्ड्स 78 कार्डों का एक प्राचीन समूह है जो सदियों से मार्गदर्शन और आत्मचिंतन के लिए उपयोग किया जाता रहा है। इसमें 22 मेजर आर्काना कार्ड हैं जो जीवन की प्रमुख घटनाओं और आध्यात्मिक पाठों को दर्शाते हैं, और 56 माइनर आर्काना कार्ड जो दैनिक जीवन की घटनाओं से संबंधित हैं।</p>
<p>टैरो भविष्य बताने का साधन नहीं है — यह आत्मचिंतन और मार्गदर्शन का उपकरण है। यह आपको अपनी वर्तमान परिस्थितियों को बेहतर समझने और सही निर्णय लेने में सहायता करता है।</p>
</div></div>

<div class="card"><h2>22 मेजर आर्काना कार्ड</h2><div class="prose hi">
<p><strong>0 — द फ़ूल (मूर्ख):</strong> नई शुरुआत, निर्दोषता, साहस। यह कार्ड बताता है कि नई यात्रा का समय आ गया है।</p>
<p><strong>I — द मैजिशियन (जादूगर):</strong> इच्छाशक्ति, कौशल, एकाग्रता। आपके पास वह सब कुछ है जो सफल होने के लिए चाहिए।</p>
<p><strong>II — हाई प्रीस्टेस (महापुरोहित):</strong> अंतर्ज्ञान, रहस्य, आंतरिक ज्ञान। अपनी आंतरिक आवाज़ सुनें।</p>
<p><strong>III — द एम्प्रेस (सम्राज्ञी):</strong> प्रकृति, उर्वरता, सौंदर्य। प्रेम और समृद्धि का समय।</p>
<p><strong>IV — द एम्परर (सम्राट):</strong> अधिकार, संरचना, नियंत्रण। नेतृत्व और अनुशासन की आवश्यकता।</p>
<p><strong>V — हाइरोफ़ेंट (धर्मगुरु):</strong> परंपरा, आध्यात्मिकता, शिक्षा। किसी गुरु या मार्गदर्शक की तलाश करें।</p>
<p><strong>VI — द लवर्स (प्रेमी):</strong> प्रेम, चुनाव, साझेदारी। महत्वपूर्ण निर्णय का समय।</p>
<p><strong>VII — द चैरियट (रथ):</strong> दृढ़ संकल्प, विजय, नियंत्रण। बाधाओं को पार करने की शक्ति।</p>
<p><strong>VIII — स्ट्रेंथ (शक्ति):</strong> आंतरिक शक्ति, साहस, धैर्य। कोमलता में ही असली शक्ति है।</p>
<p><strong>IX — द हर्मिट (सन्यासी):</strong> एकांत, आत्मचिंतन, ज्ञान की खोज। अकेले समय बिताने की आवश्यकता।</p>
<p><strong>X — व्हील ऑफ़ फ़ॉर्च�न (भाग्यचक्र):</strong> भाग्य, परिवर्तन, चक्र। जीवन में उतार-चढ़ाव स्वाभाविक हैं।</p>
</div></div>

<div class="card"><h2>टैरो कैसे पढ़ें?</h2><div class="prose hi">
<p>टैरो पढ़ने के लिए सबसे महत्वपूर्ण बात है — खुले मन से बैठना। किसी विशेष प्रश्न या स्थिति पर ध्यान केंद्रित करें।</p>
<p><strong>एक कार्ड रीडिंग:</strong> दिन की शुरुआत में एक कार्ड निकालें। यह आपके दिन का मार्गदर्शक विषय होगा।</p>
<p><strong>तीन कार्ड रीडिंग:</strong> तीन कार्ड निकालें — पहला अतीत, दूसरा वर्तमान, तीसरा भविष्य को दर्शाता है।</p>
<p><strong>उल्टा कार्ड:</strong> यदि कोई कार्ड उल्टा आता है तो उसका अर्थ विपरीत या अवरुद्ध ऊर्जा होता है।</p>
<p>टैरो को नियमित अभ्यास से सीखा जा सकता है। जितना अधिक आप अपने अंतर्ज्ञान पर विश्वास करेंगे, उतनी ही सटीक आपकी रीडिंग होगी।</p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>What is Tarot?</h2><div class="prose">
<p>Tarot is a set of 78 cards that has been used for centuries as a tool for guidance and self-reflection. It includes 22 Major Arcana cards representing life's major events and spiritual lessons, and 56 Minor Arcana cards relating to daily life situations.</p>
<p>Tarot is not fortune-telling — it is a mirror for self-understanding and a compass for decision-making. It helps you see your current situation from new perspectives and make more informed choices.</p>
</div></div>

<div class="card"><h2>The 22 Major Arcana cards</h2><div class="prose">
<p><strong>0 — The Fool:</strong> New beginnings, innocence, adventure. A fresh start awaits.</p>
<p><strong>I — The Magician:</strong> Willpower, skill, manifestation. You have everything you need to succeed.</p>
<p><strong>II — The High Priestess:</strong> Intuition, mystery, inner wisdom. Listen to your inner voice.</p>
<p><strong>III — The Empress:</strong> Nature, fertility, beauty. A time of love and abundance.</p>
<p><strong>IV — The Emperor:</strong> Authority, structure, control. Leadership and discipline needed.</p>
<p><strong>V — The Hierophant:</strong> Tradition, spirituality, teaching. Seek a mentor or guide.</p>
<p><strong>VI — The Lovers:</strong> Love, choices, partnership. Time for important decisions.</p>
<p><strong>VII — The Chariot:</strong> Determination, victory, willpower. Strength to overcome obstacles.</p>
<p><strong>VIII — Strength:</strong> Inner power, courage, patience. True strength lies in gentleness.</p>
<p><strong>IX — The Hermit:</strong> Solitude, reflection, wisdom-seeking. Time for inner contemplation.</p>
<p><strong>X — Wheel of Fortune:</strong> Destiny, change, cycles. Life's ups and downs are natural.</p>
</div></div>

<div class="card"><h2>How to read Tarot</h2><div class="prose">
<p>The most important thing in Tarot reading is approaching with an open mind. Focus on a specific question or situation.</p>
<p><strong>One-card reading:</strong> Draw a single card each morning. This becomes your guiding theme for the day.</p>
<p><strong>Three-card reading:</strong> Draw three cards — past, present, and future. This gives context to your current situation.</p>
<p><strong>Reversed cards:</strong> When a card appears upside down, it indicates blocked or reversed energy of that card's meaning.</p>
<p>Tarot is learned through regular practice. The more you trust your intuition, the more accurate your readings become.</p>
</div></div>
</div>"""
    },
    {
        "file": "numerology.html",
        "title_hi": "अंक ज्योतिष",
        "title_en": "Numerology",
        "meta": "अंक ज्योतिष — जन्म तिथि के आधार पर मूलांक, भाग्यांक और जीवन पथ संख्या। Numerology calculator with life path number and predictions",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>अंक ज्योतिष क्या है?</h2><div class="prose hi">
<p>अंक ज्योतिष (Numerology) एक प्राचीन विद्या है जो संख्याओं और उनके कंपन (vibrations) के माध्यम से व्यक्ति के जीवन, स्वभाव और भविष्य को समझने का प्रयास करती है। वैदिक अंक ज्योतिष में 1 से 9 तक के अंकों को नवग्रहों से जोड़ा जाता है।</p>
<p>प्रत्येक व्यक्ति का एक मूलांक (Root Number) होता है जो जन्म तिथि से निकाला जाता है, और एक भाग्यांक (Destiny Number) जो पूरी जन्म तारीख़ के योग से प्राप्त होता है।</p>
</div></div>

<div class="card"><h2>मूलांक कैसे निकालें?</h2><div class="prose hi">
<p>मूलांक आपकी जन्म तारीख़ का एकल अंक है। उदाहरण:</p>
<p>यदि जन्म तारीख़ है 27 — तो 2 + 7 = 9। आपका मूलांक 9 है।</p>
<p>यदि जन्म तारीख़ है 15 — तो 1 + 5 = 6। आपका मूलांक 6 है।</p>
</div></div>

<div class="card"><h2>अंकों का अर्थ</h2><div class="grid-3">
<div class="info-item"><div class="info-label">अंक 1 — सूर्य</div><div class="info-value">नेतृत्व, आत्मविश्वास</div></div>
<div class="info-item"><div class="info-label">अंक 2 — चंद्रमा</div><div class="info-value">संवेदनशीलता, कूटनीति</div></div>
<div class="info-item"><div class="info-label">अंक 3 — गुरु</div><div class="info-value">रचनात्मकता, आशावाद</div></div>
<div class="info-item"><div class="info-label">अंक 4 — राहु</div><div class="info-value">स्थिरता, मेहनत</div></div>
<div class="info-item"><div class="info-label">अंक 5 — बुध</div><div class="info-value">बुद्धि, संचार</div></div>
<div class="info-item"><div class="info-label">अंक 6 — शुक्र</div><div class="info-value">प्रेम, सौंदर्य</div></div>
<div class="info-item"><div class="info-label">अंक 7 — केतु</div><div class="info-value">आध्यात्मिकता, अंतर्ज्ञान</div></div>
<div class="info-item"><div class="info-label">अंक 8 — शनि</div><div class="info-value">अनुशासन, शक्ति</div></div>
<div class="info-item"><div class="info-label">अंक 9 — मंगल</div><div class="info-value">साहस, ऊर्जा</div></div>
</div></div>

<div class="card"><h2>अंक ज्योतिष और वैदिक ज्योतिष</h2><div class="prose hi">
<p>वैदिक अंक ज्योतिष में प्रत्येक अंक एक ग्रह से जुड़ा है। मूलांक 1 सूर्य से, 2 चंद्रमा से, 3 गुरु/बृहस्पति से, 4 राहु से, 5 बुध से, 6 शुक्र से, 7 केतु से, 8 शनि से और 9 मंगल से संबंधित है।</p>
<p>जब आपके मूलांक का ग्रह आपकी जन्म कुंडली के अनुकूल होता है, तो जीवन में सहजता आती है। विपरीत स्थिति में उपाय और मंत्रों से संतुलन लाया जा सकता है।</p>
<p>अंक ज्योतिष का उपयोग नाम सुधार, शुभ तिथि चयन, व्यवसाय नामकरण और जीवन साथी चयन में भी किया जाता है।</p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>What is Numerology?</h2><div class="prose">
<p>Numerology is an ancient science that uses numbers and their vibrations to understand a person's life, personality, and future. In Vedic numerology, numbers 1 through 9 are associated with the nine planets (Navagraha).</p>
<p>Every person has a Root Number (Moolank) derived from their birth date, and a Destiny Number (Bhagyank) calculated from the sum of their complete birth date.</p>
</div></div>

<div class="card"><h2>How to calculate your Root Number</h2><div class="prose">
<p>Your root number is the single digit sum of your birth date. Examples:</p>
<p>Born on the 27th: 2 + 7 = 9. Your root number is 9.</p>
<p>Born on the 15th: 1 + 5 = 6. Your root number is 6.</p>
</div></div>

<div class="card"><h2>Meaning of numbers</h2><div class="grid-3">
<div class="info-item"><div class="info-label">1 — Sun</div><div class="info-value">Leadership, confidence</div></div>
<div class="info-item"><div class="info-label">2 — Moon</div><div class="info-value">Sensitivity, diplomacy</div></div>
<div class="info-item"><div class="info-label">3 — Jupiter</div><div class="info-value">Creativity, optimism</div></div>
<div class="info-item"><div class="info-label">4 — Rahu</div><div class="info-value">Stability, hard work</div></div>
<div class="info-item"><div class="info-label">5 — Mercury</div><div class="info-value">Intelligence, communication</div></div>
<div class="info-item"><div class="info-label">6 — Venus</div><div class="info-value">Love, beauty</div></div>
<div class="info-item"><div class="info-label">7 — Ketu</div><div class="info-value">Spirituality, intuition</div></div>
<div class="info-item"><div class="info-label">8 — Saturn</div><div class="info-value">Discipline, power</div></div>
<div class="info-item"><div class="info-label">9 — Mars</div><div class="info-value">Courage, energy</div></div>
</div></div>
</div>"""
    },
    {
        "file": "muhurat.html",
        "title_hi": "शुभ मुहूर्त 2026",
        "title_en": "Auspicious Muhurat 2026",
        "meta": "शुभ मुहूर्त 2026 — विवाह, गृह प्रवेश, व्यापार शुभारम्भ के लिए शुभ तिथियाँ। Auspicious dates for marriage, housewarming, business in 2026",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>मुहूर्त क्या है?</h2><div class="prose hi">
<p>मुहूर्त वैदिक ज्योतिष की वह शाखा है जो किसी भी शुभ कार्य को आरम्भ करने का सर्वोत्तम समय निर्धारित करती है। हिन्दू संस्कृति में विवाह, गृह प्रवेश, व्यापार शुभारम्भ, यात्रा और अन्य महत्वपूर्ण कार्यों के लिए शुभ मुहूर्त देखना अत्यंत आवश्यक माना जाता है।</p>
<p>मुहूर्त निर्धारण में तिथि, नक्षत्र, योग, करण, वार और ग्रहों की स्थिति — इन सभी का विचार किया जाता है। अशुभ योगों जैसे राहुकाल, यमगंड और गुलिक काल से बचा जाता है।</p>
</div></div>

<div class="card"><h2>2026 में विवाह के शुभ मुहूर्त</h2><div class="prose hi">
<p>हिन्दू विवाह के लिए सबसे शुभ माह माने जाते हैं — मार्गशीर्ष, माघ, फाल्गुन और वैशाख। 2026 में प्रमुख विवाह मुहूर्त इस प्रकार हैं:</p>
<p><strong>अप्रैल 2026:</strong> 16, 17, 20, 24, 27 अप्रैल</p>
<p><strong>मई 2026:</strong> 4, 7, 11, 15, 18 मई</p>
<p><strong>जून 2026:</strong> 1, 5, 8, 12 जून (उसके बाद चातुर्मास प्रारम्भ)</p>
<p><strong>नवम्बर 2026:</strong> 16, 20, 23, 27, 30 नवम्बर (देवउठनी एकादशी के बाद)</p>
<p><strong>दिसम्बर 2026:</strong> 1, 4, 7, 11, 14 दिसम्बर</p>
<p><em>नोट: ये सामान्य शुभ तिथियाँ हैं। व्यक्तिगत कुंडली मिलान के आधार पर विशेष मुहूर्त निकलवाना आवश्यक है।</em></p>
</div></div>

<div class="card"><h2>गृह प्रवेश मुहूर्त 2026</h2><div class="prose hi">
<p>नए घर में प्रवेश के लिए सर्वोत्तम माह हैं — वैशाख, ज्येष्ठ, माघ और फाल्गुन। गृह प्रवेश के समय गृह स्वामी का सूर्य बली होना चाहिए और चतुर्थ भाव शुभ ग्रहों से दृष्ट होना चाहिए।</p>
<p>गृह प्रवेश से पूर्व गणपति पूजा, वास्तु शांति और हवन करना शुभ माना जाता है।</p>
</div></div>

<div class="card"><h2>व्यापार शुभारम्भ मुहूर्त</h2><div class="prose hi">
<p>नया व्यापार शुरू करने के लिए बुधवार और गुरुवार सर्वोत्तम वार माने जाते हैं। बुध (व्यापार का ग्रह) और गुरु (शुभ ग्रह) बली होने चाहिए।</p>
<p>शुभ नक्षत्र: रोहिणी, मृगशिरा, पुष्य, अश्विनी, रेवती, अनुराधा।</p>
<p>अशुभ नक्षत्र: भरणी, कृत्तिका, आश्लेषा, ज्येष्ठा — इन नक्षत्रों में नया कार्य प्रारम्भ न करें।</p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>What is Muhurat?</h2><div class="prose">
<p>Muhurat is the branch of Vedic astrology that determines the most auspicious time to begin any important activity. In Hindu culture, finding a good muhurat for marriage, housewarming, business launch, travel, and other significant events is considered essential.</p>
<p>Muhurat calculation considers tithi, nakshatra, yoga, karana, weekday, and planetary positions. Inauspicious periods like Rahu Kaal, Yama Ganda, and Gulika Kaal are carefully avoided.</p>
</div></div>

<div class="card"><h2>Marriage Muhurat 2026</h2><div class="prose">
<p>The most auspicious months for Hindu marriages are Margashirsha, Magha, Phalguna, and Vaishakha. Key marriage muhurat dates in 2026:</p>
<p><strong>April 2026:</strong> 16, 17, 20, 24, 27</p>
<p><strong>May 2026:</strong> 4, 7, 11, 15, 18</p>
<p><strong>June 2026:</strong> 1, 5, 8, 12 (Chaturmas begins after)</p>
<p><strong>November 2026:</strong> 16, 20, 23, 27, 30 (after Dev Uthani Ekadashi)</p>
<p><strong>December 2026:</strong> 1, 4, 7, 11, 14</p>
<p><em>Note: These are general auspicious dates. Personal kundli matching is recommended for specific muhurat.</em></p>
</div></div>
</div>"""
    },
    {
        "file": "transits.html",
        "title_hi": "ग्रह गोचर 2026",
        "title_en": "Planetary Transits 2026",
        "meta": "ग्रह गोचर 2026 — शनि, गुरु, राहु-केतु के गोचर का 12 राशियों पर प्रभाव। Planetary transits 2026 and their effects on all zodiac signs",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>ग्रह गोचर क्या है?</h2><div class="prose hi">
<p>ग्रह गोचर (Planetary Transit) का अर्थ है ग्रहों का एक राशि से दूसरी राशि में संक्रमण। वैदिक ज्योतिष में गोचर का अत्यंत महत्व है क्योंकि ग्रहों की बदलती स्थिति का सीधा प्रभाव हमारे जीवन पर पड़ता है।</p>
<p>धीमी गति वाले ग्रह — शनि (2.5 वर्ष), गुरु (1 वर्ष), राहु-केतु (1.5 वर्ष) — के गोचर का प्रभाव सबसे गहरा और दीर्घकालिक होता है।</p>
</div></div>

<div class="card"><h2>शनि गोचर 2026</h2><div class="prose hi">
<p>शनि इस समय मीन (Pisces) राशि में विराजमान हैं। शनि का गोचर सभी राशियों को प्रभावित करता है, विशेषकर मकर, कुम्भ और मीन राशि के जातकों को।</p>
<p><strong>साढ़ेसाती प्रभावित राशियाँ:</strong> कुम्भ (अंतिम चरण), मीन (मध्य चरण), मेष (प्रथम चरण)। इन राशि वालों को धैर्य, अनुशासन और कठोर परिश्रम करना होगा।</p>
<p><strong>ढैय्या प्रभावित:</strong> सिंह और तुला राशि के जातकों को शनि की ढैय्या चल रही है।</p>
<p>शनि के उपाय: शनिवार को तिल दान, काले वस्त्र पहनना, हनुमान चालीसा का पाठ, लोहे की अंगूठी धारण करना।</p>
</div></div>

<div class="card"><h2>गुरु (बृहस्पति) गोचर 2026</h2><div class="prose hi">
<p>गुरु 2026 में मिथुन राशि से कर्क राशि में प्रवेश करेंगे। गुरु का कर्क राशि में गोचर अत्यंत शुभ माना जाता है क्योंकि गुरु कर्क राशि में उच्च (exalted) होते हैं।</p>
<p>यह गोचर विशेष रूप से कर्क, वृश्चिक और मीन राशि वालों के लिए अत्यंत शुभ रहेगा। शिक्षा, संतान, धार्मिक कार्य और आध्यात्मिक उन्नति में लाभ होगा।</p>
</div></div>

<div class="card"><h2>राहु-केतु गोचर 2026</h2><div class="prose hi">
<p>राहु-केतु दिसम्बर 2026 में मकर-कर्क अक्ष पर आएंगे। यह गोचर विशेष रूप से मकर और कर्क राशि वालों के जीवन में बड़े परिवर्तन लाएगा।</p>
<p>राहु मकर राशि में व्यक्ति को महत्वाकांक्षी बनाता है, सत्ता और पद की इच्छा बढ़ाता है। केतु कर्क राशि में भावनात्मक वैराग्य और आध्यात्मिक जागृति लाता है।</p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>What are Planetary Transits?</h2><div class="prose">
<p>Planetary transits (Gochara) refer to planets moving from one zodiac sign to another. In Vedic astrology, transits have immense significance because changing planetary positions directly impact our lives.</p>
<p>Slow-moving planets — Saturn (2.5 years per sign), Jupiter (1 year), Rahu-Ketu (1.5 years) — have the deepest and most lasting effects.</p>
</div></div>

<div class="card"><h2>Saturn Transit 2026</h2><div class="prose">
<p>Saturn is currently transiting through Pisces. Saturn's transit affects all signs, especially Capricorn, Aquarius, and Pisces natives.</p>
<p><strong>Sade Sati affected signs:</strong> Aquarius (final phase), Pisces (peak phase), Aries (beginning phase). These signs need patience, discipline, and hard work.</p>
<p><strong>Dhaiyya affected:</strong> Leo and Libra natives are experiencing Saturn's Dhaiyya period.</p>
</div></div>

<div class="card"><h2>Jupiter Transit 2026</h2><div class="prose">
<p>Jupiter will move from Gemini to Cancer in 2026. Jupiter's transit through Cancer is considered extremely auspicious as Jupiter becomes exalted in Cancer.</p>
<p>This transit is especially favorable for Cancer, Scorpio, and Pisces signs. Benefits in education, children, religious activities, and spiritual growth can be expected.</p>
</div></div>
</div>"""
    },
    {
        "file": "nifty-prediction.html",
        "title_hi": "निफ्टी ज्योतिषीय भविष्यवाणी 2026",
        "title_en": "Nifty Astrological Prediction 2026",
        "meta": "निफ्टी और शेयर बाज़ार का ज्योतिषीय विश्लेषण 2026। Nifty stock market astrological prediction and planetary analysis 2026",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>वित्तीय ज्योतिष क्या है?</h2><div class="prose hi">
<p>वित्तीय ज्योतिष (Financial Astrology) ज्योतिष की वह शाखा है जो ग्रहों की स्थिति के आधार पर शेयर बाज़ार, मुद्रा बाज़ार और आर्थिक रुझानों का विश्लेषण करती है। भारत में प्रसिद्ध ज्योतिषी इसे "Astro-Economics" या "Market Astrology" भी कहते हैं।</p>
<p><strong>महत्वपूर्ण अस्वीकरण:</strong> ज्योतिषीय विश्लेषण केवल सामान्य मार्गदर्शन के लिए है। निवेश निर्णय हमेशा SEBI-पंजीकृत वित्तीय सलाहकार की सलाह से लें। बाज़ार जोखिम के अधीन है।</p>
</div></div>

<div class="card"><h2>2026 में ग्रहों का बाज़ार पर प्रभाव</h2><div class="prose hi">
<p><strong>गुरु का कर्क में उच्च:</strong> गुरु जब कर्क राशि में उच्च होते हैं, ऐतिहासिक रूप से बैंकिंग, रियल एस्टेट और कृषि क्षेत्र में तेज़ी देखी गई है। 2026 के मध्य में यह योग बनेगा।</p>
<p><strong>शनि मीन में:</strong> शनि मीन राशि में फ़ार्मा, तेल और गैस, तथा समुद्री उद्योग को प्रभावित करता है। इन क्षेत्रों में उतार-चढ़ाव रह सकता है।</p>
<p><strong>राहु-केतु अक्ष परिवर्तन:</strong> दिसम्बर 2026 में राहु-केतु अक्ष बदलने से IT, बैंकिंग और इंफ्रा सेक्टर में बड़ी हलचल संभव है।</p>
</div></div>

<div class="card"><h2>तिमाही विश्लेषण</h2><div class="prose hi">
<p><strong>Q1 (जनवरी-मार्च):</strong> बुध और शुक्र के गोचर से IT और ऑटो सेक्टर में सकारात्मक रुझान। बजट के आसपास अस्थिरता।</p>
<p><strong>Q2 (अप्रैल-जून):</strong> गुरु की राशि परिवर्तन के कारण बैंकिंग सेक्टर में तेज़ी की संभावना। मिडकैप शेयरों पर ध्यान दें।</p>
<p><strong>Q3 (जुलाई-सितम्बर):</strong> मानसून और ग्रह स्थिति के आधार पर कृषि और FMCG सेक्टर प्रभावित। रक्षात्मक रणनीति उचित।</p>
<p><strong>Q4 (अक्टूबर-दिसम्बर):</strong> त्योहारी सीज़न में उपभोक्ता क्षेत्र में तेज़ी। राहु-केतु परिवर्तन के कारण दिसम्बर में सावधानी आवश्यक।</p>
<p><em>पुनः अस्वीकरण: यह ज्योतिषीय दृष्टिकोण मात्र है, निवेश सलाह नहीं। सभी निवेश बाज़ार जोखिम के अधीन हैं।</em></p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>What is Financial Astrology?</h2><div class="prose">
<p>Financial Astrology analyzes stock market trends and economic patterns based on planetary positions. In India, this is also known as "Market Astrology" or "Astro-Economics."</p>
<p><strong>Important disclaimer:</strong> Astrological analysis is for general guidance only. Always consult a SEBI-registered financial advisor for investment decisions. Markets are subject to risk.</p>
</div></div>

<div class="card"><h2>Planetary impact on markets in 2026</h2><div class="prose">
<p><strong>Jupiter exalted in Cancer:</strong> Historically, Jupiter's exaltation has correlated with bullish trends in banking, real estate, and agriculture sectors. This alignment occurs mid-2026.</p>
<p><strong>Saturn in Pisces:</strong> Saturn in Pisces influences pharma, oil and gas, and maritime industries. Expect volatility in these sectors.</p>
<p><strong>Rahu-Ketu axis change:</strong> The December 2026 axis shift may trigger significant movement in IT, banking, and infrastructure sectors.</p>
</div></div>
</div>"""
    },
]

# ═══════════════════════════════════════
# FESTIVAL PAGES — Puja Vidhi, Katha, Significance
# ═══════════════════════════════════════

FESTIVAL_PAGES = [
    {
        "file": "diwali-puja-vidhi.html",
        "title_hi": "दिवाली पूजा विधि, कथा और महत्व",
        "title_en": "Diwali Puja Vidhi, Story and Significance",
        "meta": "दिवाली पूजा विधि, लक्ष्मी-गणेश पूजा, दीपावली की कथा और महत्व। Diwali Lakshmi Ganesh Puja method, story and significance",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>दीपावली का महत्व</h2><div class="prose hi">
<p>दीपावली हिन्दू धर्म का सबसे बड़ा त्योहार है। यह पाँच दिवसीय उत्सव है — धनतेरस, नरक चतुर्दशी, दीपावली, गोवर्धन पूजा और भाई दूज। दीपावली का अर्थ है "दीपों की पंक्ति" — अंधकार पर प्रकाश की, अज्ञान पर ज्ञान की और बुराई पर अच्छाई की विजय।</p>
<p>इस दिन भगवान श्री राम 14 वर्ष का वनवास पूरा करके अयोध्या लौटे थे। अयोध्यावासियों ने उनके स्वागत में दीप जलाए, और तभी से यह परम्परा चली आ रही है।</p>
<p>दीपावली पर लक्ष्मी-गणेश की पूजा का विशेष महत्व है। माँ लक्ष्मी धन और समृद्धि की देवी हैं, और भगवान गणेश विघ्नहर्ता हैं — दोनों की संयुक्त पूजा से घर में सुख-समृद्धि आती है।</p>
</div></div>

<div class="card"><h2>दीपावली लक्ष्मी-गणेश पूजा विधि</h2><div class="prose hi">
<p><strong>पूजा सामग्री:</strong></p>
<p>लक्ष्मी-गणेश की मूर्ति या चित्र, कमल का फूल, धूप, दीपक, अक्षत (चावल), सिन्दूर, हल्दी, कुमकुम, चन्दन, मिठाई, फल, पान-सुपारी, नारियल, कलश, आम के पत्ते, लाल कपड़ा, पुष्प, दक्षिणा के सिक्के।</p>
<p><strong>पूजा विधि (चरणबद्ध):</strong></p>
<p>1. सबसे पहले घर की सफ़ाई करें और पूजा स्थान को गंगाजल से शुद्ध करें।</p>
<p>2. लाल कपड़ा बिछाकर कलश स्थापित करें। कलश में जल, सुपारी, सिक्का और आम के पत्ते रखें।</p>
<p>3. लक्ष्मी-गणेश की मूर्ति स्थापित करें। पहले गणेश जी की पूजा करें (विघ्नहर्ता होने के कारण)।</p>
<p>4. गणेश जी को सिन्दूर, दूर्वा (दूब), मोदक अर्पित करें। "ॐ गं गणपतये नमः" मंत्र का 108 बार जाप करें।</p>
<p>5. फिर माँ लक्ष्मी की पूजा करें — कमल, हल्दी, कुमकुम, सिन्दूर, धान और सिक्के अर्पित करें।</p>
<p>6. "ॐ श्रीं ह्रीं श्रीं महालक्ष्म्यै नमः" मंत्र का 108 बार जाप करें।</p>
<p>7. आरती करें — "ॐ जय लक्ष्मी माता" गाएं।</p>
<p>8. प्रसाद वितरित करें और घर के चारों कोनों में दीपक जलाएं।</p>
</div></div>

<div class="card"><h2>दीपावली की कथा — राम की अयोध्या वापसी</h2><div class="prose hi">
<p>त्रेता युग में अयोध्या के राजा दशरथ के चार पुत्र थे — राम, लक्ष्मण, भरत और शत्रुघ्न। रानी कैकेयी ने दो वरदानों का उपयोग करते हुए राम को 14 वर्ष का वनवास और भरत को राजगद्दी माँगी।</p>
<p>राम सीता और लक्ष्मण के साथ वन चले गए। वनवास के दौरान रावण ने सीता का हरण किया। भगवान राम ने वानरों की सेना के साथ लंका पर आक्रमण किया और रावण का वध करके सीता को मुक्त कराया।</p>
<p>14 वर्ष का वनवास पूरा करके जब राम अयोध्या लौटे, तो समस्त नगरवासियों ने घी के दीपक जलाकर उनका स्वागत किया। उस रात्रि को अमावस्या थी, लेकिन दीपों के प्रकाश से सम्पूर्ण अयोध्या जगमगा उठी।</p>
<p>तभी से प्रतिवर्ष कार्तिक मास की अमावस्या को दीपावली मनाई जाती है। यह त्योहार हमें सिखाता है कि अंधकार कितना भी गहरा हो, एक छोटा सा दीपक भी उसे दूर कर सकता है।</p>
</div></div>

<div class="highlight"><p>ॐ जय लक्ष्मी माता, मैया जय लक्ष्मी माता। तुमको निशदिन सेवत, हरि विष्णु धाता।</p></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>Significance of Diwali</h2><div class="prose">
<p>Diwali is the biggest festival in Hinduism — a five-day celebration encompassing Dhanteras, Naraka Chaturdashi, Deepawali, Govardhan Puja, and Bhai Dooj. The word "Deepawali" means "row of lamps" — symbolizing the victory of light over darkness, knowledge over ignorance, and good over evil.</p>
<p>On this day, Lord Rama returned to Ayodhya after completing 14 years of exile. The citizens lit thousands of earthen lamps to welcome him home, and this tradition continues to this day.</p>
</div></div>

<div class="card"><h2>Diwali Lakshmi-Ganesh Puja method</h2><div class="prose">
<p><strong>Puja materials needed:</strong> Lakshmi-Ganesh idols, lotus flowers, incense, lamp, rice, sindoor, turmeric, kumkum, sandalwood, sweets, fruits, betel leaves, coconut, kalash, mango leaves, red cloth, coins for offering.</p>
<p><strong>Step-by-step puja vidhi:</strong></p>
<p>1. Clean the house and purify the puja area with Ganga water.</p>
<p>2. Place a red cloth and set up the kalash with water, betel nut, coin, and mango leaves.</p>
<p>3. Install Lakshmi-Ganesh idols. Worship Ganesh first (as the remover of obstacles).</p>
<p>4. Offer sindoor, durva grass, and modak to Ganesh. Chant "Om Gam Ganapataye Namah" 108 times.</p>
<p>5. Then worship Goddess Lakshmi — offer lotus, turmeric, kumkum, rice, and coins.</p>
<p>6. Chant "Om Shreem Hreem Shreem Mahalakshmyai Namah" 108 times.</p>
<p>7. Perform aarti — sing "Om Jai Lakshmi Mata."</p>
<p>8. Distribute prasad and light lamps in all corners of the home.</p>
</div></div>
</div>"""
    },
    {
        "file": "navratri-puja.html",
        "title_hi": "नवरात्रि पूजा विधि, नौ देवियाँ और व्रत कथा",
        "title_en": "Navratri Puja Vidhi, Nine Goddesses and Fasting",
        "meta": "नवरात्रि पूजा विधि, कलश स्थापना, 9 देवियों की पूजा, व्रत नियम और कथा। Navratri puja method, 9 forms of Durga and fasting rules",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>नवरात्रि का महत्व</h2><div class="prose hi">
<p>नवरात्रि हिन्दू धर्म का एक महत्वपूर्ण त्योहार है जो वर्ष में दो बार मनाया जाता है — चैत्र नवरात्रि (मार्च-अप्रैल) और शारदीय नवरात्रि (सितम्बर-अक्टूबर)। नौ रातों तक माँ दुर्गा के नौ स्वरूपों की पूजा की जाती है।</p>
<p>नवरात्रि का अर्थ है "नौ रातें" — ये नौ रातें आध्यात्मिक साधना, उपवास और देवी उपासना को समर्पित हैं। दसवें दिन विजयदशमी (दशहरा) मनाया जाता है जो बुराई पर अच्छाई की विजय का प्रतीक है।</p>
</div></div>

<div class="card"><h2>माँ दुर्गा के नौ रूप</h2><div class="prose hi">
<p><strong>प्रथम — शैलपुत्री:</strong> पर्वतराज हिमालय की पुत्री। नवरात्रि के प्रथम दिन इनकी पूजा की जाती है। वाहन वृषभ (नंदी)। रंग: लाल।</p>
<p><strong>द्वितीय — ब्रह्मचारिणी:</strong> तपस्या का प्रतीक। हाथ में कमण्डलु और जपमाला। रंग: नीला।</p>
<p><strong>तृतीय — चंद्रघंटा:</strong> मस्तक पर अर्धचन्द्राकार घंटा। शौर्य और साहस की देवी। रंग: पीला।</p>
<p><strong>चतुर्थ — कूष्माण्डा:</strong> सृष्टि की रचयित्री। सूर्य मंडल में निवास। रंग: हरा।</p>
<p><strong>पंचम — स्कन्दमाता:</strong> कार्तिकेय की माता। कमल पर विराजमान। रंग: सलेटी।</p>
<p><strong>षष्ठ — कात्यायनी:</strong> महर्षि कात्यायन की पुत्री। विवाह के लिए कन्याएं इनकी पूजा करती हैं। रंग: नारंगी।</p>
<p><strong>सप्तम — कालरात्रि:</strong> भयंकर रूप, लेकिन शुभ फलदायिनी। काले रंग की देवी। रंग: सफ़ेद।</p>
<p><strong>अष्टम — महागौरी:</strong> गौर वर्ण, शांत स्वभाव। पापों का नाश करने वाली। रंग: गुलाबी।</p>
<p><strong>नवम — सिद्धिदात्री:</strong> सभी सिद्धियों की दात्री। कमल पर विराजमान। रंग: बैंगनी।</p>
</div></div>

<div class="card"><h2>कलश स्थापना विधि</h2><div class="prose hi">
<p>नवरात्रि के प्रथम दिन कलश स्थापना की जाती है। यह पूरे नौ दिनों की पूजा का आधार है।</p>
<p><strong>सामग्री:</strong> मिट्टी का कलश, जल, सुपारी, सिक्का, आम के पत्ते, नारियल, लाल कपड़ा, जौ के बीज, मिट्टी, अखंड ज्योति का दीपक।</p>
<p><strong>विधि:</strong> शुभ मुहूर्त में स्नान करके शुद्ध वस्त्र पहनें। पूजा स्थान पर मिट्टी से वेदी बनाएं, उस पर जौ के बीज बोएं। कलश में जल, सुपारी, सिक्का और अक्षत डालें। कलश पर आम के पत्ते और नारियल रखें। कलश को लाल कपड़े से सजाएं। अखंड ज्योति प्रज्वलित करें जो नौ दिनों तक जलती रहे।</p>
</div></div>

<div class="card"><h2>नवरात्रि व्रत नियम</h2><div class="prose hi">
<p>नवरात्रि में नौ दिनों का उपवास रखा जाता है। कुछ लोग पूर्ण उपवास करते हैं, कुछ फलाहार करते हैं।</p>
<p><strong>व्रत में खाने योग्य:</strong> कुट्टू का आटा, साबूदाना, सिंघाड़ा आटा, आलू, मूंगफली, दूध, दही, फल, सेंधा नमक।</p>
<p><strong>व्रत में वर्जित:</strong> अनाज (गेहूँ, चावल), दाल, प्याज, लहसुन, माँस, मदिरा, तम्बाकू।</p>
<p><strong>अन्य नियम:</strong> ब्रह्मचर्य का पालन, सात्विक आचरण, भूमि पर शयन (वैकल्पिक), दैनिक दुर्गा सप्तशती/चंडी पाठ।</p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>Significance of Navratri</h2><div class="prose">
<p>Navratri is a major Hindu festival celebrated twice a year — Chaitra Navratri (March-April) and Sharadiya Navratri (September-October). For nine nights, the nine forms of Goddess Durga are worshipped.</p>
<p>"Navratri" means "nine nights" dedicated to spiritual practice, fasting, and goddess worship. The tenth day is Vijayadashami (Dussehra), symbolizing the victory of good over evil.</p>
</div></div>

<div class="card"><h2>Nine forms of Goddess Durga</h2><div class="prose">
<p><strong>Day 1 — Shailaputri:</strong> Daughter of the mountain king Himalaya. Color: Red.</p>
<p><strong>Day 2 — Brahmacharini:</strong> Symbol of penance. Color: Blue.</p>
<p><strong>Day 3 — Chandraghanta:</strong> Goddess of bravery. Color: Yellow.</p>
<p><strong>Day 4 — Kushmanda:</strong> Creator of the universe. Color: Green.</p>
<p><strong>Day 5 — Skandamata:</strong> Mother of Kartikeya. Color: Gray.</p>
<p><strong>Day 6 — Katyayani:</strong> Worshipped for marriage. Color: Orange.</p>
<p><strong>Day 7 — Kaalratri:</strong> Fierce but auspicious. Color: White.</p>
<p><strong>Day 8 — Mahagauri:</strong> Destroyer of sins. Color: Pink.</p>
<p><strong>Day 9 — Siddhidatri:</strong> Giver of supernatural powers. Color: Purple.</p>
</div></div>
</div>"""
    },
    {
        "file": "dussehra-puja.html",
        "title_hi": "दशहरा — विजयदशमी पूजा विधि, कथा और परम्पराएं",
        "title_en": "Dussehra Puja Vidhi, Story and Traditions",
        "meta": "दशहरा विजयदशमी पूजा विधि, रावण दहन, शस्त्र पूजा, कथा और क्षेत्रीय परम्पराएं। Dussehra Vijayadashami puja, Ravana Dahan traditions",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>दशहरा (विजयदशमी) का महत्व</h2><div class="prose hi">
<p>दशहरा या विजयदशमी अश्विन मास के शुक्ल पक्ष की दशमी तिथि को मनाया जाता है। यह नवरात्रि के बाद दसवें दिन आता है और बुराई पर अच्छाई की विजय का प्रतीक है।</p>
<p>इस दिन दो महान विजयों का स्मरण किया जाता है — भगवान राम द्वारा रावण का वध और माँ दुर्गा द्वारा महिषासुर का संहार। दोनों ही कथाएं बताती हैं कि अधर्म चाहे कितना भी शक्तिशाली हो, धर्म की अंततः विजय होती है।</p>
</div></div>

<div class="card"><h2>दशहरा पूजा विधि</h2><div class="prose hi">
<p><strong>शस्त्र पूजा (आयुध पूजा):</strong> दशहरा पर शस्त्रों और उपकरणों की पूजा करने की प्राचीन परम्परा है। आज के समय में लोग अपने वाहन, कम्प्यूटर, मशीनें और कार्य के उपकरणों की पूजा करते हैं।</p>
<p>1. शस्त्र/उपकरण को साफ़ करें और पूजा स्थान पर रखें।</p>
<p>2. हल्दी-कुमकुम, पुष्प और अक्षत से पूजा करें।</p>
<p>3. "ॐ विजयदशम्यै नमः" मंत्र का जाप करें।</p>
<p>4. नारियल फोड़ें और प्रसाद वितरित करें।</p>
<p><strong>अपराजिता पूजा:</strong> विजयदशमी पर अपराजिता (नील फूल) की पूजा का विशेष महत्व है। यह पूजा विजय प्राप्ति और शत्रु निवारण के लिए की जाती है।</p>
<p><strong>शमी वृक्ष पूजा:</strong> शमी का पेड़ दशहरा पर पूजनीय है। मान्यता है कि पांडवों ने अज्ञातवास के समय इसी पेड़ पर अपने शस्त्र छिपाए थे।</p>
</div></div>

<div class="card"><h2>भारत में दशहरा की विभिन्न परम्पराएं</h2><div class="prose hi">
<p><strong>उत्तर भारत — रावण दहन:</strong> विशाल रावण, मेघनाद और कुम्भकर्ण के पुतले बनाकर उन्हें जलाया जाता है। राम लीला का आयोजन होता है। दिल्ली की रामलीला विश्वप्रसिद्ध है।</p>
<p><strong>मैसूर — दशहरा उत्सव:</strong> कर्नाटक के मैसूर का दशहरा विश्वविख्यात है। मैसूर पैलेस की भव्य रोशनी और शाही जुलूस इसकी विशेषता है।</p>
<p><strong>पश्चिम बंगाल — सिंदूर खेला:</strong> दुर्गा पूजा के बाद विजयदशमी पर विवाहित स्त्रियाँ एक-दूसरे को सिंदूर लगाती हैं। माँ दुर्गा की मूर्तियों का विसर्जन किया जाता है।</p>
<p><strong>गुजरात — गरबा/रास:</strong> नवरात्रि से दशहरा तक रात भर गरबा और दांडिया रास होता है।</p>
<p><strong>हिमाचल — कुल्लू दशहरा:</strong> कुल्लू में दशहरा 7 दिनों तक मनाया जाता है। सभी देवी-देवताओं को रथ में सजाकर मेले में लाया जाता है।</p>
</div></div>

<div class="card"><h2>रावण वध की कथा</h2><div class="prose hi">
<p>लंकापति रावण अत्यंत विद्वान और शक्तिशाली था। ब्रह्मा से उसने ऐसा वरदान प्राप्त किया था कि कोई देवता या दानव उसे मार नहीं सकता। इस घमंड में उसने मनुष्यों को तुच्छ समझा।</p>
<p>रावण ने छल से माता सीता का हरण किया। भगवान राम ने समुद्र पर सेतु बनाकर लंका पर आक्रमण किया। भीषण युद्ध के बाद दशमी के दिन भगवान राम ने रावण की नाभि में बाण मारकर उसका वध किया।</p>
<p>रावण की दस भुजाएं और दस सिर उसके दस बुराइयों — काम, क्रोध, लोभ, मोह, मद, मत्सर, अहंकार, आलस्य, हिंसा और चोरी — का प्रतीक हैं। दशहरा हमें सिखाता है कि अपने भीतर के रावण को जलाना सबसे बड़ी विजय है।</p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>Significance of Dussehra</h2><div class="prose">
<p>Dussehra or Vijayadashami is celebrated on the tenth day of Shukla Paksha in the month of Ashwin. It marks the triumph of good over evil, commemorating two great victories — Lord Rama's defeat of Ravana and Goddess Durga's slaying of Mahishasura.</p>
</div></div>

<div class="card"><h2>Dussehra traditions across India</h2><div class="prose">
<p><strong>North India — Ravana Dahan:</strong> Giant effigies of Ravana, Meghnad, and Kumbhakarna are burned. Ram Lila performances precede the celebration.</p>
<p><strong>Mysore — Royal Dussehra:</strong> Karnataka's Mysore Dussehra is world-famous for its royal procession and illuminated palace.</p>
<p><strong>West Bengal — Sindoor Khela:</strong> Married women apply vermillion on each other after Durga Puja. Durga idols are immersed in water.</p>
<p><strong>Gujarat — Garba/Raas:</strong> Nine nights of garba and dandiya raas dancing.</p>
<p><strong>Himachal — Kullu Dussehra:</strong> A unique 7-day festival where deities are carried in processions.</p>
</div></div>
</div>"""
    },
    {
        "file": "karwa-chauth-katha.html",
        "title_hi": "करवा चौथ व्रत कथा, पूजा विधि और महत्व",
        "title_en": "Karwa Chauth Vrat Katha, Puja Vidhi and Significance",
        "meta": "करवा चौथ व्रत कथा, पूजा विधि, सरगी, चंद्र दर्शन। Karwa Chauth fast story, puja method, sargi and moon sighting traditions",
        "body_hi": """<div class="hi-only">
<div class="card"><h2>करवा चौथ का महत्व</h2><div class="prose hi">
<p>करवा चौथ कार्तिक मास के कृष्ण पक्ष की चतुर्थी तिथि को मनाया जाता है। यह विवाहित स्त्रियों का सबसे महत्वपूर्ण व्रत है, जिसमें वे अपने पति की दीर्घायु और सुखमय जीवन के लिए निर्जला (बिना पानी) व्रत रखती हैं।</p>
<p>इस व्रत की विशेषता है कि चंद्रोदय के बाद चंद्रमा को अर्घ्य देकर ही व्रत खोला जाता है। पति छलनी से चंद्रमा दिखाकर पत्नी को पानी पिलाता है — यह क्षण अत्यंत भावनात्मक और पवित्र माना जाता है।</p>
</div></div>

<div class="card"><h2>करवा चौथ पूजा विधि</h2><div class="prose hi">
<p><strong>सरगी:</strong> सूर्योदय से पहले सास द्वारा बहू को सरगी दी जाती है — इसमें मिठाई, फल, मेवे और फेनिया शामिल होती हैं। बहू सूर्योदय से पहले सरगी खाकर व्रत का संकल्प लेती है।</p>
<p><strong>दिन में:</strong> सोलह श्रृंगार करें — बिंदी, सिंदूर, चूड़ियाँ, मेहंदी, पायल आदि। व्रती महिलाएं दिन में मिलकर करवा चौथ की कथा सुनती हैं।</p>
<p><strong>शाम की पूजा:</strong></p>
<p>1. दीवार पर गेरू या मेहंदी से करवा चौथ की पूजा का चित्र बनाएं (या छलनी पर बनाएं)।</p>
<p>2. गौरी-गणेश, शिव-पार्वती और चंद्रमा की पूजा करें।</p>
<p>3. करवा (मिट्टी का छोटा बर्तन) में जल भरकर रखें।</p>
<p>4. करवा चौथ की कथा सुनें (सामूहिक रूप से)।</p>
<p>5. चंद्रोदय के बाद चंद्रमा को छलनी से देखें, अर्घ्य दें।</p>
<p>6. पति छलनी से पत्नी को चंद्रमा दिखाएं, फिर पानी और मिठाई खिलाकर व्रत खोलें।</p>
</div></div>

<div class="card"><h2>करवा चौथ की कथा</h2><div class="prose hi">
<p>प्राचीन काल में एक ब्राह्मण के सात पुत्र और एक पुत्री थी जिसका नाम वीरवती था। वीरवती का विवाह एक सम्पन्न परिवार में हुआ। विवाह के बाद पहला करवा चौथ आया।</p>
<p>वीरवती ने निर्जला व्रत रखा। परन्तु शाम होते-होते उससे भूख-प्यास सहन नहीं हुई और वह बेहोश होने लगी। उसके सातों भाइयों से उसकी दशा देखी नहीं गई।</p>
<p>भाइयों ने एक युक्ति सोची — उन्होंने पीपल के पेड़ पर छलनी के पीछे दीपक जलाकर रख दिया और वीरवती से कहा कि चंद्रमा निकल आया है। वीरवती ने उस नकली चंद्रमा को देखकर व्रत खोल लिया।</p>
<p>जैसे ही उसने अन्न-जल ग्रहण किया, उसके पति की मृत्यु हो गई। वीरवती ने वर्ष भर तप और पूजा की। अगले करवा चौथ पर उसने पूर्ण विधि-विधान से व्रत रखा और माता पार्वती की कृपा से उसका पति पुनर्जीवित हो गया।</p>
<p>इसीलिए कहा जाता है कि करवा चौथ का व्रत पूर्ण श्रद्धा और विधि से रखना चाहिए।</p>
</div></div>
</div>""",
        "body_en": """<div class="en-only">
<div class="card"><h2>Significance of Karwa Chauth</h2><div class="prose">
<p>Karwa Chauth is observed on the Chaturthi of Krishna Paksha in the month of Kartik. It is the most important fast for married women, who observe a waterless (nirjala) fast for the long life and happiness of their husbands.</p>
<p>The fast is broken only after sighting the moon through a sieve, with the husband offering water and sweets to his wife — a deeply emotional and sacred moment.</p>
</div></div>

<div class="card"><h2>Karwa Chauth Vrat Katha (story)</h2><div class="prose">
<p>In ancient times, a Brahmin had seven sons and one daughter named Veervati. After her marriage, her first Karwa Chauth arrived. She observed the waterless fast but couldn't bear the hunger by evening.</p>
<p>Her seven brothers, unable to see her suffering, placed a lamp behind a sieve in a peepal tree and told her the moon had risen. Veervati broke her fast looking at this false moon.</p>
<p>The moment she ate, her husband died. She performed penance for a full year and observed the next Karwa Chauth with complete devotion. By Goddess Parvati's grace, her husband was revived. This is why the fast must be observed with complete faith and proper ritual.</p>
</div></div>
</div>"""
    },
]

# Generate all pages
print("Generating astrology tool pages...")
for p in TOOL_PAGES:
    html = page_shell(p["title_hi"], p["title_en"], p["meta"], p["file"], p["body_hi"], p["body_en"])
    filepath = os.path.join(BASE_DIR, p["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: {p['file']}")

print("\nGenerating festival/puja pages...")
for p in FESTIVAL_PAGES:
    html = page_shell(p["title_hi"], p["title_en"], p["meta"], p["file"], p["body_hi"], p["body_en"])
    filepath = os.path.join(BASE_DIR, p["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: {p['file']}")

# Update sitemap
print("\nUpdating sitemap...")
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
all_pages = []
all_pages.append('<url><loc>https://rashifal.online/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>')
rashi_files = ["mesh","vrishabh","mithun","kark","singh","kanya","tula","vrishchik","dhanu","makar","kumbh","meen"]
for r in rashi_files:
    all_pages.append(f'<url><loc>https://rashifal.online/{r}.html</loc><changefreq>daily</changefreq><priority>0.8</priority></url>')
for p in TOOL_PAGES:
    all_pages.append(f'<url><loc>https://rashifal.online/{p["file"]}</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>')
for p in FESTIVAL_PAGES:
    all_pages.append(f'<url><loc>https://rashifal.online/{p["file"]}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>')
for page in ["methodology.html","about.html","privacy.html","terms.html","contact.html"]:
    all_pages.append(f'<url><loc>https://rashifal.online/{page}</loc><changefreq>monthly</changefreq><priority>0.4</priority></url>')

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/xmlns/sitemap/0.9">
{chr(10).join(all_pages)}
</urlset>"""
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap)

total = 1 + len(rashi_files) + len(TOOL_PAGES) + len(FESTIVAL_PAGES) + 5
print(f"  Updated: sitemap.xml ({total} URLs)")
print(f"\nDone! Total pages: {total}")
