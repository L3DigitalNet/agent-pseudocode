---
schema_version: '1.1'
id: 'runbook-1vj2iz-kate-integration'
title: 'Kate Integration'
description: 'User guide for configuring Kate with Pythonic Agent Pseudocode support.'
doc_type: 'runbook'
status: 'active'
created: '2026-07-08'
updated: '2026-07-09'
reviewed: null
owner: 'product-maintainers'
consumer: 'user'
tags:
  - 'runbook'
  - 'usage'
  - 'kate'
  - 'product'
aliases:
  - 'Kate integration'
related: []
source: []
confidence: 'medium'
visibility: 'internal'
license: null
---

# Kate Integration

## Files

- `editors/kate/agent-pseudocode.xml` — KSyntaxHighlighting XML definition.
- `editors/kate/lsp-client-settings.json` — standalone `.apseudo` LSP configuration.
- `editors/kate/lsp-client-settings.markdown-opt-in.json` — optional Markdown LSP configuration.

## Install highlighting

```bash
./scripts/install/install-kate-user.sh
```

This copies `editors/kate/agent-pseudocode.xml` to the user syntax-highlighting directory.

## Enable LSP

1. Enable Kate's LSP Client plugin.
2. Open LSP Client settings.
3. Paste `editors/kate/lsp-client-settings.json` into User Server Settings.
4. Replace `apseudo-lsp` with an absolute path to `scripts/bin/apseudo-lsp` if Kate cannot find the command.

## Supported LSP features

Kate's LSP Client can surface server-provided diagnostics, completion, hover, formatting, code actions, document symbols, folding, definition, and references depending on Kate version and plugin settings.

## Markdown

Use Markdown LSP opt-in only if you want diagnostics inside Markdown `apseudo` fences. Syntax highlighting for fenced blocks is handled primarily by the editor's Markdown support and the VS Code injection grammar; Kate's XML definition is focused on standalone pseudocode files.
