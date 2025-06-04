from app.services.source_loader import get_sources


def test_get_sources_valid_category_region():
    feeds = get_sources("technology", "us")
    assert isinstance(feeds, list)
    assert "https://techcrunch.com/feed/" in feeds
    assert "https://www.theverge.com/rss/index.xml" in feeds


def test_get_sources_fallback_global():
    global_feeds = get_sources("technology", "nonexistent")
    assert "https://techcrunch.com/feed/" in global_feeds
    assert len(global_feeds) > 0


def test_get_sources_unknown_category():
    assert get_sources("unknown", "us") == []
