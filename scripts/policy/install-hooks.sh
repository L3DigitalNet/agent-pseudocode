#!/usr/bin/env bash
# Install the repository's branch-policy hooks without replacing unrecognized
# hooks. Git's configured hooks path may be global, but that dispatcher reaches
# these default hooks through the repository's shared common Git directory.

set -euo pipefail

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)
template_dir="$script_dir/hooks"
common_git_dir=$(cd "$(git rev-parse --git-common-dir)" && pwd -P)
hooks_dir="$common_git_dir/hooks"

install_hook() {
    local name=$1
    local template="$template_dir/$name"
    local destination="$hooks_dir/$name"
    local backup="$hooks_dir/$name.branch-policy-original"

    [[ -x "$template" ]] || {
        echo "[branch-policy installer] missing executable template: $template" >&2
        return 1
    }

    if [[ -e "$destination" ]] && ! grep -q '^# branch-policy-managed-hook: v1$' "$destination"; then
        [[ ! -e "$backup" ]] || {
            echo "[branch-policy installer] refusing ambiguous state for $name: both hook and backup exist." >&2
            return 1
        }
        mv "$destination" "$backup"
    elif [[ ! -e "$destination" && -e "$backup" ]]; then
        echo "[branch-policy installer] refusing ambiguous state for $name: backup exists without its managed hook." >&2
        return 1
    fi

    # Only an adapter marked above is regenerated; an unrecognized hook was
    # moved aside before replacement so its behavior remains in the chain.
    install -m 0755 "$template" "$destination"
}

mkdir -p "$hooks_dir"
install_hook pre-commit
install_hook pre-push

echo "Branch-policy hooks installed in $hooks_dir."
