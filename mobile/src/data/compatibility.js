// Element-based compatibility scoring (mirrors the website's approach in
// simplified form). 12x12 matrix of scores 0-100, derived from element +
// modality pairings. Order matches RASHIS array.
const ELEMENTS = ['fire','earth','air','water','fire','earth','air','water','fire','earth','air','water'];

const PAIR_SCORE = {
  'fire-fire': 88,   'fire-air': 92,   'fire-earth': 60,  'fire-water': 55,
  'air-air': 85,     'air-fire': 92,   'air-earth': 58,   'air-water': 62,
  'earth-earth': 86, 'earth-water': 90,'earth-fire': 60,  'earth-air': 58,
  'water-water': 84, 'water-earth': 90,'water-fire': 55,  'water-air': 62,
};

export function compatScore(i, j) {
  if (i === j) return 78;
  const k = ELEMENTS[i] + '-' + ELEMENTS[j];
  return PAIR_SCORE[k] || 65;
}

export function compatBreakdown(i, j) {
  const base = compatScore(i, j);
  const wobble = (a, b, off) => Math.max(40, Math.min(98, base + ((a + b + off) % 11) - 5));
  return {
    overall: base,
    love:    wobble(i, j, 1),
    trust:   wobble(i, j, 4),
    comm:    wobble(i, j, 7),
    values:  wobble(i, j, 9),
  };
}

export function compatVerdict(score, lang) {
  if (score >= 85) return lang === 'hi' ? 'अद्भुत मेल' : 'Excellent match';
  if (score >= 70) return lang === 'hi' ? 'अच्छा मेल' : 'Good match';
  if (score >= 55) return lang === 'hi' ? 'संतुलित मेल' : 'Balanced match';
  return lang === 'hi' ? 'चुनौतीपूर्ण' : 'Challenging';
}

export function compatAnalysis(i, j, lang) {
  const e1 = ELEMENTS[i], e2 = ELEMENTS[j];
  const enMap = {
    'fire-air': 'Air feeds fire — naturally compatible. Conversation flows and you make each other braver.',
    'air-fire': 'Air feeds fire — naturally compatible. Conversation flows and you make each other braver.',
    'earth-water': 'Water nourishes earth. Stability meets emotional depth, a rare and grounded pairing.',
    'water-earth': 'Water nourishes earth. Stability meets emotional depth, a rare and grounded pairing.',
    'fire-fire': 'Two flames — exhilarating but watch the temperature.',
    'air-air': 'A meeting of minds. Endless conversation, but ground each other in feeling.',
    'earth-earth': 'Quiet, dependable, built to last. Beware of routine swallowing romance.',
    'water-water': 'Deep emotional resonance, but easy to drown together. Hold space for daylight.',
  };
  const hiMap = {
    'fire-air': 'वायु अग्नि को प्रबल करती है — स्वाभाविक मेल। बातचीत सहज और एक-दूसरे को साहसी बनाते हैं।',
    'air-fire': 'वायु अग्नि को प्रबल करती है — स्वाभाविक मेल। बातचीत सहज और एक-दूसरे को साहसी बनाते हैं।',
    'earth-water': 'जल पृथ्वी को सींचता है। स्थिरता और भावनात्मक गहराई का दुर्लभ संयोग।',
    'water-earth': 'जल पृथ्वी को सींचता है। स्थिरता और भावनात्मक गहराई का दुर्लभ संयोग।',
    'fire-fire': 'दो ज्वालाएँ — रोमांचक पर तापमान पर ध्यान दें।',
    'air-air': 'विचारों का मेल। अनवरत संवाद, पर भावनाओं को भी जगह दें।',
    'earth-earth': 'शांत, भरोसेमंद, टिकाऊ। दिनचर्या को रोमांस निगलने न दें।',
    'water-water': 'गहरी भावनात्मक अनुगूँज, पर साथ डूबना सरल है। प्रकाश के लिए जगह रखें।',
  };
  const key = e1 + '-' + e2;
  const fb = lang === 'hi'
    ? 'भिन्न तत्व — समझदारी और धैर्य से यह जोड़ी मजबूत बन सकती है।'
    : 'Different elements — with patience and understanding, this pairing can grow strong.';
  return (lang === 'hi' ? hiMap : enMap)[key] || fb;
}
