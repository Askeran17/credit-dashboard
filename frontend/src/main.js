// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/styles.css'

// ❌ Не нужно настраивать axios здесь — всё централизовано в api.js

createApp(App).use(router).mount('#app')


