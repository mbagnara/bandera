# Bandera Project State

## Current Checkpoint

**Phase:** 0 — Understand the Problem  
**Step:** 0.3 — Define when an incident is considered resolved\
**Status:** COMPLETED

## Current Objective

Define when an incident is considered resolved.

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

## Approved Resolution Definition — Step 0.3

Bandera considers an incident resolved when the affected operational behavior has been restored under representative conditions and there is confirmation from the customer side that the symptom defining the incident is no longer reproducible. Resolution does not require knowing the root cause or having a permanent solution. It may be achieved through a fix, a workaround, or even recovery without a known intervention, provided that restoration has been sufficiently validated.

## Decisions from Step 0.3

1. Technical recovery is not equivalent to incident resolution. Internal validation by the supporting/provider team is useful evidence but is not sufficient by itself to close the incident.
2. Customer-side validation is required, but it does not necessarily have to come from the specific user who originally reported the incident. It may come from an appropriate end user, technical contact, management representative, or another representative customer-side source.
3. Resolution should be validated under production or sufficiently representative conditions. A successful test in a development or otherwise non-representative environment is not sufficient by itself.
4. Mitigation is not equivalent to resolution. If the original abnormal behavior continues to reproduce, even intermittently, the incident remains open.
5. Incident severity may change during the lifetime of the incident. A substantial reduction in operational impact may lower severity without resolving the incident.
6. Root cause determination is separate from incident resolution. An incident may be resolved even when the root cause remains unknown.
7. A workaround can be a valid incident resolution when it restores the affected operation. The workaround must be documented, while permanent remediation may continue as separate follow-up work.
8. An incident may also be resolved when the problem disappears without a known intervention, provided the customer confirms that the symptom is no longer occurring. The incident should record that recovery occurred without a known cause or intervention.
9. The disappearance of the symptom may limit reproducibility and further root cause investigation, but it does not necessarily make retrospective root cause analysis impossible if historical evidence such as logs, metrics, traces, or change records remains available.
10. Root cause analysis, permanent remediation, or other follow-up investigation should not keep an incident artificially open once operational service has been restored and resolution has been sufficiently validated.
11. The incident record should preserve how resolution occurred and what remains unknown or pending so that validated learning can contribute to future investigations.

## Current Work

The conceptual work for Phase 0, Steps 0.1, 0.2, and 0.3 is complete. The problem definition, both problem dimensions, the incident definition, the resolution definition, and the decisions from Steps 0.2 and 0.3 have been approved. No implementation work has started.

## Next Action

Await explicit instruction before advancing the project checkpoint. No next project step has been defined.

## Open Questions

None.
