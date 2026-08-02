---
schema_version: '1.1'
id: 'adr-0004-agent-pseudocode-branch-integration-and-local-git-hook-policy'
title: 'ADR 0004: Branch Integration and Local Git Hook Policy'
description: 'Decision establishing the permanent dev branch and local safeguards for main promotion.'
doc_type: 'adr'
status: 'active'
created: '2026-08-01'
updated: '2026-08-01'
reviewed: '2026-08-01'
owner: 'agent-pseudocode-maintainers'
consumer: 'mix'
tags:
  - 'adr'
  - 'git'
  - 'branch-policy'
  - 'hooks'
aliases:
  - 'ADR 0004'
  - 'Branch integration policy'
related:
  - 'docs/how-to/enforcement/ENFORCEMENT-GUIDE.md'
  - 'docs/handoff/conventions.md'
  - 'scripts/policy/install-hooks.sh'
supersedes: []
superseded_by: null
source:
  - 'scripts/policy/hooks/pre-commit'
  - 'scripts/policy/hooks/pre-push'
  - 'tests/test_branch_policy_hooks.py'
confidence: 'high'
visibility: 'internal'
license: null
project:
  decision_makers: []
  consulted: []
  informed: []
---

# Branch Integration and Local Git Hook Policy

## Context and Problem Statement

This repository requires a durable distinction between ordinary development and release-ready history. The permanent `dev` branch serves as the development and integration branch; `main` represents work that has been completed, tested, reviewed, and approved for promotion.

The policy must be persistent and mechanically verifiable without substituting automation for code review or owner authorization. Enforcement is intentionally local: this decision does not require pull requests, hosted branch-protection rules, or a new server-side control.

Each promotion sequence ends when its approved update to `main` has been pushed successfully. Release management, tagging, artifact publication, and deployment are outside this policy. They may evolve without changing this decision if they preserve the branch lifecycle and local safeguard invariants below.

## Decision Drivers

- Keep ordinary development off `main`.
- Make the permitted promotion relationship explicit and mechanically checkable.
- Preserve existing Git-hook behavior and configuration ownership.
- Allow downstream release and publication processes to evolve independently.
- Treat client hooks as mistake prevention rather than a security boundary.

## Considered Options

- Use a permanent `dev` branch with local commit and push safeguards.
- Permit ordinary development directly on `main` and rely on manual discipline.
- Require pull requests and hosted branch protection for every promotion.

## Decision Outcome

Chosen option: "Use a permanent `dev` branch with local commit and push safeguards." This option separates routine development from release-ready history while preserving a local-only workflow.

The resulting architecture has the following invariants:

- `dev` is the permanent development and integration branch. Ordinary commits and pushes occur there without additional branch-policy restrictions.
- `main` is the protected promotion branch. It advances only by fast-forward promotion from `dev` after the work is complete, tested, reviewed, and explicitly approved by the repository owner.
- A local commit safeguard prevents ordinary direct commits on `main`.
- A local push safeguard permits an update to `main` only when local `main` and `dev` identify the same commit. It also prevents deletion and history rewrites of `main`.
- Both safeguards provide an explicit emergency bypass, but bypass use is exceptional rather than part of the normal branch lifecycle.
- Existing Git hooks and configuration outside these safeguards retain their ownership and behavior.
- Additional branches or worktrees are exceptional and require a specific isolation need; they do not replace `dev` as the integration branch.

The safeguards are advisory client-side controls. They can be bypassed and therefore prevent routine mistakes rather than establish a security boundary. Code review and owner authorization remain independent prerequisites that the safeguards do not automate.

### Consequences

- Routine development has a durable integration branch and an explicit fast-forward promotion path.
- Local mistakes are detected before they create a direct `main` commit or publish an invalid promotion.
- Existing hook behavior and configuration ownership remain independent.
- Release, tagging, publication, and deployment processes can evolve without changing this decision.
- The controls are client-side and can be bypassed intentionally.

### Confirmation

Conformance is confirmed by the isolated hook tests and the operational linked-worktree check documented in the enforcement guide. Both must show the required branch relationship and preserve predecessor-hook execution.

## Pros and Cons of the Options

### Permanent `dev` branch with local safeguards

- Good, because it separates integration work from the reviewed promotion tip without requiring hosted controls.
- Good, because it blocks the common accidental `main` commit, deletion, and history-rewrite paths locally.
- Bad, because each clone needs the local hooks installed and a configured dispatcher must preserve access to them.

### Direct development on `main`

- Good, because it has no setup cost.
- Bad, because ordinary development and reviewed promotion history are indistinguishable.
- Bad, because mistakes rely entirely on manual discipline.

### Pull requests and hosted branch protection

- Good, because a remote can enforce policy for every client.
- Bad, because it adds a hosted workflow that this repository does not require for its local development model.

## More Information

Install, preserve, and verify the safeguards through [the enforcement guide](../how-to/enforcement/ENFORCEMENT-GUIDE.md#branch-integration-and-local-git-hook-safeguards). The standard promotion sequence is:

```bash
git switch main
git merge --ff-only dev
git push origin main
git switch dev
```
