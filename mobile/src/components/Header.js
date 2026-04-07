import React from 'react';
import { View, Text, Pressable, StyleSheet } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';
import { useLang, t } from '../utils/LangContext';
import { formatDateLong, todayIST } from '../utils/dateUtils';

export default function Header({ subtitle }) {
  const { lang, setLang } = useLang();
  const insets = useSafeAreaInsets();
  return (
    <View style={[styles.wrap, { paddingTop: insets.top + 12 }]}>
      <View style={styles.row}>
        <View style={{ flex: 1 }}>
          <Text style={styles.brand}>Rashifal</Text>
          <Text style={styles.date}>{formatDateLong(todayIST(), lang)}</Text>
          {subtitle ? <Text style={styles.sub}>{subtitle}</Text> : null}
        </View>
        <View style={styles.langSwitch}>
          <Pressable onPress={() => setLang('hi')} style={[styles.langBtn, lang === 'hi' && styles.langBtnActive]}>
            <Text style={[styles.langTxt, lang === 'hi' && styles.langTxtActive]}>हिं</Text>
          </Pressable>
          <Pressable onPress={() => setLang('en')} style={[styles.langBtn, lang === 'en' && styles.langBtnActive]}>
            <Text style={[styles.langTxt, lang === 'en' && styles.langTxtActive]}>EN</Text>
          </Pressable>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: { paddingHorizontal: 18, paddingBottom: 14, borderBottomWidth: 1, borderBottomColor: colors.border },
  row: { flexDirection: 'row', alignItems: 'flex-start' },
  brand: { fontFamily: fonts.serif, fontSize: sizes.xxl, color: colors.gold, letterSpacing: 0.5 },
  date: { color: colors.textSecondary, fontSize: sizes.sm, marginTop: 2 },
  sub: { color: colors.textMuted, fontSize: sizes.xs, marginTop: 4, fontStyle: 'italic' },
  langSwitch: { flexDirection: 'row', backgroundColor: colors.surface, borderRadius: 999, borderWidth: 1, borderColor: colors.border, overflow: 'hidden' },
  langBtn: { paddingHorizontal: 12, paddingVertical: 6 },
  langBtnActive: { backgroundColor: colors.goldMuted },
  langTxt: { color: colors.textSecondary, fontSize: sizes.xs, fontFamily: fonts.bodyMedium },
  langTxtActive: { color: colors.gold },
});
