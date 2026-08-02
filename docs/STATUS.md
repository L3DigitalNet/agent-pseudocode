# Project Status

## Current snapshot

- The Pythonic Agent Pseudocode toolkit includes syntax, formatter, validator, LSP, MCP, hooks, skills, CI, and documentation.
- Project Standards 5.14.0 enables all seven evidence-backed consumer packages.
- Resolved versions: ADR 1.3, Agent Handoff 1.8, CLI Documentation 1.5, Frontmatter 1.8, Markdown Tooling 1.12, Project Spec 1.6, and Python Tooling 1.10.
- The V4 to V5 migration applied on release 5.4.0 and is now updated in place to 5.14.0; `.standards/` is the sole authority and `.project-standards.yml` is retired.
- Durable Markdown frontmatter follows accepted ADR-0003; `docs/specs/` holds project-spec-conformant specifications.
- `SPEC-QZXW` specifies the validation toolchain and is the traceability source for coverage and defect work.
- `docs/usage.md` is the authored CLI reference for `apseudo` and its per-command entry points.
- `dev` is the permanent integration branch; ADR-0004 and local safeguards require an approved fast-forward promotion before `main` advances.
- ADR-0005's Option 2 structure is complete and promoted to `main`; EV-002 records final acceptance.
- Editors, integrations, examples, automation, and user docs now use their dedicated final owners.
- Markdown lint and Prettier gates are green; the archived pre-migration transcript is a declared, reasoned exclusion.
- The `check.yml` gate remains red at 62% coverage against the 85% floor.
- Bug 004 is the only open product bug; bugs 001, 002, 003, 005, and 006 are fixed.
- Agent Handoff 1.8 provides the shared repo-local runtime and canonical `docs/` state. Its launcher works with `uv-strict-python` shims, resolving upstream issue 80.
- `cli-docs-check.yml` stays consumer-owned to keep its SHA-pinned action hardening.
