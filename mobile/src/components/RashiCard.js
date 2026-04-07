import React from 'react';
import { Pressable, Text, View, StyleSheet } from 'react-native';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';
import ZodiacIcon from './ZodiacIcon';
import { useLang } from '../utils/LangContext';

function Stars({ rating }) {
  const r = Number(rating) || 0;
  const full = Math.floor(r);
  const half = r - full >= 0.5;
  const out = [];
  for (let i = 0; i < 5; i++) {
    let ch = '☆';
    if (i < full) ch = '★';
    else if (i === full && half) ch = '⯨';
    out.push(ch);
  }
  return <Text style={styles.stars}>{out.join(' ')}</Text>;
}

export default function RashiCard({ rashi, ld, isYours, onPress }) {
  const { lang } = useLang();
  return (
    <Pressable
      onPress={onPress}
      style={({ pressed }) => [
        styles.card,
        isYours && styles.yours,
        pressed && { opacity: 0.85 },
      ]}
    >
      <View style={styles.head}>
        <ZodiacIcon id={rashi.id} size={48} />
        <View style={{ marginLeft: 10, flex: 1 }}>
          <Text style={styles.name}>{lang === 'hi' ? rashi.hi : rashi.en}</Text>
          <Text style={styles.sub}>{lang === 'hi' ? rashi.en : rashi.hi}</Text>
        </View>
      </View>
      {isYours && (
        <View style={styles.badge}>
          <Text style={styles.badgeTxt}>{lang === 'hi' ? 'आपकी राशि' : 'Your sign'}</Text>
        </View>
      )}
      <Text style={styles.dates}>{lang === 'hi' ? rashi.dt : rashi.dte}</Text>
      {ld?.prediction ? (
        <>
          <Text numberOfLines={3} style={styles.excerpt}>
            {ld.prediction}
          </Text>
          <Stars rating={ld.rating} />
        </>
      ) : (
        <Text style={styles.excerpt}>
          {lang === 'hi' ? 'आज का राशिफल जल्द उपलब्ध…' : 'Today\u2019s prediction loading…'}
        </Text>
      )}
    </Pressable>
  );
}

const styles = StyleSheet.create({
  card: {
    flex: 1,
    backgroundColor: colors.surface,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: colors.border,
    padding: 14,
    margin: 6,
    minHeight: 200,
  },
  yours: { borderColor: colors.gold },
  head: { flexDirection: 'row', alignItems: 'center' },
  name: { fontFamily: fonts.serif, fontSize: sizes.lg, color: colors.gold },
  sub: { color: colors.textMuted, fontSize: sizes.xs, letterSpacing: 0.4 },
  dates: { color: colors.textMuted, fontSize: sizes.xs, marginTop: 6 },
  excerpt: { color: colors.textSecondary, fontSize: sizes.sm, marginTop: 8, lineHeight: 20 },
  stars: { color: colors.gold, fontSize: sizes.sm, marginTop: 8, letterSpacing: 1 },
  badge: {
    alignSelf: 'flex-start',
    marginTop: 6,
    paddingHorizontal: 8,
    paddingVertical: 2,
    backgroundColor: colors.goldMuted,
    borderRadius: 999,
  },
  badgeTxt: { color: colors.gold, fontSize: 10, letterSpacing: 0.6, textTransform: 'uppercase' },
});
