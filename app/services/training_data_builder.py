import os
import json


def load_feedback(user_id: str) -> list[dict]:
    """
    Kullanıcının feedback.json dosyasını okuyup liste olarak döndürür.
    Her eleman: {"post": ..., "label": "like/dislike"}
    """
    path = f"models/{user_id}/feedback.json"
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
