import React, { createContext, useContext, useEffect, useState, useCallback } from 'react';
import { loadPrefs, patchPrefs } from './storage';

const LangContext = createContext({ lang: 'hi', setLang: () => {} });

export function LangProvider({ children }) {
  const [lang, setLangState] = useState('hi');
  const [ready, setReady] = useState(false);

  useEffect(() => {
    (async () => {
      const p = await loadPrefs();
      if (p.lang === 'hi' || p.lang === 'en') setLangState(p.lang);
      setReady(true);
    })();
  }, []);

  const setLang = useCallback(async (l) => {
    setLangState(l);
    await patchPrefs({ lang: l });
  }, []);

  return (
    <LangContext.Provider value={{ lang, setLang, ready }}>
      {children}
    </LangContext.Provider>
  );
}

export function useLang() {
  return useContext(LangContext);
}

export function t(lang, hi, en) {
  return lang === 'hi' ? hi : en;
}
