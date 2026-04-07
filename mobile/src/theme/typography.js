import { Platform } from 'react-native';

export const fonts = {
  serif: 'CormorantGaramond_600SemiBold',
  serifRegular: 'CormorantGaramond_400Regular',
  serifMedium: 'CormorantGaramond_500Medium',
  serifItalic: 'CormorantGaramond_400Regular_Italic',
  body: Platform.select({ ios: 'System', android: 'sans-serif', default: 'System' }),
  bodyMedium: Platform.select({ ios: 'System', android: 'sans-serif-medium', default: 'System' }),
};

export const sizes = {
  xs: 11,
  sm: 13,
  base: 15,
  md: 17,
  lg: 22,
  xl: 28,
  xxl: 34,
};
