from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import institutions, loans
from dotenv import load_dotenv
import os

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

# 📦 Подключаем API
app.include_router(institutions.router)
app.include_router(loans.router)

# 🖼️ Подключаем Vue SPA
frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'dist')
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")

# 🏠 Отдаём index.html по корневому маршруту
@app.get("/")
def serve_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))


