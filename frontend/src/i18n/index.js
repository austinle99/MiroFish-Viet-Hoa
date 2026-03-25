import { createI18n } from 'vue-i18n'
import service from '../api/index'
import zh from './zh.json'
import vi from './vi.json'

const savedLocale = localStorage.getItem('mirofish-locale') || 'vi'

const i18n = createI18n({
  legacy: false,
  globalInjection: true,
  locale: savedLocale,
  fallbackLocale: 'vi',
  messages: { zh, vi }
})

export function setLocale(locale) {
  i18n.global.locale.value = locale
  localStorage.setItem('mirofish-locale', locale)
  document.documentElement.setAttribute('lang', locale)

  // Sync language to backend (fire-and-forget)
  service.post('/api/settings/language', { language: locale }).catch(() => {})
}

export function getLocale() {
  return i18n.global.locale.value
}

export default i18n
