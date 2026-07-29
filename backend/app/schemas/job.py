from enum import Enum
from pydantic import BaseModel, Field, HttpUrl

class ApplicationMode(str, Enum):
    manual_review = "manual_review"
    assisted = "assisted"
    permitted_auto_fill = "permitted_auto_fill"

class JobCreate(BaseModel):
    title: str
    company: str
    location: str | None = None
    source_url: HttpUrl
    description: str
    skills: list[str] = Field(default_factory=list)

class JobMatchRequest(BaseModel):
    job: JobCreate
    profile_skills: list[str] = Field(default_factory=list)

class JobMatch(BaseModel):
    score: int = Field(ge=0, le=100)
    strengths: list[str]
    gaps: list[str]
    recommendation: ApplicationMode
    requires_confirmation: bool = True
