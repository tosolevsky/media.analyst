from app.services.user_service import get_user_settings
from app.utils.openrouter_client import call_openrouter
from app.utils.openai_client import call_openai
from app.utils.anthropic_client import call_anthropic

DEFAULT_SYSTEM_PROMPT = (
    "Aşağıdaki haber içeriğine göre özgün ve etkileyici bir sosyal medya gönderisi oluştur."
)

def build_prompt(system_prompt: str, company_prompt: str = None, feedback_prompt: str = None) -> str:
    """
    Sistem promptuna şirketin dili (company_prompt) ve varsa feedback_prompt ekleyerek tam prompt oluşturur.
    """
    prompt = system_prompt
    if company_prompt:
        prompt += "\n" + company_prompt
    if feedback_prompt:
        prompt += "\n" + feedback_prompt
    return prompt


def call_model(prompt: str, model: str, api_key: str, provider: str) -> str:
    """
    Verilen modele göre uygun AI sağlayıcısını çağırır ve cevap döner.
    """
    if provider == "openai":
        return call_openai(prompt, model, api_key)
    elif provider == "anthropic":
        return call_anthropic(prompt, model, api_key)
    else:
        return call_openrouter(prompt, model, api_key)


def generate_response(news_text: str, email: str, feedback_prompt: str = None) -> str:
    """
    Kullanıcı ayarlarına göre haber metninden özgün bir sosyal medya postu üretir.
    """
    user_settings = get_user_settings(email)
    model = user_settings.get("model")
    api_key = user_settings.get("api_key")
    provider = user_settings.get("provider", "openrouter")
    company_prompt = user_settings.get("company_prompt")

    if not api_key or not model:
        raise ValueError("API key veya model tanımlı değil.")

    full_prompt = build_prompt(DEFAULT_SYSTEM_PROMPT, company_prompt, feedback_prompt)
    full_prompt += "\n\nHaber içeriği:\n" + news_text

    return call_model(full_prompt, model, api_key, provider)
