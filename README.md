# JobHunter AI

AI Job Agent for searching, analyzing, ranking, and assisting applications for technology jobs.

The project is designed to automate only permitted actions. It must not bypass CAPTCHAs, MFA, anti-bot protections, or website terms. When a flow requires sensitive declarations, legal information, authentication, CAPTCHA, MFA, or final submission, the system pauses for human confirmation.

## MVP scope

- Resume upload and extraction.
- Intelligent profile creation.
- Periodic search in supported public sources.
- Match Score calculation.
- Dashboard with job and application metrics.
- Tailored resume and cover letter generation.
- Assisted form filling where permitted.
- Application history and notifications.

## Repository layout

```text
backend/   FastAPI API and core services
frontend/  Next.js dashboard
docs/      Architecture and product notes
docker/    Container assets
scripts/   Utility scripts
```

## Quick start

```bash
docker compose up --build
```

Backend health check: <http://localhost:8000/health>
Frontend dashboard: <http://localhost:3000>

## Smoke test

After the backend is running, validate the live HTTP endpoints with:

```bash
python3 scripts/online_smoke_test.py http://127.0.0.1:8000
```
