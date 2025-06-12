from fastapi import APIRouter, Depends, HTTPException
from src.models.review import Review
from src.utils.database import reviews_collection, colleges_collection
from src.utils.auth import get_current_user
from bson import ObjectId

router = APIRouter()

@router.get("/colleges/{id}/reviews")
def get_college_reviews(id: str):
    try:
        if not colleges_collection.find_one({"_id": ObjectId(id)}):
            raise HTTPException(status_code=404, detail="College not found")
        reviews = list(reviews_collection.find({"college_id": id}).limit(100))
        return [{"id": str(review["_id"]), **{k: v for k, v in review.items() if k != "_id"}} for review in reviews]
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid college ID")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving reviews: {str(e)}")

@router.post("/reviews")
def submit_review(review: Review, current_user: dict = Depends(get_current_user)):
    try:
        review_dict = review.dict()
        review_dict["user_id"] = str(current_user["_id"])  # Use _id from JWT
        review_dict["college_id"] = str(review.college_id)
        review_dict["_id"] = ObjectId()
        reviews_collection.insert_one(review_dict)
        return {"message": "Review submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error submitting review: {str(e)}")