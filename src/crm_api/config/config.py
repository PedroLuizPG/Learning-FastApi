from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    ENV: str = "development"
    PORT: int = 8000
    DATABASE_URL: str
    
settings = Settings()