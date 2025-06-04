import requests
from app.utils.chat_utils import get_chat_url


def verify_news(news_text: str, category: str, model_id: str, api_key: str) -> dict:
    """
    Haber metnini LLM kullanarak doğrular.
    - Gündem skoru (1-10)
    - Kategori uyumu (bool)
    """
    prompt = (
        f"Lütfen aşağıdaki haber metnini analiz et:\n"
        f"1. Gündem olma ihtimalini 1 ile 10 arasında puanla.\n"
        f"2. Bu haberin '{category}' kategorisine ait olup olmadığını sadece 'evet' veya 'hayır' olarak belirt.\n\n"
        f"Haber metni:\n{news_text}"
    )

    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        url = get_chat_url(model_id)
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"].strip()
    
        return parse_response(content)

    except Exception as e:
        return {"score": None, "category_match": False, "error": str(e)}


def parse_response(text: str) -> dict:
    import re
    score_match = re.search(r"(\d{1,2})", text)
    category_match = "evet" in text.lower()

    return {
        "score": int(score_match.group(1)) if score_match else None,
        "category_match": category_match
    }
