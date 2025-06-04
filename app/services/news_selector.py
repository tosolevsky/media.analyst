from typing import Tuple


def select_best_news(news_list: list[dict], tried_indexes: list[int]) -> Tuple[str, int, dict]:
    """
    Daha önce denenmeyen en uygun haberi seçer.
    Geriye haber metni, index'i ve orijinal item'ı döner.
    """
    for idx, item in enumerate(news_list):
        if idx in tried_indexes:
            continue

        title = item.get("title", "")
        summary = item.get("summary", "")
        news_text = f"{title}\n\n{summary}".strip()

        if news_text:
            return news_text, idx, item

    return None, -1, None
