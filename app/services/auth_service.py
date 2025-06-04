from app.core.security import create_access_token
from app.schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse

# MOCK kullanıcı kontrolü — gerçek sistemde veri tabanı kontrolü olur
FAKE_USER = {
    "email": "test@example.com",
    "password": "123456"
}

def login_user(data: LoginRequest) -> TokenResponse:
    if data.email != FAKE_USER["email"] or data.password != FAKE_USER["password"]:
        raise ValueError("E-posta veya şifre hatalı.")
    
    access_token = create_access_token({"sub": data.email})
    return TokenResponse(access_token=access_token)

def register_user(data: RegisterRequest) -> TokenResponse:
    # Burada kullanıcı kaydını veritabanına yazman gerekir
    # Şimdilik fake kayıt gibi davranıyoruz
    access_token = create_access_token({"sub": data.email})
    return TokenResponse(access_token=access_token)
