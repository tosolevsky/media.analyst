from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.logger import logger


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.warning(f"HTTP {exc.status_code} hata: {exc.detail} - {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Validasyon hatası: {exc.errors()} - {request.url}")
    return JSONResponse(
        status_code=422,
        content={"error": "Veri doğrulama hatası", "details": exc.errors()},
    )


async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Sunucu hatası: {str(exc)} - {request.url}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "Bilinmeyen bir hata oluştu. Sistem yöneticisine bildirildi."},
    )
