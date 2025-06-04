from app.services.firebase_service import firestore_db 

def get_user_settings(email: str) -> dict:
    doc_ref = firestore_db.collection("users").document(email)
    doc = doc_ref.get()
    if not doc.exists:
        raise ValueError("Kullanıcı ayarları bulunamadı.")
    return doc.to_dict()
