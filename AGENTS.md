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

## Repository Evolution

Bandera is a single evolving codebase. Do not duplicate the application into phase/version directories to preserve old versions; Git history preserves those versions.

Tags or GitHub releases may identify meaningful milestones only when explicitly requested. Do not create them automatically.

Create directories only for current application or project needs, not to represent project phases.

## Git workflow

- main is the stable integration branch.
- Project changes must not be made directly on main.
- Each new logical unit of work that modifies the repository should be developed on a dedicated short-lived branch created from an up-to-date main.
- A logical unit of work is a coherent objective that can be reviewed and merged independently as a meaningful change.
- Multiple Codex instructions, corrections, tests, and related file changes may belong to the same branch when they serve the same logical objective.
- Do not create a new branch merely because a new Codex instruction is given or because multiple files are modified.
- Do not create one branch per file.
- Branches represent active units of work, not historical versions of the application.

Use descriptive branch names appropriate to the type of work, for example:

- feat/...
- fix/...
- docs/...
- test/...
- chore/...

Normal workflow for a new logical unit of work:

1. Start from main.
2. Synchronize local main with origin/main.
3. Create a dedicated short-lived branch.
4. Perform the work on that branch.
5. Review and verify the completed logical change.
6. Stage and commit the approved change with a descriptive commit message.
7. Push the branch.
8. Merge it into main through a Pull Request.
9. After the Pull Request is merged:
   - switch back to main,
   - synchronize local main with origin/main,
   - verify the merge,
   - delete the completed local and remote work branch.

Git history and Pull Requests preserve completed work. Merged work branches do not need to be retained for historical purposes.

Git tags/releases may be used for meaningful product milestones when explicitly requested. They should not be created for every branch or ordinary change.

## Human control over Git operations

Git publication and repository-history operations remain under explicit human control.

Codex may:

- inspect Git state when needed to understand the current working context,
- inspect the current branch,
- inspect diffs and repository status,
- modify project files within the current authorized work branch,
- run appropriate application commands, tests, and verification commands,
- report changes and verification results.

Unless explicitly instructed by the user, Codex must NOT:

- create or switch branches,
- run git add,
- run git commit,
- run git push,
- create Pull Requests,
- merge Pull Requests,
- delete local or remote branches,
- create Git tags or releases,
- otherwise publish or alter repository history.

The user performs these Git operations manually after reviewing and approving the work.

## Branch safety

Before modifying repository files, Codex must verify the current Git branch.

If the requested work would modify the repository and the current branch is main:

- stop before making any changes,
- tell the user that the work requires a dedicated work branch,
- do not create or switch branches automatically,
- wait for the user to create or select the appropriate branch.

If Codex detects an obvious mismatch between the requested work and the purpose of the current branch, it should stop before making changes and surface the mismatch rather than silently placing unrelated work on the existing branch.

Codex should not independently invent a new unit of work merely because implementation requires multiple iterations. Multiple related edits, corrections, and verification cycles remain part of the current branch when they serve the same logical objective.

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

## Application Development

Bandera is a real software application, not a notebook-based project.

Use Python as the primary programming language.

Do not create Jupyter notebooks (`.ipynb`) unless explicitly requested.

Experiments and prototypes should, when appropriate, be implemented as executable Python code, tests, or application components that can evolve toward production.

Prefer code that can be run, tested, inspected, and eventually deployed as part of the application.
