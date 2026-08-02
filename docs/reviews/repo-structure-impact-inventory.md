---
schema_version: '1.1'
id: 'note-oeg4sy-repo-structure-impact-inventory'
title: 'Repository Structure Impact Inventory'
description: 'Frozen pre-move inventory for the Option 2 repository restructuring.'
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
aliases: []
related:
  - 'docs/adr/adr-0005-repository-structure-option-2.md'
  - 'docs/plans/2026-08-02-repository-structure-option-2-plan.md'
source:
  - 'repository inspection at de6cd14299f6ac8d19d72e7ab48771fa6b87a381'
confidence: 'high'
visibility: 'internal'
license: null
---

# Repository Structure Impact Inventory

## Purpose and freeze point

This is `PathImpactInventory-v1` (EV-001), the pre-move completeness gate for ADR 0005. It freezes the tracked move sources, destinations, file modes, consumers, generated and managed ownership, relative links, and historical exceptions at commit `de6cd14299f6ac8d19d72e7ab48771fa6b87a381`.

No path in this inventory has moved. T4 remains blocked unless every new live finding is added here and the unclassified count remains zero.

| View | Initial observation | Frozen result | Unclassified |
| --- | --: | --: | --: |
| Tracked move sources | 75 | 84 | 0 |
| Files with direct old-prefix literals at the anchor | 70 | 72 | 0 |
| EV-001 self-reference at the T2 checkpoint | Not applicable | 1 | 0 |
| Additional path-sensitive files without a direct old-prefix literal | Not separated | 4 | 0 |
| Tracked symbolic links in the move set | Not separated | 0 | 0 |
| Tracked regular files in the move set | Not separated | 84 | 0 |

The frozen result supersedes the exploratory counts. The increase is expected: the live scan includes every document under `docs/apseudo-docs/` and the ADR, plan, and review evidence created after the first observation.

## Classification contract

Every source or consumer has one disposition:

- **move**: relocate the tracked file to its declared target.
- **update**: keep the file in place but replace active path values or links.
- **move and update**: relocate the file and update active references in it.
- **generate**: rebuild from the named source after the source move.
- **reconcile**: change the standards source of truth and let Project Standards update its owned span or artifact.
- **historical**: retain only the exact line-level literals allowlisted below.
- **verify**: no literal change is presently required, but the file owns a behavioral assertion or parity check affected by the move.

T4 owns non-document layout and executable/configuration convergence. T5 owns the documentation taxonomy and active documentation truth. T3 owns the MCP and project-review regression baseline. T6 independently verifies the final tree.

## Target and ownership map

| Current source | Target or action | Owner | Disposition | Proof |
| --- | --- | --- | --- | --- |
| `products/vscode-extension/` | `editors/vscode/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `products/kate-integration/` | `editors/kate/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `products/README.md` | `editors/README.md` | T4 | move and update | PV-T4-001 |
| `integrations/agent-hooks/` | `integrations/agents/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `hooks/.claude/` | `integrations/agents/claude/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `hooks/.codex/` | `integrations/agents/codex/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `mcp/` | `integrations/mcp/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `scripts/apseudo-*` | `scripts/bin/apseudo-*` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `scripts/install-{enforcement,kate-user,vscode-vsix}.sh` | `scripts/install/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `scripts/install-branch-policy-hooks.sh` | `scripts/policy/install-hooks.sh` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `scripts/branch-policy-hooks/` | `scripts/policy/hooks/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `scripts/run-enforcement-smoke-test.sh` | `scripts/verify/enforcement-smoke-test.sh` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `docs/apseudo-docs/examples/markdown-fence-demo.md` | `examples/markdown/markdown-fence-demo.md` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `docs/apseudo-docs/examples/runner/` | `examples/runner/` | T4 | move and update | PV-T4-001, PV-T4-002 |
| `docs/apseudo-docs/examples/{nested-decision,review-loop}.apseudo` | `examples/standalone/` | T4 | move | PV-T4-001, PV-T4-002 |
| `products/kate-integration/examples/review-loop.apseudo` | deduplicate into `examples/standalone/review-loop.apseudo` | T4 | move/deduplicate | PV-T4-001 |
| `docs/apseudo-docs/enforcement/ENFORCEMENT-GUIDE.md` | `docs/how-to/enforcement/ENFORCEMENT-GUIDE.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/enforcement/ENFORCEMENT.md` | `docs/reference/enforcement/ENFORCEMENT.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/features/*.md` | `docs/reference/features/*.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/roadmap/*.md` | `docs/roadmap/*.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/AGENT-INSTRUCTIONS-WORDING.md` | `docs/how-to/AGENT-INSTRUCTIONS-WORDING.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/IMPLEMENTATION-GUIDE.md` | `docs/how-to/IMPLEMENTATION-GUIDE.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/INSTALL.md` | `docs/how-to/INSTALL.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/{KATE,VSCODE}.md` | `docs/how-to/editors/{KATE,VSCODE}.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/REPOSITORY-LAYOUT.md` | `docs/explanation/REPOSITORY-LAYOUT.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/RUNNER-USAGE.md` | `docs/reference/cli/RUNNER-USAGE.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/TESTING.md` | `docs/how-to/TESTING.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/agent-tasks.md` | `docs/how-to/agent-tasks.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/usage.md` | merge unique accurate content into `docs/usage.md`, then retire | T5 | merge/retire | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/use-cases/COMMON-WORKFLOWS.md` | `docs/how-to/COMMON-WORKFLOWS.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/use-cases/RUNNER-WORKFLOWS.md` | `docs/how-to/RUNNER-WORKFLOWS.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/use-cases/EXAMPLE-CATALOG.md` | `docs/reference/EXAMPLE-CATALOG.md` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/use-cases/{AGENT-FEEDING-PATHS,CHOOSING-A-SURFACE,MENTAL-MODEL,REPOSITORY-OPERATING-MODEL}.md` | corresponding files in `docs/explanation/` | T5 | move and update | PV-T5-001, PV-T5-002 |
| `docs/apseudo-docs/usage/{README.md,use-cases/README.md}` | merge navigation into `docs/README.md`, then retire | T5 | merge/retire | PV-T5-001, PV-T5-002 |

## Tracked move-source manifest

The source scan is defined over Git's index, not the working-tree directory listing. All 84 entries are regular files; 62 have mode `100644`, 22 have mode `100755`, and none has mode `120000`.

### Documentation sources: 35 files, mode `100644`

```text
docs/apseudo-docs/enforcement/ENFORCEMENT-GUIDE.md
docs/apseudo-docs/enforcement/ENFORCEMENT.md
docs/apseudo-docs/examples/markdown-fence-demo.md
docs/apseudo-docs/examples/nested-decision.apseudo
docs/apseudo-docs/examples/review-loop.apseudo
docs/apseudo-docs/examples/runner/fix-ruff.apseudo
docs/apseudo-docs/examples/runner/review-spec.apseudo
docs/apseudo-docs/features/AUTOCOMPLETE.md
docs/apseudo-docs/features/FORMATTER-LSP-AUTOCOMPLETE.md
docs/apseudo-docs/features/FORMATTER.md
docs/apseudo-docs/features/HOOKS.md
docs/apseudo-docs/features/LANGUAGE-SERVER.md
docs/apseudo-docs/features/MCP.md
docs/apseudo-docs/features/SKILLS.md
docs/apseudo-docs/roadmap/FUTURE-LINTER.md
docs/apseudo-docs/roadmap/FUTURE-VERSIONS.md
docs/apseudo-docs/usage/AGENT-INSTRUCTIONS-WORDING.md
docs/apseudo-docs/usage/IMPLEMENTATION-GUIDE.md
docs/apseudo-docs/usage/INSTALL.md
docs/apseudo-docs/usage/KATE.md
docs/apseudo-docs/usage/README.md
docs/apseudo-docs/usage/REPOSITORY-LAYOUT.md
docs/apseudo-docs/usage/RUNNER-USAGE.md
docs/apseudo-docs/usage/TESTING.md
docs/apseudo-docs/usage/VSCODE.md
docs/apseudo-docs/usage/agent-tasks.md
docs/apseudo-docs/usage/usage.md
docs/apseudo-docs/usage/use-cases/AGENT-FEEDING-PATHS.md
docs/apseudo-docs/usage/use-cases/CHOOSING-A-SURFACE.md
docs/apseudo-docs/usage/use-cases/COMMON-WORKFLOWS.md
docs/apseudo-docs/usage/use-cases/EXAMPLE-CATALOG.md
docs/apseudo-docs/usage/use-cases/MENTAL-MODEL.md
docs/apseudo-docs/usage/use-cases/README.md
docs/apseudo-docs/usage/use-cases/REPOSITORY-OPERATING-MODEL.md
docs/apseudo-docs/usage/use-cases/RUNNER-WORKFLOWS.md
```

### Editor sources: 24 files

Mode `100755` applies only to the two files beneath `scripts/`; every other entry in this block has mode `100644`.

```text
products/README.md
products/kate-integration/README.md
products/kate-integration/agent-pseudocode.xml
products/kate-integration/examples/review-loop.apseudo
products/kate-integration/lsp-client-settings.json
products/kate-integration/lsp-client-settings.markdown-opt-in.json
products/vscode-extension/.vscode/launch.json
products/vscode-extension/.vscode/tasks.json
products/vscode-extension/.vscodeignore
products/vscode-extension/LICENSE
products/vscode-extension/README.md
products/vscode-extension/agent-pseudocode-0.6.1.vsix
products/vscode-extension/extension.js
products/vscode-extension/language-configuration.json
products/vscode-extension/package-lock.json
products/vscode-extension/package.json
products/vscode-extension/scripts/check-extension.mjs
products/vscode-extension/scripts/compile-grammars.mjs
products/vscode-extension/snippets/agent-pseudocode.code-snippets
products/vscode-extension/snippets/markdown.code-snippets
products/vscode-extension/syntaxes/agent-pseudocode.tmLanguage.json
products/vscode-extension/syntaxes/agent-pseudocode.tmLanguage.yaml
products/vscode-extension/syntaxes/markdown-agent-pseudocode.tmLanguage.json
products/vscode-extension/syntaxes/markdown-agent-pseudocode.tmLanguage.yaml
```

### Agent, MCP, and script sources: 25 files

The four dormant host documents/configurations are `100644`. The MCP example configuration is `100644`. Every other entry is `100755` except that mode note.

```text
hooks/.claude/README.md
hooks/.claude/settings.json
hooks/.codex/README.md
hooks/.codex/hooks.json
integrations/agent-hooks/apseudo-hook.py
mcp/.mcp.json
mcp/apseudo-mcp
scripts/apseudo-claude
scripts/apseudo-codex
scripts/apseudo-explain
scripts/apseudo-format
scripts/apseudo-lint
scripts/apseudo-lsp
scripts/apseudo-mcp
scripts/apseudo-mermaid
scripts/apseudo-review
scripts/apseudo-run
scripts/apseudo-template
scripts/branch-policy-hooks/pre-commit
scripts/branch-policy-hooks/pre-push
scripts/install-branch-policy-hooks.sh
scripts/install-enforcement.sh
scripts/install-kate-user.sh
scripts/install-vscode-vsix.sh
scripts/run-enforcement-smoke-test.sh
```

## Direct-reference consumer manifest

The anchor scan uses the old move prefixes and exact script families, excludes only `docs/reference/pre-migration/**`, and finds 72 files. The following table classifies every anchor file. A file can be both a move source and a consumer. At the T2 checkpoint, this evidence file is the 73rd match because it records the old-to-new contract; its own literals are classified as historical migration evidence rather than as active consumers.

| Files | Class | Owner | Action |
| --- | --- | --- | --- |
| `.agents/skills/agent-pseudocode/SKILL.md`; `.agents/skills/agent-pseudocode/agents/openai.yaml`; `.agents/skills/agent-pseudocode/references/quick-reference.md`; `.claude/skills/agent-pseudocode/SKILL.md`; `.claude/skills/agent-pseudocode/references/quick-reference.md` | active deployed references | T4/T5 | update owned paths; preserve discovery roots |
| `.codex/config.toml`; `.mcp.json`; `.github/workflows/apseudo-lint.yml`; `.github/workflows/format.yml`; `.pre-commit-config.yaml`; `.prettierignore`; `.standards/config.toml` | active configuration | T4/T5 | update/reconcile owned entries and execute/parse checks |
| `AGENTS.md`; `CLAUDE.md`; `README.md`; `docs/README.md` | active instructions/navigation | T4/T5 | update current paths; preserve managed spans |
| `docs/adr/adr-0004-branch-integration-and-local-git-hook-policy.md`; `docs/handoff/architecture.md`; `docs/handoff/conventions.md`; `docs/handoff/bugs/004-lsp-serve-unhandled-read-message.md`; `docs/reference/EXECUTABLE-PSEUDOCODE-SPEC.md`; `docs/reviews/PROJECT-REVIEW-RESULT.md`; `docs/specs/apseudo-validation-toolchain.md` | active owner truth | T4/T5 | update current links, commands, and component paths |
| `docs/apseudo-docs/enforcement/ENFORCEMENT-GUIDE.md`; `docs/apseudo-docs/enforcement/ENFORCEMENT.md`; `docs/apseudo-docs/features/AUTOCOMPLETE.md`; `docs/apseudo-docs/features/FORMATTER-LSP-AUTOCOMPLETE.md`; `docs/apseudo-docs/features/FORMATTER.md`; `docs/apseudo-docs/features/HOOKS.md`; `docs/apseudo-docs/features/LANGUAGE-SERVER.md`; `docs/apseudo-docs/features/MCP.md` | moved active documentation | T5 | move and update active paths |
| `docs/apseudo-docs/roadmap/FUTURE-LINTER.md`; `docs/apseudo-docs/usage/AGENT-INSTRUCTIONS-WORDING.md`; `docs/apseudo-docs/usage/IMPLEMENTATION-GUIDE.md`; `docs/apseudo-docs/usage/INSTALL.md`; `docs/apseudo-docs/usage/KATE.md`; `docs/apseudo-docs/usage/REPOSITORY-LAYOUT.md`; `docs/apseudo-docs/usage/RUNNER-USAGE.md`; `docs/apseudo-docs/usage/TESTING.md`; `docs/apseudo-docs/usage/VSCODE.md`; `docs/apseudo-docs/usage/usage.md` | moved active documentation | T5 | move/merge and update active paths |
| `docs/apseudo-docs/usage/use-cases/AGENT-FEEDING-PATHS.md`; `docs/apseudo-docs/usage/use-cases/CHOOSING-A-SURFACE.md`; `docs/apseudo-docs/usage/use-cases/COMMON-WORKFLOWS.md`; `docs/apseudo-docs/usage/use-cases/EXAMPLE-CATALOG.md`; `docs/apseudo-docs/usage/use-cases/README.md`; `docs/apseudo-docs/usage/use-cases/REPOSITORY-OPERATING-MODEL.md`; `docs/apseudo-docs/usage/use-cases/RUNNER-WORKFLOWS.md` | moved active documentation | T5 | move/merge and update active paths |
| `integrations/agent-hooks/apseudo-hook.py`; `products/README.md`; `products/kate-integration/README.md`; `products/vscode-extension/README.md`; `scripts/apseudo-mcp`; `scripts/install-kate-user.sh`; `scripts/install-vscode-vsix.sh`; `scripts/run-enforcement-smoke-test.sh` | moved executable/product consumers | T4 | move and update active paths; execute nearest checks |
| `src/apseudo_lint/review.py` | active Python path owner | T3/T4/T5 | baseline current paths, then update final paths with content-level tests |
| `CHANGELOG.md`; `docs/adr/adr-0003-markdown-frontmatter-scope-and-conventions.md`; `docs/adr/adr-0005-repository-structure-option-2.md`; `docs/handoff/bugs/001-mcp-resource-map-stale-paths.md`; `docs/handoff/bugs/002-review-completeness-stale-paths.md`; `docs/handoff/sessions/2026-07.md`; `docs/plans/2026-08-02-repository-structure-option-2-plan.md`; `docs/reviews/FEATURE-GAP-ANALYSIS.md`; `docs/reviews/PROJECT-TRACEABILITY-REVIEW.md`; `docs/reviews/repo-structure-review.md`; `docs/superpowers/plans/2026-07-08-adopt-standards.md` | historical or mixed evidence | T5 | retain only allowlisted lines; update every active/mixed line |

## Additional path-sensitive consumers

These files are not additional direct old-prefix matches, or contain stale paths from a still earlier layout. They are nevertheless migration consumers.

| File | Current sensitivity | Owner | Action / proof |
| --- | --- | --- | --- |
| `.apseudo/scripts.toml` | runner registry points at nonexistent `docs/examples/runner/` paths | T4 | repoint to `examples/runner/`; run runner check/render/command proofs |
| `src/apseudo_lint/mcp.py` | MCP resource map points at nonexistent pre-reorganization documentation paths | T3/T5 | content-level regression baseline, then final documentation targets |
| `docs/usage.md` | command example points at nonexistent `docs/reference/language/examples/` | T5 | repoint to canonical example and run link/command proof |
| `tests/test_mcp_review_hooks.py` | behavioral owner for MCP resources, review completeness, and host hooks; no current literal covers the complete contract | T3/T4/T5 | add content/all-row assertions and update fixtures with each transition |

The same stale-family scan also finds overlapping consumers already in the 72-file set: `.github/workflows/apseudo-lint.yml`, `README.md`, `CHANGELOG.md`, `scripts/run-enforcement-smoke-test.sh`, `src/apseudo_lint/review.py`, and the two associated handoff bug records. They retain their classification above.

## Relative Markdown links in moved documents

An independent Markdown-link scan finds relative links in five moved files. T5 must resolve every link from the destination path; moving the file without recomputing these targets is not acceptable.

| Source | Relative-link responsibility |
| --- | --- |
| `docs/apseudo-docs/usage/README.md` | nested usage index, reference, roadmap, editor, and use-case links; merge into `docs/README.md` |
| `docs/apseudo-docs/usage/RUNNER-USAGE.md` | links to the old CLI usage page; retarget the canonical `docs/usage.md` or final CLI reference |
| `docs/apseudo-docs/usage/usage.md` | runner, agent-wording, reference, and roadmap links; reconcile before retirement |
| `docs/apseudo-docs/usage/use-cases/README.md` | use-case, feature, enforcement, example, editor, and reference links; merge navigation into `docs/README.md` |
| `docs/apseudo-docs/usage/use-cases/REPOSITORY-OPERATING-MODEL.md` | agent-instruction wording link; recompute from `docs/explanation/` |

## Generated, packaged, duplicated, and managed assets

| Artifact | Classification and source of truth | Owner | Required preservation |
| --- | --- | --- | --- |
| `products/vscode-extension/syntaxes/*.tmLanguage.json` | generated from adjacent YAML grammars by `scripts/compile-grammars.mjs` | T4 | move both; rebuild and prove generated parity |
| `products/vscode-extension/agent-pseudocode-0.6.1.vsix` | tracked packaged output of the VS Code extension | T4 | preserve bytes during move; rebuild/check separately without silently replacing the tracked package |
| `products/vscode-extension/package-lock.json` | npm-generated dependency lock | T4 | preserve unless the unchanged build demonstrably regenerates it |
| two `review-loop.apseudo` copies | byte-identical at SHA-256 `e37b58953da13f9ab501a6d5198d201b47fd5bd561a330dec28c4dc66cbd9308` | T4 | retain one canonical `examples/standalone/review-loop.apseudo` only after equality proof |
| `.standards/config.toml` | Project Standards configuration source of truth; contains move-root frontmatter globs and Markdown exclusions | T4/T5 | edit configuration, reconcile, validate, and prove no-op convergence |
| `.standards/lock.toml` and standards-owned spans/artifacts | generated ownership/digest record | T4/T5 | never hand-edit; accept only reconciliation output from the configured source |
| `AGENTS.md`, `CLAUDE.md`, `.codex/config.toml`, `.claude/settings.json`, managed workflows | contain mixed repository-owned and standards-owned data | T4/T5 | update only repository-owned entries; preserve/reconcile managed spans |
| `scripts/plan.py`, `scripts/check.py` | fixed repository control entry points, not move sources | T4 | remain at exact paths; preserve the singular Ruff exclusion for `scripts/plan.py` |

No tracked symlink, submodule, or Git LFS pointer occurs in the move set.

## Historical-reference allowlist

Only the following old-path literals may remain after migration. Line numbers refer to the T2 freeze commit and identify statements about past state or the accepted migration contract. The allowlist applies to literals, not whole files, except for the archived transcript tree explicitly named below.

| File and frozen lines | Reason |
| --- | --- |
| `CHANGELOG.md:13,16,40` | release history describing paths at those releases |
| `docs/adr/adr-0003-markdown-frontmatter-scope-and-conventions.md:88` | accepted ADR evidence recording the then-current scoped source list |
| `docs/adr/adr-0005-repository-structure-option-2.md:74-81,123` | accepted current-to-target mapping and rejected alternative |
| `docs/handoff/bugs/001-mcp-resource-map-stale-paths.md:26` | defect cause evidence naming the real path observed when the bug was filed |
| `docs/handoff/bugs/002-review-completeness-stale-paths.md:11,21-22` | defect cause and prior-state mapping evidence |
| `docs/handoff/sessions/2026-07.md:13` | append-only session history |
| `docs/plans/2026-08-02-repository-structure-option-2-plan.md:109-110,129,133,145,376,407,542-555,564-584` | active execution contract's explicit source-to-target mappings |
| `docs/reviews/FEATURE-GAP-ANALYSIS.md:41` | archived review snapshot |
| `docs/reviews/PROJECT-TRACEABILITY-REVIEW.md:35-45` | archived review snapshot of component paths |
| `docs/reviews/repo-structure-review.md:19,40-42,47,56-61,105-106,130-132,155,210,259,276-287,307` | decision analysis, current-state tree, and recommended mapping |
| `docs/superpowers/plans/2026-07-08-adopt-standards.md:17,20,223-224,256,270,280,572,618,670` | completed historical implementation plan |
| `docs/reviews/repo-structure-impact-inventory.md:45,65-98,107-204,217-220,235,243-247,253-255,297,302` | EV-001's tracked pre-move manifest, classification, and verification contract |
| `docs/reference/pre-migration/**` | verbatim archived transcript tree already excluded by policy |

Mixed files have active lines that are explicitly **not** allowlisted:

- `docs/adr/adr-0003-markdown-frontmatter-scope-and-conventions.md:293` describes the current taxonomy and must change.
- `docs/handoff/bugs/002-review-completeness-stale-paths.md:33` is a forward fix instruction and must be replaced by final-path/status truth.
- Every status, fix, related-link, or current-owner field outside the frozen lines above must converge to the final layout.

## Scan and verification procedure

PV-T2-001 is reproducible from the T2 checkpoint with these independent views:

1. `git ls-files -s` filtered by the target-map source prefixes enumerates the 84 sources and their modes.
2. A separate `git grep -nE` over the old prefixes and script families finds the 72 anchor files, plus EV-001 itself at the checkpoint, excluding only the pre-migration archive.
3. A stale-family scan for `docs/examples/`, `docs/reference/language/examples/`, and earlier `docs/usage/` resource paths identifies the additional path-sensitive consumers.
4. A Markdown-link scan over `docs/apseudo-docs/` identifies relative links whose resolution changes after a move.
5. Configuration scans cover TOML, JSON, JSONC, YAML, workflow, pre-commit, MCP, and host-discovery files; Project Standards ownership is read from `.standards/config.toml` and `.standards/lock.toml`.
6. Generated-source inspection ties VS Code JSON grammars to their YAML inputs, checks the tracked VSIX and npm lock, and proves the duplicate example hash.
7. Historical matches are reconciled against the line-level allowlist above.

The negative control creates a temporary candidate containing `products/__inventory_canary__`, reruns the direct-reference classifier, and must report exactly one new unclassified consumer above the 73 classified checkpoint matches. The candidate is removed before verification completes; the worktree must contain only EV-001.

## Readiness decision

All 84 move sources and all 76 direct or additional path-sensitive files have an owner, target/action, disposition, and proof. The unclassified count is zero. T3 may establish the behavioral baseline; T4 remains prohibited until T3 is complete and must recheck this inventory immediately before moving any file.
