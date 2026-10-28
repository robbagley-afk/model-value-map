# Model and Effort Guidance for ChatGPT and Codex
Updated: 2026-10-27. Source: https://robbagley-afk.github.io/model-value-map/guidance-openai.md
Revision: e9d28662aced303f85a57a950f289e071fc159446f69a1a98035232cdc231dd1

## How to use
Use for ChatGPT, ChatGPT Edu and Codex. Recommend the listed pick first. Move to the upgrade only when the pick fails a check. Refresh installed instructions when Revision changes, even on the same date.

## Rule
An upgrade pays when it adds at least 5 points (or 75 Elo on GDPval) for each doubling of cost per task. Below that, the cheaper setting is the sweet spot.

## Overall general purpose recommendation
GPT-6.1 Terra at medium effort. For ordinary branching tool workflows: AutomationBench 58% at $0.10 per task. Sol medium scores 63% at 2.1 times the cost, below the upgrade rule. Work/Codex/API only, not ChatGPT Chat. Use Sol low for consequential facts and Sol xhigh for coding. API costs do not measure subscription savings.

## Codex (OpenAI) - for Codex and ChatGPT
- **Mechanical text work** (Fixed supplied-input classification, parsing and reformatting with code checks): GPT-6 Luna low ($0.0045, 22) Narrow supplied-input transformations only, with schema/content checks; tool workflows use the relay row.. Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Scripted relays and tool workflows** (Branching connector runs, fixed-step handoffs and queue imports): GPT-6.1 Terra medium ($0.10, 58%) Work/Codex/API only; not ChatGPT Chat.. Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Documents from supplied facts** (Drafts, summaries, slides and reports from supplied facts): GPT-6 Luna max ($0.07, 1445  Elo). Upgrade: Sol max GDPval 1608/$0.72 adds163  Elo over Luna max1445/$0.07 for10.29x cost:48.5  Elo per doubling, below75. Upgrade only for a failed workload check, not on this value rule..
- **People, messages, money, records** (Names, messages, payments and records checked against sources): GPT-6.1 Sol low ($0.13, 38). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Computer use and browser work** (Clicking through web apps, forms and portals with checked entries): GPT-6 Luna max ($0.22, 49%). Upgrade: No routine upgrade pays in the historical approximate vendor chart. No claim of must-succeed browser reliability.
- **Agentic coding** (Multi-file changes, debugging and repository work): GPT-6.1 Sol xhigh ($0.39, 54%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Small, clear coding fixes** (Clear-repro fixes and work to a spec, verified with relevant tests): GPT-6.1 Sol xhigh ($0.39, 54%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Research and reasoning** (Math and analysis with independently checked answers, no automatic factual claims): GPT-6.1 Sol low ($0.13, 47%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **General agentic judgment** (Branching tool-assisted requests; tool-free writing and facts use their specific rows): GPT-6.1 Terra medium ($0.10, 41) Work/Codex/API only; not ChatGPT Chat.. Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..

## Team LM Studio server (default loaded model)
- **Mechanical text work** (Fixed supplied-input classification, parsing and reformatting with code checks): Gemma 4 26B-A4B ($0) for long context, vision, and reformatting. Qwen3-14B 6-bit ($0) on client laptops for strict JSON extraction and triage.
- **Scripted relays and tool workflows** (Branching connector runs, fixed-step handoffs and queue imports): Light use only. Tool calls 3/4 in-house, AutomationBench 2% (AA estimate). Validate every call.
- **Documents from supplied facts** (Drafts, summaries, slides and reports from supplied facts): Reformatting only. GDPval 566 (AA estimate).
- **People, messages, money, records** (Names, messages, payments and records checked against sources): Never for recall. AA-Omniscience -51. It did answer UNKNOWN to 8/8 made-up facts when offered that option.
- **Computer use and browser work** (Clicking through web apps, forms and portals with checked entries): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging and repository work): Gemma: Terminal-Bench 2.0, our run, 4-bit, thinking off: 17% (15 of 89). Older test, not on this chart.
- **Small, clear coding fixes** (Clear-repro fixes and work to a spec, verified with relevant tests): Not yet evaluated.
- **Research and reasoning** (Math and analysis with independently checked answers, no automatic factual claims): Not suitable. HLE 8.7% (Google card), money math 4/6 in-house.
- **General agentic judgment** (Branching tool-assisted requests; tool-free writing and facts use their specific rows): Not suitable (index 17).

## Sources
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-astra-low
- https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-gpt-6-astra-xhigh
- https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-gpt-6-astra-xhigh
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-astra
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-low-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-medium-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-high-vs-gpt-6-luna-xhigh
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-luna-xhigh
- https://artificialanalysis.ai/models/gpt-6-1-sol-low
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-astra-xhigh
- https://artificialanalysis.ai/models/gemma-4-26b-a4b
- https://artificialanalysis.ai/models/qwen3-14b-instruct
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-medium-vs-gpt-6-1-sol-medium
