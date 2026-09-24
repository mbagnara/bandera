# Bandera — Codex Working Instructions

## Source of Truth

Before making any change to this repository, read `BANDERA_STATE.md`.

`BANDERA_STATE.md` defines the current project checkpoint and the work that is currently allowed.

## Scope

Work only on the current step defined in `BANDERA_STATE.md`.

Do not implement, scaffold, configure, or prepare future phases unless explicitly instructed.

Do not introduce technologies, frameworks, dependencies, abstractions, or infrastructure that are not required by the current step.

## Development Principle

Bandera follows:

**Start simple → Measure → Find the limitation → Earn the complexity.**

Prefer the simplest implementation that satisfies the current objective.

## Architectural Decisions

Do not make significant architectural decisions implicitly.

If the requested work requires an architectural decision that is not already documented, stop and surface the decision instead of choosing silently.

## Project State

Do not advance the project checkpoint unless explicitly instructed.

When implementation work changes the actual state of the project, report:

- what changed;
- what was verified;
- any problems discovered;
- any open questions.

`BANDERA_STATE.md` should reflect reality, not planned work.

## Learning Constraint

This project is also a learning project.

Do not hide important implementation concepts behind unnecessary automation.

Prefer changes that can be understood, inspected, tested, and explained by the project owner.