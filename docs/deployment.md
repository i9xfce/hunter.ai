# Free Deployment Plan

## Provider choice

The default public frontend target is GitHub Pages because it provides free HTTPS hosting directly from GitHub Actions and does not require hardcoding a username. The workflow derives the repository name from `GITHUB_REPOSITORY` and configures the Next.js `basePath` automatically.

The backend target is Render using `render.yaml`. Render provides free web services with managed TLS and a free PostgreSQL option suitable for MVP validation, with the operational tradeoff that free services can sleep when idle.

## One-command bootstrap

```bash
PROJECT_NAME=jobhunter-ai ./scripts/bootstrap_deploy.sh
```

The script initializes Git if needed, authenticates with GitHub CLI, creates or reuses a repository, pushes the code, enables GitHub Pages workflow deployment, and starts the frontend deployment workflow.

## Public URLs

- GitHub Pages frontend: shown in the `Deploy frontend to GitHub Pages` workflow output.
- Render backend: created by importing `render.yaml` as a Render Blueprint or linking the repository in Render.

## Custom domains

No code change is required for a future custom domain. Configure the domain in the hosting provider and set `GITHUB_PAGES=false` for root-path static exports when not using a GitHub project page subpath.
