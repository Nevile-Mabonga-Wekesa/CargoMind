from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    APP_PORT: int

    class Config:
        env_file = ".env"

settings = Settings()
