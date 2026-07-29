# Next.js + TypeScript Build Compatibility Report

## Root cause

The frontend previously used `latest` for `next`, `react`, `react-dom`, TypeScript and type packages. On July 29, 2026, `typescript@latest` resolves to TypeScript 7.x. TypeScript 7.0 does not expose the JavaScript compiler API that Next.js type checking still uses by default, which produces the error: `TypeScript 7.0.2 does not provide the compiler API required by Next.js`.

## Decision

Use the production-stability option: pin the frontend to stable, mutually compatible versions and install the TypeScript 6 compatibility package through the official npm alias form:

```json
"typescript": "npm:@typescript/typescript6@6.0.2"
```

This keeps the package name `typescript` available for Next.js and ESLint peer dependency resolution while avoiding the TypeScript 7 compiler API incompatibility. The experimental `useTypeScriptCli` option was not enabled because the stable path is preferred for production CI/CD until TypeScript 7 compiler API support is broadly supported by the toolchain.

## Version changes

| Package | Previous | New | Reason |
| --- | --- | --- | --- |
| `next` | `latest` | `15.4.7` | Avoid unreviewed major/minor updates in CI. |
| `react` | `latest` | `19.1.1` | Match the selected Next.js 15 production line. |
| `react-dom` | `latest` | `19.1.1` | Match React runtime version. |
| `typescript` | `latest` | `npm:@typescript/typescript6@6.0.2` | Prevent TypeScript 7 compiler API breakage. |
| `@types/*` | `latest` | pinned 19/22 line | Keep React/Node types aligned with runtime versions. |
| `eslint` | absent | `9.33.0` | Provide explicit lint command for CI. |
| `eslint-config-next` | absent | `15.4.7` | Use the Next.js ESLint rules that match the framework version. |
| `tailwindcss` | `latest` | `3.4.17` | Pin stable Tailwind v3 for the existing CSS directives. |

## CI/CD updates

- GitHub Actions uses Node.js 22 LTS consistently with Docker Compose.
- CI uses `npm ci` rather than `npm install`.
- CI prints Node, npm, TypeScript, Next and React versions before lint/type-check/build.
- CI caches npm, Next.js and TypeScript incremental artifacts.

## Impact

- Builds become reproducible and protected from accidental TypeScript 7 upgrades.
- CI will fail fast on lint, type-check or build regressions.
- Future framework upgrades should be explicit pull requests with matching lockfile updates and release-note review.

## Future recommendations

- Regenerate `package-lock.json` with `npm install --package-lock-only` whenever dependency versions change. This environment is blocked by a proxy/registry 403, so the committed lockfile captures the pinned root dependency contract and CI will materialize the full install in a network-enabled GitHub Actions runner.
- Re-evaluate TypeScript 7 once Next.js and the surrounding ESLint/type-checking toolchain support its new compiler API path without experimental flags.
