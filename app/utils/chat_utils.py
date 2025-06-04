def get_chat_url(model_id: str) -> str:
    """
    Model ismine göre doğru chat API URL'sini döndürür.
    """
    model_id = model_id.lower()

    if "claude" in model_id:
        return "https://api.anthropic.com/v1/messages"
    elif "gpt" in model_id:
        return "https://api.openai.com/v1/chat/completions"
    elif "mistral" in model_id or "mixtral" in model_id:
        return "https://openrouter.ai/api/v1/chat/completions"
    else:
        raise ValueError(f"Bilinmeyen model tipi: {model_id}")
