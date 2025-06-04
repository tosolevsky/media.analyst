import os
from app.services.feedback_analysis_service import (
    fetch_user_feedbacks,
    generate_guideline_prompt,
)
from app.services.llm_service import call_openrouter
from app.services import firestore_service

def is_testing_mode() -> bool:
    """Prod / test ayrımı."""
    return os.environ.get("TESTING", "0") == "1"


def update_live_guideline(user_email: str):
    """Kullanıcı feedbacklerinden canlı guideline üretir ve Firestore'a kaydeder."""
    try:
        print(f"[GUIDELINE] Başlatıldı: {user_email}")

        feedbacks = fetch_user_feedbacks(user_email)
        print(f"[GUIDELINE] {len(feedbacks)} adet feedback bulundu.")
        if not feedbacks:
            print("[GUIDELINE] Feedback bulunamadı.")
            return

        prompt = generate_guideline_prompt(feedbacks)
        guideline_text = call_openrouter(prompt).strip()
        print("[GUIDELINE] LLM çıktı alındı.")

        # Test modundaysa veritabanına yazma
        if is_testing_mode():
            print("[TEST MODE] Guideline Firestore kaydı yapılmayacak.")
            return

        firestore_service.save_guideline_to_firestore(user_email, guideline_text)
        firestore_service.save_milestone_to_firestore(user_email, guideline_text)

    except Exception as exc:
        print(f"[GUIDELINE WARNING] update_live_guideline hata verdi: {exc}")
