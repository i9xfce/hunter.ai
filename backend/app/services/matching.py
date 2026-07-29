from app.schemas.job import ApplicationMode, JobCreate, JobMatch

def calculate_match(job: JobCreate, profile_skills: list[str]) -> JobMatch:
    """Simple deterministic MVP match score; replace with embeddings/LLM later."""
    normalized_profile = {skill.strip().lower() for skill in profile_skills}
    normalized_job = {skill.strip().lower() for skill in job.skills}
    strengths = sorted(normalized_profile & normalized_job)
    gaps = sorted(normalized_job - normalized_profile)
    score = int((len(strengths) / max(len(normalized_job), 1)) * 100)
    mode = ApplicationMode.assisted if score >= 70 else ApplicationMode.manual_review
    return JobMatch(score=score, strengths=strengths, gaps=gaps, recommendation=mode)
