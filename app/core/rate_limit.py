import time
from fastapi import HTTPException

# Geçici bellek içi rate limit verisi
user_requests = {}
RATE_LIMIT_SECONDS = 60  # her kullanıcı 60 saniyede bir istek yapabilir


def check_rate_limit(user_id: str):
    """
    Belirtilen kullanıcı için rate limit kontrolü yapar.
    Sınırı aşarsa HTTP 429 hatası fırlatır.
    """
    current_time = time.time()
    last_request_time = user_requests.get(user_id)

    if last_request_time and current_time - last_request_time < RATE_LIMIT_SECONDS:
        seconds_left = int(RATE_LIMIT_SECONDS - (current_time - last_request_time))
        raise HTTPException(
            status_code=429,
            detail=f"Çok fazla istek. Lütfen {seconds_left} saniye bekleyin."
        )

    # Rate limit geçilmediyse, son istek zamanını güncelle
    user_requests[user_id] = current_time
