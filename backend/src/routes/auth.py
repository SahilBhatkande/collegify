
from fastapi import APIRouter, HTTPException
from src.models.user import User, UserLogin
from src.utils.database import users_collection
from src.utils.auth import verify_password, get_password_hash, create_access_token
from bson import ObjectId

router = APIRouter(prefix="/auth", tags=["auth"])  # Prefix ensures /auth/register

@router.post("/register")
def register(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user.password)
    user_dict["_id"] = ObjectId()
    user_dict["college_id"] = user_dict.get("college_id", str(user_dict["_id"]))
    users_collection.insert_one(user_dict)
    access_token = create_access_token(data={"sub": str(user_dict["_id"])})
    return {"token": access_token, "user": {"id": str(user_dict["_id"]), "name": user.name, "email": user.email}}

@router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": str(db_user["_id"])})
    return {"token": access_token, "user": {"id": str(db_user["_id"]), "name": db_user["name"], "email": db_user["email"]}}
