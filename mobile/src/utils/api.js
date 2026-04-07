import { todayIST } from './dateUtils';
import { getCachedDaily, setCachedDaily } from './storage';

const BASE = 'https://rashifal.online';

export async function fetchDaily(dateStr) {
  const date = dateStr || todayIST();
  // Try network first
  try {
    const r = await fetch(`${BASE}/content/${date}.json`);
    if (r.ok) {
      const json = await r.json();
      await setCachedDaily(date, json);
      return { data: json, source: 'network' };
    }
  } catch {}
  // Fall back to cache
  const cached = await getCachedDaily(date);
  if (cached) return { data: cached, source: 'cache' };
  return { data: null, source: 'none' };
}
