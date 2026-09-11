import os


def _origins() -> list[str]:
    value = os.getenv("CORS_ORIGINS", "http://localhost:8000,http://localhost:5500")
    return [origin.strip() for origin in value.split(",") if origin.strip()]


class Settings:
    app_env = os.getenv("APP_ENV", "development")
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    cors_origins = _origins()


settings = Settings()