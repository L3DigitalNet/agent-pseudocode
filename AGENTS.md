# Agent instructions

**Session state:** Agent Handoff SessionStart injects `docs/handoff/state.md`; do not reread it when injected.
**Full conventions reference:** `docs/handoff/conventions.md`.
**Detailed review workflows:** not configured for this repo.

## Repository purpose

This repository implements the Pythonic Agent Pseudocode convention and its tooling: syntax highlighting, formatter, validator, language server, MCP server, hooks, skills, CI, and documentation.

## Pythonic Agent Pseudocode requirements

Codex MUST use the repository Pythonic Agent Pseudocode tooling for any task involving agent workflows, process instructions, `.apseudo` files, `.agentpseudo` files, `.pseudocode` files, or Markdown `apseudo` fences.

Required behavior:

1. Use the `agent-pseudocode` skill when available.
2. Use the `agent_pseudocode` MCP server when available for validation, rule explanations, templates, and project review.
3. Run `scripts/bin/apseudo-template --list` before drafting a new workflow unless the user supplied a complete structure.
4. Run `scripts/bin/apseudo-format --check --changed` before `scripts/bin/apseudo-lint --changed`.
5. Do not finish while APSEUDO-\* errors remain.
6. Do not bypass `pre-commit`, CI, hooks, or validation.
7. If a rule appears inappropriate, surface the rule ID, rationale, and proposed standard change instead of suppressing it.

Completion statement requirement:

- If pseudocode files changed, report the formatter/linter status in the final response.

## Development commands

```bash
uv sync
uv run pytest
uv run apseudo-format --check .
uv run apseudo-lint .
uv run apseudo-review .
uv run ruff check src tests integrations/agents
uv run basedpyright
```

## Style

- Python 3.11+.
- Keep runtime dependencies minimal.
- Keep editor integrations thin; do not duplicate policy outside `src/apseudo_lint`.
- Keep examples deterministic and validation-friendly.

## Executable Agent Pseudocode runner

Use `apseudo-run` or `apseudo run` for executable `.apseudo` task scripts. Before trusting a new or edited runner script, run `uv run apseudo-run --check`, `--render-prompt`, and `--print-command`. Prefer `--run-dir .apseudo/runs` for auditable runs. Do not bypass runner post-checks, diff policy, hooks, pre-commit, or CI.

## Markdown and structured-text fix pass

The managed `markdown-tooling` block below states the policy. These are the commands.

When changing Markdown, JSON, JSONC, or YAML, run the fix pass first, then the non-mutating check:

```bash
npx prettier --write .
npx markdownlint-cli2 --fix "**/*.md"

npx prettier --check .
npx markdownlint-cli2 "**/*.md"
```

Do not claim completion if either check fails. Do not edit `.prettierrc.json` or `.markdownlint.json` to bypass a check without a documented ADR exception — both are package-managed, so reconciliation reverts hand edits anyway.

<!-- prettier-ignore-start -->

<!-- BEGIN project-standards:agent-handoff -->
<!-- markdownlint-disable MD025 -->
# Agent Handoff

Use the repo-local `agent-handoff` skill at session startup and closeout. Do not reread state already injected by SessionStart. Keep project knowledge inside this repository and store credential references only, never values.
<!-- markdownlint-enable MD025 -->
<!-- END project-standards:agent-handoff -->

<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->

<!-- BEGIN project-standards:markdown-tooling -->
<!-- markdownlint-disable MD025 -->
# Markdown and structured-text tooling

Prettier owns physical formatting and markdownlint owns Markdown structure. Do not add overlapping tools.

Enabled checks: format, lint.
Markdown scope: `**/*.md`.
Structured-config scope: `**/*.json`, `**/*.jsonc`, `**/*.yml`, `**/*.yaml`.
Lint additionally skips generated directories: `.pytest_cache/**`, `.ruff_cache/**`, `.venv/**`, `node_modules/**`.

Declared exclusions:
- `docs/reference/pre-migration/**` (both): Verbatim archived ChatGPT transcript; reformatting or annotating it would destroy the historical record. Already exempt from APSEUDO fence linting per bug 003.
- `package-lock.json` (format): npm regenerates this file and reverts Prettier's formatting on every install.
- `editors/vscode/**/*.js` (format): VS Code extension JavaScript follows its product-local formatting; root Prettier would rewrite unrelated source outside the declared Markdown and structured-config scope.
- `editors/vscode/**/*.mjs` (format): VS Code extension build scripts follow their product-local formatting; root Prettier would rewrite unrelated source outside the declared Markdown and structured-config scope.
- `editors/vscode/**/*.code-snippets` (format): VS Code snippet files preserve their product-local JSON formatting and are outside the declared structured-config extensions.
- `editors/vscode/syntaxes/*.tmLanguage.json` (format): VS Code grammar JSON is generated from YAML by the product-local compiler; root Prettier would create drift after every rebuild.

Check formatting over exactly that scope, with Git as the corpus authority:

```bash
git ls-files -z -- ':(glob)**/*.md' ':(glob)**/*.json' ':(glob)**/*.jsonc' ':(glob)**/*.yml' ':(glob)**/*.yaml' ':(glob,exclude)docs/reference/pre-migration/**' ':(glob,exclude)editors/vscode/**/*.code-snippets' ':(glob,exclude)editors/vscode/**/*.js' ':(glob,exclude)editors/vscode/**/*.mjs' ':(glob,exclude)editors/vscode/syntaxes/*.tmLanguage.json' ':(glob,exclude)package-lock.json' | xargs -0 -r npx prettier --check --
```

Without Git, bound the same scope by glob instead. Prettier's CLI has no negative pattern, so this form does not apply the declared format exclusions above; pass them through an `--ignore-path` file inside the repository:

```bash
npx prettier --check --no-error-on-unmatched-pattern -- '**/*.md' '**/*.json' '**/*.jsonc' '**/*.yml' '**/*.yaml'
```

Never check or write with a bare `.`: it reaches undeclared languages and Git-excluded scratch.

Lint Markdown structure over the same Git-tracked scope:

```bash
git ls-files -z -- ':(glob)**/*.md' ':(glob,exclude).pytest_cache/**' ':(glob,exclude).ruff_cache/**' ':(glob,exclude).venv/**' ':(glob,exclude)node_modules/**' ':(glob,exclude)docs/reference/pre-migration/**' | sed -z 's|^|:|' | xargs -0 -r npx markdownlint-cli2 --no-globs
```

Never lint a bare recursive glob: it descends into any independent Git repository checked out below this one.

Run the enabled checks before claiming completion.
<!-- markdownlint-enable MD025 -->
<!-- END project-standards:markdown-tooling -->

<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->

<!-- BEGIN project-standards:python-tooling -->
<!-- markdownlint-disable MD025 -->
# Python tooling

Use uv for environments and dependency changes. Ruff owns formatting, linting, and imports.
Use basedpyright in strict mode for type checking. Do not add a competing Python gate.

Run before claiming completion:

```bash
uv run ruff format --check src tests
uv run ruff check src tests
uv run basedpyright
uv run coverage run -m pytest
uv run coverage report
uv run pip-audit
```

When the gate reports formatting or lint findings, run:

```bash
uv run ruff format src tests
uv run ruff check src tests --fix
```
<!-- markdownlint-enable MD025 -->
<!-- END project-standards:python-tooling -->

<!-- prettier-ignore-end -->

<!-- prettier-ignore-start -->

<!-- BEGIN project-standards:markdown-frontmatter -->
<!-- markdownlint-disable MD025 -->
# Markdown Frontmatter

Managed Markdown in this repository carries YAML frontmatter under the Markdown Frontmatter Standard: the eleven required fields in canonical order, every scalar quoted, and an id of the form `{doc_type}-{6-char base36 token}-{slug}`.

Create a new managed document with `scripts/new-doc-id --scaffold --doc-type <type> <name>` from the repo-local skill at `.agents/skills/markdown-frontmatter/`. Read that skill's `SKILL.md` before hand-authoring or repairing a frontmatter block.

The gate is `project-standards validate`.

`AGENTS.md`, `CLAUDE.md`, and anything under `.agents/**`, `.claude/**`, or `.codex/**` never carry frontmatter.
<!-- markdownlint-enable MD025 -->
<!-- END project-standards:markdown-frontmatter -->

<!-- prettier-ignore-end -->
