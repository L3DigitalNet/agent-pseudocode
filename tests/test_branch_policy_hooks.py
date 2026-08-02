from __future__ import annotations

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "policy" / "install-hooks.sh"
ZERO_OID = "0" * 40
REQUIRED_EMAIL = "168346341+chrisdpurcell@users.noreply.github.com"


def git(
    repo: Path,
    *args: str,
    input_text: str | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    command_env = os.environ.copy()
    if env is not None:
        command_env.update(env)
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
        env=command_env,
    )


def create_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    assert git(repo, "init", "--initial-branch=main").returncode == 0
    assert git(repo, "config", "user.name", "Branch Policy Test").returncode == 0
    assert git(repo, "config", "user.email", REQUIRED_EMAIL).returncode == 0
    (repo / "README.md").write_text("bootstrap\n", encoding="utf-8")
    assert git(repo, "add", "README.md").returncode == 0
    assert git(repo, "commit", "-m", "bootstrap", env={"ALLOW_MAIN_COMMIT": "1"}).returncode == 0
    assert git(repo, "switch", "-c", "dev").returncode == 0
    return repo


def install(repo: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(INSTALLER)],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )


def hook_path(repo: Path, name: str) -> Path:
    hooks_dir = git(repo, "rev-parse", "--git-common-dir").stdout.strip()
    return repo / hooks_dir / "hooks" / name


def commit(
    repo: Path, message: str, content: str, *, env: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    (repo / "README.md").write_text(content, encoding="utf-8")
    assert git(repo, "add", "README.md").returncode == 0
    return git(repo, "commit", "-m", message, env=env)


def test_installer_preserves_predecessors_and_is_idempotent(tmp_path: Path) -> None:
    repo = create_repo(tmp_path)
    hooks_dir = hook_path(repo, "pre-commit").parent
    trace = repo / "hook-trace.log"
    for name in ("pre-commit", "pre-push"):
        predecessor = hooks_dir / name
        predecessor.write_text(
            f"#!/usr/bin/env bash\nprintf '%s\\n' '{name}' >> '{trace}'\ncat >/dev/null || true\n",
            encoding="utf-8",
        )
        predecessor.chmod(0o755)

    first_install = install(repo)
    assert first_install.returncode == 0, first_install.stderr
    second_install = install(repo)
    assert second_install.returncode == 0, second_install.stderr

    assert (hooks_dir / "pre-commit.branch-policy-original").is_file()
    assert (hooks_dir / "pre-push.branch-policy-original").is_file()
    assert commit(repo, "dev change", "dev\n").returncode == 0

    main_oid = git(repo, "rev-parse", "main").stdout.strip()
    dev_oid = git(repo, "rev-parse", "dev").stdout.strip()
    assert main_oid != dev_oid
    pre_push = subprocess.run(
        [str(hook_path(repo, "pre-push")), "origin", "unused"],
        cwd=repo,
        input=f"refs/heads/dev {dev_oid} refs/heads/dev {ZERO_OID}\n",
        text=True,
        capture_output=True,
        check=False,
    )
    assert pre_push.returncode == 0, pre_push.stderr
    assert trace.read_text(encoding="utf-8").splitlines() == ["pre-commit", "pre-push"]


def test_pre_commit_rejects_main_but_allows_dev_and_only_explicit_override(tmp_path: Path) -> None:
    repo = create_repo(tmp_path)
    install_result = install(repo)
    assert install_result.returncode == 0, install_result.stderr

    assert git(repo, "switch", "main").returncode == 0
    denied = commit(repo, "blocked main change", "blocked\n")
    assert denied.returncode != 0
    assert "direct commits on main are blocked" in denied.stderr
    assert "git switch dev" in denied.stderr

    still_denied = commit(
        repo, "still blocked", "still blocked\n", env={"ALLOW_MAIN_COMMIT": "true"}
    )
    assert still_denied.returncode != 0
    allowed = commit(repo, "emergency main change", "emergency\n", env={"ALLOW_MAIN_COMMIT": "1"})
    assert allowed.returncode == 0, allowed.stderr

    assert git(repo, "switch", "dev").returncode == 0
    permitted = commit(repo, "ordinary dev change", "dev\n")
    assert permitted.returncode == 0, permitted.stderr


def test_pre_push_requires_matching_main_and_dev_and_rejects_unsafe_updates(tmp_path: Path) -> None:
    repo = create_repo(tmp_path)
    install_result = install(repo)
    assert install_result.returncode == 0, install_result.stderr
    assert commit(repo, "dev change", "dev\n").returncode == 0

    main_oid = git(repo, "rev-parse", "main").stdout.strip()
    dev_oid = git(repo, "rev-parse", "dev").stdout.strip()
    pre_push = hook_path(repo, "pre-push")

    def run_update(
        local_oid: str, remote_oid: str, *, env: dict[str, str] | None = None
    ) -> subprocess.CompletedProcess[str]:
        command_env = os.environ.copy()
        if env is not None:
            command_env.update(env)
        return subprocess.run(
            [str(pre_push), "origin", "unused"],
            cwd=repo,
            input=f"refs/heads/main {local_oid} refs/heads/main {remote_oid}\n",
            text=True,
            capture_output=True,
            check=False,
            env=command_env,
        )

    denied = run_update(dev_oid, main_oid)
    assert denied.returncode != 0
    assert "local main and dev must identify the same commit" in denied.stderr
    still_denied = run_update(dev_oid, main_oid, env={"ALLOW_MAIN_PUSH": "yes"})
    assert still_denied.returncode != 0
    assert run_update(dev_oid, main_oid, env={"ALLOW_MAIN_PUSH": "1"}).returncode == 0

    assert git(repo, "switch", "main").returncode == 0
    assert git(repo, "merge", "--ff-only", "dev").returncode == 0
    promoted_oid = git(repo, "rev-parse", "main").stdout.strip()
    assert promoted_oid == git(repo, "rev-parse", "dev").stdout.strip()
    allowed = run_update(promoted_oid, main_oid)
    assert allowed.returncode == 0, allowed.stderr

    deletion = run_update(ZERO_OID, main_oid)
    assert deletion.returncode != 0
    assert "deleting main is blocked" in deletion.stderr

    tree_oid = git(repo, "rev-parse", "HEAD^{tree}").stdout.strip()
    divergent_oid = git(
        repo, "commit-tree", tree_oid, "-m", "divergent remote history"
    ).stdout.strip()
    non_fast_forward = run_update(promoted_oid, divergent_oid)
    assert non_fast_forward.returncode != 0
    assert "non-fast-forward updates to main are blocked" in non_fast_forward.stderr
