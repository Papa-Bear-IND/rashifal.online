import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';

export default function CategoryCard({ icon, title, text }) {
  return (
    <View style={styles.card}>
      <View style={styles.head}>
        <Text style={styles.icon}>{icon}</Text>
        <Text style={styles.title}>{title}</Text>
      </View>
      <Text style={styles.text}>{text}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: 12,
    padding: 14,
    marginRight: 12,
    width: 220,
  },
  head: { flexDirection: 'row', alignItems: 'center', marginBottom: 8 },
  icon: { color: colors.gold, fontSize: sizes.lg, marginRight: 8 },
  title: { color: colors.gold, fontFamily: fonts.serifMedium, fontSize: sizes.md },
  text: { color: colors.textSecondary, fontSize: sizes.sm, lineHeight: 20 },
});
