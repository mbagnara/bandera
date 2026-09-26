# Bandera

Bandera is a planned AI-assisted technical incident investigation copilot intended to help engineers systematically reduce uncertainty during troubleshooting through evidence-driven investigation and human-guided decision making. It is intended to assist engineers, not replace them.

## The Problem

Technical incidents often begin with incomplete or ambiguous information. Effective troubleshooting requires progressively reducing uncertainty through evidence, hypotheses, deliberate investigative actions, and reassessment. Bandera aims to support and structure that process.

## Core Principle

> **Bandera helps the engineer decide what to learn next and why; the engineer decides and performs what to do.**

Bandera's defined role excludes directly operating the systems being investigated. Engineers retain decision-making authority, obtain evidence, and perform operational actions.

## Development Philosophy

> **Start simple → Measure → Find the limitation → Earn the complexity.**

Technologies and architectural complexity are introduced only when observed limitations justify them.

## Repository Evolution

> **One repository. One evolving codebase. Git preserves history; tags identify meaningful milestones.**

Project phases represent stages in the evolution of the same application, rather than separate copies in phase or version directories. Git history preserves previous states; tags or GitHub releases may identify meaningful stable milestones when explicitly requested.

The conceptual progression guiding development is:

```text
Problem Definition
→ Minimal Solution
→ Evaluation
→ Observed Limitation
→ Architectural Decision
→ Improved Solution
→ Re-evaluation
```

This describes the intended development approach, not stages already implemented.

## Current Status

- Phase 0 — Understand the Problem: **Completed**
- Phase 1 — Simplest Possible AI: **In progress**
- Application implementation: **Not started**

Phase 0 established the problem definition, investigation principles, human/AI responsibility boundary, uncertainty handling, investigation state, and criteria for evaluating successful investigation behavior. No application implementation exists yet.

Steps 1.1 and 1.2 are complete: the minimum Bandera behavior and the simplest experimental path for exercising it have been conceptually defined.

## Project State

[BANDERA_STATE.md](BANDERA_STATE.md) is the authoritative project checkpoint. It records the current phase, completed decisions, and allowed next work.
