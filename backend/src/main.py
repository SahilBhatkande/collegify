
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.routes import colleges, reviews, validate, ai_suggestion, auth
from fastapi.staticfiles import StaticFiles
import os

load_dotenv()

app = FastAPI()

# Serve static images from /images
images_path = os.path.join(os.path.dirname(__file__), '../../college-frontend/public/images')
app.mount("/images", StaticFiles(directory=images_path), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(colleges.router, prefix="/api")
app.include_router(reviews.router, prefix="/api")
app.include_router(validate.router, prefix="/api")
app.include_router(ai_suggestion.router, prefix="/api")
app.include_router(auth.router, prefix="/api")  # Ensure this line is present

@app.get("/")
async def root():
    return {"message": "College Recommendation Backend"}
