import pytest
from unittest.mock import patch, MagicMock
from app.services.firestore_service import (
    save_user_profile,
    get_user_profile,
    update_user_profile
)


@patch("app.services.firestore_service.firestore_db")
def test_save_user_profile(mock_db):
    mock_doc = mock_db.collection.return_value.document.return_value

    save_user_profile("user@example.com", {"api_key": "x", "model": "gpt"})
    mock_doc.set.assert_called_once_with({"api_key": "x", "model": "gpt"})


@patch("app.services.firestore_service.firestore_db")
def test_get_user_profile_found(mock_db):
    mock_doc = MagicMock()
    mock_doc.exists = True
    mock_doc.to_dict.return_value = {"model": "gpt-4"}

    mock_db.collection.return_value.document.return_value.get.return_value = mock_doc

    result = get_user_profile("user@example.com")
    assert result["model"] == "gpt-4"


@patch("app.services.firestore_service.firestore_db")
def test_get_user_profile_not_found(mock_db):
    mock_doc = MagicMock()
    mock_doc.exists = False

    mock_db.collection.return_value.document.return_value.get.return_value = mock_doc

    result = get_user_profile("user@example.com")
    assert result is None


@patch("app.services.firestore_service.firestore_db")
def test_update_user_profile(mock_db):
    mock_doc = mock_db.collection.return_value.document.return_value

    update_user_profile("user@example.com", {"company_prompt": "Sade yaz"})
    mock_doc.update.assert_called_once_with({"company_prompt": "Sade yaz"})
