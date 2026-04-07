// Always returns YYYY-MM-DD in IST regardless of device locale.
export function todayIST() {
  const n = new Date();
  const ist = new Date(n.getTime() + (n.getTimezoneOffset() + 330) * 60000);
  const y = ist.getFullYear();
  const m = String(ist.getMonth() + 1).padStart(2, '0');
  const d = String(ist.getDate()).padStart(2, '0');
  return `${y}-${m}-${d}`;
}

export function formatDateLong(dateStr, lang) {
  const d = new Date(dateStr + 'T00:00:00');
  const monthsHi = ['जनवरी','फ़रवरी','मार्च','अप्रैल','मई','जून','जुलाई','अगस्त','सितंबर','अक्टूबर','नवंबर','दिसंबर'];
  const monthsEn = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const wdHi = ['रविवार','सोमवार','मंगलवार','बुधवार','गुरुवार','शुक्रवार','शनिवार'];
  const wdEn = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  if (lang === 'hi') {
    return `${wdHi[d.getDay()]}, ${d.getDate()} ${monthsHi[d.getMonth()]} ${d.getFullYear()}`;
  }
  return `${wdEn[d.getDay()]}, ${monthsEn[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}`;
}

export function formatUpdated(iso, lang) {
  if (!iso) return '';
  const d = new Date(iso);
  if (isNaN(d)) return '';
  const monthsHi = ['जनवरी','फ़रवरी','मार्च','अप्रैल','मई','जून','जुलाई','अगस्त','सितंबर','अक्टूबर','नवंबर','दिसंबर'];
  const monthsEn = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const h = d.getHours();
  const mm = String(d.getMinutes()).padStart(2, '0');
  if (lang === 'hi') {
    const ampm = h < 12 ? 'प्रातः' : h < 16 ? 'दोपहर' : h < 19 ? 'शाम' : 'रात्रि';
    const h12 = ((h + 11) % 12) + 1;
    return `अंतिम अपडेट: ${d.getDate()} ${monthsHi[d.getMonth()]}, ${ampm} ${h12}:${mm}`;
  }
  const ampm = h < 12 ? 'AM' : 'PM';
  const h12 = ((h + 11) % 12) + 1;
  return `Last updated: ${monthsEn[d.getMonth()]} ${d.getDate()}, ${h12}:${mm} ${ampm}`;
}
