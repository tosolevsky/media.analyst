import pytest
from unittest.mock import patch
from app.services.bot_service import generate_response


@patch("app.services.bot_service.get_user_settings")
@patch("app.services.bot_service.call_model")
def test_generate_response_success(mock_call_model, mock_get_user_settings):
    # Test verileri
    mock_get_user_settings.return_value = {
        "model": "gpt-4",
        "api_key": "testkey",
        "provider": "openai",
        "company_prompt": "Kısa, sade ve profesyonel yaz."
    }

    mock_call_model.return_value = "Mocked tweet output"

    result = generate_response("Bu bir haber içeriğidir.", "test@example.com")

    assert result == "Mocked tweet output"
    mock_call_model.assert_called_once()
