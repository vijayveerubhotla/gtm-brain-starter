---
name: icp-scoring
description: Assess company fit separately from dated timing signals using an approved company model; produce reasons and missing evidence. Use for account selection and tier review, not message sending.
---

Read the company ICP, exclusions and current model version. Confirm the account unit and source for each feature. Keep fit, timing and confidence separate; exclusions override scores.

Use `scripts/evaluate_example.py` for the deterministic example only after replacing its illustrative weights with the approved model. Read `references/evidence-rules.md` when evidence is incomplete. Low confidence or missing required facts produces research, never activation.

Return a receipt: company, fit, decayed signal score, evidence dates, reason codes, unknowns, exclusions, rule version and a reviewed next action. No automatic CRM writes or outreach. Calibration requires mature outcomes and a holdout or prospective test.
