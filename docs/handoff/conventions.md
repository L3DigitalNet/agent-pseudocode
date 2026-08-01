# Conventions

**Last updated:** 2026-08-01

## Quick Reference

| # | Applies when | Rule |
| --- | --- | --- |
| C-001 | Adding a new pseudocode rule | Define it in `src/apseudo_lint/rules.py`; `docs/reference/RULES.md` is generated from it, never hand-edited. |
| C-002 | Editing validator/formatter behavior | The validator and formatter are the policy source of truth — LSP, MCP, hooks, pre-commit, CI, VS Code, and Kate integrations must call or reuse `src/apseudo_lint`, never reimplement rules. |
| C-003 | Adding a CLI entry point | Add it to `[project.scripts]` in `pyproject.toml` and document it per the `cli-documentation` standard (`docs/apseudo-docs/usage/usage.md`). |
| C-004 | Editing `.project-standards.yml`'s `markdown.frontmatter` block | Keep enforcement on the ADR-0003 durable-doc corpus and preserve its exclusions for temporary, operational, harness-owned, and fixture files. |
| C-005 | Installing/syncing Python deps | Use bare `uv sync` (or `uv sync --all-groups`), never `uv sync --extra dev` — `dev` is a `[dependency-groups]` entry, not an extra, since the python-tooling adoption. |
| C-006 | Developing or promoting repository changes | Commit and push ordinary work on `dev`; advance `main` only by approved `git merge --ff-only dev` and its branch safeguards. |

## C-001: Rule catalog is generated, not authored

**Applies when:** touching `docs/reference/RULES.md` (formerly `docs/specs/RULES.md`).

**Rule:** Never hand-edit the rule catalog. It states at its own top: "This file is generated from `src/apseudo_lint/rules.py`."

**Why:** it's the shared explanatory layer for the CLI, LSP, MCP server, hooks, and docs — a hand-edit would drift from the actual rule implementations.

**Related:** [[C-002]]

## C-002: Validator/formatter own policy; integrations reuse it

**Applies when:** working in `integrations/agent-hooks/`, `products/vscode-extension/`, `products/kate-integration/`, or the language server.

**Rule:** Call into `src/apseudo_lint`; never duplicate rule logic.

**Why:** stated explicitly in this repo's `CLAUDE.md` under "Tooling architecture."

## C-003: New CLI entry points need standard-compliant docs

**Applies when:** adding a `[project.scripts]` entry.

**Rule:** Follow the `cli-documentation` standard's section registry (`NAME`, `SYNOPSIS`, `DESCRIPTION`, `OPTIONS`, `EXIT STATUS`, `ENVIRONMENT`, `FILES`, `EXAMPLES`, `NOTES`, `SEE ALSO`) in `docs/apseudo-docs/usage/usage.md` or a dedicated per-command page.

**Why:** adopted 2026-07-08 (Task 5 of the adoption plan); `usage.md` and `RUNNER-USAGE.md` already followed this shape independently before adoption.

## C-004: markdown-frontmatter follows ADR-0003 corpus scope

**Applies when:** editing `.project-standards.yml`'s `markdown.frontmatter` block, or adopting frontmatter elsewhere in the repo.

**Rule:** `include` follows the ADR-0003 durable-documentation corpus: `docs/**/*.md`, `docs/research/*.md`, `products/**/*.md`, and `hooks/**/*.md`. Preserve the ADR-0003 exclusions for scratchpads, handoff state, reviews, plans, fixtures, root operational files, agent harness files, templates, generated content, and vendored content.

**Why:** ADR-0003 was accepted and migrated on 2026-07-09. The widened scope validates durable docs without forcing project-standards frontmatter onto operational files with different lifetimes.

## C-005: `dev` dependencies sync via bare `uv sync`

**Applies when:** installing or syncing this repo's Python dependencies.

**Rule:** Use `uv sync` (or `uv sync --all-groups`). `uv sync --extra dev` no longer works.

**Why:** the `python-tooling` adoption (2026-07-09, ADR-0002) moved `dev` from `[project.optional-dependencies]` (an "extra") to `[dependency-groups]`, which syncs by default with bare `uv sync`.

## C-006: `dev` is the integration branch; `main` is the approved promotion branch

**Applies when:** creating ordinary commits, pushing development work, or promoting reviewed work to `main`.

**Rule:** Work normally on `dev`. Do not commit directly to `main`. After tests, review, and explicit owner approval, run `git switch main`, `git merge --ff-only dev`, `git push origin main`, then `git switch dev`.

**Why:** ADR-0004 makes the integration relationship durable while keeping review and approval independent of the local mechanical safeguards. `scripts/install-branch-policy-hooks.sh` installs the safeguards and preserves predecessor hooks.
