import os
from datetime import datetime, timezone
from app.services.firebase_service import firestore_db

# Ortam kontrolü
TESTING = os.getenv("TESTING") == "1"
if TESTING:
    print("FIREBASE TESTING: True")
else:
    print("FIREBASE TESTING: False")


def save_guideline_to_firestore(email: str, guideline: str):
    try:
        if TESTING:
            print("[TEST MODE] Guideline Firestore kaydı yapılmayacak.")
            return

        firestore_db.collection("guidelines").add({
            "user_email": email,
            "guideline": guideline,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

    except Exception as e:
        print(f"[ERROR] save_guideline_to_firestore: {str(e)}")


def save_milestone_to_firestore(email: str, count: int, guideline: str):
    try:
        if TESTING:
            print("[TEST MODE] Milestone Firestore kaydı yapılmayacak.")
            return

        firestore_db.collection("milestones").add({
            "user_email": email,
            "feedback_count": count,
            "guideline": guideline,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

    except Exception as e:
        print(f"[ERROR] save_milestone_to_firestore: {str(e)}")
