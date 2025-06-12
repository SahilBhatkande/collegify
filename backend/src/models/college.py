from pydantic import BaseModel
from typing import Optional

class College(BaseModel):
    id: Optional[str] = None
    name: str
    location: str
    fees: float
    placement: float
    campus: str
    description: Optional[str] = None
    rank: Optional[int] = None  # CHANGE: Added for filtering
    score: Optional[float] = None  # CHANGE: Added for filtering