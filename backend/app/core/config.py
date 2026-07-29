from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = Field(default="JobHunter AI")
    database_url: str = Field(default="postgresql://jobhunter:jobhunter@postgres:5432/jobhunter")
    redis_url: str = Field(default="redis://redis:6379/0")
    require_human_confirmation: bool = Field(default=True)

settings = Settings()
