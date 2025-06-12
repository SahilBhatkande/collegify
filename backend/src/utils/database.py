from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Use MongoDB Atlas URI from .env
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.get_database("collegeDB")

colleges_collection = db["colleges"]
users_collection = db["users"]  # Added users collection
reviews_collection = db["reviews"]