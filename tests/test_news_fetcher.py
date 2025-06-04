from unittest.mock import patch, MagicMock
from app.services.news_fetcher import fetch_news


@patch("app.services.news_fetcher.get_sources")
@patch("app.services.news_fetcher.feedparser.parse")
def test_fetch_news(mock_parse, mock_get_sources):
    mock_get_sources.return_value = ["http://example.com/rss"]
    mock_parse.return_value = MagicMock(entries=[
        {"title": "t", "summary": "s", "link": "l"}
    ])

    result = fetch_news("tech", "us")

    mock_get_sources.assert_called_once_with("tech", "us")
    mock_parse.assert_called_once_with("http://example.com/rss")

    assert result == [{"title": "t", "summary": "s", "link": "l"}]
