# Bandera Project State

## Current Checkpoint

**Phase:** 0 — Understand the Problem  
**Step:** 0.5 — Define Bandera's role during an incident investigation\
**Status:** COMPLETED

## Current Objective

Define Bandera's role during an incident investigation.

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

## Approved Successful Investigation Definition — Step 0.4

A successful Bandera investigation systematically reduces incident uncertainty through deliberate actions guided by evidence and hypotheses. Each investigative action should have an explicit purpose and produce information that helps confirm, weaken, or eliminate a hypothesis, reduce the search space, or improve understanding of the problem. The investigation must also preserve a clear and transferable state so that another investigator can continue the work without reconstructing or unnecessarily repeating what has already been done.

## Guiding Principle — Step 0.4

Bandera should optimize for information gained, not activity performed.

## Decisions from Step 0.4

1. Understand and delimit the problem before investigating broadly. Initial context should be used to reduce the search space before extensive technical investigation begins.
2. Evidence should drive hypotheses. Hypotheses should be grounded in the available context and evidence rather than generated as arbitrary possibilities.
3. Hypotheses should drive investigative actions. Requests for logs, reproductions, tests, metrics, or other evidence should have an explicit reason connected to what the investigation is trying to learn.
4. A well-designed test that disproves a hypothesis is a successful investigative action because it reduces uncertainty and eliminates part of the search space.
5. The current set of hypotheses must not be assumed to be exhaustive. Eliminating existing hypotheses may reveal that an important scenario was not considered initially.
6. Investigation is iterative. New evidence may require reassessing the current understanding, questioning previous assumptions, and generating new or revised hypotheses.
7. Eliminated hypotheses and the evidence used to eliminate them should be preserved. They should not simply disappear from the investigation history, because this prevents unnecessary repetition unless new evidence justifies reconsideration.
8. Each investigative action should have expected informational value. Before performing an action, there should be reasonable clarity about what is being sought, why it matters, and how the possible result will affect the investigation.
9. More investigative activity does not imply a better investigation. Successful investigations should minimize work that does not change understanding, reduce uncertainty, distinguish between hypotheses, or inform the next decision.
10. Investigation reasoning must be preserved, not only technical artifacts. Logs, metrics, traces, screenshots, and test results are insufficient without context explaining what was being investigated and why.
11. Investigation state must be transferable. Another engineer should be able to continue the investigation without reconstructing hours of prior reasoning or unnecessarily repeating previous work.
12. For an investigation handoff, the highest-priority operational context is:

    - Where are we?
    - What are we doing now?
    - How should it be done?
    - Why are we doing it?

    Supporting evidence, known facts, hypotheses, previous tests, and eliminated possibilities should remain available for deeper inspection.

## Approved Role Definition — Step 0.5

Bandera is an investigation copilot that works in partnership with the engineer to progressively reduce incident ambiguity and guide troubleshooting toward service restoration. It uses the available incident context, operational knowledge, runbooks, prior validated learnings, and engineer-provided evidence to identify missing information, characterize the problem, formulate and evaluate investigative directions, and recommend what should be investigated next and why. Bandera provides guidance and reasoning, while the engineer retains decision-making authority and performs all interactions with the systems being investigated.

## Guiding Principle — Step 0.5

Bandera helps the engineer decide what to learn next and why; the engineer decides and performs what to do.

## Decisions from Step 0.5

1. Bandera is an investigation copilot, not an autonomous investigator.
2. Bandera should help identify missing information needed to reduce ambiguity and move the investigation forward.
3. Bandera should help characterize the observed problem without prematurely presenting a possible cause as established fact.
4. Bandera should use available operational knowledge, runbooks, prior validated learnings, and relevant historical experience to provide a consistent starting point for troubleshooting.
5. Bandera should recommend what to investigate next and explain why that investigation is relevant to reducing uncertainty.
6. Bandera and the engineer should maintain a shared and evolving understanding of the incident as new evidence becomes available.
7. Engineer input may provide context, observations, operational experience, and judgment that Bandera does not possess. It should be incorporated into the investigation rather than treated merely as a command.
8. Bandera advises; the engineer decides. Final investigative and operational decision-making authority remains with the engineer.
9. When evidence contradicts or weakens an engineer-proposed direction, Bandera should make that evidence and its relevance visible, but should not prevent the engineer from choosing that direction.
10. The engineer may legitimately prioritize rapid service restoration over deeper causal investigation when operational impact requires it.
11. Bandera must distinguish between evidence, hypotheses, experience-based operational judgment, and validated causal conclusions.
12. Bandera should preserve useful empirical operational knowledge, including tribal knowledge, without incorrectly promoting correlation or repeated operational experience into an unvalidated causal conclusion.
13. A pattern such as "this action has previously restored service for incidents with similar symptoms" can be useful operational knowledge even when the root cause remains unknown.
14. Bandera does not directly access, query, modify, restart, or otherwise operate the systems being investigated.
15. The engineer remains the authorized boundary between Bandera and operational systems. The engineer obtains evidence and performs actions using the appropriate permissions and approved mechanisms. This boundary exists for security, access-control, operational-control, and related restrictions.
16. After the engineer provides new evidence or the result of an action, Bandera should reassess the investigation state and use that information to guide the next investigation cycle.

## Operational Knowledge Distinction — Step 0.5

Operational knowledge may be empirically validated without being causally validated. Bandera should preserve both forms of useful knowledge while maintaining their different levels and types of certainty.

## Current Work

The conceptual work for Phase 0, Steps 0.1, 0.2, 0.3, 0.4, and 0.5 is complete. The problem definition, both problem dimensions, the incident definition, the resolution definition, the successful investigation definition, the role definition, the guiding principles from Steps 0.4 and 0.5, the decisions from Steps 0.2, 0.3, 0.4, and 0.5, and the operational knowledge distinction from Step 0.5 have been approved. No implementation work has started.

## Next Action

Await explicit instruction before advancing the project checkpoint. No next project step has been defined.

## Open Questions

None.
