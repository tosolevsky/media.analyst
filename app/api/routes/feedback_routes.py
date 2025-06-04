from fastapi import APIRouter, Depends
from app.schemas.feedback_schema import FeedbackRequest
from app.services.feedback_service import save_feedback
from app.core.deps import get_current_user

router = APIRouter()

@router.post("/", status_code=201)
def submit_feedback(
    data: FeedbackRequest,
    user_email: str = Depends(get_current_user)
):
    save_feedback(data, user_email)
    return {"message": "Geri bildirim alındı. Teşekkürler!"}
