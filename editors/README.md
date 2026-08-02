---
schema_version: '1.1'
id: 'index-8t70up-products-and-editor-integrations'
title: 'Products and Editor Integrations'
description: 'Index for product and editor integration assets in the agent-pseudocode repository.'
doc_type: 'index'
status: 'active'
created: '2026-07-08'
updated: '2026-07-09'
reviewed: null
owner: 'product-maintainers'
consumer: 'user'
tags:
  - 'product'
  - 'index'
  - 'editor-integration'
aliases: []
related: []
source: []
confidence: 'medium'
visibility: 'internal'
license: null
---

# Editor Integrations

This folder contains distributable editor integrations. Each editor keeps its manifest, source, build tooling, and local installation guidance together.

| Folder | Purpose |
| --- | --- |
| `editors/vscode/` | VS Code extension source: TextMate grammars, Markdown injection grammar, snippets, LSP client, and VSIX packaging scripts. |
| `editors/kate/` | Kate / KSyntaxHighlighting XML definition and Kate LSP client examples. |

Generated distribution artifacts such as `.vsix` packages are intentionally produced inside the relevant product folder during packaging and are not required for source development.
