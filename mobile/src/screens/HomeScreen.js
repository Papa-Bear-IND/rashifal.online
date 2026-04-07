import React, { useEffect, useState, useCallback } from 'react';
import {
  View, Text, ScrollView, FlatList, RefreshControl, Pressable, StyleSheet, ActivityIndicator,
} from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { colors } from '../theme/colors';
import { fonts, sizes } from '../theme/typography';
import Header from '../components/Header';
import RashiCard from '../components/RashiCard';
import CategoryCard from '../components/CategoryCard';
import { RASHIS, rashiFromDate } from '../data/rashis';
import { fetchDaily } from '../utils/api';
import { loadPrefs } from '../utils/storage';
import { useLang, t } from '../utils/LangContext';

export default function HomeScreen({ navigation }) {
  const { lang } = useLang();
  const [dd, setDD] = useState(null);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [yourId, setYourId] = useState(null);
  const [source, setSource] = useState('');

  const load = useCallback(async () => {
    const { data, source } = await fetchDaily();
    setDD(data);
    setSource(source);
    setLoading(false);
    setRefreshing(false);
  }, []);

  useEffect(() => {
    load();
  }, [load]);

  useFocusEffect(
    useCallback(() => {
      (async () => {
        const p = await loadPrefs();
        if (p.dob) {
          const d = new Date(p.dob + 'T00:00:00');
          if (!isNaN(d)) setYourId(rashiFromDate(d));
        } else {
          setYourId(null);
        }
      })();
    }, [])
  );

  const onRefresh = () => {
    setRefreshing(true);
    load();
  };

  const yourIdx = yourId ? RASHIS.findIndex((r) => r.id === yourId) : -1;
  const ordered = yourIdx >= 0 ? [RASHIS[yourIdx], ...RASHIS.filter((_, i) => i !== yourIdx)] : RASHIS;

  const open = (rashi) => {
    const idx = RASHIS.findIndex((r) => r.id === rashi.id);
    navigation.navigate('RashiDetail', { idx });
  };

  const cats = [
    { key: 'love',    icon: '♥', titleHi: 'प्रेम',   titleEn: 'Love' },
    { key: 'career',  icon: '⚒', titleHi: 'करियर',  titleEn: 'Career' },
    { key: 'health',  icon: '✚', titleHi: 'स्वास्थ्य', titleEn: 'Health' },
    { key: 'finance', icon: '₹', titleHi: 'धन',     titleEn: 'Finance' },
  ];

  return (
    <View style={styles.root}>
      <Header subtitle={lang === 'hi' ? 'वैदिक ज्योतिष पद्धति पर आधारित' : 'Based on Vedic Astrology principles'} />
      {loading ? (
        <View style={styles.centerFill}>
          <ActivityIndicator color={colors.gold} />
          <Text style={styles.loadingTxt}>
            {lang === 'hi' ? 'आज का राशिफल लोड हो रहा है…' : 'Loading today\u2019s rashifal…'}
          </Text>
        </View>
      ) : (
        <ScrollView
          contentContainerStyle={{ paddingBottom: 24 }}
          refreshControl={
            <RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={colors.gold} />
          }
        >
          {!dd && (
            <View style={styles.notice}>
              <Text style={styles.noticeTxt}>
                {lang === 'hi'
                  ? 'राशिफल लोड नहीं हुआ। नीचे खींचकर पुनः प्रयास करें।'
                  : 'Could not load today\u2019s rashifal. Pull down to retry.'}
              </Text>
            </View>
          )}

          <View style={styles.titleBlock}>
            <Text style={styles.h2}>{lang === 'hi' ? 'आज का राशिफल' : 'Today\u2019s Rashifal'}</Text>
            <Text style={styles.h2Sub}>
              {lang === 'hi'
                ? 'सभी 12 राशियों के लिए आज ग्रहों का संदेश'
                : 'What the planets say for all 12 signs today'}
            </Text>
          </View>

          <FlatList
            data={ordered}
            scrollEnabled={false}
            keyExtractor={(r) => r.id}
            numColumns={2}
            contentContainerStyle={{ paddingHorizontal: 8 }}
            renderItem={({ item }) => {
              const i = RASHIS.findIndex((r) => r.id === item.id);
              const rd = dd?.rashis?.[i];
              const ld = rd ? (lang === 'hi' ? rd.hindi : rd.english) : null;
              return (
                <RashiCard
                  rashi={item}
                  ld={ld}
                  isYours={yourId === item.id}
                  onPress={() => open(item)}
                />
              );
            }}
          />

          <View style={styles.titleBlock}>
            <Text style={styles.h2}>{lang === 'hi' ? 'श्रेणियाँ' : 'Categories'}</Text>
          </View>
          <ScrollView
            horizontal
            showsHorizontalScrollIndicator={false}
            contentContainerStyle={{ paddingHorizontal: 14, paddingBottom: 8 }}
          >
            {cats.map((c) => {
              const i = yourIdx >= 0 ? yourIdx : 0;
              const rd = dd?.rashis?.[i];
              const ld = rd ? (lang === 'hi' ? rd.hindi : rd.english) : null;
              return (
                <CategoryCard
                  key={c.key}
                  icon={c.icon}
                  title={lang === 'hi' ? c.titleHi : c.titleEn}
                  text={
                    ld?.[c.key] ||
                    (lang === 'hi' ? 'अपनी राशि के लिए विवरण देखें' : 'Open your rashi for details')
                  }
                />
              );
            })}
          </ScrollView>

          <Pressable
            style={styles.compatBtn}
            onPress={() => navigation.navigate('Compatibility')}
          >
            <Text style={styles.compatBtnTxt}>
              {lang === 'hi' ? 'राशि अनुकूलता जाँचें' : 'Check Rashi Compatibility'}
            </Text>
          </Pressable>

          {source === 'cache' && (
            <Text style={styles.cacheNote}>
              {lang === 'hi' ? 'ऑफ़लाइन — सहेजा गया डेटा' : 'Offline — showing cached data'}
            </Text>
          )}
        </ScrollView>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: colors.background },
  centerFill: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  loadingTxt: { color: colors.textMuted, marginTop: 12, fontSize: sizes.sm },
  titleBlock: { paddingHorizontal: 18, paddingTop: 18, paddingBottom: 8 },
  h2: { fontFamily: fonts.serif, color: colors.gold, fontSize: sizes.xl },
  h2Sub: { color: colors.textMuted, fontSize: sizes.sm, marginTop: 2 },
  compatBtn: {
    marginHorizontal: 18,
    marginTop: 16,
    paddingVertical: 14,
    borderRadius: 999,
    borderWidth: 1,
    borderColor: colors.gold,
    alignItems: 'center',
  },
  compatBtnTxt: { color: colors.gold, fontSize: sizes.base, letterSpacing: 0.4 },
  notice: {
    margin: 14, padding: 12, borderRadius: 10,
    backgroundColor: 'rgba(220,80,80,0.1)', borderWidth: 1, borderColor: 'rgba(220,80,80,0.4)',
  },
  noticeTxt: { color: colors.textPrimary, fontSize: sizes.sm },
  cacheNote: { color: colors.textMuted, fontSize: sizes.xs, textAlign: 'center', marginTop: 16 },
});
