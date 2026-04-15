---
name: bcedu-postman-changelog
description: Generate a detailed Markdown changelog by comparing two versions of a Postman collection JSON file. Use when asked to generate a changelog, diff, or summary of changes between Postman collection versions.
---

# Postman Changelog

Generates a structured Markdown changelog by comparing two versions of a Postman collection JSON file. Handles git-based comparisons (staged changes, current branch vs. main) and explicit two-file comparisons.

## When to Apply

Use this skill when the user asks to:
- Generate a changelog for a Postman collection
- Document what changed between two Postman collection versions
- Compare Postman collections from different git states (staged, branch vs. main, etc.)

## Commands

| Command | File | When to Apply |
| ------- | ---- | ------------- |
| Generate Changelog | commands/generate-changelog.md | When generating a changelog from a Postman collection comparison |
