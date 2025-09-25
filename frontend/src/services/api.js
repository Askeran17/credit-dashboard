// src/services/api.js
import axios from "axios";

// 🔁 Автоматическое переключение между локальной и прод-средой
const baseURL = import.meta.env.DEV
  ? "http://localhost:8000/api"
  : "/api";

// 📦 Создаём экземпляр axios с базовой конфигурацией
const api = axios.create({
  baseURL,
  timeout: 10000,
});

// 💡 Можно добавить интерсепторы позже (например, для токенов или логов)

export default api;
