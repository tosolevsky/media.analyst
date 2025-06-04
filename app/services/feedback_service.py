from datetime import datetime, timezone
from app.schemas.feedback_schema import FeedbackRequest
from app.services.guideline_writer import update_live_guideline
from app.services.firestore_service import save_feedback_to_firestore
from app.services.feedback_analysis_service import fetch_user_feedbacks
from app.core.logger import logger


def save_feedback(data: FeedbackRequest, email: str):
    logger.info("DEBUG | save_feedback çalıştı")

    # 1. Sentiment'a göre geçerli ID aralığı belirle
    if data.sentiment == "like":
        valid_ids = set(range(1, 11))     # 1–10 olumlu nedenler
        liked_bool = True
    elif data.sentiment == "dislike":
        valid_ids = set(range(11, 21))    # 11–20 olumsuz nedenler
        liked_bool = False
    else:
        raise ValueError("Geçersiz sentiment değeri.")

    # 2. Gönderilen reason ID'leri geçerli mi kontrol et
    for rid in data.reasons:
        if rid not in valid_ids:
            raise ValueError(f"Sentiment '{data.sentiment}' için geçersiz reason ID: {rid}")

    # 3. Firestore'a kaydedilecek belge yapısı
    feedback_doc = {
        "post_id": data.post_id,
        "liked": liked_bool,
        "reasons": data.reasons,
        "comment": data.comment,
        "sentiment": data.sentiment,
        "user_email": email,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    # 4. Firestore'a kaydet
    save_feedback_to_firestore(feedback_doc)

    # 5. Guideline güncelle (sessiz hata geçilir)
    try:
        update_live_guideline(email)
    except Exception as e:
        logger.warning("[GUIDELINE WARNING] update_live_guideline hata verdi: %s", str(e))

    # 6. Gerekirse ileri analiz için geçmişleri de çekebilirsin
    try:
        all_feedbacks = fetch_user_feedbacks(email)
        # (opsiyonel) Bu verilerle analiz yapılabilir
    except Exception as e:
        logger.warning("[GUIDELINE WARNING] fetch_user_feedbacks hata verdi: %s", str(e))
