export const FESTIVALS = [
  { date: '2026-03-19', nameHi: 'चैत्र नवरात्रि', nameEn: 'Chaitra Navratri', descHi: 'देवी दुर्गा की नौ रातों की उपासना का पावन पर्व।',     descEn: 'Nine sacred nights dedicated to Goddess Durga.' },
  { date: '2026-03-28', nameHi: 'राम नवमी',       nameEn: 'Ram Navami',       descHi: 'भगवान श्रीराम का जन्मोत्सव।',                       descEn: 'The birth celebration of Lord Rama.' },
  { date: '2026-04-12', nameHi: 'हनुमान जयंती',   nameEn: 'Hanuman Jayanti',  descHi: 'पवनपुत्र हनुमान जी का प्राकट्य दिवस।',              descEn: 'The appearance day of Lord Hanuman.' },
  { date: '2026-05-03', nameHi: 'अक्षय तृतीया',   nameEn: 'Akshaya Tritiya',  descHi: 'अक्षय शुभता और समृद्धि का दिन।',                    descEn: 'A day of unending auspiciousness and prosperity.' },
  { date: '2026-07-21', nameHi: 'गुरु पूर्णिमा',  nameEn: 'Guru Purnima',     descHi: 'गुरुओं के प्रति कृतज्ञता का पर्व।',                  descEn: 'A day to honour and thank one\u2019s gurus.' },
  { date: '2026-08-12', nameHi: 'रक्षा बंधन',     nameEn: 'Raksha Bandhan',   descHi: 'भाई-बहन के पवित्र स्नेह का त्यौहार।',                descEn: 'The festival of the sacred bond between siblings.' },
  { date: '2026-08-22', nameHi: 'जन्माष्टमी',     nameEn: 'Janmashtami',      descHi: 'भगवान श्रीकृष्ण का जन्मोत्सव।',                      descEn: 'The birth celebration of Lord Krishna.' },
  { date: '2026-10-03', nameHi: 'नवरात्रि',        nameEn: 'Navratri',         descHi: 'शक्ति की नौ रातें — आरम्भ।',                          descEn: 'The beginning of the nine nights of Shakti.' },
  { date: '2026-10-12', nameHi: 'दशहरा',           nameEn: 'Dussehra',         descHi: 'असत्य पर सत्य की विजय का उत्सव।',                    descEn: 'The victory of truth over falsehood.' },
  { date: '2026-10-23', nameHi: 'करवा चौथ',       nameEn: 'Karwa Chauth',     descHi: 'पतियों की दीर्घायु के लिए सुहागिनों का व्रत।',         descEn: 'A fast observed by wives for their husbands\u2019 long life.' },
  { date: '2026-11-08', nameHi: 'दीवाली',          nameEn: 'Diwali',           descHi: 'प्रकाश और लक्ष्मी पूजन का महान पर्व।',               descEn: 'The grand festival of light and Lakshmi puja.' },
  { date: '2026-11-10', nameHi: 'छठ पूजा',        nameEn: 'Chhath Puja',      descHi: 'सूर्य देव और छठी मैया की उपासना।',                   descEn: 'A devotion to Surya Dev and Chhathi Maiya.' },
  { date: '2026-11-22', nameHi: 'देव दीवाली',      nameEn: 'Dev Diwali',       descHi: 'देवताओं की दीवाली — काशी का पर्व।',                  descEn: 'The Diwali of the gods, celebrated in Kashi.' },
  { date: '2027-01-14', nameHi: 'मकर संक्रांति',  nameEn: 'Makar Sankranti',  descHi: 'सूर्य के मकर राशि में प्रवेश का पर्व।',              descEn: 'The Sun\u2019s transit into Capricorn.' },
  { date: '2027-02-01', nameHi: 'बसंत पंचमी',     nameEn: 'Basant Panchami',  descHi: 'देवी सरस्वती की वंदना और वसंत का स्वागत।',           descEn: 'Honouring Goddess Saraswati and welcoming spring.' },
  { date: '2027-02-14', nameHi: 'महाशिवरात्रि',   nameEn: 'Maha Shivaratri',  descHi: 'भगवान शिव की महान रात्रि।',                          descEn: 'The great night of Lord Shiva.' },
  { date: '2027-03-14', nameHi: 'होली',            nameEn: 'Holi',             descHi: 'रंगों और प्रेम का उल्लासमय पर्व।',                   descEn: 'The joyous festival of colours and love.' },
];

export function upcomingFestivals(now = new Date(), limit = 20) {
  const today = new Date(now);
  today.setHours(0, 0, 0, 0);
  return FESTIVALS
    .map((f) => ({ ...f, _d: new Date(f.date + 'T00:00:00') }))
    .filter((f) => f._d >= today)
    .sort((a, b) => a._d - b._d)
    .slice(0, limit)
    .map((f) => ({
      ...f,
      daysUntil: Math.round((f._d - today) / 86400000),
    }));
}
