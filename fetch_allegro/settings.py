from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Allegro API Settings
    ALLEGRO_CLIENT_ID: str
    ALLEGRO_CLIENT_SECRET: str
    ALLEGRO_TOKEN_URL: str
    ALLEGRO_SALE_CATEGORIES_URL: str
    ALLEGRO_SALE_PRODUCTS_URL: str
