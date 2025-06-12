from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.utils.database import users_collection
from src.utils.auth import create_access_token
from bson import ObjectId

router = APIRouter()

class ValidationRequest(BaseModel):
    id: str
@router.post("/validate")
def validate_student(request: ValidationRequest):
    user = users_collection.find_one({"college_id": request.id})  # Changed from "id" to "college_id"
    if not user:
        raise HTTPException(status_code=400, detail="Invalid ID")
    access_token = create_access_token({"sub": str(user["_id"])})  # Use _id for token
    return {"token": access_token, "user": {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}}