from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user_schema import UserProfile
from app.core.deps import get_current_user
from app.services.firestore_service import (
    save_user_profile,
    get_user_profile,
    update_user_profile
)

router = APIRouter()


@router.post("/profiles", summary="Yeni profil oluştur")
def create_profile(
    profile: UserProfile,
    user_email: str = Depends(get_current_user)
):
    save_user_profile(user_email, profile.dict())
    return {"message": "Profil başarıyla oluşturuldu."}


@router.get("/profiles/me", response_model=UserProfile, summary="Profilimi getir")
def read_own_profile(
    user_email: str = Depends(get_current_user)
):
    profile_data = get_user_profile(user_email)
    if not profile_data:
        raise HTTPException(status_code=404, detail="Profil bulunamadı.")
    return profile_data


@router.put("/profiles", summary="Profilimi güncelle")
def update_profile(
    profile: UserProfile,
    user_email: str = Depends(get_current_user)
):
    update_user_profile(user_email, profile.dict(exclude_unset=True))
    return {"message": "Profil başarıyla güncellendi."}
