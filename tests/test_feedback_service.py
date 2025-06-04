import pytest
from unittest.mock import patch
from app.services.feedback_service import save_feedback
from app.schemas.feedback_schema import FeedbackRequest


@patch("app.services.feedback_service.fetch_user_feedbacks")
@patch("app.services.feedback_service.update_live_guideline")
@patch("app.services.feedback_service.save_feedback_to_firestore")
def test_save_feedback(mock_save, mock_guideline, mock_fetch):
    # Firestore ve guideline fonksiyonlarını devre dışı bırak
    mock_save.return_value = None
    mock_guideline.return_value = None
    mock_fetch.return_value = []

    # Geçerli bir geri bildirim örneği
    data = FeedbackRequest(
        post_id="abc123",
        reasons=[12, 13],  # dislike → 11–20 arası
        comment="çok uzun olmuş",
        sentiment="dislike"
    )

    # Fonksiyonu çağır
    save_feedback(data, "test@example.com")

    # Firestore fonksiyonu çağrıldı mı?
    mock_save.assert_called_once()
    saved_data = mock_save.call_args[0][0]

    assert saved_data["post_id"] == "abc123"
    assert saved_data["sentiment"] == "dislike"
    assert saved_data["liked"] is False
    assert saved_data["reasons"] == [12, 13]
    assert saved_data["user_email"] == "test@example.com"
