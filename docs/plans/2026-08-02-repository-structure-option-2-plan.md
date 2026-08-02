---
plan_format: 3
title: 'Repository Structure Option 2 Implementation Plan'
slug: 'repository-structure-option-2'
size: full
status: complete
revision: 2
revises_revision: 1
revision_reason: 'record the validated byte-identical bridge integration and its managed Ruff exclusion'
pause_reason: ''
source: 'user-approved Option 2 and docs/reviews/repo-structure-review.md'
spec_ref: ''
created: 2026-08-02
updated: 2026-08-02
owners:
  - 'project-maintainers'
---

# Repository Structure Option 2 Implementation Plan

> **Definition, not state.** Authoring drafts live in `.project-pipeline/2026-08-02-repository-structure-option-2/authoring/`; generated per-phase execution status and evidence pointers live in `.project-pipeline/2026-08-02-repository-structure-option-2/execution/`.

## 1. Objective

Restructure the Agent Pseudocode repository into the approved Option 2 layout without changing the Python package's behavior, public CLI surface, editor features, agent integrations, or required discovery paths. The first physical move is prohibited until an accepted ADR and a durable impact inventory account for every tracked move source, active path consumer, managed/generated artifact, historical reference, file mode, and validation owner.

The resulting repository keeps `src/apseudo_lint/`, `tests/`, root package metadata, and mandatory dot-directory discovery surfaces in place; it exposes editor assets under `editors/`, host adapters under `integrations/`, canonical copyable workflows under `examples/`, role-specific automation under `scripts/`, and user documentation directly under purpose-based `docs/` categories.

## 2. Authority and Source Map

| Source | Source Role | Authority / Use | Version / Date | Affected Plan Surface |
| --- | --- | --- | --- | --- |
| `request` | normative | Approves Option 2, requires an ADR, and requires complete impact knowledge before the first move | 2026-08-02 | §§1–13, T1–T6 |
| `repo:docs/reviews/repo-structure-review.md#decision` | decision | Selects the product-aware layout and records its boundaries | 2026-08-02 | §§3–6, T1–T6, Appendix A |
| `repo:docs/reviews/repo-structure-review.md#recommended-path-mapping` | decision | Defines the approved prefix-level path mapping | 2026-08-02 | §§4–6, T2, T4–T6, Appendix A |
| `repo:docs/adr/adr.template.md` | current-state evidence | Supplies the repository ADR shape and metadata contract | current at `762805c` | T1 |
| `repo:docs/handoff/architecture.md#components` | current-state evidence | Identifies policy, editor, integration, and documentation owners | 2026-07-08 | §§3–5, T2–T6 |
| `repo:pyproject.toml` | current-state evidence | Defines the installable package, twelve CLI entry points, test roots, and Python gates | current at `762805c` | §§3–7, T3–T6 |
| `repo:src/apseudo_lint/review.py::review_project` | current-state evidence | Defines path-sensitive project completeness checks | current at `762805c` | T3–T6 |
| `repo:src/apseudo_lint/mcp.py::APseudoMCPServer._read_resource` | current-state evidence | Defines MCP URI-to-document path resolution | current at `762805c` | T3, T5, T6 |
| `repo:src/apseudo_lint/main_cli.py::_docs` | current-state evidence | Defines the generated task-document default and explicit output behavior | current at `a7a48bf` | T7 |
| `repo:tests/test_mcp_review_hooks.py::test_review_project_reports_expected_tooling` | current-state evidence | Defines existing MCP, review, and hook integration coverage | current at `762805c` | T3–T6 |
| `repo:tests/test_runner_operational.py::test_unified_cli_doctor_and_registry_docs` | current-state evidence | Defines current explicit-output task-document generation coverage | current at `a7a48bf` | T7 |
| `repo:docs/README.md#layout` | current-state evidence | Defines the current documentation navigation and layout summary | current at `762805c` | T5 |
| `repo:docs/handoff/bugs/001-mcp-resource-map-stale-paths.md#cause` | current-state evidence | Records known stale MCP document paths | open, 2026-07-09 | T2, T3, T5 |
| `repo:docs/handoff/bugs/002-review-completeness-stale-paths.md#cause` | current-state evidence | Records known stale project-review document paths | open, 2026-07-09 | T2, T3, T5 |
| `repo:.standards/config.toml` | current-state evidence | Defines standards-managed Markdown and formatting scopes that reference move roots | Project Standards 5.14.0 | T2, T4–T6 |
| `repo:.github/workflows/apseudo-lint.yml` | operational evidence | Defines current CI path filters and integration commands | current at `762805c` | T2, T4, T6 |
| `repo:scripts/plan.py::main` | operational evidence | Provides the format-3 state, recovery, and checkpoint bridge used by this plan | plan-authoring 3.3.0 helper hash recorded in §4 | §§3, 7, 10, 13 |

Conflict precedence: the 2026-08-02 request and selected review decision define the target. Current implementation, tests, configuration, bugs, and documentation orient the transition and preservation surface but do not override the decision. Accepted ADRs, changelogs, append-only session records, and the 2026-07-08 plan remain historical evidence; an old literal path inside them is not automatically an active consumer.

## 3. Scope, Boundaries, and Constraints

### 3.1 In Scope

- Record ADR 0005 for the approved Option 2 ownership model and exceptions.
- Produce a durable, zero-unclassified impact inventory before any move.
- Correct and test known path-resolution defects that would weaken the baseline.
- Move editor, host-integration, script, example, and user-documentation trees to the Appendix A mappings.
- Update every active runtime, build, CI, hook, MCP, runner, test, installer, standards-config, frontmatter, and documentation consumer.
- Rebuild or verify generated editor assets and the tracked VSIX without changing release policy.
- Reconcile ADR, handoff, bug, review, and navigation truth after the transition.
- Capture durable final verification evidence and an explicit inherited-gate statement.

### 3.2 Out of Scope and Deferred

- Renaming the Python distribution, import package, CLI commands, or APSEUDO rule identifiers.
- Splitting the repository into independently versioned packages.
- Removing the tracked VSIX or changing how releases publish artifacts.
- Deduplicating `.agents/` and `.claude/` skills or inventing a new generator for host discovery copies.
- Moving `.agents/`, `.apseudo/`, `.claude/`, `.codex/`, `.github/`, `.standards/`, `src/`, `tests/`, `pyproject.toml`, `uv.lock`, `scripts/plan.py`, or `scripts/check.py`.
- Locally reformatting, lint-fixing, or forking the byte-identical format-3 bridge; bridge defects belong to the upstream plan-authoring package.
- Fixing bug 004, raising coverage to 85%, or changing the known hosted `check.yml` coverage boundary. Revisit coverage only under its existing project workstream.
- Committing, pushing, publishing, or promoting to another branch during plan authoring. Execution task checkpoints may commit under the plan contract; a push still requires separate authorization.

### 3.3 Ownership and Preserved Behavior

| Boundary | Owner / Responsibility | Failure / Change Requests Route To |
| --- | --- | --- |
| `src/apseudo_lint/` | Policy engine, CLI, LSP, MCP, runner, and project review | Project maintainers; T3/T4/T5 |
| `editors/` | Thin VS Code and Kate integrations | Project maintainers; T4 |
| `integrations/` | Host-neutral agent hook and MCP launch/config examples | Project maintainers; T4 |
| Root discovery files | Host-required deployed configuration; locations remain fixed | Owning host or standards package; T4/T5 |
| `scripts/` | Plan/check bridge plus categorized source-tree utilities | Project maintainers; T4 |
| `examples/` | Canonical copyable user workflows | Project maintainers; T4 |
| `docs/` | User docs plus fixed ADR, handoff, plans, research, reviews, specs, and roadmap owners | Documentation and project maintainers; T5 |
| Historical records | Preserve factual old paths unless their lifecycle metadata or forward pointer changes | T2 inventory allowlist; T5 |
| Observable behavior | CLI names/options/exits, APSEUDO rules, MCP URIs, hook decisions, runner semantics, editor features | T3 characterization and T6 verification |

### 3.4 Constraints and Authorization

| ID | Constraint / Authorization Boundary | Source | Affected Task(s) |
| --- | --- | --- | --- |
| C-001 | No physical move begins until T1 and T2 have terminal checkpoints | request | T3–T6 |
| C-002 | Use `git ls-files` as the tracked-tree authority and preserve executable modes | request; repository evidence | T2, T4, T6 |
| C-003 | Required discovery paths and standards-owned spans remain at their host-defined locations | review decision; repository instructions | T1, T2, T4–T6 |
| C-004 | Configure then run `project-standards reconcile --apply`; do not hand-edit digest-locked payloads | repository standards contract | T4, T5 |
| C-005 | Run APSEUDO formatting before linting; no APSEUDO diagnostic may remain | repository instructions | T1–T6 |
| C-006 | Markdown/structured-text fix passes precede non-mutating checks | repository instructions | T1, T2, T4–T6 |
| C-007 | Preserve unrelated work and stage only task-owned paths | repository instructions | T1–T6 |
| C-008 | No push, release, marketplace publication, or branch promotion is authorized | request scope | T1–T6 |
| C-009 | Preserve the byte-identical format-3 bridge and its exact standards-configured Ruff exclusion | plan-authoring bridge contract; repository Python-tooling configuration | T4, T6 |

## 4. Current State and Target State

### 4.1 Current State

- The repository has 235 tracked files; 75 tracked files are physically under the approved move roots and 70 active text files contain direct old-prefix references in the initial 2026-08-02 sweep.
- The Python package already uses `src/apseudo_lint/` with root `tests/` and must remain there.
- Editor assets live under `products/`; host integration assets are split among `integrations/agent-hooks/`, `hooks/`, and `mcp/`.
- User documentation is nested under `docs/apseudo-docs/`; the standards-owned CLI reference at `docs/usage.md` overlaps with the older `docs/apseudo-docs/usage/usage.md`.
- Copyable examples are duplicated or split across documentation and Kate trees; `.apseudo/scripts.toml` and smoke/CI commands already contain partially migrated `docs/examples/` paths that do not exist.
- MCP resource paths and project-review completeness paths contain known stale references recorded as bugs 001 and 002. `apseudo-review` currently reports missing completeness rows while exiting zero, so exit status alone is not an adequate oracle.
- The hosted Python check remains red at the coverage threshold; the session state records coverage improvement as separate active work.
- Before this plan was authored, `scripts/plan.py` lacked format-3 state and recovery commands. With explicit owner authorization, authoring replaced it byte-for-byte with plan-authoring 3.3.0's helper at SHA-256 `567210e5b2de93111452602b99d80ebea8f7380ff41ca48f72addbb40c3c35d9`. Validate, promote, generate, sync, and next were exercised successfully. The managed Python-tooling configuration excludes only this vendored bridge from Ruff so repository formatting cannot invalidate its byte identity. The upstream package self-test currently stops at its package-contract fixture commit hashes before exercising helper assertions; this does not change the repository bridge checksum or successful local command results.

### 4.2 Target State

- The exact physical and documentation mappings in Appendix A exist; old move roots are absent.
- Every active path consumer resolves to the new target. Remaining old literals are line-level classified historical evidence, not executable or current navigation.
- MCP resources return real document content, every required project-review row is `OK`, registered runner examples resolve, hook configs execute the relocated implementation, and editor checks/package generation work from `editors/`.
- `docs/README.md` is the single user-documentation index. Direct child categories separate how-to, reference, explanation, roadmap, and fixed project-lifecycle owners. `docs/usage.md` remains the standards-owned canonical CLI reference; the older duplicate usage page is merged or retired after content comparison.
- The impact inventory and final verification report remain as durable evidence.

### 4.3 Delta Summary

| Area | Current | Target | Must Preserve | Risk / Unknown |
| --- | --- | --- | --- | --- |
| Python core | Root `src/` and `tests/` | Unchanged | APIs, CLI behavior, tests | Existing coverage gate is red |
| Editors | `products/{vscode-extension,kate-integration}` | `editors/{vscode,kate}` | Extension package root, file modes, VSIX | Marketplace/release policy unchanged |
| Agent/MCP integration | Three competing top-level roots | `integrations/{agents,mcp}` plus fixed discovery files | Hook decisions, MCP initialize/resources | Host configs contain literal commands |
| Scripts | Mixed root scripts | `bin/`, `install/`, `policy/`, `verify/`; plan/check fixed | Command behavior and executable modes | Many instructions call old shims |
| Examples | Docs/Kate split and stale partial paths | Root `examples/{markdown,runner,standalone}` | Example contents and runner validity | One duplicate blob must have one canonical owner |
| User docs | `docs/apseudo-docs/` | Direct purpose-based `docs/` categories | Content, frontmatter IDs, working links | CLI reference overlap needs comparison |
| Historical evidence | Old paths mixed with active refs | Explicit allowlist and forward pointers | Historical accuracy | Blind replacement would corrupt records |

## 5. Change Surface and Architecture

### 5.1 Components and Ownership

| Component / Surface | Current Responsibility | Planned Responsibility | Paths / Contracts | Owning Task(s) |
| --- | --- | --- | --- | --- |
| Architecture decision | Review recommendation only | Accepted ADR 0005 | `docs/adr/adr-0005-repository-structure-option-2.md` | T1 |
| Impact accounting | Ad hoc searches | Frozen PathImpactInventory-v1 | `docs/reviews/repo-structure-impact-inventory.md` | T2 |
| Path-sensitive behavior | Stale MCP/review checks | Characterized, correct current baseline | MCP resources; project-review rows | T3 |
| Physical non-doc layout | `products/`, `hooks/`, `mcp/`, mixed `scripts/`, split examples | Appendix A prefix map | LayoutMap-v1 | T4 |
| Documentation architecture | Nested topic/mechanism buckets | Purpose-based categories | DocumentationMap-v1 | T5 |
| Integrated acceptance | Independent gates and inherited red coverage | One reconciled verification record | EV-002 | T6 |

### 5.2 Control and Ownership View

```text
src/apseudo_lint (policy and runtime)
    ├── editors/ (thin VS Code and Kate clients)
    ├── integrations/ (agent-hook and MCP adapters)
    ├── scripts/ (source-tree commands and maintenance entry points)
    ├── examples/ (canonical user workflows)
    └── docs/ (how-to, reference, explanation, and project truth)

root discovery files ──point to── integrations/
tests and CI ──verify── every boundary above
```

Dependency direction remains inward toward `src/apseudo_lint`; no editor, host adapter, or document becomes a second policy engine.

### 5.3 Change-Surface Matrix

| Surface | Current Owner | Target Change | Invariant / Preservation | Proof | Task |
| --- | --- | --- | --- | --- | --- |
| Observable behavior | Python package and adapters | Paths only; bugs 001/002 corrected | CLI, rules, hooks, MCP, runner, editors remain functional | PV-T3-001, PV-T6-001 | T3, T6 |
| Architecture / dependency direction | `src` plus scattered adapters | Explicit `editors/` and `integrations/` boundaries | Adapters reuse `src` | PV-T4-001 | T4 |
| Public / cross-task interface | CLI names, MCP URIs, hooks, examples | Locations change; names/semantics do not | Existing external identifiers remain | PV-T4-002, PV-T6-001 | T4, T6 |
| Data / persistent state | None | Not applicable | No runtime data migration | PV-T6-001 | T6 |
| Configuration / user-owned files | Root discovery and standards config | Literal paths updated in owned spans | Discovery locations and unrelated content preserved | PV-T4-002, PV-T5-002 | T4, T5 |
| Security / trust boundary | Hook bypass guards and runner policy | Guarded paths follow relocated implementation | No bypass weakened | PV-T4-002 | T4 |
| Compatibility / migration | Old filesystem paths | One Git transition with historical allowlist | File contents/modes/history and public identifiers preserved | PV-T2-001, PV-T4-001 | T2, T4 |
| Operations / deployment | CI, installers, pre-commit, VSIX build | Commands use new paths | Local/CI entry points remain runnable | PV-T4-002, PV-T6-001 | T4, T6 |
| Documentation / owner truth | Nested and overlapping docs | DocumentationMap-v1 and reconciled indexes | Frontmatter IDs and authoritative content preserved | PV-T5-001, PV-T5-002 | T5 |
| Durable acceptance evidence | No migration-specific record | Inventory plus final verification report | Evidence contains no secrets or unbounded logs | PV-T2-001, PV-T6-001 | T2, T6 |

### 5.4 Binding Decisions

| ID | Decision | Rationale | Alternatives Actually Considered | Source / ADR | Affected Task(s) |
| --- | --- | --- | --- | --- | --- |
| D-001 | Use the Option 2 product-aware layout | Matches shipped surfaces without workspace indirection | Minimal clarification; full packages monorepo | request; review; ADR 0005 to record | T1–T6 |
| D-002 | Preserve root discovery locations | Hosts and standards require them | Move everything for symmetry | review decision | T1, T2, T4–T6 |
| D-003 | Keep `scripts/plan.py` and `scripts/check.py` fixed | They are repository control entry points, not command shims | Move every script under a subdirectory | approved Option 2 refinement | T1, T4 |
| D-004 | Preserve the tracked VSIX during this restructuring | Artifact deletion changes release policy | Stop tracking it during the move | review non-goal | T1, T4 |
| D-005 | Keep historical records accurate and classify old literals | Blind replacement would rewrite history | Replace every old string | request; bug lessons 001/002/005 | T2, T5 |

## 6. Requirements and Acceptance

| ID | Requirement | Source | Priority | Owner Task | Task(s) | Proof(s) |
| --- | --- | --- | --- | --- | --- | --- |
| REQ-001 | ADR 0005 records the approved target, fixed-root exceptions, compatibility position, and confirmation gates before any move | request | Must | T1 | T1 | PV-T1-001 |
| REQ-002 | A durable inventory classifies every tracked move source and every active, managed, generated, or historical consumer with zero unclassified entries | request | Must | T2 | T2 | PV-T2-001 |
| REQ-003 | `src/`, `tests/`, package metadata, control scripts, and required discovery roots remain at their approved locations; the format-3 bridge remains byte-identical with its exact Ruff exclusion | review decision; bridge contract | Must | T4 | T4, T6 | PV-T4-001, PV-T6-001 |
| REQ-004 | VS Code and Kate assets live under `editors/` and retain build/install behavior | review decision | Must | T4 | T4, T6 | PV-T4-001, PV-T4-002, PV-T6-001 |
| REQ-005 | Agent hook and MCP assets live under `integrations/` while root discovery configs resolve to them | review decision | Must | T4 | T4, T6 | PV-T4-001, PV-T4-002, PV-T6-001 |
| REQ-006 | Source-tree shims, installers, policy hooks, and smoke utilities occupy the Appendix A script roles while `scripts/plan.py` and `scripts/check.py` remain fixed | review decision | Must | T4 | T4, T6 | PV-T4-001, PV-T4-002, PV-T6-001 |
| REQ-007 | Root `examples/` is the canonical source for Markdown, runner, and standalone examples; registries and docs resolve to it | review decision | Must | T4 | T4, T5, T6 | PV-T4-002, PV-T5-001, PV-T6-001 |
| REQ-008 | User docs are flattened into the Appendix A purpose-based taxonomy; fixed project-lifecycle doc roots stay fixed | review decision | Must | T5 | T5, T6, T7 | PV-T5-001, PV-T6-001, PV-T7-001 |
| REQ-009 | No unclassified active old-prefix reference remains after migration | request | Must | T6 | T2, T4, T5, T6, T7 | PV-T2-001, PV-T4-001, PV-T5-001, PV-T6-001, PV-T7-001 |
| REQ-010 | Public CLI behavior, APSEUDO policy, LSP, MCP URIs, hook decisions, runner behavior, pre-commit, CI configuration, and editor features are preserved | repository evidence | Must | T6 | T3, T4, T5, T6, T7 | PV-T3-001, PV-T4-002, PV-T5-001, PV-T6-001, PV-T7-001 |
| REQ-011 | Generated grammars and the tracked VSIX are rebuilt or independently verified at their new editor path | review decision | Should | T4 | T4, T6 | PV-T4-002, PV-T6-001 |
| REQ-012 | Standards-managed changes are made through configuration and reconciliation without unmanaged digest drift | repository standards contract | Must | T5 | T4, T5, T6 | PV-T4-002, PV-T5-002, PV-T6-001 |
| REQ-013 | Bugs 001 and 002 are regression-tested and closed against final paths; bug 005's whole-repository path-consumer lesson is applied | bug records | Must | T5 | T3, T5, T6, T7 | PV-T3-001, PV-T5-001, PV-T6-001, PV-T7-001 |
| REQ-014 | Final reporting separates changed-surface success from the inherited coverage/check.yml failure and proves coverage did not regress | repository state | Must | T6 | T3, T6 | PV-T3-002, PV-T6-001 |
| REQ-015 | Git moves preserve tracked contents and executable modes, and no tracked artifact is silently dropped | request | Must | T6 | T2, T4, T6 | PV-T2-001, PV-T4-001, PV-T6-001 |

## 7. Verification and Evidence Strategy

### 7.1 Commands and Layers

- **Tree and path contract:** `git ls-files`, `git ls-files -s`, targeted `git grep -I`, link validation, and a line-level historical allowlist.
- **Python behavior:** targeted MCP/review/hook/runner tests, `uv run pytest`, Ruff, BasedPyright, pip-audit, wheel build/install smoke, and coverage comparison.
- **Agent Pseudocode:** run the relocated formatter check before the relocated linter, plus runner `--check`, `--render-prompt`, and `--print-command` for moved executable examples.
- **Editors:** VS Code grammar build/check/package and Kate asset/install-source inspection.
- **Configuration and standards:** JSON/JSONC/TOML parsing, pre-commit, `project-standards reconcile`, frontmatter validation, handoff validation, and drift check.
- **Documentation:** Prettier/markdownlint fix and check passes, frontmatter, local-link/reference checks, canonical CLI-doc comparison, and stale-path scan.

### 7.2 Oracle and Negative-Control Policy

- The pre-move `git ls-files`/mode inventory and T3 behavior tests are independent preservation oracles.
- The ADR and Appendix A mappings are the target-location oracle.
- A temporary injected old-prefix reference must be detected by the inventory and final stale-path procedure; this rejects a hollow allowlist that silently ignores new stale consumers.
- MCP tests assert resource contents, not merely a successful JSON-RPC response.
- Project-review tests assert every required completeness row is `OK`, not merely the command's current zero exit status.
- Editor acceptance rebuilds generated artifacts from source and compares tracked output rather than trusting file presence.
- Coverage is compared to the captured T3 baseline; the existing 85% threshold is not weakened or falsely reported green.

### 7.3 Environments and Evidence

| Environment | Purpose | Prerequisites | Version / Provenance | Durable Evidence |
| --- | --- | --- | --- | --- |
| Local Fedora checkout | Inventory, behavior, docs, standards, and integration gates | Clean task-owned baseline; existing `uv` and npm dependencies | Commit and tool versions recorded by task | EV-001, EV-002 |
| GitHub Actions definitions | Path filters and command parity inspection | No push required | Workflow files at final commit | EV-002 |
| VS Code extension package directory | Grammar/build/package verification | Existing npm lock and local Node toolchain | Node/npm/vsce versions recorded | EV-002 |

Repeatable task command output remains ephemeral. The frozen inventory and final verification summary are durable because they define migration completeness and the inherited-gate boundary.

### 7.4 Failure Triage

A verification task never implements fixes. It blocks, records evidence, appends a correction task with `corrects` and `discovered_from`, waits for correction completion, then reruns from its anchor. A newly discovered path consumer before T4 is appended to EV-001; after T4 it creates correction work and cannot be hidden by expanding the historical allowlist without evidence and owner review.

## 8. Execution Summary

| Task | Title | Disposition | Work Type | Phase | Depends On | Requirement(s) | Primary Proof | Parallel / Conflict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | Record ADR 0005 | active | documentation | P1 | None | REQ-001 | PV-T1-001 | no / ADR index |
| T2 | Freeze the path-impact inventory | active | documentation | P1 | T1 | REQ-002, REQ-009, REQ-015 | PV-T2-001 | no / inventory authority |
| T3 | Establish a correct path-sensitive baseline | active | brownfield-behavior | P1 | T2 | REQ-010, REQ-013, REQ-014 | PV-T3-001 | no / shared final path owners |
| T4 | Apply the atomic non-document layout transition | active | transition | P2 | T3 | REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-009, REQ-010, REQ-011, REQ-012, REQ-015 | PV-T4-001 | no / broad path writes |
| T5 | Apply the documentation taxonomy and owner reconciliation | active | documentation | P2 | T3, T4 | REQ-007, REQ-008, REQ-009, REQ-010, REQ-012, REQ-013 | PV-T5-001 | no / owns shared docs and final path tables |
| T6 | Verify the integrated repository and capture evidence | active | verification | P3 | T5 | REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, REQ-013, REQ-014, REQ-015 | PV-T6-001 | no / verification-only |
| T7 | Correct the generated task-document default | active | brownfield-behavior | P4 | T4 | REQ-008, REQ-009, REQ-010, REQ-013 | PV-T7-001 | no / T5 generated-doc contract |

## 9. Implementation Tasks

### Phase P1: Decision, inventory, and pre-move baseline

#### T1: Record ADR 0005

- **disposition:** active
- **outcome:** ADR 0005 records the approved Option 2 target, exceptions, migration boundary, compatibility position, and confirmation gates.
- **work_type:** documentation
- **checkpoint:** one green documentation commit with required `Plan-*` trailers
- **boundary:** cross-task
- **depends_on:** []
- **dependency_reason:** none
- **requirements:** [REQ-001]
- **proof:** [PV-T1-001]
- **source_refs:** [request, repo:docs/reviews/repo-structure-review.md#decision, repo:docs/adr/adr.template.md]
- **consumes:** [approved Option 2 decision, repository ADR template]
- **produces:** [ADR-0005 repository-layout decision contract]
- **preserves:** [accepted ADR history, fixed discovery-path requirements]
- **invariants:** [ADR precedes impact freeze and every physical move]
- **executor_discretion:** [concise prose and option-comparison wording within the approved decision]
- **files:** [`docs/adr/adr-0005-repository-structure-option-2.md` (create; owner T1), `docs/adr/README.md` (modify; owner T1)]
- **parallel_safe:** no
- **conflicts_with:** []
- **supersedes:** []
- **superseded_by:** []
- **evidence:** [ephemeral]
- **recovery:** remove the unaccepted draft and restore the ADR index; no move task becomes ready.
- **acceptance:** PV-T1-001 proves valid ADR metadata, exact accepted mappings/exceptions, an updated index, and repository documentation checks.
- **sub-tasks:**
  - **T1.1 INVENTORY** — inspect ADR numbering, template, accepted related decisions, and the selected review clauses.
  - **T1.2 UPDATE** — create ADR 0005 with status `active` and update the ADR index.
  - **T1.3 VERIFY REFERENCES** — validate metadata, links, numbering, and confirmation criteria.
  - **T1.4 Verify Task** — run PV-T1-001 and commit the checkpoint with required trailers.

#### T2: Freeze the path-impact inventory

- **disposition:** active
- **outcome:** a durable inventory accounts for every move source and consumer and proves zero unclassified entries before any physical move.
- **work_type:** documentation
- **checkpoint:** one green inventory commit with EV-001 and required `Plan-*` trailers
- **boundary:** cross-task
- **depends_on:** [T1]
- **dependency_reason:** consumes the accepted path and exception contract recorded by T1
- **requirements:** [REQ-002, REQ-009, REQ-015]
- **proof:** [PV-T2-001]
- **source_refs:** [request, repo:docs/reviews/repo-structure-review.md#recommended-path-mapping, repo:.standards/config.toml, repo:.github/workflows/apseudo-lint.yml]
- **consumes:** [ADR-0005 repository-layout decision contract, live tracked tree]
- **produces:** [PathImpactInventory-v1, historical-reference allowlist]
- **preserves:** [tracked file modes, standards ownership, historical accuracy]
- **invariants:** [T4 remains blocked unless the unclassified count is zero]
- **executor_discretion:** [inventory table grouping and read-only helper commands]
- **files:** [`docs/reviews/repo-structure-impact-inventory.md` (create evidence; owner T2)]
- **parallel_safe:** no
- **conflicts_with:** []
- **supersedes:** []
- **superseded_by:** []
- **evidence:** [EV-001]
- **recovery:** discard an incomplete inventory and rerun from the unchanged Git tree; do not waive unknown entries.
- **acceptance:** PV-T2-001 proves the inventory covers all 75 initially observed move-root files, all 70 initially observed direct-reference files, relative links within moved documents, modes, generated/managed assets, and any additional live findings with zero unclassified rows.
- **sub-tasks:**
  - **T2.1 INVENTORY** — enumerate tracked sources, modes, symlinks, direct/relative consumers, generated outputs, managed spans, tests, configs, and historical candidates.
  - **T2.2 UPDATE** — classify each row by target, owner task, action, proof, and historical/active disposition in EV-001.
  - **T2.3 VERIFY REFERENCES** — reconcile independent `git ls-files`, `git grep`, Markdown-link, config, and executable-path scans; run the injected-old-path negative control.
  - **T2.4 Verify Task** — confirm zero unclassified entries, run PV-T2-001, and commit EV-001 with required trailers.

#### T3: Establish a correct path-sensitive baseline

- **disposition:** active
- **outcome:** MCP resources and project completeness checks resolve the current real files, regressions are behaviorally pinned, and the pre-move coverage/gate baseline is recorded.
- **work_type:** brownfield-behavior
- **checkpoint:** one green behavior checkpoint with required `Plan-*` trailers
- **boundary:** cross-task
- **depends_on:** [T2]
- **dependency_reason:** consumes EV-001 so regression coverage includes every path-sensitive Python owner discovered before moves
- **requirements:** [REQ-010, REQ-013, REQ-014]
- **proof:** [PV-T3-001, PV-T3-002]
- **source_refs:** [repo:src/apseudo_lint/mcp.py::APseudoMCPServer._read_resource, repo:src/apseudo_lint/review.py::review_project, repo:tests/test_mcp_review_hooks.py::test_review_project_reports_expected_tooling, repo:docs/handoff/bugs/001-mcp-resource-map-stale-paths.md#cause, repo:docs/handoff/bugs/002-review-completeness-stale-paths.md#cause]
- **consumes:** [PathImpactInventory-v1, current MCP URI and review-check interfaces]
- **produces:** [path-sensitive regression contract, pre-move gate and coverage baseline]
- **preserves:** [MCP URI names, review areas, CLI behavior, existing APSEUDO diagnostics]
- **invariants:** [tests assert returned content and every required review row, not exit status alone]
- **executor_discretion:** [test fixture decomposition and private assertion helpers]
- **files:** [`src/apseudo_lint/mcp.py` (modify; owner T3), `src/apseudo_lint/review.py` (modify; owner T3), `tests/test_mcp_review_hooks.py` (modify; owner T3), `.project-pipeline/2026-08-02-repository-structure-option-2/execution/logs/T3/` (ephemeral; owner T3)]
- **parallel_safe:** no
- **conflicts_with:** []
- **supersedes:** []
- **superseded_by:** []
- **evidence:** [ephemeral]
- **recovery:** revert source/test changes to the T2 checkpoint; retain observed baseline output only in ephemeral logs.
- **acceptance:** PV-T3-001 proves real MCP contents and all current completeness rows; PV-T3-002 records the exact full-gate/coverage baseline without presenting inherited failures as success.
- **sub-tasks:**
  - **T3.0 CHARACTERIZE** — capture current MCP not-found results, review `MISSING` rows, targeted tests, full gate stopping point, and coverage percentage.
  - **T3.1 Verify Baseline** — confirm failures match bugs 001/002 and inherited coverage status rather than load/configuration errors.
  - **T3.2 RED** — add content-level MCP and all-rows-OK review tests; expected failures are the stale current paths.
  - **T3.3 Verify RED** — run the targeted tests and confirm the intended stale-path failures.
  - **T3.4 GREEN** — repoint current MCP/review owners to real pre-move files without changing public identifiers.
  - **T3.5 Verify GREEN** — run targeted tests and nearest MCP/review/hook regressions.
  - **T3.6 REFACTOR** — consolidate only test helpers needed for path-contract clarity; assess and record none if unnecessary.
  - **T3.7 Verify Task** — run PV-T3-001/PV-T3-002 and commit with required trailers.

### Phase P2: Atomic layout and documentation transition

#### T4: Apply the atomic non-document layout transition

- **disposition:** active
- **outcome:** editor, integration, script, and example assets occupy their Appendix A targets and every executable/configuration consumer uses the new locations.
- **work_type:** transition
- **checkpoint:** one green structural checkpoint with required `Plan-*` trailers
- **boundary:** public
- **depends_on:** [T3]
- **dependency_reason:** consumes the accepted ADR, frozen impact inventory, and green path-sensitive baseline
- **requirements:** [REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-009, REQ-010, REQ-011, REQ-012, REQ-015]
- **proof:** [PV-T4-001, PV-T4-002]
- **source_refs:** [repo:docs/reviews/repo-structure-review.md#recommended-path-mapping, repo:pyproject.toml, repo:.standards/config.toml, repo:.github/workflows/apseudo-lint.yml, repo:src/apseudo_lint/review.py::review_project, repo:tests/test_mcp_review_hooks.py::test_review_project_reports_expected_tooling]
- **consumes:** [ADR-0005 decision, PathImpactInventory-v1, path-sensitive regression contract]
- **produces:** [LayoutMap-v1, updated active executable/config consumers]
- **preserves:** [public identifiers, required roots, file contents/modes, generated-source ownership, hook bypass protections]
- **invariants:** [all moves use inventory targets; no old directory is retained as an unapproved compatibility shim]
- **executor_discretion:** [mechanical Git move ordering inside one task and private installer helper adjustments]
- **files:** [`products/**` (move to `editors/**`; owner T4), `integrations/agent-hooks/**` (move to `integrations/agents/**`; owner T4), `hooks/**` (move into `integrations/agents/**`; owner T4), `mcp/**` (move to `integrations/mcp/**`; owner T4), `scripts/**` except `scripts/plan.py` and `scripts/check.py` (move/modify; owner T4), `docs/apseudo-docs/examples/**` and `products/kate-integration/examples/**` (move/deduplicate into `examples/**`; owner T4), `.agents/**` and `.claude/**` (modify deployed references only; owner T4), `.codex/config.toml` and `.mcp.json` (modify; owner T4), `.github/workflows/**` and `.pre-commit-config.yaml` (modify; owner T4), `.standards/config.toml` and `.prettierignore` (configure; owner T5), `src/apseudo_lint/review.py` and `tests/test_mcp_review_hooks.py` (modify; owner T3), `AGENTS.md` (modify active non-doc path references; owner T4), `CLAUDE.md` (modify active non-doc path references; owner T4), `README.md` (modify active non-doc path references; owner T5), `docs/**/*.md` (modify active non-doc path references; owner T5)]
- **parallel_safe:** no
- **conflicts_with:** [T5]
- **supersedes:** []
- **superseded_by:** []
- **evidence:** [ephemeral]
- **recovery:** restore the T3 checkpoint if any prefix cannot reach a green integrated state; do not checkpoint a partial layout or leave old/new duplicate roots.
- **acceptance:** PV-T4-001 proves exact trees, modes, fixed roots, and classified old references; PV-T4-002 proves Python, hook, MCP, runner, pre-commit, CI-config, editor-build, installer, and generated-artifact behavior from new paths.
- **sub-tasks:**
  - **T4.1 PRECHECK** — revalidate T1–T3 checkpoints, zero-unclassified EV-001, clean task-owned diff, target-path absence, and current file hashes/modes.
  - **T4.2 APPLY** — perform inventory-governed Git moves and update every active executable/configuration consumer, deployed reference, and standards configuration.
  - **T4.3 VERIFY** — prove LayoutMap-v1, active-reference convergence, behavior regressions, editor builds, example runner checks, managed reconciliation, and generated artifact parity.
  - **T4.4 Verify Task** — run PV-T4-001/PV-T4-002 and commit one atomic structural checkpoint with required trailers.

#### T5: Apply the documentation taxonomy and owner reconciliation

- **disposition:** active
- **outcome:** user documentation follows DocumentationMap-v1, active navigation and owner truth use final paths, duplicate CLI usage is reconciled, and path bugs close against the final tree.
- **work_type:** documentation
- **checkpoint:** one green documentation/reconciliation checkpoint with required `Plan-*` trailers
- **boundary:** cross-task
- **depends_on:** [T3, T4]
- **dependency_reason:** consumes T3's path-sensitive regression contract and T4's LayoutMap-v1 so documentation can move directly to final paths without transitional links
- **requirements:** [REQ-007, REQ-008, REQ-009, REQ-010, REQ-012, REQ-013]
- **proof:** [PV-T5-001, PV-T5-002]
- **source_refs:** [repo:docs/reviews/repo-structure-review.md#decision, repo:docs/README.md#layout, repo:docs/handoff/architecture.md#components, repo:docs/handoff/bugs/001-mcp-resource-map-stale-paths.md#cause, repo:docs/handoff/bugs/002-review-completeness-stale-paths.md#cause, repo:.standards/config.toml]
- **consumes:** [path-sensitive regression contract, LayoutMap-v1, DocumentationMap-v1, PathImpactInventory-v1, canonical `docs/usage.md`]
- **produces:** [RepositoryLayout-v1, final owner/path table, fixed bug records and indexes]
- **preserves:** [frontmatter IDs, normative reference ownership, historical records, standards-owned spans]
- **invariants:** [fixed `docs/adr`, `docs/handoff`, `docs/plans`, `docs/research`, `docs/reviews`, and `docs/specs` owners remain; old CLI usage is not deleted until unique accurate content is accounted for]
- **executor_discretion:** [local prose edits and index grouping within DocumentationMap-v1]
- **files:** [`docs/apseudo-docs/**` (move/merge/delete according to Appendix A; owner T5), `docs/**/*.md` (modify active navigation and owner truth; owner T5), `README.md` (modify; owner T5), `src/apseudo_lint/mcp.py` (final path update; owner T3), `src/apseudo_lint/review.py` (final path update; owner T3), `tests/test_mcp_review_hooks.py` (final path update; owner T3), `.standards/config.toml` (configure; owner T5)]
- **parallel_safe:** no
- **conflicts_with:** [T4]
- **supersedes:** []
- **superseded_by:** []
- **evidence:** [ephemeral]
- **recovery:** restore the T4 checkpoint if link/frontmatter/reconcile checks cannot reach green; do not retain a half-classified docs tree.
- **acceptance:** PV-T5-001 proves every DocumentationMap-v1 source reaches one target or approved merge/retirement and all active links/resources resolve; PV-T5-002 proves standards reconciliation, frontmatter, Markdown, handoff, bug, and owner-truth conformance.
- **sub-tasks:**
  - **T5.1 INVENTORY** — compare every source document to DocumentationMap-v1, classify unique content in the duplicate CLI page, and recheck managed/historical ownership.
  - **T5.2 UPDATE** — move/merge docs, update active links/frontmatter/owner truth, finalize MCP/review paths, close bugs 001/002, and reconcile standards-managed outputs.
  - **T5.3 VERIFY REFERENCES** — run documentation, MCP resource, review completeness, historical allowlist, frontmatter, standards, and handoff checks.
  - **T5.4 Verify Task** — run PV-T5-001/PV-T5-002 and commit the checkpoint with required trailers.

### Phase P3: Integrated acceptance

#### T6: Verify the integrated repository and capture evidence

- **disposition:** active
- **outcome:** an independent final pass proves the complete target layout and preserved behavior and records the inherited coverage/hosted-CI boundary without implementing fixes.
- **work_type:** verification
- **checkpoint:** one durable acceptance-evidence commit with required `Plan-*` trailers
- **boundary:** public
- **depends_on:** [T5]
- **dependency_reason:** verifies the complete ADR, inventory, baseline, structural, and documentation outputs from T1–T5
- **requirements:** [REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, REQ-013, REQ-014, REQ-015]
- **proof:** [PV-T6-001]
- **source_refs:** [request, repo:docs/reviews/repo-structure-review.md#decision, repo:pyproject.toml, repo:.github/workflows/apseudo-lint.yml, repo:scripts/plan.py::main]
- **consumes:** [ADR-0005, EV-001, RepositoryLayout-v1, T3 baseline, all task proofs]
- **produces:** [EV-002 final repository-structure verification record]
- **preserves:** [fixed acceptance thresholds, verification-only boundary, unrelated coverage work]
- **invariants:** [no fixes or allowlist expansion occur inside T6; failures append correction tasks]
- **executor_discretion:** [sanitized evidence formatting and command-log summarization]
- **files:** [`docs/reviews/repo-structure-verification.md` (create evidence; owner T6), `.project-pipeline/2026-08-02-repository-structure-option-2/execution/logs/T6/` (ephemeral; owner T6)]
- **parallel_safe:** no
- **conflicts_with:** []
- **supersedes:** []
- **superseded_by:** []
- **evidence:** [EV-002]
- **recovery:** block on any unexpected failure, append a correction task, and rerun from the anchored final checkpoint; never repair inside verification.
- **acceptance:** PV-T6-001 reconciles every Must/Should requirement, proves exact final paths and behavior, confirms no coverage regression from T3, and records inherited hosted-CI status separately.
- **sub-tasks:**
  - **T6.1 ANCHOR** — record T1–T5 checkpoints, EV-001 hash, final tree hash inputs, tool versions, and T3 baseline.
  - **T6.2 VERIFY PREREQUISITES** — confirm required local tools, fixed discovery roots, clean task-owned state, and complete proof inputs.
  - **T6.3 RUN** — execute the full Appendix B matrix without changing implementation, thresholds, or allowlists.
  - **T6.4 TRIAGE** — classify failures as correction work, inherited coverage status, or unavailable external acceptance; do not fix here.
  - **T6.5 RERUN** — rerun the complete affected matrix after any correction or record why no rerun is required.
  - **T6.6 CAPTURE EVIDENCE** — commit sanitized EV-002 and the final checkpoint with required trailers.

### Phase P4: Bounded correction work

#### T7: Correct the generated task-document default

- **disposition:** active
- **outcome:** `apseudo docs generate` writes to DocumentationMap-v1's canonical task-document path by default while preserving explicit `--output` behavior.
- **work_type:** brownfield-behavior
- **checkpoint:** one green corrective behavior checkpoint with required `Plan-*` trailers
- **boundary:** public
- **depends_on:** [T4]
- **dependency_reason:** consumes LayoutMap-v1 and the final example registry while unblocking T5's DocumentationMap-v1 acceptance
- **requirements:** [REQ-008, REQ-009, REQ-010, REQ-013]
- **proof:** [PV-T7-001]
- **source_refs:** [repo:docs/reviews/repo-structure-review.md#recommended-path-mapping, repo:src/apseudo_lint/main_cli.py::_docs, repo:tests/test_runner_operational.py::test_unified_cli_doctor_and_registry_docs]
- **consumes:** [LayoutMap-v1, DocumentationMap-v1, `.apseudo/scripts.toml` registry]
- **produces:** [path-sensitive default-output regression]
- **preserves:** [explicit `--output` behavior, generated document content, command name, exit statuses]
- **invariants:** [default generation does not recreate an unowned `docs/usage/` subtree]
- **executor_discretion:** [focused test decomposition only]
- **files:** [`src/apseudo_lint/main_cli.py` (modify; owner T7), `tests/test_runner_operational.py` (modify; owner T7), `.project-pipeline/2026-08-02-repository-structure-option-2/execution/logs/T7/` (ephemeral; owner T7)]
- **parallel_safe:** no
- **conflicts_with:** []
- **corrects:** [T5]
- **discovered_from:** [T5]
- **supersedes:** []
- **superseded_by:** []
- **evidence:** [ephemeral]
- **recovery:** restore the T4 checkpoint versions of the two owned files; T5 remains blocked until this correction passes.
- **acceptance:** PV-T7-001 proves default generation uses `docs/how-to/agent-tasks.md`, explicit output still works, content remains registry-derived, and focused/full regressions pass.
- **sub-tasks:**
  - **T7.0 CHARACTERIZE** — record the current default path and explicit-output behavior.
  - **T7.1 Verify Baseline** — confirm the default contradicts DocumentationMap-v1 while explicit output remains correct.
  - **T7.2 RED** — add a focused default-output test expecting the canonical final path.
  - **T7.3 Verify RED** — run the focused test and confirm only the stale default-path assertion fails.
  - **T7.4 GREEN** — repoint the default to `docs/how-to/agent-tasks.md` without changing explicit output.
  - **T7.5 Verify GREEN** — run focused and nearest CLI/runner regressions.
  - **T7.6 REFACTOR** — assess whether test consolidation is needed and record none if unnecessary.
  - **T7.7 Verify Task** — run PV-T7-001 and commit with required trailers.

## 10. Integration, Migration, and Recovery

### 10.1 Integration Sequence and Gates

1. T1 records the target decision; no other task can reinterpret Option 2.
2. T2 freezes EV-001 with zero unclassified rows; no physical move is ready before this gate.
3. T3 establishes a correct, behaviorally asserted path baseline and records the inherited full-gate state.
4. T4 performs one atomic non-document path transition and ends with executable, configuration, editor, and example consumers green.
5. T5 moves documentation directly to final categories and reconciles all active owner truth.
6. T6 independently accepts the integrated repository and captures EV-002.

### 10.2 Migration and Compatibility

- Old/new coexistence: none after each transition checkpoint; unapproved shims or duplicate roots are failures.
- Sequencing: ADR → inventory → baseline → non-doc transition → docs transition → verification.
- Idempotency: the final tree and zero-old-active-reference scans converge; reruns make no changes after format/reconcile outputs are current.
- Point of no return: none before task commits. Git checkpoints make all moves recoverable locally.
- Rollback: restore the preceding task checkpoint while preserving unrelated changes; never mix selective old/new roots.
- Forward repair: a post-checkpoint failure appends a correction task owning the missed consumer and reruns the blocked verification.

### 10.3 Rollout / Operational Authorization

No live deployment or external publication is in scope. Local task commits are execution checkpoints only. Push, branch promotion, release creation, PyPI, and VS Code Marketplace publication require separate authorization.

### 10.4 Late Failure and Correction Loop

T6 blocks and records the failed proof. Append the next permanent task ID with `corrects`, `discovered_from: [T6]`, the affected requirement/proof, and the same shared-file owner declared in this plan. Run `scripts/plan.py sync`, complete the correction checkpoint, and rerun T6 from ANCHOR. Completed task definitions remain immutable.

## 11. Risks, Assumptions, and Open Questions

### 11.1 Risks

| ID | Risk | Likelihood | Impact | Treatment / Contingency | Owner / Task |
| --- | --- | --- | --- | --- | --- |
| R-001 | A non-obvious path consumer is missed | high | high | Zero-unclassified EV-001, independent scans, injected stale-path negative control | T2/T6 |
| R-002 | Historical references are rewritten or active ones incorrectly allowlisted | medium | high | Line-level classification with source-role rationale and reviewer-visible diffs | T2/T5 |
| R-003 | Host discovery stops loading relocated integrations | medium | high | Preserve discovery roots; parse configs and execute hook/MCP integration proofs | T4 |
| R-004 | Script relocation breaks hooks, skills, or pre-commit | high | high | Treat all discovered callers as one atomic T4 transition; no compatibility shims | T4 |
| R-005 | Docs reclassification loses unique CLI guidance | medium | medium | Compare old page against canonical `docs/usage.md` before merge/retirement | T5 |
| R-006 | Generated VS Code files or VSIX become stale | medium | medium | Rebuild from source and compare/package at new root | T4/T6 |
| R-007 | Full verification is misreported because coverage is already below 85% | high | high | Capture T3 baseline, prove no regression, report inherited red separately | T3/T6 |
| R-008 | Managed payloads drift after direct path edits | medium | high | Configure then reconcile; validate digests and drift | T4/T5/T6 |

### 11.2 Assumptions

| ID | Assumption | Impact if False |
| --- | --- | --- |
| A-001 | The user-approved Option 2 includes the bounded refinements in D-003 and D-004 | Stop T1 and amend the ADR/plan if control scripts or VSIX policy must also change |
| A-002 | No external consumer requires old repository-relative paths as a stable API | A compatibility/redirect decision is required before T4 |
| A-003 | Current npm/uv dependencies are available locally for verification | T4/T6 block; do not weaken editor or Python acceptance |

### 11.3 Open Questions

None.

## 12. Final Verification

- Every Must/Should requirement maps to a completed task and passing Appendix B proof.
- The exact Appendix A target tree exists, all fixed roots remain, all old move roots are absent, and tracked modes/content reconcile to EV-001.
- The active old-prefix scan is empty after subtracting the reviewed line-level historical allowlist; the injected stale-path negative control is detected.
- Targeted and full Python tests, Ruff, BasedPyright, pip-audit, wheel/install CLI smoke, MCP resources, project review, hooks, runner, and pre-commit checks pass for the changed surface.
- APSEUDO format and lint gates pass from their new script locations; executable examples pass `--check`, `--render-prompt`, and `--print-command`.
- VS Code build/check/package and Kate asset/install-path checks pass from `editors/` and generated output is current.
- Prettier, markdownlint, frontmatter, documentation links/references, project-standards reconciliation/validation, Agent Handoff validation, and drift checks pass.
- Coverage is no lower than the T3 baseline. Any still-red 85%/hosted check is explicitly recorded as inherited, not as restructuring success.
- EV-001 and EV-002 exist, are sanitized, and are independently inspectable.
- No blocker, unapproved deviation, stale active owner claim, or orphan discovered item remains.

## 13. Close-out

- **Completed:** 2026-08-02; all seven tasks are terminal and the final Definition of Done passes against committed implementation.
- **Implementation and acceptance checkpoints:** T1 `de6cd14`, T2 `bf317b2`, T3 `b846e44`, T4 `a7a48bf`, T7 `2478dc3`, T5 `73861df`, and T6 `bdb4203`.
- **Decisions / deviations harvested:** T4 updated the component-built branch hook installer regression under existing REQ-011 authority. T5 discovered the generated task-document default mismatch; the user-approved scope override added T7, which corrected and pinned the default before T5 resumed. No acceptance target or approved layout was weakened.
- **Risks closed / accepted:** active path, behavior, mode, generated-artifact, standards, and documentation risks are closed. Coverage remains the inherited 62% against 85%; hosted CI is not run for the unpushed commits. A fresh npm install was externally unavailable, while T4's green editor proof and byte-identical generated/package artifacts remain current.
- **Deferred/discovered work filed:** no restructuring correction remains. Coverage, bug 004, NFR-004, and generated RULES ownership remain in their existing STATUS/TODO/spec/bug owners.
- **ADR/documentation/handoff reconciliation:** ADR 0005, final navigation, architecture/conventions, bugs 001/002, status, tasks, plan index, and the August session record reflect the accepted final tree.
- **Durable evidence verified:** EV-001 remains at `docs/reviews/repo-structure-impact-inventory.md`; EV-002 is `docs/reviews/repo-structure-verification.md` and records the final matrix.
- **Plan status/index:** master status is `complete`; the handoff plan index records completion.
- **Scratch teardown:** authorized only after this close-out commit is confirmed; durable ADR, plan, EV-001, EV-002, and checkpoint commits remain.

## Appendix A. Interface and State Contracts

### A.1 Prefix and Ownership Map

| Current | Target | Owner Task | Compatibility / Preservation |
| --- | --- | --- | --- |
| `products/vscode-extension/` | `editors/vscode/` | T4 | Preserve self-contained extension package and tracked VSIX |
| `products/kate-integration/` | `editors/kate/` | T4 | Preserve Kate definition/settings; canonical examples move separately |
| `integrations/agent-hooks/` | `integrations/agents/` | T4 | Preserve executable mode and hook semantics |
| `hooks/.claude/` | `integrations/agents/claude/` | T4 | Remains dormant/example configuration, outside discovery |
| `hooks/.codex/` | `integrations/agents/codex/` | T4 | Remains dormant/example configuration, outside discovery |
| `mcp/` | `integrations/mcp/` | T4 | Root `.mcp.json` and `.codex/config.toml` stay fixed and point here |
| `scripts/apseudo-*` | `scripts/bin/apseudo-*` | T4 | Preserve command behavior and executable modes; update every caller |
| `scripts/install-*.sh` | `scripts/install/` | T4 | Preserve installer behavior; descriptive filenames stay stable |
| `scripts/branch-policy-hooks/` | `scripts/policy/hooks/` | T4 | Preserve hook modes and installer ownership |
| `scripts/install-branch-policy-hooks.sh` | `scripts/policy/install-hooks.sh` | T4 | Update ADR/docs/tests and installer references |
| `scripts/run-enforcement-smoke-test.sh` | `scripts/verify/enforcement-smoke-test.sh` | T4 | Update internal paths and CI/docs callers |
| `docs/apseudo-docs/examples/markdown-fence-demo.md` | `examples/markdown/markdown-fence-demo.md` | T4 | Preserve frontmatter/content and validate new docs-relative links |
| `docs/apseudo-docs/examples/runner/` | `examples/runner/` | T4 | Preserve executable modes and runner registry names |
| `docs/apseudo-docs/examples/{nested-decision,review-loop}.apseudo` | `examples/standalone/` | T4 | Preserve APSEUDO contents |
| duplicate Kate `review-loop.apseudo` | canonical `examples/standalone/review-loop.apseudo` | T4 | Remove duplicate only after byte equality is proved |
| `scripts/plan.py`, `scripts/check.py` | unchanged | authoring/T4 | Repository control entry points remain fixed; preserve the recorded plan bridge hash and exact Ruff exclusion |
| root discovery dot-directories/configs | unchanged | T4/T5 | Update owned path values only |

### A.2 DocumentationMap-v1

| Current Documentation Source | Target / Disposition | Owner |
| --- | --- | --- |
| `docs/apseudo-docs/enforcement/ENFORCEMENT-GUIDE.md` | `docs/how-to/enforcement/ENFORCEMENT-GUIDE.md` | T5 |
| `docs/apseudo-docs/enforcement/ENFORCEMENT.md` | `docs/reference/enforcement/ENFORCEMENT.md` | T5 |
| `docs/apseudo-docs/features/*.md` | `docs/reference/features/*.md` | T5 |
| `docs/apseudo-docs/roadmap/*.md` | `docs/roadmap/*.md` | T5 |
| `docs/apseudo-docs/usage/AGENT-INSTRUCTIONS-WORDING.md` | `docs/how-to/AGENT-INSTRUCTIONS-WORDING.md` | T5 |
| `docs/apseudo-docs/usage/IMPLEMENTATION-GUIDE.md` | `docs/how-to/IMPLEMENTATION-GUIDE.md` | T5 |
| `docs/apseudo-docs/usage/INSTALL.md` | `docs/how-to/INSTALL.md` | T5 |
| `docs/apseudo-docs/usage/{KATE,VSCODE}.md` | `docs/how-to/editors/{KATE,VSCODE}.md` | T5 |
| `docs/apseudo-docs/usage/REPOSITORY-LAYOUT.md` | `docs/explanation/REPOSITORY-LAYOUT.md` | T5 |
| `docs/apseudo-docs/usage/RUNNER-USAGE.md` | `docs/reference/cli/RUNNER-USAGE.md` | T5 |
| `docs/apseudo-docs/usage/TESTING.md` | `docs/how-to/TESTING.md` | T5 |
| `docs/apseudo-docs/usage/agent-tasks.md` | `docs/how-to/agent-tasks.md` | T5 |
| `docs/apseudo-docs/usage/usage.md` | Compare with canonical `docs/usage.md`; merge unique accurate content, then retire | T5 |
| `docs/apseudo-docs/usage/use-cases/AGENT-FEEDING-PATHS.md` | `docs/explanation/AGENT-FEEDING-PATHS.md` | T5 |
| `docs/apseudo-docs/usage/use-cases/CHOOSING-A-SURFACE.md` | `docs/explanation/CHOOSING-A-SURFACE.md` | T5 |
| `docs/apseudo-docs/usage/use-cases/COMMON-WORKFLOWS.md` | `docs/how-to/COMMON-WORKFLOWS.md` | T5 |
| `docs/apseudo-docs/usage/use-cases/EXAMPLE-CATALOG.md` | `docs/reference/EXAMPLE-CATALOG.md` | T5 |
| `docs/apseudo-docs/usage/use-cases/MENTAL-MODEL.md` | `docs/explanation/MENTAL-MODEL.md` | T5 |
| `docs/apseudo-docs/usage/use-cases/REPOSITORY-OPERATING-MODEL.md` | `docs/explanation/REPOSITORY-OPERATING-MODEL.md` | T5 |
| `docs/apseudo-docs/usage/use-cases/RUNNER-WORKFLOWS.md` | `docs/how-to/RUNNER-WORKFLOWS.md` | T5 |
| `docs/apseudo-docs/usage/{README.md,use-cases/README.md}` | Merge navigation into `docs/README.md`; retire nested indexes | T5 |
| `docs/{adr,handoff,plans,reference/language,research,reviews,specs}/` | Fixed owner roots; only active links/metadata change | T5 |

### A.3 Historical Reference Contract

Potential historical literals are classified line-by-line in EV-001. Accepted ADRs, `CHANGELOG.md`, append-only handoff sessions, completed historical plans, bug cause sections, archived reviews, and `docs/reference/pre-migration/**` may retain old paths when the literal describes past state. Current indexes, instructions, configuration, code, tests, examples, runbooks, active references, and bug fix/status sections may not use the historical allowlist.

### A.4 Layout State Transitions

| State | Meaning | Entry Condition | Valid Transition | Invalid Transition Behavior | Recovery / Cleanup | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| inventoried | Target and every consumer classified | T1/T2 complete | baseline | Block T3+ on unknowns | Rerun T2 | T2 |
| baseline-green | Path behavior pinned and current bugs corrected | T3 proofs pass | non-doc-moved | No move from red baseline | Restore T2 checkpoint | T3 |
| non-doc-moved | LayoutMap-v1 applied | T4 proofs pass | docs-final | No partial old/new roots | Restore T3 checkpoint | T4 |
| docs-final | DocumentationMap-v1 applied | T5 proofs pass | verified | No unresolved active links | Restore T4 checkpoint | T5 |
| verified | Full acceptance captured | T6 proof and EV-002 pass | close-out | Correction task on failure | Rerun T6 after correction | T6 |

### A.5 Configuration Ownership

| Artifact | Format | Owned Span / Entry | Preserved Content | Atomicity / Conflict Rule | Owner Task |
| --- | --- | --- | --- | --- | --- |
| `.mcp.json` | JSON | Agent Pseudocode server command only | Other MCP servers | Parse before/after; command resolves new launcher | T4 |
| `.codex/config.toml` | TOML | Agent Pseudocode MCP command only | Other Codex config | Parse before/after; root file remains | T4 |
| `.standards/config.toml` | TOML | Move-root include/exclusion globs and the exact `scripts/plan.py` Ruff exclusion | Package selections and unrelated config | Configure, reconcile, validate; bridge exclusion remains singular | T4/T5 |
| `.pre-commit-config.yaml` | YAML | Local APSEUDO entries | Other hooks | All entries resolve and pre-commit passes | T4 |
| `.apseudo/scripts.toml` | TOML | `fix-ruff` and `review-spec` paths | Names, descriptions, defaults | Both scripts resolve and runner checks pass | T4 |
| root agent discovery files | host formats | Path values owned by Agent Pseudocode integration | Standards-managed handoff entries and unrelated config | Preserve discovery location and parse semantics | T4/T5 |

## Appendix B. Requirement-to-Proof Traceability

| Proof ID | Requirement(s) | Task | Method | Oracle | Command / Procedure | Expected Result | Negative Control | Environment | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PV-T1-001 | REQ-001 | T1 | documentation/ADR validation | Request, selected review decision, ADR template | Validate ADR/frontmatter/index and documentation gates | ADR 0005 is active, indexed, and contains exact target/exception/confirmation contracts | Omit a fixed-root exception in a temporary candidate; review must reject it | local | ephemeral |
| PV-T2-001 | REQ-002, REQ-009, REQ-015 | T2 | repository inventory and static inspection | Independent tracked-tree, mode, grep, link, config, and history views | Reconcile all inventory scans into EV-001 and assert zero unclassified rows | EV-001 accounts for every source and consumer with modes and zero unclassified rows | Inject a temporary old-prefix consumer; scan must report it as unclassified | local Git | EV-001 |
| PV-T3-001 | REQ-010, REQ-013 | T3 | regression/integration | Real document contents and required review areas | Targeted MCP resource and project-review tests plus nearest regressions | Every MCP URI returns expected content and every required review row is `OK` | Point a fixture/resource at a missing file; content/row assertions fail despite command exit | local Python | ephemeral |
| PV-T3-002 | REQ-014 | T3 | characterization | Current repository gate commands and coverage report | Run full gate to stopping point and record exact baseline percentage/failure | Exact baseline percentage and inherited stopping failure are recorded without a green claim | A fabricated green summary disagrees with captured command exit/output | local Python | ephemeral |
| PV-T4-001 | REQ-003, REQ-004, REQ-005, REQ-006, REQ-009, REQ-015 | T4 | filesystem/contract inspection | ADR 0005, EV-001 hashes/modes, Appendix A | Compare final non-doc tree, fixed roots, modes, and active prefix scan to contracts | Final non-doc tree matches the mapping, fixed roots remain, modes match, and no active old prefix remains | Restore one old-root sentinel or drop executable mode; proof fails | local Git/filesystem | ephemeral |
| PV-T4-002 | REQ-004, REQ-005, REQ-006, REQ-007, REQ-010, REQ-011, REQ-012 | T4 | integration/build/configuration | T3 regressions, package manifests, host configs, runner examples | Run targeted Python/hooks/MCP/runner/pre-commit/CI-config/editor/install/reconcile checks | New paths execute, generated outputs are current, and public identifiers are unchanged | Substitute one old command path in a temporary config; parse may pass but execution/path proof fails | local Python/Node | ephemeral |
| PV-T5-001 | REQ-007, REQ-008, REQ-009, REQ-010, REQ-013 | T5 | documentation/reference and integration | DocumentationMap-v1, canonical docs, MCP/review content tests | Verify source-to-target accounting, links, resources, review rows, bug status, and old-path allowlist | Every document is accounted for, active links/resources resolve, review rows pass, and bug/index truth is current | Add a current Markdown link to an old root; reference scan fails | local | ephemeral |
| PV-T5-002 | REQ-012 | T5 | configuration/documentation validation | Project Standards lock/config and frontmatter schema | Reconcile, validate, run Markdown/frontmatter/handoff/drift gates, then prove no-op convergence | Managed outputs converge, metadata and documentation gates pass, and drift is absent | Rerun reconciliation after a managed-path drift canary; check must detect or repair it | local standards tooling | ephemeral |
| PV-T6-001 | REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, REQ-013, REQ-014, REQ-015 | T6 | integration verification | All task proofs, ADR, EV-001, T3 baseline, repository-native gates | Run §12 matrix and capture EV-002 without edits | All requirements pass, coverage does not regress, and inherited hosted status is reported separately | Injected stale path, missing example, missing review row, mode loss, or coverage regression prevents acceptance | local Python/Node/Git | EV-002 |
| PV-T7-001 | REQ-008, REQ-009, REQ-010, REQ-013 | T7 | regression/integration | DocumentationMap-v1, registry fixture, current explicit-output test | Assert default and explicit-output destinations plus generated registry content; run focused/full regressions | Default output is `docs/how-to/agent-tasks.md`, explicit output is unchanged, and no stale docs owner is recreated | Restore the old `docs/usage/agent-tasks.md` default; focused regression fails | local Python | ephemeral |

## Appendix C. Durable Evidence

| Evidence ID | Producing Task | Path | Contents / Provenance | Privacy Exclusions | Retention Reason |
| --- | --- | --- | --- | --- | --- |
| EV-001 | T2 | `docs/reviews/repo-structure-impact-inventory.md` | Tracked move sources, modes, consumers, mappings, owners, generated/managed classification, and historical allowlist at the T2 commit | No home paths beyond repository-relative paths; no full private config or secrets | Proves the pre-move completeness gate and explains every migration edit |
| EV-002 | T6 | `docs/reviews/repo-structure-verification.md` | Final commit, tool versions, proof summary, exact final path checks, coverage comparison, and inherited hosted-CI statement | No credentials, unbounded logs, or workstation-specific private state | Supports independent acceptance and later path-regression diagnosis |

## Appendix D. Deferred Work

| Item | Reason Deferred | Source / Scope Relationship | Follow-up / Reopen Trigger |
| --- | --- | --- | --- |
| Rename distribution/import package | Breaking identity change unrelated to layout | Review finding, explicitly out of scope | Separate design/ADR request |
| Stop tracking VSIX | Changes release/delivery policy | Review recommendation was nonbinding | Separate release-policy decision |
| Deduplicate host skills through generation | Requires canonical-source/deployment design | Option 2 keeps discovery copies | Evidence of drift or explicit design request |
| Raise coverage to 85% | Existing independent workstream | Session state and check.yml | Continue current coverage plan |
| Fix LSP malformed-message bug 004 | Runtime behavior unrelated to paths | Existing bug record | Separate implementation task |
| Repair plan-authoring 3.3.0 package-contract fixture commit hashes | The failure is in the installed upstream skill's evaluation provenance, not this repository's byte-identical bridge behavior | Authoring verification finding; outside repository restructuring | Repair and validate in the owning agent-configs repository before relying on its package self-test receipt |
