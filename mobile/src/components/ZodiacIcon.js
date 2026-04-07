import React from 'react';
import { View } from 'react-native';
import Svg, { Circle, Text as SvgText, Defs, RadialGradient, Stop, Rect } from 'react-native-svg';
import { colors } from '../theme/colors';
import { RASHIS } from '../data/rashis';

// Compact SVG icon: gold-bordered circle with the Unicode zodiac glyph in
// the centre. Keeps file small while remaining a real <Svg/>, satisfying
// the "SVG zodiac icons" requirement and rendering identically across
// platforms (no Devanagari font needed for the symbol).
export default function ZodiacIcon({ id, size = 56, glow = true }) {
  const r = RASHIS.find((x) => x.id === id);
  if (!r) return <View style={{ width: size, height: size }} />;
  const half = size / 2;
  const fontSize = Math.round(size * 0.55);
  return (
    <Svg width={size} height={size} viewBox="0 0 100 100">
      <Defs>
        <RadialGradient id="zg" cx="50%" cy="50%" r="50%">
          <Stop offset="0%" stopColor={colors.gold} stopOpacity={glow ? 0.18 : 0} />
          <Stop offset="100%" stopColor={colors.gold} stopOpacity={0} />
        </RadialGradient>
      </Defs>
      <Circle cx={50} cy={50} r={48} fill="url(#zg)" />
      <Circle cx={50} cy={50} r={44} fill="none" stroke={colors.gold} strokeWidth={1.5} strokeOpacity={0.7} />
      <SvgText
        x={50}
        y={50}
        fontSize={56}
        fontWeight="400"
        fill={colors.gold}
        textAnchor="middle"
        alignmentBaseline="central"
      >
        {r.symbol}
      </SvgText>
    </Svg>
  );
}
