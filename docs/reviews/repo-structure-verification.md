---
schema_version: '1.1'
id: 'note-o488j9-repo-structure-verification'
title: 'Repository Structure Verification'
description: 'Final acceptance evidence for the Option 2 repository restructuring.'
doc_type: 'note'
status: 'active'
created: '2026-08-02'
updated: '2026-08-02'
reviewed: '2026-08-02'
owner: 'project-maintainers'
consumer: 'maintainer'
tags:
  - 'architecture'
  - 'migration'
  - 'repository'
  - 'verification'
aliases: []
related:
  - 'docs/adr/adr-0005-repository-structure-option-2.md'
  - 'docs/plans/2026-08-02-repository-structure-option-2-plan.md'
  - 'docs/reviews/repo-structure-impact-inventory.md'
source:
  - 'local verification at 73861df3561091cb546ce1e706380280bbf2d4e4'
  - 'https://docs.npmjs.com/cli/using-npm/config/'
  - 'https://docs.npmjs.com/cli/commands/npm-ci/'
confidence: 'high'
visibility: 'internal'
license: null
---

# Repository Structure Verification

## Acceptance result

The Option 2 repository restructuring is accepted at implementation commit `73861df3561091cb546ce1e706380280bbf2d4e4`. The final tree matches ADR 0005, all active path consumers resolve to an approved owner, and the independently runnable local behavior and documentation gates pass.

Two boundaries remain outside restructuring success:

- Coverage is 62% against the existing 85% floor. This exactly matches the T3 baseline and is not a restructuring regression.
- A fresh VS Code dependency install could not complete through the configured package gateway, and the local npm cache lacked one locked package. The editor tree and its generated/package artifacts are byte-identical to T4's green build, check, and package checkpoint, so no repository correction is indicated.

Hosted CI has not run for these local commits. The `dev` branch is seven commits ahead of `origin/dev`, GitHub reports no run for the implementation commit, and no push was authorized.

## Evidence anchors

| Output | Commit |
| --- | --- |
| ADR decision | `de6cd14299f6ac8d19d72e7ab48771fa6b87a381` |
| Frozen path-impact inventory (EV-001) | `bf317b2cd455164fef191aed4c3616ee19491b32` |
| Path-sensitive baseline | `b846e4461d5f1735a689cd89cca1bcfe79817b7f` |
| Non-document layout transition | `a7a48bfb9df62f4e1af07d907d5c1164082e9345` |
| Generated task-document correction | `2478dc397f6113a56683a73cd877fe881b093007` |
| Documentation taxonomy and final implementation tree | `73861df3561091cb546ce1e706380280bbf2d4e4` |

- EV-001 SHA-256: `68b836b9b3cae72fa6930401151e113559066a3f091bb276b02f9931fa2243e8`.
- Recursive T5 `git ls-tree` SHA-256: `5ac4e23cb75eb4ae8535c75f720b3f1b5c98f7e0768ec062cf0a29d4e99e9400`.
- The EV-002 checkpoint is the commit carrying `Plan-Task: T6`; the report cannot contain its own commit hash without creating a circular identity.

## Verified final layout

```text
agent-pseudocode/
├── .agents/               # Agent and skill discovery
├── .claude/               # Claude discovery and active hooks
├── .codex/                # Codex discovery configuration
├── .github/               # Hosted repository policy
├── .standards/            # Standards control plane
├── docs/
│   ├── adr/               # Architecture decisions
│   ├── explanation/       # Concepts and operating model
│   ├── handoff/           # Durable agent state
│   ├── how-to/            # Task-oriented guidance
│   ├── plans/             # Executable implementation plans
│   ├── reference/         # Technical reference
│   ├── research/          # Research evidence
│   ├── reviews/           # Assessments and acceptance evidence
│   ├── roadmap/           # Future direction
│   └── specs/             # Forward-looking specifications
├── editors/
│   ├── kate/              # Kate syntax and LSP assets
│   └── vscode/            # VS Code extension package
├── examples/
│   ├── markdown/          # Markdown fence examples
│   ├── runner/            # Executable task scripts
│   └── standalone/        # Standalone pseudocode
├── integrations/
│   ├── agents/            # Agent hook implementations and examples
│   └── mcp/               # MCP launcher/configuration example
├── scripts/
│   ├── bin/               # Source-tree command shims
│   ├── install/           # Installers
│   ├── policy/            # Branch-policy hooks and installer
│   └── verify/            # Integrated smoke verification
├── src/apseudo_lint/      # Installable Python implementation
└── tests/                 # Behavioral and regression tests
```

The fixed project roots remain in place. The former `products/`, `hooks/`, `mcp/`, `integrations/agent-hooks/`, `docs/apseudo-docs/`, and intermediate `docs/apseudo-examples/` roots are absent. The 53 T4 move entries remain unchanged: 31 mode-`100644` files and 22 mode-`100755` files. With the three fixed scripts included, the final `editors/`, `examples/`, `integrations/`, and `scripts/` trees contain 56 tracked files at modes 32/24.

## Requirement and proof reconciliation

| Contract | Result | Evidence |
| --- | --- | --- |
| ADR and frozen inventory (`REQ-001`, `REQ-002`) | Pass | T1/T2 checkpoints and EV-001 hash |
| Final directory and script layout (`REQ-003`–`REQ-007`, `REQ-011`, `REQ-015`) | Pass | Exact roots, modes, unchanged T4 surface, runner and installer proofs |
| Documentation taxonomy and active paths (`REQ-008`, `REQ-009`) | Pass | 27 ID-preserving moves, three approved retirements, zero unclassified active prefixes |
| Behavior preservation (`REQ-010`, `REQ-013`) | Pass | 72 full tests, 18 focused tests, 21 review rows, MCP/hook/runner assertions |
| Standards ownership (`REQ-012`) | Pass | Reconciliation, frontmatter/reference, Markdown, and handoff gates |
| Baseline preservation (`REQ-014`) | Pass | Coverage remains 62%; test count increased from 71 to 72 |

The stale-path negative control was detected. The managed-drift negative control rejected a removed package-owned VS Code recommendation with `CP-MODIFIED-MANAGED`; the original bytes were restored before acceptance.

## Verification matrix

| Area | Result | Observation |
| --- | --- | --- |
| Full Python tests | Pass | 72 passed |
| Focused path-sensitive tests | Pass | 18 passed |
| Coverage comparison | Inherited failure | 62%, equal to T3; 85% floor remains red |
| Ruff and BasedPyright | Pass | Format, lint, and strict type checks clean |
| Python package build/install | Pass | sdist/wheel built; isolated offline wheel install and CLI smoke passed |
| Dependency audit | Pass with declared skip | No known vulnerabilities; unpublished local package not on PyPI |
| MCP, review, hooks, and pre-commit | Pass | Zero review diagnostics; all 21 rows OK; configured hooks pass |
| Runner examples | Pass | Both scripts pass check, prompt render, and command render |
| APSEUDO | Pass | Formatter precedes linter; zero diagnostics |
| Kate | Pass | Isolated installation is byte-identical to source |
| VS Code tracked artifacts | Pass | Both grammars and VSIX match the green T4 checkpoint; VSIX ZIP is valid |
| Fresh VS Code dependency install | Externally unavailable | Gateway wait; offline retry reports missing cached `undici-7.28.0.tgz` |
| Structured text and docs | Pass | Prettier, markdownlint, frontmatter, IDs, and references clean |
| Project Standards | Pass | Reconciliation and validation converge without drift |
| Agent Handoff | Pass with inherited warnings | Validation and drift-check pass; existing length/structure warnings remain |
| Hosted CI | Not run | Local branch is ahead of remote; no workflow run exists for the local commit |

The cache-only npm retry followed npm's documented `offline` behavior: no network requests are made, and missing cache data fails explicitly. That result is evidence about this workstation's cache, not evidence of a source defect.

## Tool versions

| Tool                             | Version                  |
| -------------------------------- | ------------------------ |
| Git                              | 2.55.0                   |
| uv                               | 0.11.6                   |
| Python                           | 3.14.6                   |
| Agent Pseudocode                 | 0.6.1                    |
| Ruff                             | 0.15.20                  |
| BasedPyright                     | 1.39.9 (Pyright 1.1.411) |
| pytest                           | 9.1.1                    |
| Node.js / npm                    | 24.18.0 / 11.16.0        |
| Prettier                         | 3.8.3                    |
| markdownlint-cli2 / markdownlint | 0.22.1 / 0.40.0          |
| Project Standards                | 5.14.0                   |

## Conclusion

`PV-T6-001` passes for the repository restructuring. Every Must/Should requirement has a completed owner task and inspectable proof. No unapproved deviation, stale active owner claim, orphaned migration item, or correction task remains. Coverage improvement and a future hosted/editor reinstall run remain separate from this accepted layout migration.
