import os
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from app.services.training_data_builder import load_feedback
from app.core.logger import logger


def feedback_to_dataframe(user_id: str):
    data = load_feedback(user_id)
    texts = [item["post"] for item in data]
    labels = [1 if item["label"] == "like" else 0 for item in data]
    return pd.DataFrame({"text": texts, "label": labels})


def train_if_ready(user_id: str):
    df = feedback_to_dataframe(user_id)

    if len(df) < 5:
        logger.warning("⚠️ Eğitim için en az 5 kayıt gerekli. Şu an: %d", len(df))
        return

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["text"])
    y = df["label"]

    model = LogisticRegression()
    model.fit(X, y)

    model_path = f"models/{user_id}/post_model.pkl"
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    joblib.dump(model, model_path)
    logger.info("✅ Model kaydedildi: %s", model_path)
