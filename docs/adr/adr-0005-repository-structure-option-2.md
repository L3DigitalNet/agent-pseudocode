---
schema_version: '1.1'
id: 'adr-0005-agent-pseudocode-repository-structure-option-2'
title: 'ADR 0005: Adopt the Option 2 Product-Aware Repository Structure'
description: 'Decision to organize editor, integration, example, script, and user-documentation assets around explicit product responsibilities.'
doc_type: 'adr'
status: 'active'
created: '2026-08-02'
updated: '2026-08-17'
reviewed: '2026-08-02'
owner: 'agent-pseudocode-maintainers'
consumer: 'mix'
tags:
  - 'adr'
  - 'architecture'
  - 'repository-layout'
aliases:
  - 'ADR 0005'
  - 'Repository structure Option 2'
related:
  - 'docs/reviews/repo-structure-review.md'
  - 'docs/plans/2026-08-02-repository-structure-option-2-plan.md'
supersedes: []
superseded_by: null
source:
  - 'docs/reviews/repo-structure-review.md#decision'
  - 'docs/plans/2026-08-02-repository-structure-option-2-plan.md'
confidence: 'high'
visibility: 'internal'
license: null
project:
  decision_makers:
    - 'repository-owner'
  consulted: []
  informed:
    - 'project-maintainers'
---

# Adopt the Option 2 Product-Aware Repository Structure

## Context and Problem Statement

The repository ships one Python policy/runtime package together with editor support, agent hooks, MCP launch assets, source-tree commands, copyable examples, and several kinds of documentation. Its current top-level directories mix product names, delivery mechanisms, host discovery locations, and historical documentation buckets. A reader cannot determine component ownership from the tree without already understanding the project.

The repository structure review compared three bounded layouts against the tracked tree and current packaging, testing, editor, host-integration, and documentation contracts. How should these assets be organized so their owners are legible without disrupting the conventional Python core or host-required discovery paths?

## Decision Drivers

- Keep the conventional root Python project, `src/apseudo_lint/`, and `tests/`.
- Make editor support and host integrations distinct ownership boundaries.
- Establish one canonical home for copyable user examples.
- Organize user documentation by reader purpose rather than legacy mechanism.
- Keep host discovery files where their consumers require them.
- Expose script roles without changing installed CLI names or behavior.
- Prevent stale path consumers and silent file loss during the transition.
- Avoid the release and workspace complexity of a packages monorepo.

## Considered Options

- Clarify the current layout with minimal physical movement.
- Adopt a product-aware toolchain layout with explicit ownership directories.
- Convert the repository into a full packages monorepo.

## Decision Outcome

Chosen option: "Adopt a product-aware toolchain layout with explicit ownership directories," because it makes every non-discovery directory describe its responsibility while preserving the repository's established Python packaging and test conventions.

The target ownership model is:

| Responsibility | Target | Current sources |
| --- | --- | --- |
| Python policy and runtime | `src/apseudo_lint/` | unchanged |
| Python tests and adversarial fixtures | `tests/` | unchanged |
| Editor integrations | `editors/{vscode,kate}/` | `products/` |
| Agent and MCP adapters | `integrations/{agents,mcp}/` | `integrations/agent-hooks/`, `hooks/`, `mcp/` |
| Copyable workflows | `examples/{markdown,runner,standalone}/` | documentation and Kate example trees |
| Source-tree command shims | `scripts/bin/` | `scripts/apseudo-*` |
| Installers | `scripts/install/` | root-level installer scripts |
| Policy hooks | `scripts/policy/` | `scripts/branch-policy-hooks/` and its installer |
| Verification utilities | `scripts/verify/` | enforcement smoke utility |
| User documentation | purpose-based direct children of `docs/` | `docs/apseudo-docs/` |

The documentation taxonomy uses `tutorials/`, `how-to/`, `reference/`, and `explanation/` for user material. Existing project-lifecycle owners such as `docs/adr/`, `docs/handoff/`, `docs/plans/`, `docs/research/`, `docs/reviews/`, and `docs/specs/` remain fixed.

The following exceptions are binding:

- `.agents/`, `.apseudo/`, `.claude/`, `.codex/`, `.github/`, `.standards/`, root discovery configuration, `src/`, `tests/`, `pyproject.toml`, and `uv.lock` remain at their consumer- or tool-required locations.
- `scripts/check.py` remains a fixed repository control entry point. As decided on 2026-08-02 this exception also covered `scripts/plan.py`, the format-3 plan bridge, which was required to stay byte-identical to its recorded upstream helper and to retain its exact managed Ruff exclusion. That bridge was retired on 2026-08-17 when the plan engine was consolidated upstream (L3DigitalNet/agent-configs#44); the script and its Ruff exclusion are gone, and no layout exception applies to it any more.
- The tracked VSIX remains part of this restructuring; changing artifact publication or tracking policy requires a separate decision.
- Python distribution/import names, public CLI names, MCP URIs, APSEUDO rule identifiers, runner semantics, hook decisions, and editor behavior do not change as part of the layout transition.
- Old directory trees are not retained as compatibility shims. Historical records may retain old path literals only when a line-level inventory classifies them as descriptions of past state.

No physical move may begin until the implementation plan's ADR checkpoint and durable impact-inventory checkpoint are both complete. The inventory must classify every tracked move source, executable mode, active path consumer, managed or generated artifact, relative documentation link, and historical literal with zero unclassified entries.

### Consequences

- Good, because component ownership becomes visible directly from the tree.
- Good, because editor and host-adapter code no longer compete with the Python core for top-level meaning.
- Good, because examples and user documentation gain one canonical taxonomy.
- Good, because the pre-move inventory and behavior baseline make path coverage an explicit acceptance condition rather than a best-effort search.
- Bad, because many active path consumers must change atomically and the transition cannot safely be split into casual directory-by-directory cleanup.
- Bad, because historical path literals require classification rather than a mechanical global replacement.
- Neutral, because the resulting tree is not a packages monorepo and does not create independent component versioning or release boundaries.

### Confirmation

This decision is confirmed only when all of the following are true:

- the durable pre-move inventory has zero unclassified entries;
- the exact target mappings exist and obsolete move roots are absent;
- required discovery roots, Python project files, control scripts, tracked contents, and executable modes are preserved;
- all active configuration, CI, test, hook, MCP, runner, installer, editor, and documentation consumers resolve to final paths;
- MCP resources return real content and every required project-review row is `OK`;
- generated editor assets and the tracked VSIX are rebuilt or independently verified at their final path;
- Python, APSEUDO, editor, documentation, frontmatter, standards, handoff, and repository path-contract checks pass for the changed surface; and
- final evidence distinguishes restructuring success from the inherited 85% coverage threshold rather than weakening or misreporting that gate.

## Pros and Cons of the Options

### Clarify the Current Layout

- Good, because it minimizes path churn and migration risk.
- Bad, because `products/`, `hooks/`, `mcp/`, and `docs/apseudo-docs/` continue to obscure responsibility.
- Bad, because documentation alone cannot establish a canonical example or integration owner.

### Product-Aware Toolchain Layout

- Good, because it establishes explicit ownership without disturbing the conventional Python project.
- Good, because it scales to the repository's current shipped surfaces without workspace orchestration.
- Bad, because it requires one carefully inventoried, cross-cutting path transition.

### Full Packages Monorepo

- Good, because it would support independently versioned packages and releases.
- Bad, because the repository does not currently have multiple components that justify independent packaging.
- Bad, because it would move root Python project metadata, complicate `uv` and test defaults, and require new workspace-level orchestration.

## More Information

The repository structure review contains the external research, complete current tree assessment, visual alternatives, and detailed prefix mapping that informed this decision. The format-3 implementation plan owns sequencing, impact inventory, proof, recovery, and durable verification evidence. This ADR fixes the target and exceptions; it does not authorize opportunistic moves outside that plan.
