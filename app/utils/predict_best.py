import joblib


def predict_best_post(posts: list[str], model_path: str) -> str:
    """
    Eğitimli model ile 3 post arasından en iyi olanı seçer.
    """
    model = joblib.load(model_path)
    scores = model.predict_proba(posts)
    best_index = scores[:, 1].argmax()
    return posts[best_index]
