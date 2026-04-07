import React, { useEffect, useState } from 'react';
import {
  View, Text, ScrollView, StyleSheet, Pressable, Share, ActivityIndicator,
} from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';
import { RASHIS } from '../data/rashis';
import { fetchDaily } from '../utils/api';
import { useLang } from '../utils/LangContext';
import ZodiacIcon from '../components/ZodiacIcon';
import { formatUpdated } from '../utils/dateUtils';

function Stars({ rating }) {
  const r = Number(rating) || 0;
  const full = Math.floor(r);
  const half = r - full >= 0.5;
  let s = '';
  for (let i = 0; i < 5; i++) s += i < full ? '★ ' : i === full && half ? '⯨ ' : '☆ ';
  return <Text style={styles.stars}>{s.trim()}</Text>;
}

function CatBlock({ icon, title, text }) {
  return (
    <View style={styles.catCard}>
      <Text style={styles.catTitle}>{icon}  {title}</Text>
      <Text style={styles.catText}>{text}</Text>
    </View>
  );
}

export default function RashiDetailScreen({ route, navigation }) {
  const { idx } = route.params || { idx: 0 };
  const insets = useSafeAreaInsets();
  const { lang } = useLang();
  const [dd, setDD] = useState(null);
  const [loading, setLoading] = useState(true);

  const r = RASHIS[idx];

  useEffect(() => {
    (async () => {
      const { data } = await fetchDaily();
      setDD(data);
      setLoading(false);
    })();
  }, []);

  const rd = dd?.rashis?.[idx];
  const ld = rd ? (lang === 'hi' ? rd.hindi : rd.english) : null;

  const fb = lang === 'hi' ? 'जल्द उपलब्ध' : 'Coming soon';

  const onShare = async () => {
    if (!ld) return;
    const name = lang === 'hi' ? r.hi : r.en;
    const label = lang === 'hi' ? 'राशिफल' : 'rashifal';
    const dateStr = lang === 'hi' ? dd?.date_hi || '' : dd?.date || '';
    const sentences = (ld.prediction || '').split(/(?<=[।.!?])\s+/).slice(0, 2).join(' ');
    const more = lang === 'hi'
      ? 'और पढ़ें — https://rashifal.online'
      : 'Read more at https://rashifal.online';
    const text = `${name} ${label} (${dateStr}): ${sentences}\n\n${more}`;
    try {
      await Share.share({ message: text, title: `${name} ${label}` });
    } catch {}
  };

  return (
    <View style={[styles.root, { paddingTop: insets.top }]}>
      <View style={styles.topbar}>
        <Pressable onPress={() => navigation.goBack()} style={styles.backBtn}>
          <Text style={styles.backTxt}>{lang === 'hi' ? '‹ वापस' : '‹ Back'}</Text>
        </Pressable>
      </View>

      {loading ? (
        <View style={styles.center}>
          <ActivityIndicator color={colors.gold} />
        </View>
      ) : (
        <ScrollView contentContainerStyle={{ padding: 18, paddingBottom: 40 }}>
          <View style={styles.headWrap}>
            <ZodiacIcon id={r.id} size={88} />
            <Text style={styles.name}>{lang === 'hi' ? r.hi : r.en}</Text>
            <Text style={styles.sub}>{lang === 'hi' ? r.en : r.hi} · {lang === 'hi' ? r.dt : r.dte}</Text>
          </View>

          <Text style={styles.prediction}>
            {ld?.prediction || (lang === 'hi'
              ? 'आज का विस्तृत राशिफल जल्द उपलब्ध होगा।'
              : 'Today\u2019s detailed prediction will be available shortly.')}
          </Text>

          <View style={styles.metaRow}>
            <View style={styles.metaItem}>
              <Text style={styles.metaLabel}>{lang === 'hi' ? 'शुभ अंक' : 'Lucky #'}</Text>
              <Text style={styles.metaValue}>{ld?.lucky_number || '—'}</Text>
            </View>
            <View style={styles.metaItem}>
              <Text style={styles.metaLabel}>{lang === 'hi' ? 'शुभ रंग' : 'Lucky Color'}</Text>
              <Text style={styles.metaValue}>{ld?.lucky_color || '—'}</Text>
            </View>
            <View style={styles.metaItem}>
              <Text style={styles.metaLabel}>{lang === 'hi' ? 'रेटिंग' : 'Rating'}</Text>
              {ld ? <Stars rating={ld.rating} /> : <Text style={styles.metaValue}>—</Text>}
            </View>
          </View>

          <View style={styles.metaRow}>
            <View style={styles.metaItem}>
              <Text style={styles.metaLabel}>{lang === 'hi' ? 'स्वामी' : 'Ruler'}</Text>
              <Text style={styles.metaValue}>{lang === 'hi' ? r.ruHi : r.ruEn}</Text>
            </View>
            <View style={styles.metaItem}>
              <Text style={styles.metaLabel}>{lang === 'hi' ? 'तत्व' : 'Element'}</Text>
              <Text style={styles.metaValue}>{lang === 'hi' ? r.elHi : r.elEn}</Text>
            </View>
            <View style={styles.metaItem}>
              <Text style={styles.metaLabel}>{lang === 'hi' ? 'गुण' : 'Quality'}</Text>
              <Text style={styles.metaValue}>{lang === 'hi' ? r.qHi : r.qEn}</Text>
            </View>
          </View>

          <CatBlock icon="♥" title={lang === 'hi' ? 'प्रेम एवं रिश्ते' : 'Love & Relationships'} text={ld?.love || fb} />
          <CatBlock icon="⚒" title={lang === 'hi' ? 'करियर एवं व्यवसाय' : 'Career & Business'} text={ld?.career || fb} />
          <CatBlock icon="✚" title={lang === 'hi' ? 'स्वास्थ्य' : 'Health'} text={ld?.health || fb} />
          <CatBlock icon="₹" title={lang === 'hi' ? 'धन एवं वित्त' : 'Money & Finance'} text={ld?.finance || fb} />

          {ld?.remedy ? (
            <View style={styles.remedy}>
              <Text style={styles.remedyHead}>{lang === 'hi' ? '🌿  आज का उपाय' : '🌿  Today\u2019s Remedy'}</Text>
              <Text style={styles.remedyText}>{ld.remedy}</Text>
            </View>
          ) : null}

          {ld?.mantra && (ld.mantra.sanskrit || ld.mantra.meaning) ? (
            <View style={styles.mantra}>
              <Text style={styles.mantraLabel}>{lang === 'hi' ? 'आज का मंत्र' : 'Mantra of the Day'}</Text>
              <Text style={styles.mantraSanskrit}>{ld.mantra.sanskrit}</Text>
              <Text style={styles.mantraMeaning}>{ld.mantra.meaning}</Text>
            </View>
          ) : null}

          <Pressable style={styles.shareBtn} onPress={onShare}>
            <Text style={styles.shareTxt}>
              {lang === 'hi' ? 'राशिफल साझा करें' : 'Share this rashifal'}
            </Text>
          </Pressable>

          {dd?.generated_at ? (
            <Text style={styles.updated}>{formatUpdated(dd.generated_at, lang)}</Text>
          ) : null}
        </ScrollView>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: colors.background },
  topbar: { paddingHorizontal: 14, paddingVertical: 8 },
  backBtn: { alignSelf: 'flex-start', paddingVertical: 6, paddingHorizontal: 8 },
  backTxt: { color: colors.gold, fontSize: sizes.base },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  headWrap: { alignItems: 'center', marginBottom: 18 },
  name: { fontFamily: fonts.serif, fontSize: sizes.xxl, color: colors.gold, marginTop: 8 },
  sub: { color: colors.textMuted, fontSize: sizes.sm, marginTop: 4 },
  prediction: { color: colors.textPrimary, fontSize: sizes.base, lineHeight: 24, marginBottom: 16 },
  metaRow: { flexDirection: 'row', gap: 10, marginBottom: 10 },
  metaItem: {
    flex: 1, backgroundColor: colors.goldMuted, borderRadius: 10,
    padding: 10, alignItems: 'center',
  },
  metaLabel: { color: colors.gold, fontSize: 10, letterSpacing: 0.5, textTransform: 'uppercase' },
  metaValue: { color: colors.textPrimary, fontFamily: fonts.serifMedium, fontSize: sizes.md, marginTop: 4 },
  stars: { color: colors.gold, fontSize: sizes.sm, marginTop: 4 },
  catCard: {
    backgroundColor: colors.surfaceHigh, borderWidth: 1, borderColor: colors.border,
    borderRadius: 12, padding: 12, marginTop: 10,
  },
  catTitle: { color: colors.gold, fontFamily: fonts.serifMedium, fontSize: sizes.md, marginBottom: 6 },
  catText: { color: colors.textSecondary, fontSize: sizes.sm, lineHeight: 20 },
  remedy: {
    marginTop: 16, backgroundColor: colors.surface, borderRadius: 12,
    borderWidth: 1, borderColor: colors.border, padding: 14,
  },
  remedyHead: { color: colors.gold, fontFamily: fonts.serifMedium, fontSize: sizes.md, marginBottom: 6 },
  remedyText: { color: colors.textSecondary, fontSize: sizes.sm, lineHeight: 20 },
  mantra: {
    marginTop: 12, backgroundColor: colors.goldMuted, borderLeftWidth: 3,
    borderLeftColor: colors.gold, borderRadius: 8, padding: 14,
  },
  mantraLabel: { color: colors.gold, fontSize: 10, letterSpacing: 0.6, textTransform: 'uppercase', marginBottom: 6 },
  mantraSanskrit: { color: colors.textPrimary, fontFamily: fonts.serifItalic, fontSize: sizes.lg, lineHeight: 28 },
  mantraMeaning: { color: colors.textMuted, fontSize: sizes.sm, marginTop: 4 },
  shareBtn: {
    marginTop: 20, alignSelf: 'center',
    paddingHorizontal: 22, paddingVertical: 12,
    borderRadius: 999, borderWidth: 1, borderColor: colors.gold,
  },
  shareTxt: { color: colors.gold, fontSize: sizes.base },
  updated: { color: colors.textMuted, fontSize: sizes.xs, textAlign: 'center', marginTop: 14 },
});
