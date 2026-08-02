# Architecture

**Last updated:** 2026-08-02

## Components

- `src/apseudo_lint/` — policy and runtime source of truth for CLI, LSP, MCP, review, and runner behavior.
- `editors/` — thin VS Code and Kate adapters; they reuse the Python policy engine.
- `integrations/agents/` — shared agent hook plus dormant Claude and Codex host examples.
- `integrations/mcp/` — source-tree MCP launcher and example registration.
- `scripts/` — fixed control scripts plus categorized command, installer, policy, and verification utilities.
- `examples/` — canonical Markdown, runner, and standalone examples.
- `docs/how-to/`, `docs/explanation/`, `docs/reference/`, `docs/roadmap/` — purpose-based user documentation.
- `docs/adr/`, `docs/handoff/`, `docs/plans/`, `docs/research/`, `docs/reviews/`, `docs/specs/` — fixed project-lifecycle owners.
