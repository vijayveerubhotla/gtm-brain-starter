---
status: template
tags: [gtm-brain-starter, public-template]
---

# GTM brain starter

An original, sanitized starter from GTMhub. One company operating system for bounded GTM jobs: context, skills, plugins, commands, scripts, references, connectors and memory.

This is a starting example, not a client brain or the full engagement handover. Its scoring model is illustrative and uncalibrated. Replace it with your company's approved commercial rules before applying it to real accounts.

## Try it locally

Python 3.10 or later is enough. No accounts, API keys or network requests are required.

```sh
python3 scripts/evaluate_example.py --input examples/accounts.json --config examples/model.json --as-of 2026-10-08
python3 scripts/test_examples.py
```

The output shows fit, decayed timing, missing evidence, exclusions and a reviewed next action. It never sends messages, writes a CRM or chooses a campaign automatically.

## Adapt the operating system

Start with `CLAUDE.md` and fill the company context. Confirm the measurement definition and the owner of each decision. Keep facts, hypotheses and unknowns visible. Add a plugin or skill for one defined job with a readable input/output contract, not a prompt that claims to run the entire GTM system.

The skills are in `.claude/skills/`. They can also be placed in an agent's supported skills directory. Read each skill before using it. `icp-scoring` separates fit from timing; `signal-decay` validates event dates and expiry; `decision-review` turns observations into a bounded next decision.

## Connect systems deliberately

The connectors folder holds configuration guidance only. Keep credentials in the runtime's secret store. Start with read-only access to the minimum records required by the job. Trial writes on an approved sample and preserve a rollback path before connecting live work.

Do not store contact lists, private transcripts, client prices or credentials in a public repository. The examples use reserved `.test` domains and invented facts. No client material is included.

## License and scope

MIT for the original code and template text in this pack. It contains no copied private company brain, provider credentials or third-party proprietary playbook. The generic operating design should be adapted to the company's tools, permissions and actual evidence.

Learn the method at https://gtmhub.ai/library/gtm-brain/.
