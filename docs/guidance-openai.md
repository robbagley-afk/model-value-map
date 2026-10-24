# Model and Effort Guidance for ChatGPT and Codex
Updated: 2026-10-24. Source: https://robbagley-afk.github.io/model-value-map/guidance-openai.md
Revision: eec16b50ec170279202153ad14d9e25e243bf895b5c918456e8853b6c39e7cfe

## How to use
Use for ChatGPT, ChatGPT Edu and Codex. Recommend the listed pick first. Move to the upgrade only when the pick fails a check. Refresh installed instructions when Revision changes, even on the same date.

## Rule
An upgrade pays when it adds at least 5 points (or 75 Elo on GDPval) for each doubling of cost per task. Below that, the cheaper setting is the sweet spot.

## Overall general purpose recommendation
GPT-6.1 Sol at medium effort. Balanced capability and cost for everyday, multistep work. Use the task-specific picks below when your work needs something different.

## Codex (OpenAI) - for Codex and ChatGPT
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): GPT-6 Luna max ($0.07, 38), best when the step calls tools (AutomationBench 53%). Upgrade: GPT-6.1 Sol low ($0.13, 42).
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): GPT-6.1 Sol medium ($0.21, 63%). Upgrade: Rarely. GPT-6.1 Sol xhigh ($0.39, 67%) adds 4 points.
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): GPT-6 Luna max (1433, $0.07). Upgrade: GPT-6.1 Sol max (1596, $0.72).
- **People, messages, money, records** (Customer and community messages, payments, exact names): GPT-6.1 Sol high ($0.32, 41), verify names and figures. Upgrade: Rarely. Sol max ($0.72, 42) adds 1 point.
- **Computer use and browser work** (Clicking through web apps, forms, portals): GPT-6 Luna max (49%, $0.22). Sol and Astra not yet evaluated on this chart.
- **Agentic coding** (Multi-file changes, debugging, repo work): GPT-6.1 Sol xhigh ($0.39, 54%). Upgrade: Rarely. GPT-6.1 Sol max ($0.72, 56%) adds 2 points.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): GPT-6.1 Sol medium ($0.21, 48%). Upgrade: GPT-6.1 Sol xhigh ($0.39, 54%).
- **Research and reasoning** (Analysis, tradeoffs, hard questions): GPT-6.1 Sol low ($0.13, 47%). Upgrade: GPT-6.1 Sol medium ($0.21, 50%) after a failed task check; its 3-point gain is below the value threshold.
- **General agentic judgment** (Open-ended multistep tasks, planning): GPT-6.1 Sol medium ($0.21, 48). Upgrade: GPT-6.1 Sol high ($0.32, 50).

## Team LM Studio server (default loaded model)
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): Gemma 4 26B-A4B ($0) for long context, vision, and reformatting. Qwen3-14B 6-bit ($0) on client laptops for strict JSON extraction and triage.
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): Light use only. Tool calls 3/4 in-house, AutomationBench 2% (AA estimate). Validate every call.
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): Reformatting only. GDPval 566 (AA estimate).
- **People, messages, money, records** (Customer and community messages, payments, exact names): Never for recall. AA-Omniscience -51. It did answer UNKNOWN to 8/8 made-up facts when offered that option.
- **Computer use and browser work** (Clicking through web apps, forms, portals): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging, repo work): Gemma: Terminal-Bench 2.0, our run, 4-bit, thinking off: 17% (15 of 89). Older test, not on this chart.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): Not yet evaluated.
- **Research and reasoning** (Analysis, tradeoffs, hard questions): Not suitable. HLE 8.7% (Google card), money math 4/6 in-house.
- **General agentic judgment** (Open-ended multistep tasks, planning): Not suitable (index 17).

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
