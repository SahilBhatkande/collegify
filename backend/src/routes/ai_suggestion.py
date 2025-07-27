from fastapi import APIRouter
from src.utils.database import colleges_collection
import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
import re

load_dotenv()

router = APIRouter()

@router.post("/ai-suggestion")
def get_ai_suggestions(data: dict):
    api_key = os.getenv("API_KEY")
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        prompt = data.get('prompt') or data.get('preferences') or ''
        if not prompt:
            return {"error": "No prompt provided."}
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        query = {}
        if data.get("college_id"):
            query["college_id"] = data.get("college_id")
        colleges = list(colleges_collection.find(query))
        return [{"id": str(college["_id"]), **{k: v for k, v in college.items() if k != "_id"}} for college in colleges]