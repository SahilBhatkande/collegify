from fastapi import APIRouter
from src.utils.database import colleges_collection
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

@router.post("/ai-suggestion")
def get_ai_suggestions(data: dict):
    api_key = os.getenv("API_KEY")
    try:
        response = requests.post(
            "https://api.collegeai.com/data",
            json=data,
            headers={"Authorization": f"{api_key}"}
        )
        response.raise_for_status()
        colleges = response.json()
        return colleges
    except Exception:
        query = {}
        if data.get("college_id"):
            query["college_id"] = data.get("college_id")
        colleges = list(colleges_collection.find(query))
        return [{"id": str(college["_id"]), **{k: v for k, v in college.items() if k != "_id"}} for college in colleges]