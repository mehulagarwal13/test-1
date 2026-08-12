# Contributing to test-1

Thank you for your interest in contributing to `test-1`. This guide covers how to report issues, branch and commit conventions, the pull request checklist, local testing, and the review process.

## Getting Started

New to this repository? Start with [`docs/introduction.md`](docs/introduction.md), then [`docs/local-development.md`](docs/local-development.md) for the day-to-day workflow.

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
- [ ] `python tests/validate_repo.py` passes locally
- [ ] Any related issue is linked in the PR description

## Local Testing

```bash
python tests/validate_repo.py
```

## Review Process

Every pull request should have at least one review before merging. Reviewers should check correctness, clarity, and scope. Address feedback with new commits rather than force-pushing over history, unless the reviewer asks otherwise.

## Changelog

Notable changes are tracked in [`CHANGELOG.md`](CHANGELOG.md).
