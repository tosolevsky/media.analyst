from app.services.news_fetcher import fetch_news
from app.services.news_selector import select_best_news
from app.services.news_verifier import verify_news


def get_verified_news(category: str, region: str, model_id: str, api_key: str):
    """
    Kategori ve bölgeye göre haberleri çek, en uygun olanı doğrula ve döndür.
    Gerekirse birden fazla haber dener.
    """
    news_list = fetch_news(category, region)
    tried_indexes = []

    while True:
        news_text, index, item = select_best_news(news_list, tried_indexes)
        if news_text is None:
            return None, None

        result = verify_news(news_text, category, model_id, api_key)
        score = result["score"]
        category_ok = result["category_match"]

        if score is not None and score >= 8 and category_ok:
            return news_text, item

        tried_indexes.append(index)
