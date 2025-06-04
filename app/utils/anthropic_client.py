import httpx

def call_anthropic(prompt: str, model: str, api_key: str) -> str:
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    body = {
        "model": model,
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = httpx.post(url, headers=headers, json=body, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data["content"][0]["text"]
    except httpx.HTTPStatusError as e:
        return f"[Anthropic HTTP hatası]: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"[Anthropic API hatası]: {str(e)}"
