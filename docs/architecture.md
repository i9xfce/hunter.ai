# JobHunter AI Architecture

JobHunter AI is organized around independent connectors and a safe application workflow. The platform automates public and permitted steps, pauses for CAPTCHA, MFA, legal declarations, salary decisions, or final submission, and records every action.

## Modules

1. Resume intake extracts skills, experience, languages, links, certifications, and contact data from PDF, DOCX, or TXT files.
2. Job connectors collect vacancies from supported public sources and ATS-specific integrations without bypassing anti-bot protections.
3. Matching compares job requirements with the candidate profile and produces a score, strengths, gaps, and a next action.
4. Document generation prepares tailored resumes and cover letters for candidate review.
5. Assisted application uses Playwright where permitted and always requires human confirmation for sensitive answers or submission.
6. Dashboard presents pipeline metrics, applications, interviews, notifications, and AI queries.

## MVP stack

- Backend: Python, FastAPI, PostgreSQL, Redis.
- Frontend: Next.js, React, Tailwind CSS.
- Automation: Playwright-first connector layer.
- AI: cloud LLM providers with a future Ollama option.
- Search: FAISS and sentence-transformers in a later milestone.
