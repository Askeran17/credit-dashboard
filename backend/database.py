from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import certifi

load_dotenv(find_dotenv())
# Get MongoDB URI from environment variable
mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise ValueError("❌ MONGO_URI is not set. Check your environment variables.")

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri, tls=True, tlsCAFile=certifi.where())
db = client["credit_dashboard"]

# 🧪 Test connection
try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas")
except Exception as e:
    print("❌ Connection failed:", e)


