# Project Status

## Current snapshot

- The Pythonic Agent Pseudocode toolkit includes syntax, formatter, validator, LSP, MCP, hooks, skills, CI, and documentation.
- Project Standards 5.13.0 enables all seven evidence-backed consumer packages.
- Resolved versions are adr 1.3, agent-handoff 1.7, cli-documentation 1.5, markdown-frontmatter 1.7, markdown-tooling 1.11, project-spec 1.5, and python-tooling 1.10.
- The V4 to V5 migration applied on release 5.4.0 and updated in place to 5.13.0; `.standards/` is the sole authority and `.project-standards.yml` is retired.
- Durable Markdown frontmatter follows accepted ADR-0003; `docs/specs/` holds project-spec-conformant specifications.
- `SPEC-QZXW` specifies the validation toolchain and is the traceability source for coverage and defect work.
- `docs/usage.md` is the authored CLI reference for `apseudo` and its per-command entry points.
- The 135-second repository explainer is locally verified under ignored `dist/video/final/` with AAC-LC narrated and speaker MP4s, selected `marin` WAV, captions, manifests, report, and checksums; publication remains separate.
- Markdown lint and Prettier gates are green; the archived pre-migration transcript is a declared, reasoned exclusion.
- The `check.yml` gate remains red at 62% coverage against the 85% floor; one stale production-entry assertion also fails because completed scene inputs now advance verification to the inventory gate (bug 008).
- Four product bugs remain open in `docs/handoff/bugs/`; bugs 003, 005, 006, and 007 are fixed.
- Agent Handoff 1.6 provides the shared repo-local runtime and canonical `docs/` state. Its managed Codex command currently fails under `uv-strict-python` shims; upstream project-standards issue 80 tracks the integration defect.
- `cli-docs-check.yml` stays consumer-owned to keep its SHA-pinned action hardening.
