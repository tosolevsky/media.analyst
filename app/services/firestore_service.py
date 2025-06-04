import os
from datetime import datetime, timezone
from app.services.firebase_service import firestore_db
from app.core.logger import logger

# Ortam kontrolü
TESTING = os.getenv("TESTING") == "1"
if TESTING:
    logger.info("FIREBASE TESTING: True")
else:
    logger.info("FIREBASE TESTING: False")


def save_guideline_to_firestore(email: str, guideline: str):
    try:
        if TESTING:
            logger.info("[TEST MODE] Guideline Firestore kaydı yapılmayacak.")
            return

        firestore_db.collection("guidelines").add({
            "user_email": email,
            "guideline": guideline,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

    except Exception as e:
        logger.warning("[ERROR] save_guideline_to_firestore: %s", str(e))


def save_milestone_to_firestore(email: str, guideline: str):
    try:
        if TESTING:
            logger.info("[TEST MODE] Milestone Firestore kaydı yapılmayacak.")
            return

        firestore_db.collection("milestones").add({
            "user_email": email,
            "guideline": guideline,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

    except Exception as e:
        logger.warning("[ERROR] save_milestone_to_firestore: %s", str(e))


def save_feedback_to_firestore(data: dict):
    """Save a feedback document under the ``feedback`` collection."""
    firestore_db.collection("feedback").add(data)


def save_user_profile(email: str, data: dict):
    """Create or overwrite a user profile document."""
    doc_ref = firestore_db.collection("profiles").document(email)
    doc_ref.set(data)


def get_user_profile(email: str) -> dict | None:
    """Retrieve a user profile or return ``None`` if it doesn't exist."""
    doc_ref = firestore_db.collection("profiles").document(email)
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None


def update_user_profile(email: str, data: dict):
    """Update fields of a user profile document."""
    doc_ref = firestore_db.collection("profiles").document(email)
    doc_ref.update(data)
