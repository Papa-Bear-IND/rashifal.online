import React, { useEffect, useState, useCallback } from 'react';
import { View, ActivityIndicator, StatusBar } from 'react-native';
import { NavigationContainer, DefaultTheme } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import {
  useFonts,
  CormorantGaramond_400Regular,
  CormorantGaramond_500Medium,
  CormorantGaramond_600SemiBold,
  CormorantGaramond_400Regular_Italic,
} from '@expo-google-fonts/cormorant-garamond';
import Svg, { Path, Circle, Rect, Line } from 'react-native-svg';

import { colors } from './src/theme/colors';
import HomeScreen from './src/screens/HomeScreen';
import RashiDetailScreen from './src/screens/RashiDetailScreen';
import PanchangScreen from './src/screens/PanchangScreen';
import FestivalScreen from './src/screens/FestivalScreen';
import CompatibilityScreen from './src/screens/CompatibilityScreen';
import SettingsScreen from './src/screens/SettingsScreen';
import { LangProvider } from './src/utils/LangContext';

const Tab = createBottomTabNavigator();
const Stack = createStackNavigator();

const navTheme = {
  ...DefaultTheme,
  dark: true,
  colors: {
    ...DefaultTheme.colors,
    background: colors.background,
    card: colors.background,
    text: colors.textPrimary,
    primary: colors.gold,
    border: 'rgba(245,240,230,0.08)',
  },
};

function TabIcon({ name, color }) {
  const stroke = color;
  switch (name) {
    case 'home':
      return (
        <Svg width={22} height={22} viewBox="0 0 24 24" fill="none" stroke={stroke} strokeWidth={1.6} strokeLinecap="round" strokeLinejoin="round">
          <Path d="M3 11l9-8 9 8" />
          <Path d="M5 10v10h14V10" />
        </Svg>
      );
    case 'calendar':
      return (
        <Svg width={22} height={22} viewBox="0 0 24 24" fill="none" stroke={stroke} strokeWidth={1.6} strokeLinecap="round" strokeLinejoin="round">
          <Rect x={3} y={5} width={18} height={16} rx={2} />
          <Line x1={3} y1={10} x2={21} y2={10} />
          <Line x1={8} y1={3} x2={8} y2={7} />
          <Line x1={16} y1={3} x2={16} y2={7} />
        </Svg>
      );
    case 'lamp':
      return (
        <Svg width={22} height={22} viewBox="0 0 24 24" fill="none" stroke={stroke} strokeWidth={1.6} strokeLinecap="round" strokeLinejoin="round">
          <Path d="M5 14h14l-2 4H7z" />
          <Path d="M9 14c0-3 1-5 3-7 2 2 3 4 3 7" />
          <Line x1={12} y1={5} x2={12} y2={3} />
        </Svg>
      );
    case 'gear':
      return (
        <Svg width={22} height={22} viewBox="0 0 24 24" fill="none" stroke={stroke} strokeWidth={1.6} strokeLinecap="round" strokeLinejoin="round">
          <Circle cx={12} cy={12} r={3} />
          <Path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8 2 2 0 1 1-2.8 2.8 1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5 2 2 0 1 1-4 0 1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.8.3 2 2 0 1 1-2.8-2.8 1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1 2 2 0 1 1 0-4 1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.8 2 2 0 1 1 2.8-2.8 1.7 1.7 0 0 0 1.8.3 1.7 1.7 0 0 0 1-1.5 2 2 0 1 1 4 0 1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3 2 2 0 1 1 2.8 2.8 1.7 1.7 0 0 0-.3 1.8 1.7 1.7 0 0 0 1.5 1 2 2 0 1 1 0 4 1.7 1.7 0 0 0-1.5 1z" />
        </Svg>
      );
  }
  return null;
}

function HomeStack() {
  return (
    <Stack.Navigator screenOptions={{ headerShown: false, cardStyle: { backgroundColor: colors.background } }}>
      <Stack.Screen name="HomeMain" component={HomeScreen} />
      <Stack.Screen name="RashiDetail" component={RashiDetailScreen} />
      <Stack.Screen name="Compatibility" component={CompatibilityScreen} />
    </Stack.Navigator>
  );
}

function Tabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        headerShown: false,
        tabBarStyle: {
          backgroundColor: 'rgba(7,11,20,0.95)',
          borderTopColor: 'rgba(245,240,230,0.08)',
          height: 64,
          paddingBottom: 8,
          paddingTop: 8,
        },
        tabBarActiveTintColor: colors.gold,
        tabBarInactiveTintColor: colors.textMuted,
        tabBarLabelStyle: { fontSize: 11, letterSpacing: 0.4 },
        tabBarIcon: ({ color }) => {
          const map = { Home: 'home', Panchang: 'calendar', Festivals: 'lamp', Settings: 'gear' };
          return <TabIcon name={map[route.name]} color={color} />;
        },
      })}
    >
      <Tab.Screen name="Home" component={HomeStack} />
      <Tab.Screen name="Panchang" component={PanchangScreen} />
      <Tab.Screen name="Festivals" component={FestivalScreen} />
      <Tab.Screen name="Settings" component={SettingsScreen} />
    </Tab.Navigator>
  );
}

export default function App() {
  const [fontsLoaded] = useFonts({
    CormorantGaramond_400Regular,
    CormorantGaramond_500Medium,
    CormorantGaramond_600SemiBold,
    CormorantGaramond_400Regular_Italic,
  });

  if (!fontsLoaded) {
    return (
      <View style={{ flex: 1, backgroundColor: colors.background, alignItems: 'center', justifyContent: 'center' }}>
        <ActivityIndicator color={colors.gold} />
      </View>
    );
  }

  return (
    <SafeAreaProvider>
      <LangProvider>
        <StatusBar barStyle="light-content" backgroundColor={colors.background} />
        <NavigationContainer theme={navTheme}>
          <Tabs />
        </NavigationContainer>
      </LangProvider>
    </SafeAreaProvider>
  );
}
