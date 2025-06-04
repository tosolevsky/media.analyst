import httpx

def call_google(prompt: str, model: str, api_key: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = httpx.post(url, headers=headers, json=body, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except httpx.HTTPStatusError as e:
        return f"[Gemini HTTP hatası]: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"[Gemini API hatası]: {str(e)}"
