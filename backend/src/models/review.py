from pydantic import BaseModel
from typing import Optional

class Review(BaseModel):
    id: Optional[str] = None
    college_id: str
    comment: str
    user_id: str