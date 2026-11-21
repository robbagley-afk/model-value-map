# Model and Effort Guidance for ChatGPT and Codex
Updated: 2026-11-21. Source: https://robbagley-afk.github.io/model-value-map/guidance-openai.md
Revision: 6ca9b8abddacb453f27f9892b07d1fef7866caf5b8f24cfb1cb367996bc973b7

## How to use
Use for ChatGPT, ChatGPT Edu and Codex. Recommend the listed pick first. Move to the upgrade only when the pick fails a check. Refresh installed instructions when Revision changes, even on the same date.

## Rule
Start with the lowest-cost available setting that reliably passes the task checks. Compare eligible settings on the same task benchmark and version. As a guide, an upgrade should add about 5 points per doubling of benchmark cost, or about 75 Elo on GDPval. On a close call, favor the cheaper, faster setting when both meet the task requirements. Escalate when failures or rework justify it.
Filter to settings available on your plan and able to use the required tools. Set the minimum quality and reliability for the task, then compare score, cost and comparable time. Drop settings another eligible option matches or beats on every measured dimension and improves on at least one. Measure first-pass completion and time including retries on recurring work. API benchmark costs and times describe the test workload. Subscription usage and workflow duration need their own evidence.
Underlying benchmark methodology: https://artificialanalysis.ai/methodology.

## Overall general purpose recommendation
GPT-6.2 Sol at medium effort. AA v5.0.1 index 52.68 at $0.4061/task. High gains 2.21 points for 1.39x cost, about 4.67 per doubling within the 10% close-call band. Medium takes 3.56 versus 5.16 minutes per AA task. Astra high adds 7.41 points for 5.11x cost, below the guide. Retain Sol6.1 low for factual reliability. API costs do not measure subscription usage.

## When to use GPT-6.1 Terra
Every number below is already sourced in this guide's task rows and news. API task costs do not measure subscription usage. Terra is available in Work, Codex and the API only, not in ChatGPT Chat.
- **Scripted relays and ordinary branching tool workflows**: start with Terra low ($0.07, AutomationBench 56.2%). Terra medium scores 58% at $0.17 and adds 1.6 points for 2.43x the cost, which does not clear the upgrade rule. Use a higher effort only after a failed task check.
- **General-purpose default**: Terra medium (AutomationBench 58% at $0.17). Sol medium adds 5 points at $0.36 (2.1x the cost), or 4.6 points per cost doubling, below the 5-point threshold.
- **General agentic judgment on a budget**: Terra high ($0.26, index 42.4) is the cheaper choice next to Sol xhigh ($0.76, index 52).
- **Do not pick Terra for facts, names, messages, money or records**: use Sol low ($0.16, AA-Omniscience 38) and verify consequential claims.
- **Do not pick Terra for coding**: use Sol xhigh ($0.76, 54%).
Source: https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-medium-vs-gpt-6-1-sol-medium

## Codex (OpenAI) - for Codex and ChatGPT
- **Mechanical text work** (Fixed supplied-input classification, parsing and reformatting with code checks): GPT-6 Luna low ($0.01, 10) Narrow supplied-input transformations only, with schema/content checks; tool workflows use the relay row.. Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Scripted relays and tool workflows** (Branching connector runs, fixed-step handoffs and queue imports): GPT-6.2 Sol medium ($0.4061, 70.28% AutomationBench). Work/Codex/API availability, with paid plan and account access checked before use.. Upgrade: Upgrade only after a failed workload check. API task cost does not measure subscription usage..
- **Documents from supplied facts** (Drafts, summaries, slides and reports from supplied facts): GPT-6 Luna max ($0.07, 1445  Elo). Upgrade: Sol max GDPval 1608/$0.72 adds163  Elo over Luna max1445/$0.07 for10.29x cost:48.5  Elo per doubling, below75. Upgrade only for a failed workload check, not on this value rule..
- **People, messages, money, records** (Names, messages, payments and records checked against sources): GPT-6.1 Sol low ($0.16, 38). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Computer use and browser work** (Clicking through web apps, forms and portals with checked entries): GPT-6 Luna max ($0.22, 49%). Upgrade: No routine upgrade pays in the historical approximate vendor chart. No claim of must-succeed browser reliability.
- **Agentic coding** (Multi-file changes, debugging and repository work): GPT-6.2 Sol medium ($0.4061, 56.06% Terminal-Bench 4.0). Work/Codex/API availability, with paid plan and account access checked before use.. Upgrade: Upgrade only after a failed workload check. API task cost does not measure subscription usage..
- **Small, clear coding fixes** (Clear-repro fixes and work to a spec, verified with relevant tests): GPT-6.2 Sol medium ($0.4061, 56.06% Terminal-Bench 4.0). Work/Codex/API availability, with paid plan and account access checked before use.. Upgrade: Upgrade only after a failed workload check. API task cost does not measure subscription usage..
- **Research and reasoning** (Math and analysis with independently checked answers, no automatic factual claims): GPT-6.1 Sol low ($0.13, 47%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **General agentic judgment** (Branching tool-assisted requests; tool-free writing and facts use their specific rows): GPT-6.2 Sol medium ($0.4061, index 52.68). Work/Codex/API availability, with paid plan and account access checked before use.. Upgrade: Upgrade only after a failed workload check. API task cost does not measure subscription usage..

## Team LM Studio server (default loaded model)
- **Mechanical text work** (Fixed supplied-input classification, parsing and reformatting with code checks): Gemma 4 26B-A4B ($0) for long context, vision, and reformatting. Qwen3-14B 6-bit ($0) on client laptops for strict JSON extraction and triage.
- **Scripted relays and tool workflows** (Branching connector runs, fixed-step handoffs and queue imports): Light use only. Tool calls 3/4 in-house, AutomationBench 2% (AA estimate). Validate every call.
- **Documents from supplied facts** (Drafts, summaries, slides and reports from supplied facts): Reformatting only. GDPval 566 (AA estimate).
- **People, messages, money, records** (Names, messages, payments and records checked against sources): Never for recall. AA-Omniscience -51. It did answer UNKNOWN to 8/8 made-up facts when offered that option.
- **Computer use and browser work** (Clicking through web apps, forms and portals with checked entries): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging and repository work): Gemma: Terminal-Bench 2.0, our run, 4-bit, thinking off: 17% (15 of 89). Older test, not on this chart.
- **Small, clear coding fixes** (Clear-repro fixes and work to a spec, verified with relevant tests): Not yet evaluated.
- **Research and reasoning** (Math and analysis with independently checked answers, no automatic factual claims): Not suitable. HLE 8.7% (Google card), money math 4/6 in-house.
- **General agentic judgment** (Branching tool-assisted requests; tool-free writing and facts use their specific rows): Not suitable (historical v4.3.2 index 17).

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
- https://artificialanalysis.ai/models/gpt-6-1-terra
- https://artificialanalysis.ai/models/gpt-6-2-sol
- https://artificialanalysis.ai/models/gpt-6-2-astra
