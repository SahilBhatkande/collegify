from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.models.college import College
from src.utils.database import colleges_collection
from bson import ObjectId

router = APIRouter()

class CollegeFilter(BaseModel):
    rank: Optional[float] = None
    score: Optional[float] = None
    location: Optional[str] = None
    placement: Optional[float] = None
    fees: Optional[float] = None

@router.get("/colleges")
def search_colleges(search: str = ""):
    try:
        query = {"name": {"$regex": search, "$options": "i"}} if search else {}
        colleges = list(colleges_collection.find(query).limit(100))
        return [{"id": str(college["_id"]), **{k: v for k, v in college.items() if k != "_id"}} for college in colleges]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")

@router.post("/colleges/filter")
def filter_colleges(filters: CollegeFilter):
    try:
        query = {}
        if filters.rank is not None:
            query["rank"] = {"$lte": float(filters.rank)}
        if filters.score is not None:
            query["score"] = {"$gte": float(filters.score)}
        if filters.location:
            query["location"] = {"$regex": filters.location, "$options": "i"}
        if filters.placement is not None:
            query["placement"] = {"$gte": float(filters.placement)}
        if filters.fees is not None:
            query["fees"] = {"$lte": float(filters.fees)}
        colleges = list(colleges_collection.find(query).limit(100))
        return [{"id": str(college["_id"]), **{k: v for k, v in college.items() if k != "_id"}} for college in colleges]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid filter value: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Filter failed: {str(e)}")

@router.get("/colleges/{id}")
def get_college_details(id: str):
    try:
        college = colleges_collection.find_one({"_id": ObjectId(id)})
        if not college:
            raise HTTPException(status_code=404, detail="College not found")
        return {"id": str(college["_id"]), **{k: v for k, v in college.items() if k != "_id"}}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid college ID")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving college: {str(e)}")