---
schema_version: '1.1'
id: 'runbook-uzku0w-repository-layout'
title: 'Repository Layout'
description: 'Guide to the repository layout for Pythonic Agent Pseudocode tooling and documentation.'
doc_type: 'runbook'
status: 'active'
created: '2026-07-08'
updated: '2026-07-09'
reviewed: null
owner: 'tooling-maintainers'
consumer: 'user'
tags:
  - 'runbook'
  - 'usage'
aliases: []
related: []
source: []
confidence: 'medium'
visibility: 'internal'
license: null
---

# Repository Layout

This repository is arranged for standalone GitHub development while keeping the later `project-standards` conversion path clean.

## Root policy

The root keeps only files that are either conventional repository entry points or required for tool discovery:

| Root item | Reason it remains at root |
| --- | --- |
| `README.md`, `CHANGELOG.md`, `LICENSE` | Standard project entry points. |
| `pyproject.toml`, `uv.lock` | Python package and uv environment source of truth. |
| `AGENTS.md`, `CLAUDE.md` | Agent instruction discovery. |
| `.agents/`, `.claude/`, `.codex/` | Agent skill, hook, and config discovery locations. |
| `.github/` | GitHub Actions discovery. |
| `.apseudo/`, `.apseudo-lint.toml`, `.mcp.json` | Runner registry, validator config, and MCP discovery. |
| `.pre-commit-config.yaml`, `.pre-commit-hooks.yaml` | pre-commit discovery and local hook publishing. |
| `.editorconfig`, `.gitignore` | Editor and Git conventions. |
| `src/`, `tests/` | Python package and test suite. |
| `scripts/` | Fixed control scripts and categorized source-tree utilities. |
| `docs/`, `editors/`, `examples/`, `integrations/` | Documentation, editor support, examples, and host adapters. |

## Grouped areas

| Folder | Contents |
| --- | --- |
| `docs/` | Purpose-based user documentation plus fixed ADR, handoff, plan, research, review, and specification owners. |
| `editors/` | Thin VS Code and Kate integrations. |
| `examples/` | Canonical Markdown, runner, and standalone pseudocode examples. |
| `integrations/agents/` | Shared Claude Code and Codex hook implementation plus dormant host examples. |
| `integrations/mcp/` | Source-tree MCP launcher and example registration. |
| `src/apseudo_lint/` | Shared Python implementation used by CLI tools, LSP, MCP, runner, hooks, and tests. |
| `scripts/bin/` | Source-tree wrappers for public console commands. |
| `scripts/install/`, `scripts/policy/`, `scripts/verify/` | Installers, branch-policy hooks, and verification utilities. |
| `tests/` | Unit tests and valid/invalid fixtures. |

## Path convention

Repository documentation should use paths relative to the repository root. That keeps instructions stable when a document moves within `docs/` and matches the way agents normally operate from the project root.
