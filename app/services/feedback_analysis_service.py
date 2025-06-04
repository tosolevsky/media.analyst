from collections import Counter
from app.constants.feedback_reasons import FEEDBACK_REASON_MAP
from app.services.firebase_service import firestore_db
from pathlib import Path

BASE_DIR = Path("user_guidelines")

def fetch_user_feedbacks(email: str, limit: int = 100):
    feedbacks = (
        firestore_db.collection("feedback")
        .where("user", "==", email)
        .order_by("timestamp", direction="DESCENDING")
        .limit(limit)
        .get()
    )
    return [f.to_dict() for f in feedbacks]

def summarize_feedback(feedbacks: list[dict], max_reasons=5) -> str:
    reason_counter = Counter()
    for fb in feedbacks:
        reason_counter.update(fb.get("reasons", []))

    most_common = reason_counter.most_common(max_reasons)
    summary_lines = [FEEDBACK_REASON_MAP.get(rid, f"ID-{rid}") for rid, _ in most_common]

    summary_text = "Kullanıcı geri bildirimlerinden öne çıkan noktalar:\n"
    summary_text += "\n".join(f"- {line}" for line in summary_lines)

    return summary_text

def generate_guideline_prompt(feedbacks: list[dict]) -> str:
    """Kullanıcı geri bildirimlerine göre prompt oluşturur"""
    dislikes = [f for f in feedbacks if f["sentiment"] == "dislike"]
    likes = [f for f in feedbacks if f["sentiment"] == "like"]

    prompt = "Kullanıcı geri bildirimlerine göre içerik oluşturma yönergelerini güncelle:\n\n"

    if dislikes:
        prompt += "Olumsuz geri bildirimler:\n"
        for f in dislikes:
            prompt += f"- {f['comment']}\n"

    if likes:
        prompt += "\nOlumlu geri bildirimler:\n"
        for f in likes:
            prompt += f"- {f['comment']}\n"

    prompt += "\nYukarıdaki verilere dayanarak yeni yazım yönergelerini 1 paragraf olarak sade bir şekilde öner.\n"
    return prompt
