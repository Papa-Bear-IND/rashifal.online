import React, { useState } from 'react';
import { View, Text, ScrollView, Pressable, StyleSheet } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';
import { RASHIS } from '../data/rashis';
import { compatBreakdown, compatVerdict, compatAnalysis } from '../data/compatibility';
import { useLang } from '../utils/LangContext';
import ZodiacIcon from '../components/ZodiacIcon';

function Picker({ value, onChange, label }) {
  const { lang } = useLang();
  const [open, setOpen] = useState(false);
  const r = value != null ? RASHIS[value] : null;
  return (
    <View style={{ flex: 1 }}>
      <Text style={styles.pickerLabel}>{label}</Text>
      <Pressable style={styles.pickerBox} onPress={() => setOpen((o) => !o)}>
        <Text style={styles.pickerVal}>
          {r ? (lang === 'hi' ? r.hi : r.en) : (lang === 'hi' ? 'चुनें' : 'Pick')}
        </Text>
      </Pressable>
      {open && (
        <View style={styles.dropdown}>
          {RASHIS.map((rr, i) => (
            <Pressable
              key={rr.id}
              style={styles.dropItem}
              onPress={() => { onChange(i); setOpen(false); }}
            >
              <Text style={styles.dropTxt}>{lang === 'hi' ? rr.hi : rr.en}</Text>
            </Pressable>
          ))}
        </View>
      )}
    </View>
  );
}

function Bar({ label, value }) {
  return (
    <View style={styles.barRow}>
      <Text style={styles.barLabel}>{label}</Text>
      <View style={styles.barTrack}>
        <View style={[styles.barFill, { width: `${value}%` }]} />
      </View>
      <Text style={styles.barVal}>{value}</Text>
    </View>
  );
}

export default function CompatibilityScreen({ navigation }) {
  const insets = useSafeAreaInsets();
  const { lang } = useLang();
  const [a, setA] = useState(null);
  const [b, setB] = useState(null);

  const result = a != null && b != null ? compatBreakdown(a, b) : null;

  return (
    <View style={[styles.root, { paddingTop: insets.top }]}>
      <View style={styles.topbar}>
        {navigation && (
          <Pressable onPress={() => navigation.goBack()}>
            <Text style={styles.backTxt}>{lang === 'hi' ? '‹ वापस' : '‹ Back'}</Text>
          </Pressable>
        )}
        <Text style={styles.h1}>{lang === 'hi' ? 'राशि अनुकूलता' : 'Rashi Compatibility'}</Text>
      </View>
      <ScrollView contentContainerStyle={{ padding: 18, paddingBottom: 60 }}>
        <View style={styles.row}>
          <Picker value={a} onChange={setA} label={lang === 'hi' ? 'आपकी राशि' : 'Your sign'} />
          <View style={{ width: 14 }} />
          <Picker value={b} onChange={setB} label={lang === 'hi' ? 'साथी की राशि' : "Partner\u2019s sign"} />
        </View>

        {result && (
          <View style={styles.resultCard}>
            <View style={styles.resultHead}>
              <ZodiacIcon id={RASHIS[a].id} size={56} />
              <Text style={styles.heart}>♥</Text>
              <ZodiacIcon id={RASHIS[b].id} size={56} />
            </View>
            <Text style={styles.score}>{result.overall}</Text>
            <Text style={styles.scoreLabel}>
              {lang === 'hi' ? 'अनुकूलता' : 'compatibility'}
            </Text>
            <Text style={styles.verdict}>{compatVerdict(result.overall, lang)}</Text>

            <Bar label={lang === 'hi' ? 'प्रेम' : 'Love'} value={result.love} />
            <Bar label={lang === 'hi' ? 'विश्वास' : 'Trust'} value={result.trust} />
            <Bar label={lang === 'hi' ? 'संवाद' : 'Communication'} value={result.comm} />
            <Bar label={lang === 'hi' ? 'मूल्य' : 'Values'} value={result.values} />

            <Text style={styles.analysis}>{compatAnalysis(a, b, lang)}</Text>
          </View>
        )}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: colors.background },
  topbar: { paddingHorizontal: 18, paddingVertical: 10, borderBottomWidth: 1, borderBottomColor: colors.border },
  backTxt: { color: colors.gold, fontSize: sizes.base, marginBottom: 4 },
  h1: { fontFamily: fonts.serif, fontSize: sizes.xl, color: colors.gold },
  row: { flexDirection: 'row', alignItems: 'flex-start' },
  pickerLabel: { color: colors.gold, fontSize: 11, letterSpacing: 0.6, textTransform: 'uppercase', marginBottom: 6 },
  pickerBox: {
    backgroundColor: colors.charcoal, borderWidth: 1, borderColor: colors.border,
    borderRadius: 10, padding: 12,
  },
  pickerVal: { color: colors.textPrimary, fontSize: sizes.base },
  dropdown: {
    marginTop: 6, backgroundColor: colors.charcoal, borderWidth: 1, borderColor: colors.border,
    borderRadius: 10, maxHeight: 260,
  },
  dropItem: { padding: 12, borderBottomWidth: 1, borderBottomColor: colors.border },
  dropTxt: { color: colors.textPrimary, fontSize: sizes.sm },
  resultCard: {
    marginTop: 24, backgroundColor: colors.surface, borderWidth: 1, borderColor: colors.border,
    borderRadius: 16, padding: 18, alignItems: 'center',
  },
  resultHead: { flexDirection: 'row', alignItems: 'center', gap: 14 },
  heart: { color: colors.gold, fontSize: sizes.xl, marginHorizontal: 12 },
  score: { fontFamily: fonts.serif, fontSize: 60, color: colors.gold, marginTop: 12 },
  scoreLabel: { color: colors.textMuted, fontSize: sizes.xs, letterSpacing: 0.6, textTransform: 'uppercase' },
  verdict: { fontFamily: fonts.serifMedium, color: colors.textPrimary, fontSize: sizes.lg, marginTop: 6, marginBottom: 14 },
  barRow: { flexDirection: 'row', alignItems: 'center', alignSelf: 'stretch', marginTop: 8 },
  barLabel: { color: colors.textSecondary, fontSize: sizes.sm, width: 110 },
  barTrack: { flex: 1, height: 6, backgroundColor: colors.charcoal, borderRadius: 3, overflow: 'hidden', marginHorizontal: 8 },
  barFill: { height: 6, backgroundColor: colors.gold },
  barVal: { color: colors.gold, fontSize: sizes.sm, width: 32, textAlign: 'right' },
  analysis: { color: colors.textSecondary, fontSize: sizes.sm, lineHeight: 20, marginTop: 16, alignSelf: 'stretch', textAlign: 'center' },
});
