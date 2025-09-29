// Vitest global setup for Vue + browser APIs
import { vi } from 'vitest'
import { config } from '@vue/test-utils'

// Router mock helper (we'll set per-test as needed)
config.global.mocks = {
  $router: {
    push: vi.fn()
  }
}

// LocalStorage mock for tests
class LocalStorageMock {
  store = {}
  clear() { this.store = {} }
  getItem(key) { return this.store[key] || null }
  setItem(key, value) { this.store[key] = String(value) }
  removeItem(key) { delete this.store[key] }
}

Object.defineProperty(window, 'localStorage', {
  value: new LocalStorageMock(),
  writable: false
})

// Clipboard mock to avoid errors in components using it
if (!navigator.clipboard) {
  navigator.clipboard = {
    writeText: vi.fn().mockResolvedValue(undefined)
  }
}
