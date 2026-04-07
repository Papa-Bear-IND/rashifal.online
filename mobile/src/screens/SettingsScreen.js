import React, { useEffect, useState } from 'react';
import {
  View, Text, ScrollView, Pressable, Switch, StyleSheet, Linking, Platform,
} from 'react-native';
import DateTimePicker from '@react-native-community/datetimepicker';
import Header from '../components/Header';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';
import { loadPrefs, patchPrefs } from '../utils/storage';
import { useLang } from '../utils/LangContext';
import { RASHIS, rashiFromDate } from '../data/rashis';

const APP_VERSION = '1.0.0';
const PLAY_STORE_URL = 'https://play.google.com/store/apps/details?id=online.rashifal.app';

export default function SettingsScreen() {
  const { lang, setLang } = useLang();
  const [dob, setDob] = useState(null);
  const [showPicker, setShowPicker] = useState(false);
  const [notify, setNotify] = useState(false);
  const [favs, setFavs] = useState([]);

  useEffect(() => {
    (async () => {
      const p = await loadPrefs();
      if (p.dob) setDob(new Date(p.dob + 'T00:00:00'));
      setNotify(!!p.notify);
      setFavs(p.favs || []);
    })();
  }, []);

  const onDate = async (event, picked) => {
    setShowPicker(Platform.OS === 'ios');
    if (event?.type === 'dismissed') return;
    const d = picked || dob;
    if (!d) return;
    setDob(d);
    const iso = d.toISOString().slice(0, 10);
    await patchPrefs({ dob: iso });
  };

  const toggleFav = async (id) => {
    const next = favs.includes(id) ? favs.filter((x) => x !== id) : [...favs, id].slice(0, 6);
    setFavs(next);
    await patchPrefs({ favs: next });
  };

  const toggleNotify = async (v) => {
    setNotify(v);
    await patchPrefs({ notify: v });
  };

  const yourId = dob ? rashiFromDate(dob) : null;
  const yourRashi = yourId ? RASHIS.find((r) => r.id === yourId) : null;

  return (
    <View style={styles.root}>
      <Header subtitle={lang === 'hi' ? 'आपकी प्राथमिकताएं' : 'Your Preferences'} />
      <ScrollView contentContainerStyle={{ padding: 18, paddingBottom: 40 }}>
        <Section title={lang === 'hi' ? 'जन्म तिथि' : 'Birth Date'}>
          <Pressable style={styles.row} onPress={() => setShowPicker(true)}>
            <Text style={styles.rowTxt}>
              {dob ? dob.toDateString() : (lang === 'hi' ? 'तिथि चुनें' : 'Pick a date')}
            </Text>
            <Text style={styles.gold}>›</Text>
          </Pressable>
          {yourRashi && (
            <Text style={styles.helper}>
              {lang === 'hi' ? 'आपकी राशि: ' : 'Your rashi: '}
              <Text style={styles.gold}>{lang === 'hi' ? yourRashi.hi : yourRashi.en}</Text>
            </Text>
          )}
          {showPicker && (
            <DateTimePicker
              value={dob || new Date(1995, 0, 1)}
              mode="date"
              display={Platform.OS === 'ios' ? 'spinner' : 'default'}
              onChange={onDate}
              maximumDate={new Date()}
              themeVariant="dark"
            />
          )}
        </Section>

        <Section title={lang === 'hi' ? 'भाषा' : 'Language'}>
          <View style={{ flexDirection: 'row', gap: 10 }}>
            <Pressable
              style={[styles.langBtn, lang === 'hi' && styles.langBtnActive]}
              onPress={() => setLang('hi')}
            >
              <Text style={[styles.langBtnTxt, lang === 'hi' && styles.langBtnTxtActive]}>हिन्दी</Text>
            </Pressable>
            <Pressable
              style={[styles.langBtn, lang === 'en' && styles.langBtnActive]}
              onPress={() => setLang('en')}
            >
              <Text style={[styles.langBtnTxt, lang === 'en' && styles.langBtnTxtActive]}>English</Text>
            </Pressable>
          </View>
        </Section>

        <Section title={lang === 'hi' ? 'दैनिक स्मरण' : 'Daily Reminder'}>
          <View style={[styles.row, { borderBottomWidth: 0 }]}>
            <Text style={styles.rowTxt}>
              {lang === 'hi' ? 'सूचना भेजें' : 'Send notifications'}
            </Text>
            <Switch
              value={notify}
              onValueChange={toggleNotify}
              trackColor={{ true: colors.gold, false: colors.charcoal }}
              thumbColor={notify ? colors.goldLight : '#ccc'}
            />
          </View>
        </Section>

        <Section title={lang === 'hi' ? 'पसंदीदा राशियाँ' : 'Favorite Rashis'}>
          <Text style={styles.helper}>
            {lang === 'hi' ? 'परिवार के सदस्यों की राशियाँ चुनें' : 'Pick your family members\u2019 signs'}
          </Text>
          <View style={styles.favGrid}>
            {RASHIS.map((r) => {
              const sel = favs.includes(r.id);
              return (
                <Pressable
                  key={r.id}
                  style={[styles.favItem, sel && styles.favItemSel]}
                  onPress={() => toggleFav(r.id)}
                >
                  <Text style={[styles.favTxt, sel && styles.favTxtSel]}>
                    {lang === 'hi' ? r.hi : r.en}
                  </Text>
                </Pressable>
              );
            })}
          </View>
        </Section>

        <Section title={lang === 'hi' ? 'के बारे में' : 'About'}>
          <Text style={styles.aboutLine}>Rashifal.online</Text>
          <Text style={styles.aboutSub}>Est. 2026 · Bhopal, India</Text>
          <Pressable
            style={styles.linkRow}
            onPress={() => Linking.openURL('https://rashifal.online/methodology.html')}
          >
            <Text style={styles.linkTxt}>
              {lang === 'hi' ? 'हमारी पद्धति' : 'Our Methodology'}
            </Text>
            <Text style={styles.gold}>›</Text>
          </Pressable>
          <Pressable
            style={styles.linkRow}
            onPress={() => Linking.openURL('https://rashifal.online')}
          >
            <Text style={styles.linkTxt}>rashifal.online</Text>
            <Text style={styles.gold}>›</Text>
          </Pressable>
          <Pressable
            style={styles.linkRow}
            onPress={() => Linking.openURL(PLAY_STORE_URL).catch(() => {})}
          >
            <Text style={styles.linkTxt}>
              {lang === 'hi' ? 'इस ऐप को रेट करें' : 'Rate this app'}
            </Text>
            <Text style={styles.gold}>›</Text>
          </Pressable>
          <Text style={styles.version}>v{APP_VERSION}</Text>
        </Section>
      </ScrollView>
    </View>
  );
}

function Section({ title, children }) {
  return (
    <View style={styles.section}>
      <Text style={styles.sectionTitle}>{title}</Text>
      <View style={styles.sectionBody}>{children}</View>
    </View>
  );
}

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: colors.background },
  section: { marginBottom: 22 },
  sectionTitle: {
    color: colors.gold, fontSize: 11, letterSpacing: 0.8,
    textTransform: 'uppercase', marginBottom: 8, paddingHorizontal: 4,
  },
  sectionBody: {
    backgroundColor: colors.surface, borderRadius: 12,
    borderWidth: 1, borderColor: colors.border, padding: 14,
  },
  row: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between',
    paddingVertical: 8,
  },
  rowTxt: { color: colors.textPrimary, fontSize: sizes.base },
  gold: { color: colors.gold, fontSize: sizes.lg },
  helper: { color: colors.textMuted, fontSize: sizes.xs, marginTop: 6 },
  langBtn: {
    flex: 1, paddingVertical: 12, alignItems: 'center',
    borderRadius: 10, borderWidth: 1, borderColor: colors.border,
  },
  langBtnActive: { borderColor: colors.gold, backgroundColor: colors.goldMuted },
  langBtnTxt: { color: colors.textSecondary, fontSize: sizes.base },
  langBtnTxtActive: { color: colors.gold, fontFamily: fonts.bodyMedium },
  favGrid: { flexDirection: 'row', flexWrap: 'wrap', marginTop: 8, gap: 8 },
  favItem: {
    paddingHorizontal: 12, paddingVertical: 8, borderRadius: 999,
    borderWidth: 1, borderColor: colors.border, backgroundColor: colors.surfaceHigh,
  },
  favItemSel: { borderColor: colors.gold, backgroundColor: colors.goldMuted },
  favTxt: { color: colors.textSecondary, fontSize: sizes.sm },
  favTxtSel: { color: colors.gold },
  aboutLine: { fontFamily: fonts.serif, color: colors.gold, fontSize: sizes.lg },
  aboutSub: { color: colors.textMuted, fontSize: sizes.xs, marginTop: 2, marginBottom: 10 },
  linkRow: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between',
    paddingVertical: 10, borderTopWidth: 1, borderTopColor: colors.border,
  },
  linkTxt: { color: colors.textPrimary, fontSize: sizes.sm },
  version: {
    color: colors.textMuted, fontSize: sizes.xs, textAlign: 'center',
    marginTop: 12,
  },
});
