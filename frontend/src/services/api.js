import axios from "axios";

const baseURL = import.meta.env.DEV
  ? "http://localhost:8000/api"
  : "/api";

const api = axios.create({
  baseURL,
  timeout: 10000,
});

export default api;
