from app.services.feedback_analysis_service import (
    fetch_user_feedbacks,
    generate_guideline_prompt,
)
from app.services.llm_service import call_openrouter
from app.services import firestore_service
from app.core.logger import logger
from app.utils.environment import is_testing_mode


def update_live_guideline(user_email: str):
    """Kullanıcı feedbacklerinden canlı guideline üretir ve Firestore'a kaydeder."""
    try:
        logger.info("[GUIDELINE] Başlatıldı: %s", user_email)

        feedbacks = fetch_user_feedbacks(user_email)
        logger.info("[GUIDELINE] %d adet feedback bulundu.", len(feedbacks))
        if not feedbacks:
            logger.info("[GUIDELINE] Feedback bulunamadı.")
            return

        prompt = generate_guideline_prompt(feedbacks)
        guideline_text = call_openrouter(prompt).strip()
        logger.info("[GUIDELINE] LLM çıktı alındı.")

        # Test modundaysa veritabanına yazma
        if is_testing_mode():
            logger.info("[TEST MODE] Guideline Firestore kaydı yapılmayacak.")
            return

        firestore_service.save_guideline_to_firestore(user_email, guideline_text)
        firestore_service.save_milestone_to_firestore(user_email, guideline_text)

    except Exception as exc:
        logger.warning("[GUIDELINE WARNING] update_live_guideline hata verdi: %s", exc)
