# Architecture Learnings

Bandera intentionally evolves through:

> Start simple → Measure → Find the limitation → Earn the complexity.

This document preserves generalizable architectural and engineering reasoning discovered during that process, including why complexity was introduced, deferred, or rejected. It records learnings that could materially affect Bandera's design, evaluation, evolution, or eventual production operation.

It is not a chronological development log, an ADR collection, a roadmap, or a place to speculate about future architecture.

Entries do not automatically authorize implementation. `BANDERA_STATE.md` remains authoritative for the current project checkpoint and allowed work. `README.md` explains what Bandera is and why it exists; `AGENTS.md` defines how Codex operates in the repository.

---

## 1. Conversation History and Investigation State Are Different Concepts

### Context

Bandera conducts a multi-turn investigation with an engineer.

The conversation history records the sequence of interactions between the engineer and Bandera.

However, the chronological conversation is not necessarily the best representation of the current investigation.

### Learning

History and current investigation state serve different purposes.

> History explains how we got here.
> Investigation state explains where we are now.

Conversation history may contain:

* previous assumptions;
* corrected information;
* superseded hypotheses;
* questions and answers;
* investigative actions;
* evidence as it was discovered;
* earlier interpretations that are no longer current.

An explicit investigation state should eventually represent the current operational understanding of the incident, including relevant elements such as:

* affected operation or behavior;
* observed deviation;
* scope and impact;
* current known facts;
* relevant unknowns;
* evidence;
* hypotheses and their current status;
* investigative direction;
* actions already completed;
* current restoration status;
* next useful action;
* reasoning for that action.

### Architectural implication

The initial Bandera implementation may use conversation history alone as its runtime context because that is the simplest way to test the core investigation behavior.

However, conversation history and investigation state must not be treated as conceptually identical.

An explicit investigation state is a deliberately deferred capability.

---

## 2. Explicit Investigation State Is a Required Future Capability

### Context

During the minimal implementation, maintaining a structured investigation state would introduce additional design questions before Bandera's basic investigation behavior has been validated.

Therefore, it is intentionally deferred.

### Learning

Deferring explicit investigation state does not mean that the capability is optional.

A structured current state will eventually be operationally important beyond LLM context management.

It can support:

* investigation continuity;
* engineer-to-engineer handoff;
* internal incident updates;
* management/status updates;
* customer-facing incident communications;
* incident review;
* future operational learning.

Different audiences may require different representations of the same underlying investigation state.

For example, detailed uncertain technical hypotheses may be useful to the investigating engineers but inappropriate for a customer-facing status update.

### Architectural implication

Bandera should eventually maintain a representation of current investigation state that can be independently transformed into appropriate operational communications and handoff views.

The initial implementation should not build this capability yet, but it should avoid unnecessary decisions that would make its later introduction difficult.

---

## 3. Durable Persistence Is Deferred, Not Rejected

### Context

The first Bandera implementation needs only one active investigation during one application execution.

If the application stops, the investigation may be lost.

### Learning

Persistence is not required to answer the first Phase 1 question:

> Can Bandera maintain a coherent multi-turn investigation and behave as the investigation copilot defined during Phase 0?

Adding durable persistence immediately would force the project to solve another problem before the core behavior has been demonstrated:

> Where and how should investigation information be stored?

That decision would introduce storage technology, schemas, lifecycle behavior, recovery semantics, and other concerns that are not yet necessary.

### Architectural principle

> Do not solve persistence before the behavior worth persisting has been validated.

### Architectural implication

The first implementation may keep its runtime context only in memory.

Durable persistence remains an expected future requirement because real investigations must eventually survive process restarts and support continuation, handoff, communication, auditability, and learning.

No storage technology should be selected until the actual persistence requirements justify that decision.

---

## 4. Service Restoration Is Not Causal Proof

### Context

Incident response can prioritize rapid restoration, particularly when operational impact and urgency are high.

A workaround, restart, rollback, failover, configuration change, or other action may restore normal service.

### Learning

Successful restoration does not by itself establish root cause.

For example:

1. a service is unavailable;
2. an engineer restarts a component;
3. service returns;
4. the customer confirms that the original symptom no longer occurs.

This may be sufficient to determine that the incident is resolved according to Bandera's resolution criteria.

It is not sufficient by itself to conclude:

> The restarted component caused the incident.

Restoration and causal validation are separate claims with different evidentiary requirements.

### Architectural principle

> Restoration ≠ root-cause proof.

Bandera must preserve this distinction even when an operational action appears strongly correlated with recovery.

### Architectural implication

Bandera's reasoning and future state representation should distinguish among:

* observed evidence;
* hypotheses;
* operational actions;
* restoration outcomes;
* validated causal conclusions.

This distinction is important for troubleshooting quality, incident communication, post-incident analysis, and future organizational knowledge.

---

## 5. The Development Model Is a Baseline, Not Automatically the Production Model

### Context

Bandera may begin development using a locally executable open-weight LLM.

A future production system may use that model, another local model, a hosted open-weight model, or a cloud frontier model.

### Learning

LLMs must not be treated as behaviorally interchangeable dependencies.

Different models can produce materially different behavior even when given similar:

* instructions;
* conversation history;
* context;
* sampling parameters;
* investigation scenarios.

Therefore, successfully developing Bandera against one model does not prove that replacing it with another model will preserve Bandera's behavior.

Likewise, the model used during development should not automatically become the production model.

### Architectural principle

> Bandera behavior should be defined independently from the model used to implement it.

The initial model is a development baseline.

Production model selection is a qualification decision.

### Architectural implication

Avoid unnecessarily designing Bandera around model-specific quirks.

Model-specific configuration may be necessary, but Bandera's required investigation behavior should remain independently defined.

---

## 6. Model Selection Should Become Evaluation-Driven

### Context

General model benchmarks are useful signals but do not directly answer whether a model is suitable for Bandera's investigation workflow.

Bandera has specific behavioral requirements.

### Learning

Model selection should progressively become a task-specific qualification process driven by Bandera scenarios and evaluation criteria.

The evolution should conceptually follow:

Behavior specification
→ baseline model
→ Bandera-specific investigation scenarios
→ evaluation criteria
→ measured behavior
→ model comparison
→ production qualification

The goal is not identical textual output across models.

The goal is sufficiently consistent satisfaction of Bandera's behavioral requirements.

### Candidate behavioral criteria

Future model evaluation may include whether the model:

* distinguishes facts and evidence from hypotheses;
* handles uncertainty explicitly;
* avoids unsupported causal conclusions;
* identifies important unknowns;
* updates its understanding when new evidence arrives;
* does not unnecessarily repeat completed investigation;
* recommends useful next investigative actions;
* explains why those actions are useful;
* considers operational impact and urgency;
* exposes relevant trade-offs;
* preserves engineer decision authority;
* recognizes legitimate resolution;
* recognizes when an investigation is blocked;
* does not confuse successful restoration with root-cause validation.

### Important implication

Useful scenarios discovered during development should begin to be preserved because failures, corrections, and difficult cases can later become evaluation cases.

A full evaluation framework is not required yet.

---

## 7. Production Model Qualification Requires More Than Reasoning Quality

### Context

A model may perform well in investigation reasoning while still being unsuitable for a production deployment.

### Learning

Production model selection is a multidimensional engineering decision.

Eventually, candidate models should be evaluated across at least three broad dimensions.

### Behavioral quality

Examples:

* investigation reasoning;
* instruction following;
* uncertainty handling;
* technical troubleshooting capability;
* context handling;
* causal restraint;
* consistency.

### Operational characteristics

Examples:

* latency;
* throughput;
* context-window requirements;
* reliability;
* availability;
* deployment complexity;
* hardware requirements;
* observability;
* model/version stability.

### Business, security, and governance characteristics

Examples:

* cost;
* licensing;
* commercial-use terms;
* privacy;
* data handling and retention;
* security;
* deployment location;
* vendor dependency;
* support;
* lifecycle and versioning.

### Architectural implication

The model with the strongest generic benchmark score is not automatically the best production model for Bandera.

Production qualification should be based on Bandera's actual behavioral, operational, security, governance, and business requirements.

---

## 8. Local Models and Cloud Models Can Serve Different Experimental Roles

### Context

Bandera's development environment can run capable local models.

Local execution may provide low-cost iteration, privacy, reproducibility, and experimentation without making a production deployment decision.

Cloud frontier models may provide a useful higher-capability reference.

### Learning

The correct distinction is not:

> local model now → replace it with cloud model later.

A better experimental model is:

> development baseline + capability reference + evaluation.

A local model can serve as the development baseline.

A capable cloud model can later serve as a reference when investigating whether a failure comes primarily from:

* Bandera's instructions;
* insufficient context;
* application design;
* evaluation ambiguity;
* or model capability.

For example, if both the local baseline and a capable cloud reference fail the same scenario, the problem may lie in Bandera's design or instructions.

If the local baseline repeatedly fails scenarios that a stronger model handles reliably, this provides evidence of a model capability gap.

### Architectural implication

Local and cloud models should eventually be compared using the same Bandera-specific scenarios and behavioral criteria rather than informal impressions.

This does not require integrating multiple models into the initial application.

---

## 9. Evaluation Should Begin as Learning Before It Becomes Infrastructure

### Context

Bandera is still developing its minimum viable investigation behavior.

Building a sophisticated evaluation platform now would violate the project's principle of earning complexity.

However, postponing all evaluation thinking until the system is mature would lose valuable information.

### Learning

Evaluation should begin before evaluation infrastructure.

Early development should preserve:

* representative incident scenarios;
* surprising failures;
* incorrect causal conclusions;
* useful responses;
* cases where the model mishandled uncertainty;
* cases where operational urgency changed the appropriate recommendation;
* regressions discovered after changing instructions or models.

These artifacts can progressively become the foundation of Bandera's formal evaluation suite.

### Architectural principle

> Small first does not mean quality later.

It means starting with the smallest useful mechanism for learning whether the system satisfies its required behavior.

---

## Document Maintenance Rule

Add a learning to this document only when it represents a generalizable engineering or architectural insight that could materially influence Bandera's design, evaluation, evolution, or production operation.

Do not use this document for:

* routine implementation notes;
* installation instructions;
* transient debugging details;
* chronological progress updates;
* speculative feature lists;
* decisions that belong only in `BANDERA_STATE.md`;
* technologies that have not been justified by an observed requirement.

When a learning later leads to an implementation decision, preserve the learning here and record the current project decision separately in `BANDERA_STATE.md` or the appropriate future decision mechanism.
