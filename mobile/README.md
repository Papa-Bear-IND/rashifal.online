# Rashifal Mobile

Expo / React Native companion app for [rashifal.online](https://rashifal.online).

## Features
- Daily rashifal for all 12 signs in Hindi & English
- Personal rashi from saved birth date
- Today's panchang (tithi, nakshatra, yoga, karana, rahu kaal, sunrise/sunset)
- Upcoming festivals with countdown
- Rashi compatibility checker
- Pull-to-refresh, offline cache via AsyncStorage
- Native share for predictions

## Stack
- Expo SDK 51, React Native 0.74
- React Navigation (bottom tabs + stack)
- react-native-svg for zodiac glyphs
- @expo-google-fonts/cormorant-garamond for headings
- AsyncStorage for prefs + daily cache

## Setup
```bash
cd mobile
npm install
npx expo start
```

Then scan the QR with Expo Go (Android/iOS) or press `a` / `i` for an emulator.

## Data
The app fetches `https://rashifal.online/content/YYYY-MM-DD.json` (the same
file the website consumes), caches it in AsyncStorage, and falls back to the
cache when offline.

## Project layout
```
src/
  screens/      Home, RashiDetail, Panchang, Festival, Compatibility, Settings
  components/   RashiCard, ZodiacIcon, Header, CategoryCard
  data/         rashis, compatibility, festivals
  utils/        api, storage, dateUtils, LangContext
  theme/        colors, typography
```
