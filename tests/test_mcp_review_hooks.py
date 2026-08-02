from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from apseudo_lint.mcp import APseudoMCPServer
from apseudo_lint.review import review_project
from apseudo_lint.rules import get_rule

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_REVIEW_PATHS = {
    "Language convention": "docs/reference/PYTHONIC_PSEUDOCODE_STANDARD.md",
    "Token specification": "docs/reference/language/TOKEN-SPEC.md",
    "VS Code extension": "editors/vscode/package.json",
    "Kate syntax": "editors/kate/agent-pseudocode.xml",
    "Formatter": "src/apseudo_lint/formatting.py",
    "Validator": "src/apseudo_lint/lint.py",
    "Language server": "src/apseudo_lint/lsp.py",
    "MCP server": "src/apseudo_lint/mcp.py",
    "Executable runner": "src/apseudo_lint/runner.py",
    "Runner CLI": "src/apseudo_lint/runner_cli.py",
    "Claude hooks": ".claude/settings.json",
    "Codex hooks": ".codex/config.toml",
    "Claude skill": ".claude/skills/agent-pseudocode/SKILL.md",
    "Codex skill": ".agents/skills/agent-pseudocode/SKILL.md",
    "pre-commit": ".pre-commit-config.yaml",
    "CI": ".github/workflows/apseudo-lint.yml",
    "Agent wording": "docs/how-to/AGENT-INSTRUCTIONS-WORDING.md",
    "Traceability review": "docs/reviews/PROJECT-TRACEABILITY-REVIEW.md",
    "Executable runner spec": "docs/reference/EXECUTABLE-PSEUDOCODE-SPEC.md",
    "Runner usage": "docs/reference/cli/RUNNER-USAGE.md",
    "Future versions": "docs/roadmap/FUTURE-VERSIONS.md",
}


def test_rule_catalog_explains_known_rule() -> None:
    rule = get_rule("APSEUDO-WHILE-001")
    assert rule is not None
    assert "bounded" in rule.as_markdown().lower()


def test_mcp_initialize_and_validate_text() -> None:
    server = APseudoMCPServer(root=ROOT)
    init = server.handle_message({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
    assert init is not None
    assert init["result"]["serverInfo"]["name"] == "agent-pseudocode"

    response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "validate_text",
                "arguments": {"text": "process demo():\n    while ready:\n        do_work()\n"},
            },
        }
    )
    assert response is not None
    text = response["result"]["content"][0]["text"]
    payload = json.loads(text)
    assert payload["summary"]["diagnostics"] > 0


def test_mcp_template_tool_returns_body() -> None:
    server = APseudoMCPServer(root=ROOT)
    response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {
                "name": "generate_template",
                "arguments": {"name": "bounded-review-loop"},
            },
        }
    )
    assert response is not None
    assert "process review_until_accepted" in response["result"]["content"][0]["text"]


@pytest.mark.parametrize(
    ("uri", "expected_heading"),
    [
        pytest.param(
            "apseudo://standard",
            "# Pythonic Pseudocode Standard for AI Agent Instructions",
            id="standard",
        ),
        pytest.param("apseudo://rules", "# APSEUDO Rule Catalog", id="rules"),
        pytest.param(
            "apseudo://agent-instructions",
            "# Repository Agent Instruction Wording",
            id="agent-instructions",
        ),
        pytest.param(
            "apseudo://feature-gap-analysis",
            "# Feature Gap Analysis: Pythonic Agent Pseudocode Toolkit",
            id="feature-gap-analysis",
        ),
        pytest.param(
            "apseudo://traceability-review",
            "# Project Traceability Review",
            id="traceability-review",
        ),
    ],
)
def test_mcp_resource__registered_uri__returns_document_content(
    uri: str, expected_heading: str
) -> None:
    server = APseudoMCPServer(root=ROOT)
    response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "resources/read",
            "params": {"uri": uri},
        }
    )

    assert response is not None
    text = response["result"]["contents"][0]["text"]
    assert "Resource file not found:" not in text
    assert expected_heading in text


def test_review_project_reports_expected_tooling() -> None:
    review = review_project(ROOT)
    observed_paths = {check.area: check.detail for check in review.checks}
    expected_paths = {area: f"`{path}` present" for area, path in EXPECTED_REVIEW_PATHS.items()}
    failures = {check.area: check.detail for check in review.checks if check.status != "OK"}

    assert observed_paths == expected_paths
    assert failures == {}


def test_hook_blocks_no_verify_command() -> None:
    payload = {
        "cwd": str(ROOT),
        "tool_name": "Bash",
        "tool_input": {"command": "git commit --no-verify"},
    }
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "integrations" / "agents" / "apseudo-hook.py"),
            "--host",
            "codex",
            "--event",
            "pre-tool-use",
        ],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 2
    assert "--no-verify" in result.stderr
