from dotenv import load_dotenv
load_dotenv() 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.routes import auth_routes, bot_routes
from app.core.logger import logger
from app.core.exception_handler import (
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler,
)

def create_app() -> FastAPI:
    app = FastAPI(
        title="Media Analyst API",
        description="AI destekli içerik üretim ve analiz servisi",
        version="1.0.0"
    )

    # Global Exception Handler'lar
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)

    # CORS Ayarları (gerekirse prod ortamda allow_origins sınırlandırılır)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Router'ları bağla
    app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
    app.include_router(bot_routes.router, prefix="/bot", tags=["Bot"])

    logger.info("Media Analyst API başarıyla başlatıldı.")
    return app


app = create_app()
