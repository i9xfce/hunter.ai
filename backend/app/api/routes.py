from fastapi import APIRouter, UploadFile
from app.schemas.job import JobMatch, JobMatchRequest
from app.services.matching import calculate_match

router = APIRouter()

@router.post("/resumes/upload", tags=["resumes"])
async def upload_resume(file: UploadFile) -> dict[str, str]:
    return {"filename": file.filename or "resume", "status": "received"}

@router.post("/jobs/match", response_model=JobMatch, tags=["jobs"])
def match_job(payload: JobMatchRequest) -> JobMatch:
    return calculate_match(payload.job, payload.profile_skills)
