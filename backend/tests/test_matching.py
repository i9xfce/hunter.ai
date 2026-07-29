from app.services.matching import score_skills

def test_score_skills_returns_strengths_gaps_and_percentage() -> None:
    score, strengths, gaps = score_skills(
        ["Python", "AWS", "Terraform"],
        ["python", "AWS", "Docker"],
    )
    assert score == 66
    assert strengths == ["aws", "python"]
    assert gaps == ["terraform"]
