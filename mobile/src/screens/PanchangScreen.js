import React, { useEffect, useState, useCallback } from 'react';
import { View, Text, ScrollView, StyleSheet, RefreshControl, ActivityIndicator } from 'react-native';
import Header from '../components/Header';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';
import { fetchDaily } from '../utils/api';
import { useLang } from '../utils/LangContext';

const RAHU_KAAL = {
  0: '4:30 PM – 6:00 PM',
  1: '7:30 AM – 9:00 AM',
  2: '3:00 PM – 4:30 PM',
  3: '12:00 PM – 1:30 PM',
  4: '1:30 PM – 3:00 PM',
  5: '10:30 AM – 12:00 PM',
  6: '9:00 AM – 10:30 AM',
};

const SUN_TIMES = [
  [6.95, 17.78],[6.78, 18.05],[6.43, 18.22],[6.00, 18.33],[5.68, 18.45],[5.55, 18.62],
  [5.65, 18.65],[5.85, 18.43],[6.03, 18.05],[6.20, 17.65],[6.45, 17.45],[6.78, 17.55],
];

function fmtTime(h) {
  const hh = Math.floor(h);
  const mm = Math.round((h - hh) * 60);
  const ampm = hh >= 12 ? 'PM' : 'AM';
  const h12 = ((hh + 11) % 12) + 1;
  return `${h12}:${String(mm).padStart(2, '0')} ${ampm}`;
}

function Card({ label, value, sub }) {
  return (
    <View style={styles.card}>
      <Text style={styles.label}>{label}</Text>
      <Text style={styles.value}>{value}</Text>
      {sub ? <Text style={styles.sub}>{sub}</Text> : null}
    </View>
  );
}

export default function PanchangScreen() {
  const { lang } = useLang();
  const [dd, setDD] = useState(null);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  const load = useCallback(async () => {
    const { data } = await fetchDaily();
    setDD(data);
    setLoading(false);
    setRefreshing(false);
  }, []);

  useEffect(() => { load(); }, [load]);

  const onRefresh = () => { setRefreshing(true); load(); };

  const now = new Date();
  const ist = new Date(now.getTime() + (now.getTimezoneOffset() + 330) * 60000);
  const wd = ist.getDay();
  const month = ist.getMonth();
  const [sr, ss] = SUN_TIMES[month];
  const noon = (sr + ss) / 2;
  const abhijit = `${fmtTime(noon - 0.4)} – ${fmtTime(noon + 0.4)}`;
  const p = dd?.panchang;
  const dash = lang === 'hi' ? 'जल्द उपलब्ध' : 'Coming soon';
  const val = (o) => (o ? (lang === 'hi' ? o.hi : o.en) || dash : dash);

  return (
    <View style={styles.root}>
      <Header subtitle={lang === 'hi' ? 'आज का पंचांग' : 'Today\u2019s Panchang'} />
      {loading ? (
        <View style={styles.center}><ActivityIndicator color={colors.gold} /></View>
      ) : (
        <ScrollView
          contentContainerStyle={{ padding: 14, paddingBottom: 30 }}
          refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={colors.gold} />}
        >
          <Card label={lang === 'hi' ? 'तिथि' : 'Tithi'} value={val(p?.tithi)} />
          <Card label={lang === 'hi' ? 'नक्षत्र' : 'Nakshatra'} value={val(p?.nakshatra)} />
          <Card label={lang === 'hi' ? 'योग' : 'Yoga'} value={val(p?.yoga)} />
          <Card label={lang === 'hi' ? 'करण' : 'Karana'} value={val(p?.karana)} />
          <Card
            label={lang === 'hi' ? 'राहुकाल' : 'Rahu Kaal'}
            value={RAHU_KAAL[wd]}
            sub={lang === 'hi' ? 'अशुभ काल — टालें' : 'Inauspicious — avoid'}
          />
          <Card
            label={lang === 'hi' ? 'शुभ मुहूर्त' : 'Shubh Muhurat'}
            value={abhijit}
            sub={lang === 'hi' ? 'अभिजीत मुहूर्त' : 'Abhijit Muhurat'}
          />
          <Card
            label={lang === 'hi' ? 'सूर्योदय' : 'Sunrise'}
            value={fmtTime(sr)}
            sub={lang === 'hi' ? 'भोपाल' : 'Bhopal'}
          />
          <Card
            label={lang === 'hi' ? 'सूर्यास्त' : 'Sunset'}
            value={fmtTime(ss)}
            sub={lang === 'hi' ? 'भोपाल' : 'Bhopal'}
          />
          {p?.special && (p.special.hi || p.special.en) ? (
            <Card label={lang === 'hi' ? 'विशेष' : 'Special'} value={val(p.special)} />
          ) : null}
        </ScrollView>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: colors.background },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  card: {
    backgroundColor: colors.surface, borderWidth: 1, borderColor: colors.border,
    borderRadius: 12, padding: 14, marginBottom: 10,
  },
  label: { color: colors.gold, fontSize: 11, letterSpacing: 0.6, textTransform: 'uppercase' },
  value: { color: colors.textPrimary, fontFamily: fonts.serifMedium, fontSize: sizes.lg, marginTop: 4 },
  sub: { color: colors.textMuted, fontSize: sizes.xs, marginTop: 2 },
});
