---
schema_version: '1.1'
id: 'index-aqjczt-documentation-index'
title: 'Documentation Index'
description: 'Index for the durable documentation tree in the agent-pseudocode repository.'
doc_type: 'index'
status: 'active'
created: '2026-07-08'
updated: '2026-07-09'
reviewed: null
owner: 'docs-maintainers'
consumer: 'mix'
tags:
  - 'docs'
  - 'index'
aliases: []
related: []
source: []
confidence: 'medium'
visibility: 'internal'
license: null
---

# Documentation Index

User documentation is grouped by purpose. Project-lifecycle records retain their established owners, and copyable examples live at the repository root.

## Layout

| Folder | Purpose |
| --- | --- |
| [`docs/how-to/`](how-to/) | Installation, enforcement, testing, editor setup, agent wording, and task-oriented workflows. |
| [`docs/explanation/`](explanation/) | Mental models, surface selection, agent delivery, repository operation, and layout rationale. |
| [`docs/reference/`](reference/) | CLI, feature, enforcement, language, rule, and executable-runner reference material. |
| [`docs/roadmap/`](roadmap/) | Future-version and deferred-work documents. |
| [`examples/`](../examples/) | Canonical Markdown, runner, and standalone examples. |
| [`docs/adr/`](adr/) | Architecture decision records. |
| [`docs/handoff/`](handoff/) | Durable session state, architecture, conventions, bugs, and deployment facts. |
| [`docs/plans/`](plans/) | Implementation plans and their execution contracts. |
| [`docs/research/`](research/) | Repository research records. |
| [`docs/reviews/`](reviews/) | Project reviews, traceability reviews, and migration evidence. |
| [`docs/specs/`](specs/) | Project specifications. |

## Primary documents

| Need | Start here |
| --- | --- |
| Learn the language convention | [`docs/reference/PYTHONIC_PSEUDOCODE_STANDARD.md`](reference/PYTHONIC_PSEUDOCODE_STANDARD.md) |
| Understand the practical mental model | [`docs/explanation/MENTAL-MODEL.md`](explanation/MENTAL-MODEL.md) |
| Choose prose, Markdown fences, standalone files, or runner scripts | [`docs/explanation/CHOOSING-A-SURFACE.md`](explanation/CHOOSING-A-SURFACE.md) |
| Understand how agents receive pseudocode | [`docs/explanation/AGENT-FEEDING-PATHS.md`](explanation/AGENT-FEEDING-PATHS.md) |
| Use the CLI tools | [`docs/usage.md`](usage.md) |
| Use executable `.apseudo` runner scripts | [`docs/reference/cli/RUNNER-USAGE.md`](reference/cli/RUNNER-USAGE.md) |
| See runner workflows | [`docs/how-to/RUNNER-WORKFLOWS.md`](how-to/RUNNER-WORKFLOWS.md) |
| See common task-oriented workflows | [`docs/how-to/COMMON-WORKFLOWS.md`](how-to/COMMON-WORKFLOWS.md) |
| Browse canonical examples | [`docs/reference/EXAMPLE-CATALOG.md`](reference/EXAMPLE-CATALOG.md) |
| Understand executable script semantics | [`docs/reference/EXECUTABLE-PSEUDOCODE-SPEC.md`](reference/EXECUTABLE-PSEUDOCODE-SPEC.md) |
| Install the toolkit and editor support | [`docs/how-to/INSTALL.md`](how-to/INSTALL.md) |
| Configure VS Code | [`docs/how-to/editors/VSCODE.md`](how-to/editors/VSCODE.md) |
| Configure Kate | [`docs/how-to/editors/KATE.md`](how-to/editors/KATE.md) |
| Copy agent instructions into another repo | [`docs/how-to/AGENT-INSTRUCTIONS-WORDING.md`](how-to/AGENT-INSTRUCTIONS-WORDING.md) |
| Understand the repository operating model | [`docs/explanation/REPOSITORY-OPERATING-MODEL.md`](explanation/REPOSITORY-OPERATING-MODEL.md) |
| Review available APSEUDO rules | [`docs/reference/RULES.md`](reference/RULES.md) |
| See future planned improvements | [`docs/roadmap/FUTURE-VERSIONS.md`](roadmap/FUTURE-VERSIONS.md) |
