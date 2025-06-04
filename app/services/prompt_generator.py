from pathlib import Path

DEFAULT_PROMPT = (
    "Aşağıdaki haber metni için 3 farklı, kısa ve etkili sosyal medya gönderisi öner:\n"
    "- Her biri 280 karakteri geçmesin.\n"
    "- Yalnızca post metnini yaz.\n"
    "- Numara koyma, sadece metinleri sırayla üret.\n\n"
    "Haber metni:\n{news_text}"
)

BASE_DIR = Path("user_guidelines")

def generate_prompt(user_email: str, news_text: str) -> str:
    user_dir = BASE_DIR / user_email
    live_file = user_dir / "live_guideline.txt"

    base_prompt = DEFAULT_PROMPT.format(news_text=news_text)

    if live_file.exists():
        guideline_text = live_file.read_text(encoding="utf-8").strip()
        return f"{guideline_text}\n\n{base_prompt}"

    return base_prompt
