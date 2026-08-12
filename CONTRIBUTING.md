# Contributing to test-1

Thank you for your interest in contributing. This guide is being built up section by section -- see the sections below.

## Reporting Issues

Before opening a new issue, search existing issues to avoid duplicates. When filing a new one, include:

- A clear, descriptive title
- What you expected to happen vs. what actually happened
- Steps to reproduce, if applicable

## Branch Naming

Use a short, descriptive prefix that matches the kind of change:

- `docs/<topic>` for documentation-only changes
- `test/<topic>` for test-only changes
- `fix/<topic>` for bug fixes
- `feature/<topic>` for new functionality

## Commit Messages

Follow the Conventional Commits style used throughout this repository's history:

```text
<type>: <short, present-tense summary>
```

Common types: `docs`, `test`, `fix`, `feature`, `chore`. Keep each commit focused on one logical change.

## Pull Request Checklist

Before requesting review, confirm:

- [ ] The PR description explains *why*, not just *what*
- [ ] Commits are focused and use conventional messages
- [ ] `python tests/validate_repo.py` passes locally (if present)
- [ ] Any related issue is linked in the PR description
