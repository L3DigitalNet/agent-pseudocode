---
schema_version: '1.1'
id: 'note-1pfhqe-repo-structure-review'
title: 'Repository Structure Review'
description: 'Assessment and restructuring options for the Agent Pseudocode repository.'
doc_type: 'note'
status: 'active'
created: '2026-08-02'
updated: '2026-08-02'
reviewed: '2026-08-02'
owner: 'project-maintainers'
consumer: 'mix'
tags:
  - 'architecture'
  - 'repository'
  - 'review'
aliases: []
related:
  - 'docs/apseudo-docs/usage/REPOSITORY-LAYOUT.md'
  - 'docs/handoff/architecture.md'
source:
  - 'https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/'
  - 'https://docs.pytest.org/en/stable/explanation/goodpractices.html'
  - 'https://code.visualstudio.com/api/references/extension-manifest'
  - 'https://diataxis.fr/start-here/'
  - 'https://pre-commit.com/'
confidence: 'high'
visibility: 'internal'
license: null
---

# Repository Structure Review

## Executive assessment

This is a language-tooling repository, not merely a Python package. It ships one installable Python distribution as its policy and runtime core, then adds editor support, agent integrations, repository enforcement, discovery configuration, examples, and documentation around that core.

The Python portion is already arranged well. `pyproject.toml`, `src/apseudo_lint/`, and `tests/` follow the accepted `src`-layout model described by the [Python Packaging User Guide][pypa-src] and recommended by [pytest for new projects][pytest-layout]. The main structural problems are outside that core:

- `products/` is too generic for a directory containing only editor integrations.
- `hooks/`, `integrations/`, and `mcp/` divide closely related agent-facing integration assets by mechanism rather than by ownership.
- `docs/apseudo-docs/` adds a redundant namespace inside an already dedicated `docs/` directory.
- User examples are split across documentation, product, and test-fixture trees without an obvious canonical examples surface.
- The root `scripts/` directory combines public source-tree command wrappers, installers, policy-hook scripts, smoke tests, and project automation.
- Required discovery directories make the root look busy, but moving them would break their consumers. They need explicit ownership, not relocation for its own sake.

The recommended outcome is a conservative, product-aware layout: keep the Python package at the root, rename `products/` to `editors/`, consolidate non-discovery agent assets beneath `integrations/`, flatten user documentation directly under `docs/`, and separate command shims from maintenance automation within `scripts/`. Do not convert this repository into a deep `packages/` monorepo unless each shipped surface gains an independent release lifecycle.

## What the repository ships

The live tree and manifests show the following deliverables.

| Deliverable | Current source | Distribution or use surface |
| --- | --- | --- |
| Python policy engine and tooling | `src/apseudo_lint/` | Python distribution `agent-pseudocode-syntax-toolkit` |
| Twelve CLI entry points | `pyproject.toml` and `scripts/apseudo-*` | Linter, formatter, LSP, MCP, templates, review, Mermaid, and runners |
| VS Code extension | `products/vscode-extension/` | Self-contained VSIX extension with grammar, snippets, and LSP client |
| Kate integration | `products/kate-integration/` | KSyntaxHighlighting definition and LSP settings |
| Agent lifecycle integration | `integrations/agent-hooks/` | Shared Claude Code and Codex hook implementation |
| Dormant host configurations | `hooks/.claude/` and `hooks/.codex/` | Opt-in examples that are intentionally outside discovery paths |
| MCP launch/configuration surfaces | root discovery config and `mcp/` | Repository MCP discovery and a source-tree launcher |
| Agent skills | `.agents/skills/` and `.claude/skills/` | Codex/OpenAI and Claude discovery locations |
| Repository enforcement | pre-commit metadata, `.github/workflows/`, and branch hooks | Consumer hooks and hosted CI |
| Language and project documentation | `docs/` | Standards, usage guides, references, reviews, ADRs, and handoff state |

This inventory changes the right comparison set. A pure Python cookie-cutter is too narrow, while a large JavaScript monorepo is too heavy. The closest general model is a Python language server/tooling package with separately packaged editor and host integrations.

## External conventions that apply

There is no single official directory standard for a mixed Python, editor, and agent-tooling repository. The defensible layout comes from composing the conventions of each shipped surface:

1. **Keep the Python `src` layout.** PyPA explains that it prevents accidental imports from the working tree and limits editable installs to intended importable code. Pytest strongly suggests `src/` for new projects and supports a separate root `tests/` directory. This repository already follows both conventions. See [PyPA's comparison][pypa-src] and [pytest's good practices][pytest-layout].

2. **Keep the VS Code extension self-contained.** VS Code requires `package.json` at the root of the extension's own directory. Its manifest, JavaScript entry point, grammars, snippets, README, and package lock therefore belong together even when that directory is nested in a larger repository. See the [official extension manifest reference][vscode-manifest].

3. **Organize user documentation by reader need.** Diátaxis distinguishes tutorials, how-to guides, reference, and explanation. The current `usage/` and `features/` buckets mix those purposes, while the extra `apseudo-docs/` level contributes no meaning. See the [Diátaxis overview][diataxis].

4. **Leave discovery files where consumers require them.** For example, pre-commit explicitly expects its consumer configuration at the project root; the repository also publishes hook metadata there. Similar constraints apply to GitHub workflows and agent-host discovery directories. See the [pre-commit documentation][pre-commit].

These sources support constraints rather than a universal tree. The remaining choices are information-architecture judgments based on what this repository actually owns.

## Current conceptual tree

This view omits individual implementation files and generated local state so the ownership boundaries are visible.

```text
agent-pseudocode/
├── .agents/                   # OpenAI/Codex skills and handoff hook
├── .apseudo/                  # executable-runner registry
├── .claude/                   # Claude discovery config and duplicated skill
├── .codex/                    # Codex discovery config
├── .github/workflows/         # CI workflows
├── .standards/                # managed standards payloads
├── docs/
│   ├── apseudo-docs/          # user docs: usage, features, enforcement, examples
│   ├── adr/
│   ├── handoff/
│   ├── reference/
│   ├── research/
│   ├── reviews/
│   └── specs/
├── hooks/                     # dormant Claude/Codex host configurations
├── integrations/
│   └── agent-hooks/           # shared active hook implementation
├── mcp/                       # MCP example config and launcher
├── products/
│   ├── kate-integration/
│   └── vscode-extension/
├── scripts/                   # CLI shims, installers, tests, policy, plan bridge
├── src/
│   └── apseudo_lint/          # installable Python implementation
├── tests/                     # Python tests and language fixtures
├── pyproject.toml
├── package.json               # repository Markdown-formatting dependency
└── discovery and policy files
```

### What is already strong

- The policy engine is centralized in `src/apseudo_lint/`; editor and host integrations do not own separate rule engines.
- Python source and tests have conventional, immediately recognizable locations.
- The VS Code extension is internally cohesive and satisfies the extension-root manifest requirement.
- Standards-managed, CI, pre-commit, and agent-host discovery surfaces are visible where their tools expect them.
- Product-specific build files are not mixed into the Python import package.

### What makes the tree hard to understand

| Finding | Why it matters | Severity |
| --- | --- | --- |
| `products/` contains only editor support | A maintainer cannot predict whether future CLIs, skills, or MCP assets belong there | Medium |
| Agent assets span four top-level families | `hooks/`, `integrations/`, `mcp/`, and discovery dot-directories look like competing owners | High |
| `docs/apseudo-docs/` repeats the repository subject | Paths become longer without distinguishing audience, lifecycle, or document type | High |
| Documentation categories overlap | `usage/`, `features/`, `enforcement/`, and `use-cases/` mix task, concept, and reference content | Medium |
| `scripts/` has several responsibilities | Public command shims and maintainer-only automation appear equally supported | Medium |
| Examples have no canonical home | Readers must infer whether a documentation example, Kate example, or test fixture is authoritative | Medium |
| A built `.vsix` is tracked beside extension source | Generated delivery state is mixed with editable source and can become stale | Medium |
| Product, distribution, and import names differ | `agent-pseudocode`, `agent-pseudocode-syntax-toolkit`, and `apseudo_lint` increase cognitive load | Medium |

The root itself is not the primary defect. Most root entries are conventional metadata or mandatory discovery points. Hiding them in a new umbrella directory would trade visual tidiness for broken or more complex tooling.

## Option 1: Minimal clarification

This option changes names and indexes but avoids broad path movement.

```text
agent-pseudocode/
├── docs/
│   ├── apseudo-docs/          # retained; reorganize its index by reader need
│   ├── adr/
│   ├── handoff/
│   ├── reference/
│   └── reviews/
├── integrations/
│   └── agent-hooks/
├── products/                  # retained; rename index language to "editor products"
│   ├── kate-integration/
│   └── vscode-extension/
├── scripts/
├── src/apseudo_lint/
└── tests/
```

**Advantages:** lowest migration risk, minimal link churn, and no packaging changes.

**Disadvantages:** preserves the two most confusing names, leaves agent integration assets fragmented, and improves the directory tree mostly through documentation. This is appropriate only if path stability is more important than structural clarity.

## Option 2: Product-aware toolchain layout — recommended

This layout keeps the conventional Python core while making every non-discovery directory name answer “what kind of thing belongs here?”

```text
agent-pseudocode/
├── .agents/                       # required deployed/discovery assets
├── .apseudo/                      # required runner discovery
├── .claude/                       # required deployed/discovery assets
├── .codex/                        # required deployed/discovery assets
├── .github/workflows/
├── .standards/
├── docs/
│   ├── README.md
│   ├── tutorials/                 # guided learning
│   ├── how-to/                    # installation and task procedures
│   ├── reference/                 # language, rules, CLI, protocols
│   ├── explanation/               # architecture, concepts, use-case reasoning
│   ├── adr/                       # repository decisions
│   ├── handoff/                   # standards-managed project knowledge
│   ├── plans/                     # implementation plans when present
│   ├── research/
│   ├── reviews/
│   └── specs/
├── editors/
│   ├── kate/
│   │   ├── README.md
│   │   ├── agent-pseudocode.xml
│   │   └── lsp-client-settings*.json
│   └── vscode/
│       ├── package.json
│       ├── extension.js
│       ├── snippets/
│       ├── syntaxes/
│       └── scripts/
├── examples/                      # canonical user-facing workflows
│   ├── standalone/
│   └── markdown/
├── integrations/
│   ├── agents/
│   │   ├── apseudo-hook.py
│   │   ├── claude/                # dormant/example host configuration
│   │   └── codex/                 # dormant/example host configuration
│   └── mcp/
│       ├── README.md
│       ├── config.example.json
│       └── apseudo-mcp             # source-tree launcher if still needed
├── scripts/
│   ├── bin/                       # source-tree apseudo-* compatibility shims
│   ├── install/                   # editor and enforcement installers
│   ├── policy/                    # branch-policy hooks and installer
│   └── check.py                   # small root-level maintainer entry points
├── src/
│   └── apseudo_lint/
├── tests/
│   ├── fixtures/                  # validator-only valid/invalid inputs
│   └── test_*.py
├── pyproject.toml
├── uv.lock
├── package.json                   # repository-only formatting tools
└── required root discovery files
```

### Why this is the best fit

- It preserves Python packaging and test conventions without adding workspace indirection.
- `editors/` describes both VS Code and Kate accurately; neither is the core product by itself.
- `integrations/` becomes the source owner for host adapters, while the root dot-directories remain clearly deployed or discovery-facing copies.
- Direct `docs/` categories remove one redundant path segment and let reader need drive navigation.
- `examples/` becomes the canonical place for copyable, user-facing workflows; `tests/fixtures/` remains intentionally adversarial or machine-oriented.
- Subdirectories under `scripts/` reveal support level without forcing the installable CLI package away from its standard `src/` location.

### Important boundary

Do not move required host discovery files merely to make the tree symmetrical. The canonical source for a generated or deployed asset may live under `integrations/`, but the consumer-facing copy still has to exist where its host looks for it. Any such relationship should be generated or checked for drift, not maintained as two silent sources of truth.

## Option 3: Full packages monorepo

This is visually regular but disproportionate today.

```text
agent-pseudocode/
├── packages/
│   ├── python-toolkit/
│   │   ├── pyproject.toml
│   │   ├── src/apseudo_lint/
│   │   └── tests/
│   ├── vscode-extension/
│   │   └── package.json
│   └── kate-integration/
├── integrations/
│   ├── agents/
│   └── mcp/
├── docs/
├── examples/
├── tools/
└── workspace-level configuration
```

**Advantages:** explicit package boundaries, clean support for independent versions, and a natural future home for additional distributable packages.

**Disadvantages:** moves `pyproject.toml` away from the repository root, complicates the current `uv` workflow, separates tests from the default Python project, and requires workspace-level orchestration that the repository does not currently need. The Kate assets are not an independent package in the same sense as the Python distribution or VSIX.

Adopt this only after at least two components require independent versioning, release automation, dependency graphs, or ownership. Directory symmetry alone is not enough justification.

## Recommended path mapping

| Current path | Recommended path | Reason |
| --- | --- | --- |
| `products/vscode-extension/` | `editors/vscode/` | Names the integration by host and retains its self-contained package root |
| `products/kate-integration/` | `editors/kate/` | Matches the same host-oriented taxonomy |
| `integrations/agent-hooks/` | `integrations/agents/` | Makes the shared runtime and host examples one ownership area |
| `hooks/.claude/` | `integrations/agents/claude/` | Keeps dormant configuration out of discovery while removing a competing root owner |
| `hooks/.codex/` | `integrations/agents/codex/` | Same as the Claude path |
| `mcp/` | `integrations/mcp/` | MCP is a host integration around the Python core, not a separate core package |
| `docs/apseudo-docs/usage/` | `docs/how-to/` and `docs/tutorials/` | Split task instructions from learning journeys |
| `docs/apseudo-docs/features/` | `docs/reference/` or `docs/explanation/` | Split factual interface descriptions from design context |
| `docs/apseudo-docs/enforcement/` | `docs/how-to/enforcement/` and `docs/explanation/enforcement/` | Separate operation from rationale |
| `docs/apseudo-docs/examples/` | `examples/` | Establish one canonical, copyable example set |
| `scripts/apseudo-*` | `scripts/bin/apseudo-*` | Mark source-tree compatibility shims as a coherent public family |
| `scripts/branch-policy-hooks/` | `scripts/policy/hooks/` | Group policy implementation with its installer |

Not every document should move mechanically by current folder. Classify each one by purpose first. For example, a command reference belongs in `reference/`, while “How to configure VS Code” belongs in `how-to/` even if both currently live under `usage/`.

## Migration risks and controls

The proposed layout is conceptually simple but path-heavy. The current paths are referenced throughout documentation, workflows, scripts, editor settings, hook guards, MCP configuration, and project review checks.

1. Create a path manifest from `git ls-files` and search every old prefix before moving anything.
2. Move one ownership area at a time: editors, integrations, examples, then docs.
3. Update executable and generated interfaces before narrative documentation.
4. Preserve mandatory root discovery files and validate any generated-copy or drift-check relationship.
5. Update project-review completeness checks so old paths cannot silently return.
6. Regenerate or relocate the tracked VSIX deliberately; preferably publish build artifacts through releases and keep generated packages out of editable source.
7. Run the full Python, extension, Markdown, frontmatter, pseudocode, pre-commit, and project-review gates after the final path update.

The distribution/import naming mismatch should be handled separately. Renaming `apseudo_lint` or the Python distribution while moving directories would combine a potentially breaking API change with a mechanical repository migration.

## Decision

Adopt **Option 2** as the target architecture, but implement it as a dedicated, planned migration rather than opportunistic cleanup. The highest-value first step is flattening `docs/apseudo-docs/` and defining `editors/` and `integrations/` as the two non-core ownership boundaries. Keep `src/apseudo_lint/`, `tests/`, root package metadata, and required discovery surfaces in place.

This yields a repository that reads in one pass:

> The language and runtime live in `src`; editor support lives in `editors`; host adapters live in `integrations`; copyable workflows live in `examples`; user and project knowledge live in `docs`.

[diataxis]: https://diataxis.fr/start-here/
[pre-commit]: https://pre-commit.com/
[pypa-src]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[pytest-layout]: https://docs.pytest.org/en/stable/explanation/goodpractices.html#choosing-a-test-layout
[vscode-manifest]: https://code.visualstudio.com/api/references/extension-manifest
