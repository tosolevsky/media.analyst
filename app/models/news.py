from pydantic import BaseModel
from typing import Optional


class NewsItem(BaseModel):
    title: str
    summary: str
    link: Optional[str] = None


class NewsVerificationResult(BaseModel):
    score: Optional[int]
    category_match: bool
    error: Optional[str] = None


class NewsSelectionResult(BaseModel):
    news_text: str
    item: NewsItem
