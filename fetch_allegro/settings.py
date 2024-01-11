from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    CLIENT_ID: str
    CLIENT_SECRET: str
    TOKEN_URL: str
    SALE_CATEGORIES_URL: str
