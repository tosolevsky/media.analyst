from app.utils.chat_utils import get_chat_url
from app.utils.predict_best import predict_best_post
import requests


def suggest_post(news_text: str, category: str, model_id: str, api_key: str, model_path: str) -> str:
    """
    LLM ile 3 post önerisi al, en iyisini prediction model ile seç ve döndür.
    """
    prompt = (
        f"Aşağıdaki haber metni için 3 farklı, kısa ve etkili sosyal medya gönderisi öner:\n"
        f"- Her biri 280 karakteri geçmesin.\n"
        f"- Yalnızca post metnini yaz.\n"
        f"- Numara koyma, sadece metinleri sırayla üret.\n\n"
        f"Haber metni:\n{news_text}"
    )

    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
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
        post_list = [line.strip() for line in content.split("\n") if line.strip()]

        return predict_best_post(post_list, model_path)

    except Exception as e:
        return f"[POST OLUŞTURMA HATASI]: {str(e)}"
