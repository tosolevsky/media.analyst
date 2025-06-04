from pydantic import BaseModel

class BotRequest(BaseModel):
    prompt: str

class BotResponse(BaseModel):
    result: str
