# Bandera Project State

## Current Checkpoint

**Phase:** 0 — Understand the Problem  
**Step:** 0.2 — Define what constitutes an incident for Bandera\
**Status:** COMPLETED

## Current Objective

Define what constitutes an incident for Bandera.

## Approved Problem Definition

Bandera seeks to help systematically reduce the uncertainty of an initially ambiguous technical incident through the collection and analysis of evidence, the formulation and testing of hypotheses, and the validation of potential solutions until the expected service behavior is restored and confirmed.

At the same time, Bandera seeks to preserve the validated learnings produced during each investigation so that the available operational knowledge progressively improves and future incident troubleshooting becomes more effective.

## Problem Dimensions

1. Reduce uncertainty in the current incident.
2. Preserve validated learning to improve future incident investigations.

## Decisions Made

- Bandera is a generic AI-assisted incident investigation and management system.
- Bandera will evolve from the simplest possible implementation toward a production-grade AI system.
- Development follows the principle: **Start simple → Measure → Find the limitation → Earn the complexity.**
- Only one project step is worked on at a time.
- Technologies are introduced only when a demonstrated problem justifies them.
- The repository is the shared source of truth between ChatGPT and VS Code/Codex.

## Approved Incident Definition — Step 0.2

Bandera considers an incident to be any observed deviation from the expected behavior of an identifiable operation or service that requires investigation or restoration. Starting triage does not require knowing the cause or having complete technical evidence; it requires enough context to describe the symptom, the affected operation, its scope, and its context. Operational impact is evaluated separately and contributes to determining incident severity.

## Decisions from Step 0.2

1. Observed behavior should be distinguished from expected behavior.
2. The affected operation or service should be identifiable because a single user-facing activity may depend on multiple independent services.
3. The number of affected users describes scope but does not by itself determine business impact or severity.
4. Business impact depends on the operational function or business process affected, not simply on the number or organizational rank of affected users.
5. A single-user issue can still be a valid incident, including a low-severity incident.
6. Geographic distribution and access context, such as corporate network or VPN, are relevant contextual facts that can help reduce ambiguity.
7. Approximate start time is diagnostically valuable for correlating the incident with releases, configuration changes, infrastructure changes, or external dependency events, but an unknown start time does not prevent triage from beginning.
8. Detailed technical evidence such as logs, metrics, traces, screenshots, and technical errors can be collected during triage and is not required for initial incident acceptance.
9. Maintain a strict distinction between facts and hypotheses. For example, "affected users are connected through VPN" is a fact; "VPN is causing the latency" is a hypothesis.
10. Operational impact contributes to severity classification; it does not determine whether the issue qualifies as an incident.

## Current Work

The conceptual work for Phase 0, Steps 0.1 and 0.2 is complete. The problem definition, both problem dimensions, the incident definition, and the decisions from Step 0.2 have been approved. No implementation work has started.

## Next Action

Await explicit instruction before advancing the project checkpoint. No next project step has been defined.

## Open Questions

None.
