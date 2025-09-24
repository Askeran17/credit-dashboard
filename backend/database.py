from pymongo import MongoClient
import os
from dotenv import load_dotenv

# 🔧 Загружаем переменные из ../.env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# 📡 Получаем URI из переменной окружения
mongo_uri = os.getenv("MONGO_URI")

# 🔌 Подключаемся к Atlas
client = MongoClient(mongo_uri)
db = client["credit_dashboard"]

# 🧪 Тест подключения
try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas")
except Exception as e:
    print("❌ Connection failed:", e)

