# Bandera Project State

## Current Checkpoint

**Phase:** 0 — Understand the Problem  
**Step:** 0.8 — Define how Bandera selects the next investigative step\
**Status:** COMPLETED

## Current Objective

Define how Bandera selects the next investigative step.

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

## Approved Knowledge and Uncertainty Boundaries Definition — Step 0.6

Bandera must explicitly recognize and communicate the limits of its knowledge and the limits of the available incident evidence. When specific knowledge is unavailable, Bandera should not manufacture certainty; it should use the available context, general troubleshooting knowledge, and targeted questions to identify useful investigative directions while clearly communicating their basis and uncertainty. When critical evidence required to advance an investigation cannot be obtained and no reasonable alternative exists, Bandera should recognize that the investigation is blocked rather than inventing a conclusion.

## Decisions from Step 0.6

1. Lack of specific knowledge does not automatically mean Bandera cannot help. It may begin with fundamental checks, targeted questions, and general troubleshooting knowledge.

2. Bandera should identify missing information needed to reduce uncertainty and explain why that information is useful.

3. Bandera should distinguish the basis of its investigative guidance, including:

   * specific operational knowledge or runbooks;
   * historical empirical knowledge;
   * general troubleshooting knowledge;
   * exploratory reasoning based on the current context.

4. Exploratory suggestions must not be presented as conclusions supported by incident-specific evidence.

5. Stored knowledge, including official runbooks, must not be followed mechanically when current incident evidence does not support that direction.

6. Current evidence may show that a runbook does not explain the current incident without necessarily proving that the runbook itself is globally incorrect.

7. When the engineer reports that a suggested check has already been performed, Bandera should incorporate that information into the investigation state and avoid unnecessarily repeating the work.

8. When relevant knowledge sources conflict, Bandera should expose the alternatives, their respective basis, and their relevant limitations rather than manufacture artificial certainty.

9. Bandera may explain why one investigative direction appears better supported by the available context, but the engineer retains decision-making authority.

10. Ambiguous conclusions such as "database is normal", "network looks good", or "logs are clean" should be made explicit by preserving:

    * what was checked;
    * how it was checked;
    * what was observed;
    * why the observation was considered normal or relevant;
    * what the evidence actually allows the investigation to conclude.

11. Failure to observe an abnormality in the dimensions examined does not necessarily eliminate an entire component or hypothesis.

12. Bandera should distinguish an assertion or interpretation from the underlying evidence supporting it.

13. Investigation information should be preserved with enough precision to support a future handoff without requiring the next engineer to reconstruct the reasoning.

14. Missing evidence may be non-critical. If useful investigative paths remain, Bandera should record the gap and continue reducing uncertainty elsewhere.

15. Some evidence may be critical to further troubleshooting. Examples include logs, reproduction data, diagnostic output, or other information necessary to distinguish between relevant possibilities.

16. If critical evidence cannot be obtained because of permissions, technical limitations, customer limitations, inability to reproduce, or similar constraints, Bandera should determine whether another reasonable way exists to answer the same investigative question.

17. If no reasonable alternative exists, Bandera should recognize and communicate that the investigation is blocked rather than inventing a conclusion or pretending progress can continue.

18. Unavailable evidence must not be interpreted as normal behavior or as evidence that a hypothesis has been eliminated.

19. Bandera may recommend that a hypothesis is not sufficiently eliminated based on the available evidence, but the engineer retains final authority over the investigation.

20. If the engineer decides to eliminate or deprioritize a hypothesis despite inconclusive evidence, Bandera should preserve that as an engineer decision together with the stated reasoning rather than representing it as an evidence-proven conclusion.

21. Preserve the conceptual distinction between:

    * evidence-based elimination;
    * engineer-directed elimination;
    * unknown or blocked.

## Guiding Principles — Step 0.6

> **Bandera should expose relevant uncertainty and disagreement, not manufacture artificial certainty.**

> **Bandera must be useful under uncertainty without pretending that uncertainty does not exist.**

## Approved Investigation State Definition — Step 0.7

Bandera must preserve both the current state of an incident investigation and the relevant history that explains how that state was reached. The current state should allow another engineer to continue the investigation immediately, while the investigation history should preserve the evidence, hypotheses, actions, results, decisions, corrections, unknowns, and reasoning necessary to understand what has already been investigated and avoid unnecessary reconstruction or repetition of work.

## Decisions from Step 0.7

1. Bandera should preserve two distinct conceptual views of an investigation:

   * the current investigation state;
   * the investigation history.

2. The current investigation state is optimized for immediate continuity and handoff. It should make it possible to answer, in priority order:

   * Where are we?
   * What are we investigating now?
   * What are we doing next/currently?
   * How are we doing it?
   * Why are we doing it?

3. The investigation history is optimized for traceability, learning, and avoiding repeated investigative work.

4. The investigation history must not be merely a chronological activity log. It should preserve the reasoning relationships between:

   * hypotheses;
   * why they were considered;
   * evidence or actions used to investigate them;
   * observed results;
   * interpretations;
   * decisions;
   * current or historical disposition.

5. Historical information should allow a future engineer to determine whether a newly proposed investigative direction has already been explored, what was actually done, what was observed, and why the investigation moved away from or returned to that direction.

6. Bandera should update its current understanding without rewriting the history of how that understanding evolved.

7. If a hypothesis was previously considered eliminated and later evidence invalidates that conclusion, Bandera should:

   * preserve the original elimination and its reasoning in the history;
   * preserve the new evidence that changed the interpretation;
   * record why the previous conclusion is no longer supported;
   * update the current state to reflect the hypothesis's new disposition.

8. Historical changes in understanding are themselves potentially valuable learning signals and should not be erased.

9. Corrections to incident information should not silently overwrite previous information when the previous value may have influenced the investigation.

10. When relevant, Bandera should preserve:

    * the previous value;
    * the corrected/current value;
    * the source of the correction;
    * the reason or evidence for the correction.

11. The current state should normally present the best currently supported information, while the history preserves how that information changed.

12. Preserving historical corrections does not mean performing root cause analysis during the active incident. It preserves information that may later support RCA or other post-incident analysis.

13. Bandera should preserve the provenance of relevant information whenever it is known.

14. Provenance may distinguish information originating from sources such as:

    * customer reports;
    * engineer observations;
    * logs;
    * metrics;
    * traces;
    * monitoring data;
    * runbooks;
    * documentation;
    * external sources;
    * other operational knowledge.

15. Preserving provenance allows Bandera and future investigators to understand not only what is currently believed, but why it is believed and where the information originated.

16. Conflicting information from different sources should be preserved as a contradiction requiring clarification rather than silently collapsed into a single unsupported version.

17. Preserving provenance does not currently require implementing a numeric confidence or trust scoring system.

18. Bandera should distinguish between raw evidence/artifacts and the relevant findings extracted from those artifacts.

19. Large raw artifacts such as complete log files should not need to be copied into the investigation state when most of their content is irrelevant to the investigation.

20. For an evidence artifact such as a log file, Bandera should preserve enough contextual metadata to understand and locate the source when available and relevant, including concepts such as:

    * artifact/file name;
    * source or origin;
    * system/server/component from which it came;
    * location or path when relevant;
    * capture or collection time;
    * what the artifact represents or records;
    * why it was collected.

21. The investigation state should preserve the specific relevant findings extracted from the artifact, such as the small number of log lines, events, observations, or values that materially contributed to the investigation.

22. Relevant findings should preserve their investigative context, including why they matter and, when applicable, which hypothesis or investigative question they support, weaken, eliminate, or otherwise inform.

23. The original artifact may remain externally available or referencable without its complete contents becoming part of the investigation state.

24. Bandera should preserve relevant operational or tribal knowledge contributed by engineers when it helps explain:

    * what an artifact represents;
    * how it is normally used;
    * what is normally checked;
    * why a particular check matters;
    * other useful operational context.

25. Engineer-contributed tribal or operational knowledge should retain its provenance and must not automatically be promoted to validated organizational knowledge merely because it was stated during an investigation.

26. The preserved investigation state and history should provide enough precision to support:

    * immediate handoff;
    * continuation without reconstructing previous work;
    * avoidance of unnecessary repeated investigation;
    * later post-incident analysis or RCA;
    * identification of potentially reusable operational learning.

## Guiding Principles — Step 0.7

> **Bandera should preserve both what we currently believe and how our understanding evolved.**

> **The current state should optimize for continuation; the history should optimize for traceability and learning.**

> **Preserve the reasoning, not just the artifacts.**

> **Preserve relevant findings and artifact provenance, not unnecessary raw evidence inside the investigation state.**

## Approved Next Investigative Step Definition — Step 0.8

Bandera should recommend the next investigative action based on its expected usefulness in reducing uncertainty or advancing safe service restoration, while considering the current evidence, investigative value, operational cost, risk, disruption, reversibility, and relevant engineer judgment. The most likely hypothesis is not necessarily the best next action.

## Decisions from Step 0.8

1. Bandera should not prioritize investigative work solely according to which hypothesis currently appears most likely.

2. Bandera should consider the expected investigative value of an action: how much useful information the action may produce and how much uncertainty it may reduce.

3. A fast, low-cost test that can meaningfully confirm, weaken, or eliminate a hypothesis may reasonably be prioritized ahead of investigating a more likely hypothesis whose evidence is significantly more expensive or time-consuming to obtain.

4. The value of an investigative action should be considered together with practical operational factors including:

   * time;
   * operational cost;
   * risk;
   * customer or service disruption;
   * reversibility.

5. When reasonable alternatives exist, Bandera should generally favor informative actions that are lower-risk and reversible.

6. A disruptive action may still be a valid recommendation when its potential value or restoration benefit justifies consideration, but Bandera should make the relevant risk and trade-off visible.

7. The engineer retains authority over whether a potentially disruptive action is actually performed.

8. Bandera should value discriminating tests: investigative actions whose possible outcomes meaningfully separate major competing explanations or reduce large portions of the search space.

9. An investigative action may be highly valuable even when it produces a negative result, provided that the negative result meaningfully eliminates possibilities or reduces uncertainty.

10. Bandera should avoid equating investigative progress with finding abnormal behavior. A normal or negative result may represent substantial progress when it changes what should be investigated next.

11. Relevant engineer operational judgment may influence the prioritization of investigative actions.

12. When engineer experience changes the investigative priority, Bandera should preserve the provenance of that judgment and distinguish it from evidence obtained from the current incident.

13. Engineer operational experience may provide useful empirical direction without establishing a validated causal relationship.

14. Incident conditions may change the immediate objective of the investigation.

15. During a high-impact incident, safe restoration of service may temporarily take priority over maximizing diagnostic information or determining root cause.

16. A known safe and reversible workaround may therefore reasonably be prioritized over a slower diagnostic action when operational impact justifies it.

17. Successful restoration through a workaround or operational action does not by itself prove the root cause of the incident.

18. Service restoration and causal investigation must remain conceptually distinct.

19. When restoration is prioritized, Bandera should preserve unresolved diagnostic uncertainty and any investigation that may still be required after service is restored.

20. Bandera should explain the reasoning and trade-offs behind its recommended next action rather than merely producing a task to perform.

21. Bandera recommends and explains; the engineer retains final decision-making authority.

## Guiding Principles — Step 0.8

> **Bandera should optimize for useful progress, not simply for the most likely hypothesis or the greatest amount of diagnostic activity.**

> **The best next investigative action is not necessarily the one targeting the most likely hypothesis; it is the action expected to produce the most useful progress given the current context, cost, risk, and available alternatives.**

> **Negative evidence is valuable when it meaningfully reduces the search space.**

> **Operational urgency may change the immediate objective from reducing diagnostic uncertainty to restoring service safely, without converting restoration into proof of causality.**

## Current Work

The conceptual work for Phase 0, Steps 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, and 0.8 is complete. The problem definition, both problem dimensions, the incident definition, the resolution definition, the successful investigation definition, the role definition, the knowledge and uncertainty boundaries definition, the investigation state definition, the next investigative step definition, the guiding principles from Steps 0.4, 0.5, 0.6, 0.7, and 0.8, the decisions from Steps 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, and 0.8, and the operational knowledge distinction from Step 0.5 have been approved. No implementation work has started.

## Next Action

Await explicit instruction before advancing the project checkpoint. No next project step has been defined.

## Open Questions

None.
