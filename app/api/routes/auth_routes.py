from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth_schema import LoginRequest, RegisterRequest, TokenResponse
from app.services.auth_service import login_user, register_user
from app.core.deps import get_current_user

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    try:
        return login_user(data)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/register", response_model=TokenResponse)
def register(data: RegisterRequest):
    return register_user(data)

@router.get("/me")
def read_current_user(email: str = Depends(get_current_user)):
    return {"email": email}
