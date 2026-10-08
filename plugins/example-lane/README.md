---
status: template
tags: [gtm-brain-starter, public-template]
---

# Example lane plugin

Job: prepare a reviewed account-selection receipt from permitted company facts. This example plugin uses the same company context as any other lane.

Input contract: a company domain, evidence-bearing fit features, dated relevant signals and exclusion state. Output contract: fit and timing separately, reason codes, missing evidence and an owner-review disposition.

Skills: `icp-scoring` and `signal-decay`. Script: `scripts/evaluate_example.py`. Reference: `references/evidence-rules.md`. Connector: none in the example.

Failure path: unresolved identity, missing evidence, contradictory signals or exclusion produces research, hold or exclude, never an automatic sequence. The operator remains accountable for the commercial decision.
