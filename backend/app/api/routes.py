from fastapi import APIRouter, UploadFile
from app.schemas.job import JobCreate, JobMatch
from app.services.matching import calculate_match

router = APIRouter()

@router.post("/resumes/upload", tags=["resumes"])
async def upload_resume(file: UploadFile) -> dict[str, str]:
    return {"filename": file.filename or "resume", "status": "received"}

@router.post("/jobs/match", response_model=JobMatch, tags=["jobs"])
def match_job(job: JobCreate, profile_skills: list[str]) -> JobMatch:
    return calculate_match(job, profile_skills)
