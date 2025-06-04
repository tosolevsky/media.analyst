from pydantic import BaseModel
from typing import List, Optional


class PostRequest(BaseModel):
    news_text: str
    category: str
    model_id: str
    api_key: str
    model_path: str


class PostResponse(BaseModel):
    post: str
    alternatives: Optional[List[str]] = None  # İstenirse LLM'den dönen tüm post'lar
