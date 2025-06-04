import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

print("DEBUG | TESTING =", os.getenv("TESTING"))

load_dotenv()

TESTING = os.getenv("TESTING") == "1"
print("FIREBASE TESTING:", TESTING)

if TESTING:
    print("TEST ortamı aktif, Firebase başlatılmayacak.")
    firestore_db = None

else:
    if not firebase_admin._apps:
        try:
            service_account_info = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
            cred = credentials.Certificate(service_account_info)
            firebase_admin.initialize_app(cred)
        except Exception as e:
            raise RuntimeError(f"Firebase başlatılamadı: {str(e)}")

    firestore_db = firestore.client()
