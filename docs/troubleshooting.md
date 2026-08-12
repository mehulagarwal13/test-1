# Troubleshooting

**`python tests/validate_repo.py` reports a missing file**
Run it from the repository root, not from inside `tests/`.

**A pull request shows commits you didn't expect**
Rebase or reset your feature branch against the current default branch before pushing again.

**Git push is rejected**
Pull the latest default branch and rebase your feature branch on top of it.
