from pydantic import BaseModel
from typing import Optional


class ErrorResponse(BaseModel):
    error: str


class StatusMessage(BaseModel):
    status: str
    detail: Optional[str] = None
