from unittest.mock import patch
from app.services.guideline_writer import update_live_guideline

@patch("app.services.guideline_writer.is_testing_mode", return_value=False)
@patch("app.services.guideline_writer.fetch_user_feedbacks")
@patch("app.services.guideline_writer.call_openrouter")
@patch("app.services.firestore_service.save_guideline_to_firestore")
@patch("app.services.firestore_service.save_milestone_to_firestore")
def test_update_live_guideline(
    mock_milestone,
    mock_save,
    mock_openrouter,
    mock_fetch,
    mock_test_flag,
):
    mock_fetch.return_value = [
        {"sentiment": "dislike", "reasons": [12], "comment": "çok uzun"},
        {"sentiment": "like", "reasons": [1], "comment": "sade ve net"},
    ]
    mock_openrouter.return_value = "Daha kısa yazmalısın."

    update_live_guideline("test@example.com")

    mock_openrouter.assert_called_once()
    mock_save.assert_called_once_with("test@example.com", "Daha kısa yazmalısın.")
    mock_milestone.assert_called_once_with("test@example.com", "Daha kısa yazmalısın.")
