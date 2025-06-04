import os
import json
from dotenv import load_dotenv
from app.core.logger import logger

load_dotenv()
TESTING = os.getenv("TESTING") == "1"
logger.info("FIREBASE TESTING: %s", TESTING)

if TESTING:
    logger.info("TEST ortamı aktif, Firebase başlatılmayacak.")
    firestore_db = None
else:
    import firebase_admin
    from firebase_admin import credentials, firestore

    if not firebase_admin._apps:
        try:
            service_account_info = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
            cred = credentials.Certificate(service_account_info)
            firebase_admin.initialize_app(cred)
        except Exception as e:
            raise RuntimeError(f"Firebase başlatılamadı: {str(e)}")

    firestore_db = firestore.client()
