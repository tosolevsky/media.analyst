import pytest
from unittest.mock import patch, MagicMock
from app.services.user_service import get_user_settings


@patch("app.services.user_service.firestore_db")
def test_get_user_settings_success(mock_db):
    # Sahte belge verisi
    mock_doc = MagicMock()
    mock_doc.exists = True
    mock_doc.to_dict.return_value = {
        "api_key": "abc",
        "model": "gpt-4",
        "company_prompt": "Kurumsal dil kullan"
    }

    # firestore_db.collection("profiles").document(...).get() = mock_doc
    mock_db.collection.return_value.document.return_value.get.return_value = mock_doc

    # Fonksiyonu çağır
    result = get_user_settings("test@example.com")

    # Beklenen sonucu test et
    assert result["api_key"] == "abc"
    assert result["model"] == "gpt-4"
    assert result["company_prompt"] == "Kurumsal dil kullan"


@patch("app.services.user_service.firestore_db")
def test_get_user_settings_not_found(mock_db):
    mock_doc = MagicMock()
    mock_doc.exists = False
    mock_db.collection.return_value.document.return_value.get.return_value = mock_doc

    with pytest.raises(ValueError, match="Kullanıcı ayarları bulunamadı."):
        get_user_settings("none@example.com")
