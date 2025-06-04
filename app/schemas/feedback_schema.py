from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class FeedbackRequest(BaseModel):
    post_id: str
    sentiment: Literal["like", "dislike"]
    reasons: List[int] = Field(default_factory=list, max_length=10)
    comment: Optional[str] = Field(default=None, max_length=100)
