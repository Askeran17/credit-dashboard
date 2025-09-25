from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import institutions, loans
from dotenv import load_dotenv
import os
import requests

# 🔧 Загружаем переменные из ../.env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

app = FastAPI()

# 🌐 CORS — только в режиме разработки
ENV = os.getenv("ENV", "development")
if ENV == "development":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

# 📦 Подключаем API на /api/*
app.include_router(institutions.router, prefix="/api")
app.include_router(loans.router, prefix="/api")

# 🌍 IP endpoint
@app.get("/api/ip")
def get_ip():
    import requests
    return {"ip": requests.get("https://api.ipify.org").text}

# 🖼️ Подключаем Vue SPA на /
frontend_path = os.path.join(os.path.dirname(__file__), 'static')
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")

# 🏠 Отдаём index.html по корневому маршруту
@app.get("/")
def serve_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# 🌍 Показываем внешний IP контейнера (для MongoDB Atlas whitelist)
@app.get("/ip")
def get_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return {"ip": ip}
    except Exception as e:
        return {"error": str(e)}
