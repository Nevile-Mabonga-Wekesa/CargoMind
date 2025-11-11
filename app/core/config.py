from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    JWT_SECRET: str
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
    JWT_SECRET = "your_secret_key"
    JWT_ALGORITHM: str = "H256"

    class Config:
        env_file = ".env"

settings = Settings()
