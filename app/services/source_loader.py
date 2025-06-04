from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import bot_routes

app = FastAPI(title="Media Analyst Backend", version="1.0")

# CORS ayarları (geliştirme için tümüne izin veriyoruz)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router ekleme
app.include_router(bot_routes.router)

@app.get("/")
def root():
    return {"message": "Media Analyst Backend çalışıyor."}
