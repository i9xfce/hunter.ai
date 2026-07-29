from app.schemas.job import ApplicationMode, JobCreate, JobMatch

def normalize_skills(skills: list[str]) -> set[str]:
    return {skill.strip().lower() for skill in skills if skill.strip()}

def score_skills(job_skills: list[str], profile_skills: list[str]) -> tuple[int, list[str], list[str]]:
    normalized_profile = normalize_skills(profile_skills)
    normalized_job = normalize_skills(job_skills)
    strengths = sorted(normalized_profile & normalized_job)
    gaps = sorted(normalized_job - normalized_profile)
    score = int((len(strengths) / max(len(normalized_job), 1)) * 100)
    return score, strengths, gaps

def calculate_match(job: JobCreate, profile_skills: list[str]) -> JobMatch:
    """Simple deterministic MVP match score; replace with embeddings/LLM later."""
    score, strengths, gaps = score_skills(job.skills, profile_skills)
    mode = ApplicationMode.assisted if score >= 70 else ApplicationMode.manual_review
    return JobMatch(score=score, strengths=strengths, gaps=gaps, recommendation=mode)
