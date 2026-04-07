import React from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import Header from '../components/Header';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';
import { upcomingFestivals } from '../data/festivals';
import { useLang } from '../utils/LangContext';

function formatDate(dateStr, lang) {
  const d = new Date(dateStr + 'T00:00:00');
  const monthsHi = ['जनवरी','फ़रवरी','मार्च','अप्रैल','मई','जून','जुलाई','अगस्त','सितंबर','अक्टूबर','नवंबर','दिसंबर'];
  const monthsEn = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  if (lang === 'hi') return `${d.getDate()} ${monthsHi[d.getMonth()]} ${d.getFullYear()}`;
  return `${monthsEn[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}`;
}

export default function FestivalScreen() {
  const { lang } = useLang();
  const list = upcomingFestivals();

  return (
    <View style={styles.root}>
      <Header subtitle={lang === 'hi' ? 'आगामी त्योहार' : 'Upcoming Festivals'} />
      <FlatList
        data={list}
        keyExtractor={(f) => f.date + f.nameEn}
        contentContainerStyle={{ padding: 14, paddingBottom: 30 }}
        renderItem={({ item }) => {
          const days = item.daysUntil;
          const cd = days === 0
            ? (lang === 'hi' ? 'आज' : 'Today')
            : (lang === 'hi' ? `${days} दिन शेष` : `${days} day${days === 1 ? '' : 's'} away`);
          return (
            <View style={styles.card}>
              <View style={styles.head}>
                <Text style={styles.name}>{lang === 'hi' ? item.nameHi : item.nameEn}</Text>
                <View style={styles.pill}><Text style={styles.pillTxt}>{cd}</Text></View>
              </View>
              <Text style={styles.sub}>{lang === 'hi' ? item.nameEn : item.nameHi}</Text>
              <Text style={styles.date}>{formatDate(item.date, lang)}</Text>
              <Text style={styles.desc}>{lang === 'hi' ? item.descHi : item.descEn}</Text>
            </View>
          );
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: colors.background },
  card: {
    backgroundColor: colors.surface, borderWidth: 1, borderColor: colors.border,
    borderRadius: 14, padding: 14, marginBottom: 12,
  },
  head: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' },
  name: { fontFamily: fonts.serif, color: colors.gold, fontSize: sizes.lg, flex: 1, marginRight: 10 },
  pill: { backgroundColor: colors.goldMuted, paddingHorizontal: 10, paddingVertical: 4, borderRadius: 999 },
  pillTxt: { color: colors.gold, fontSize: 11 },
  sub: { color: colors.textMuted, fontSize: sizes.xs, marginTop: 2 },
  date: { color: colors.textSecondary, fontSize: sizes.sm, marginTop: 6 },
  desc: { color: colors.textSecondary, fontSize: sizes.sm, marginTop: 6, lineHeight: 20 },
});
