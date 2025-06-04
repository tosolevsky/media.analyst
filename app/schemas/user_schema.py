from pydantic import BaseModel
from typing import Optional

class UserProfile(BaseModel):
    api_key: str
    model: str
    profile_name: Optional[str] = None
    company_prompt: Optional[str] = None

class TokenHeader(BaseModel):
    token: str
