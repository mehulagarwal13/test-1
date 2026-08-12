"""Lightweight sanity check for this documentation-focused repository.

Not a framework-based test suite (there is no application code here yet) --
just a small, dependency-free script confirming the repository's core
documentation exists and is non-empty. Run with:

    python tests/validate_repo.py
"""
from __future__ import annotations

import pathlib
import sys

# Files every clone of this repository is expected to have. Extend this list
# (never remove from it silently) as new core documentation is added, so a
# missing file is caught here rather than discovered by a confused contributor.
REQUIRED_FILES = ["README.md"]


def main() -> int:
    # Resolved from this file's own location, not the current working directory,
    # so the check behaves the same regardless of where it's invoked from.
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    failures = []

    for name in REQUIRED_FILES:
        path = repo_root / name
        if not path.exists():
            failures.append(f"missing required file: {name}")
        elif path.stat().st_size == 0:
            failures.append(f"required file is empty: {name}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: all required documentation files are present and non-empty.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
