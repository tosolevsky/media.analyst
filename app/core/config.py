import os
import json
from dotenv import load_dotenv
from pydantic import BaseSettings, Field

# .env dosyasını yükle (sadece lokal geliştirme için geçerlidir)
load_dotenv()


class Settings(BaseSettings):
    """
    Ortam değişkenlerinden uygulama yapılandırmasını yükler.
    SERVICE_ACCOUNT_JSON, Render ya da .env ile tanımlanmalı.
    """
    service_account_json: dict = Field(default_factory=dict)

    class Config:
        env_prefix = ''

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return (
                init_settings,
                env_settings,
                file_secret_settings,
                cls.parse_service_json,
            )

        @staticmethod
        def parse_service_json(settings: BaseSettings):
            """
            SERVICE_ACCOUNT_JSON ortam değişkeni varsa JSON formatında ayrıştırır.
            """
            raw_json = os.getenv("SERVICE_ACCOUNT_JSON")
            if not raw_json:
                raise ValueError("SERVICE_ACCOUNT_JSON is not set in environment variables.")

            try:
                parsed = json.loads(raw_json)
                return {'service_account_json': parsed}
            except json.JSONDecodeError as e:
                raise ValueError("SERVICE_ACCOUNT_JSON is not valid JSON.") from e


# Proje boyunca import edilebilecek ayarlar objesi
settings = Settings()
