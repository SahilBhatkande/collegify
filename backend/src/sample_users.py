from src.utils.database import users_collection
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from bson import ObjectId

# Load environment variables
load_dotenv()

# Initialize password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["collegeDB"]
users_collection = db["users"]

# Clear existing users (optional, comment out to append)
users_collection.delete_many({})

# Sample users
sample_users = [
    {
        "_id": ObjectId(),
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": hash_password("password123"),
        "college_id": "student001"
    },
    {
        "_id": ObjectId(),
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "password": hash_password("password456"),
        "college_id": "student002"
    },
    {
        "_id": ObjectId(),
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "password": hash_password("password789"),
        "college_id": "student003"
    },
    {
        "_id": ObjectId(),
        "name": "Bob Brown",
        "email": "bob.brown@example.com",
        "password": hash_password("password101"),
        "college_id": "student004"
    },
    {
        "_id": ObjectId(),
        "name": "Emma Wilson",
        "email": "emma.wilson@example.com",
        "password": hash_password("password202"),
        "college_id": "student005"
    }
]

# Insert users into MongoDB Atlas
users_collection.insert_many(sample_users)
print("5 users inserted successfully into users collection.")