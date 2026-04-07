// Rashi master list — mirrors website RASHIS array
export const RASHIS = [
  { id: 'mesh',      hi: 'मेष',     en: 'Aries',       symbol: '\u2648', dt: '21 मार्च – 19 अप्रैल',  dte: 'Mar 21 – Apr 19', elHi: 'अग्नि',  elEn: 'Fire',  ruHi: 'मंगल',  ruEn: 'Mars',    qHi: 'चर',         qEn: 'Cardinal' },
  { id: 'vrishabh',  hi: 'वृषभ',    en: 'Taurus',      symbol: '\u2649', dt: '20 अप्रैल – 20 मई',     dte: 'Apr 20 – May 20', elHi: 'पृथ्वी', elEn: 'Earth', ruHi: 'शुक्र', ruEn: 'Venus',   qHi: 'स्थिर',      qEn: 'Fixed' },
  { id: 'mithun',    hi: 'मिथुन',   en: 'Gemini',      symbol: '\u264A', dt: '21 मई – 20 जून',         dte: 'May 21 – Jun 20', elHi: 'वायु',  elEn: 'Air',   ruHi: 'बुध',   ruEn: 'Mercury', qHi: 'द्विस्वभाव', qEn: 'Mutable' },
  { id: 'kark',      hi: 'कर्क',    en: 'Cancer',      symbol: '\u264B', dt: '21 जून – 22 जुलाई',     dte: 'Jun 21 – Jul 22', elHi: 'जल',    elEn: 'Water', ruHi: 'चंद्र', ruEn: 'Moon',    qHi: 'चर',         qEn: 'Cardinal' },
  { id: 'singh',     hi: 'सिंह',    en: 'Leo',         symbol: '\u264C', dt: '23 जुलाई – 22 अगस्त',   dte: 'Jul 23 – Aug 22', elHi: 'अग्नि', elEn: 'Fire',  ruHi: 'सूर्य', ruEn: 'Sun',     qHi: 'स्थिर',      qEn: 'Fixed' },
  { id: 'kanya',     hi: 'कन्या',   en: 'Virgo',       symbol: '\u264D', dt: '23 अगस्त – 22 सितम्बर', dte: 'Aug 23 – Sep 22', elHi: 'पृथ्वी', elEn: 'Earth', ruHi: 'बुध',   ruEn: 'Mercury', qHi: 'द्विस्वभाव', qEn: 'Mutable' },
  { id: 'tula',      hi: 'तुला',    en: 'Libra',       symbol: '\u264E', dt: '23 सितम्बर – 22 अक्टूबर', dte: 'Sep 23 – Oct 22', elHi: 'वायु', elEn: 'Air',   ruHi: 'शुक्र', ruEn: 'Venus',   qHi: 'चर',         qEn: 'Cardinal' },
  { id: 'vrishchik', hi: 'वृश्चिक', en: 'Scorpio',     symbol: '\u264F', dt: '23 अक्टूबर – 21 नवम्बर', dte: 'Oct 23 – Nov 21', elHi: 'जल',   elEn: 'Water', ruHi: 'मंगल',  ruEn: 'Mars',    qHi: 'स्थिर',      qEn: 'Fixed' },
  { id: 'dhanu',     hi: 'धनु',     en: 'Sagittarius', symbol: '\u2650', dt: '22 नवम्बर – 21 दिसम्बर', dte: 'Nov 22 – Dec 21', elHi: 'अग्नि', elEn: 'Fire',  ruHi: 'गुरु',  ruEn: 'Jupiter', qHi: 'द्विस्वभाव', qEn: 'Mutable' },
  { id: 'makar',     hi: 'मकर',     en: 'Capricorn',   symbol: '\u2651', dt: '22 दिसम्बर – 19 जनवरी',  dte: 'Dec 22 – Jan 19', elHi: 'पृथ्वी', elEn: 'Earth', ruHi: 'शनि',   ruEn: 'Saturn',  qHi: 'चर',         qEn: 'Cardinal' },
  { id: 'kumbh',     hi: 'कुम्भ',   en: 'Aquarius',    symbol: '\u2652', dt: '20 जनवरी – 18 फरवरी',   dte: 'Jan 20 – Feb 18', elHi: 'वायु',  elEn: 'Air',   ruHi: 'शनि',   ruEn: 'Saturn',  qHi: 'स्थिर',      qEn: 'Fixed' },
  { id: 'meen',      hi: 'मीन',     en: 'Pisces',      symbol: '\u2653', dt: '19 फरवरी – 20 मार्च',   dte: 'Feb 19 – Mar 20', elHi: 'जल',    elEn: 'Water', ruHi: 'गुरु',  ruEn: 'Jupiter', qHi: 'द्विस्वभाव', qEn: 'Mutable' },
];

// Simplified Vedic moon-sign mapping (matches website)
const RANGES = [
  { id: 'mesh',      start: [4, 14],  end: [5, 14] },
  { id: 'vrishabh',  start: [5, 15],  end: [6, 14] },
  { id: 'mithun',    start: [6, 15],  end: [7, 14] },
  { id: 'kark',      start: [7, 15],  end: [8, 14] },
  { id: 'singh',     start: [8, 15],  end: [9, 15] },
  { id: 'kanya',     start: [9, 16],  end: [10, 15] },
  { id: 'tula',      start: [10, 16], end: [11, 14] },
  { id: 'vrishchik', start: [11, 15], end: [12, 14] },
  { id: 'dhanu',     start: [12, 15], end: [1, 13] },
  { id: 'makar',     start: [1, 14],  end: [2, 11] },
  { id: 'kumbh',     start: [2, 12],  end: [3, 13] },
  { id: 'meen',      start: [3, 14],  end: [4, 13] },
];

export function rashiFromDate(dob) {
  const m = dob.getMonth() + 1;
  const d = dob.getDate();
  for (const r of RANGES) {
    const [sm, sd] = r.start;
    const [em, ed] = r.end;
    if (sm <= em) {
      if ((m === sm && d >= sd) || (m === em && d <= ed) || (m > sm && m < em)) return r.id;
    } else {
      if ((m === sm && d >= sd) || (m === em && d <= ed) || m > sm || m < em) return r.id;
    }
  }
  return null;
}
