from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import certifi

load_dotenv(find_dotenv())
# 📡 Получаем URI из переменной окружения
mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError("❌ MONGO_URI is not set. Check your environment variables.")

# 🔌 Подключаемся к Atlas
client = MongoClient(mongo_uri, tls=True, tlsCAFile=certifi.where())
db = client["credit_dashboard"]

# 🧪 Тест подключения
try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas")
except Exception as e:
    print("❌ Connection failed:", e)


