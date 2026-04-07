import AsyncStorage from '@react-native-async-storage/async-storage';

const PREFS_KEY = 'rashifal_prefs';
const CACHE_PREFIX = 'rashifal_daily_';

export async function loadPrefs() {
  try {
    const raw = await AsyncStorage.getItem(PREFS_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export async function savePrefs(p) {
  try {
    await AsyncStorage.setItem(PREFS_KEY, JSON.stringify(p));
  } catch {}
}

export async function patchPrefs(patch) {
  const cur = await loadPrefs();
  const next = { ...cur, ...patch };
  await savePrefs(next);
  return next;
}

export async function getCachedDaily(dateStr) {
  try {
    const raw = await AsyncStorage.getItem(CACHE_PREFIX + dateStr);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

export async function setCachedDaily(dateStr, data) {
  try {
    await AsyncStorage.setItem(CACHE_PREFIX + dateStr, JSON.stringify(data));
  } catch {}
}
