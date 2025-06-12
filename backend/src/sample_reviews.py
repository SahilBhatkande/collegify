from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson import ObjectId

# Load environment variables
load_dotenv()

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["collegeDB"]
reviews_collection = db["reviews"]
users_collection = db["users"]
colleges_collection = db["colleges"]

# Clear existing reviews (optional, comment out to append)
reviews_collection.delete_many({})

# Get sample user and college IDs
users = list(users_collection.find().limit(5))  # From sample_users.py
colleges = list(colleges_collection.find().limit(5))  # From sample_data.py

# Sample reviews
sample_reviews = [
    {
        "_id": ObjectId(),
        "college_id": str(colleges[0]["_id"]),  # e.g., IIT Delhi
        "user_id": str(users[0]["_id"]),  # e.g., John Doe
        "comment": "Excellent faculty and research opportunities!"
    },
    {
        "_id": ObjectId(),
        "college_id": str(colleges[0]["_id"]),
        "user_id": str(users[1]["_id"]),  # Jane Smith
        "comment": "Great campus but competitive environment."
    },
    {
        "_id": ObjectId(),
        "college_id": str(colleges[1]["_id"]),  # e.g., IIT Bombay
        "user_id": str(users[2]["_id"]),  # Third user
        "comment": "Amazing placement support!"
    },
    {
        "_id": ObjectId(),
        "college_id": str(colleges[1]["_id"]),
        "user_id": str(users[3]["_id"]),  # Fourth user
        "comment": "Modern facilities, highly recommended."
    },
    {
        "_id": ObjectId(),
        "college_id": str(colleges[2]["_id"]),  # e.g., IIT Madras
        "user_id": str(users[4]["_id"]),  # Fifth user
        "comment": "Beautiful campus and strong academics."
    }
]

# Insert reviews
reviews_collection.insert_many(sample_reviews)
print("5 reviews inserted successfully into reviews collection.")