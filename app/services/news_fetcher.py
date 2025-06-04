import feedparser
from app.services.source_loader import get_sources


def fetch_news(category: str, region: str) -> list[dict]:
    """
    Seçilen kategori ve bölgeye göre RSS kaynaklarından haber çeker.
    Her haber bir sözlük olarak döner: {"title": ..., "summary": ..., "link": ...}
    """
    sources = get_sources(category, region)
    news_items = []

    for url in sources:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            news_items.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", "")
            })

    return news_items
