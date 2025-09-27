from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import institutions, loans
from dotenv import load_dotenv, find_dotenv
from starlette.requests import Request
import os
import requests

# 🔧 Загружаем переменные из .env
load_dotenv(find_dotenv())

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

# 📦 Подключаем API
app.include_router(institutions.router, prefix="/api")
app.include_router(loans.router, prefix="/api")

# 🖼️ Подключаем Vue SPA
if ENV == "development":
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist'))
else:
    frontend_path = os.path.join(os.path.dirname(__file__), 'static')

app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")

# 🌍 Показываем внешний IP контейнера (для MongoDB Atlas whitelist)
@app.get("/ip")
def get_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return {"ip": ip}
    except Exception as e:
        return {"error": str(e)}

# 🔁 SPA fallback для Vue Router
@app.middleware("http")
async def spa_fallback(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 404 and not request.url.path.startswith("/api"):
        return FileResponse(os.path.join(frontend_path, "index.html"))
    return response

