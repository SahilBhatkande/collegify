from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["collegeDB"]
colleges = db["colleges"]

# Clear existing data (optional, comment out if you want to append)
colleges.delete_many({})

# 10 colleges with varied data
sample_colleges = [
    {
        "name": "IIT Bombay",
        "location": "Mumbai, Maharashtra",
        "fees": 200000,
        "placement": 15.0,
        "campus": "Large, modern campus with advanced facilities",
        "description": "Premier engineering institute in India.",
        "rank": 1,
        "score": 90
    },
    {
        "name": "IIT Delhi",
        "location": "New Delhi, Delhi",
        "fees": 220000,
        "placement": 14.5,
        "campus": "Sprawling campus with research labs",
        "description": "Top-tier institute known for innovation.",
        "rank": 2,
        "score": 88
    },
    {
        "name": "Anna University",
        "location": "Chennai, Tamil Nadu",
        "fees": 150000,
        "placement": 10.0,
        "campus": "Sprawling campus with good infrastructure",
        "description": "Leading technical university in South India.",
        "rank": 10,
        "score": 85
    },
    {
        "name": "BITS Pilani",
        "location": "Pilani, Rajasthan",
        "fees": 400000,
        "placement": 12.0,
        "campus": "Modern campus with strong industry ties",
        "description": "Private institute with excellent placements.",
        "rank": 4,
        "score": 87
    },
    {
        "name": "NIT Trichy",
        "location": "Tiruchirappalli, Tamil Nadu",
        "fees": 180000,
        "placement": 11.0,
        "campus": "Large campus with advanced facilities",
        "description": "Top NIT known for engineering excellence.",
        "rank": 8,
        "score": 86
    },
    {
        "name": "IIT Madras",
        "location": "Chennai, Tamil Nadu",
        "fees": 210000,
        "placement": 14.0,
        "campus": "Green campus with cutting-edge labs",
        "description": "Renowned for research and academics.",
        "rank": 3,
        "score": 89
    },
    {
        "name": "VIT Vellore",
        "location": "Vellore, Tamil Nadu",
        "fees": 350000,
        "placement": 9.0,
        "campus": "Modern campus with global partnerships",
        "description": "Private university with diverse programs.",
        "rank": 12,
        "score": 84
    },
    {
        "name": "IIT Kharagpur",
        "location": "Kharagpur, West Bengal",
        "fees": 200000,
        "placement": 13.5,
        "campus": "Vast campus with historic significance",
        "description": "One of the oldest and top IITs.",
        "rank": 5,
        "score": 88
    },
    {
        "name": "Jadavpur University",
        "location": "Kolkata, West Bengal",
        "fees": 100000,
        "placement": 8.5,
        "campus": "Urban campus with strong academics",
        "description": "State university with affordable fees.",
        "rank": 15,
        "score": 83
    },
    {
        "name": "IIIT Hyderabad",
        "location": "Hyderabad, Telangana",
        "fees": 300000,
        "placement": 12.5,
        "campus": "Tech-focused campus with startup culture",
        "description": "Leading institute for IT and CS.",
        "rank": 7,
        "score": 86
    }
]

# Insert data into MongoDB Atlas
colleges.insert_many(sample_colleges)
print("10 colleges inserted successfully.")