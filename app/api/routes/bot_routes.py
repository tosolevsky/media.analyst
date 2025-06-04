from fastapi import APIRouter, Depends
from app.core.deps import get_current_user
from app.schemas.bot_schema import BotRequest, BotResponse
from app.services.bot_service import generate_response

router = APIRouter()

@router.post("/generate", response_model=BotResponse)
async def generate_post(
    request: BotRequest,
    user_email: str = Depends(get_current_user)
):
    result = generate_response(request.prompt, user_email)
    return BotResponse(result=result)
