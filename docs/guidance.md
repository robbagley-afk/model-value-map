# Model and Effort Guidance
Updated: 2026-10-09. Source: https://robbagley-afk.github.io/model-value-map/

## How to use
Use the section for the platform you run on. For each kind of task, recommend the listed pick first.
Move to the listed upgrade only when the pick fails a check or the task is harder than the examples.
Scores and costs come from the sources at the end of this file.

## Rule
An upgrade pays when it adds at least 5 points (or 75 Elo on GDPval) for each doubling of cost per task. Below that, the cheaper setting is the sweet spot.

## Claude (Anthropic) - for Claude Code and Claude apps
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): Haiku 5.5 low ($0.02, 29). Upgrade: Haiku 5.5 medium ($0.05, 34) if low misses.
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): Sonnet 5.5 low ($0.35, 49%). Opus 5.5 low ($0.55, 53%) when the run touches names or facts. Upgrade: Opus 5.5 medium ($1.34, 61%) when the workflow branches.
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): Haiku 5.5 xhigh (pilot): 1511 at $0.12, vendor chart $0.27, near Sonnet 5.5 high at less than half the cost. Upgrade: Haiku 5.5 max (1618, $0.21) for final polish.
- **People, messages, money, records** (Customer and community messages, payments, exact names): Opus 5.5 low ($0.55, 39). Upgrade: Rarely. Opus 5.5 max adds 7 points for 11x the cost.
- **Computer use and browser work** (Clicking through web apps, forms, portals): Haiku 5.5 xhigh (pilot, 67.5%, $0.30). Upgrade: Haiku 5.5 max (72.4%, $0.62) ties Sonnet 5.5 high (73%, $1.50). Sonnet 5.5 xhigh (81%, $2.30) for must-succeed runs.
- **Agentic coding** (Multi-file changes, debugging, repo work): Opus 5.5 medium ($1.34, 53%). Upgrade: Opus 5.5 high ($1.82, 57%) for hard bugs.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): Haiku 5.5 max (pilot, $0.21, 33%), ahead of Opus 5.5 low (31%, $0.55). Upgrade: Opus 5.5 medium if the fix stalls.
- **Research and reasoning** (Analysis, tradeoffs, hard questions): Opus 5.5 low ($0.55, 48%). Vendor chart shows Sonnet 5.5 high at 48% for $0.08 per question. Upgrade: Opus 5.5 high ($1.82, 56%).
- **General agentic judgment** (Open-ended multistep tasks, planning): Opus 5.5 medium ($1.34, 51). Upgrade: Opus 5.5 high ($1.82, 54).

## Codex (OpenAI) - for Codex and ChatGPT
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): GPT-6 Luna max ($0.07, 38), best when the step calls tools (AutomationBench 53%). Upgrade: GPT-6.1 Sol low ($0.13, 42).
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): GPT-6 Luna max ($0.07, 53%). Upgrade: GPT-6.1 Sol medium ($0.21, 63%).
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): GPT-6 Luna max (1432, $0.07). Upgrade: GPT-6.1 Sol max (1575, $0.72).
- **People, messages, money, records** (Customer and community messages, payments, exact names): GPT-6.1 Sol high ($0.32, 41), verify names and figures. Upgrade: Rarely. Sol max ($0.72, 42) adds 1 point.
- **Computer use and browser work** (Clicking through web apps, forms, portals): GPT-6 Luna max (49%, $0.22). Sol and Astra not yet evaluated on this chart.
- **Agentic coding** (Multi-file changes, debugging, repo work): GPT-6.1 Sol medium ($0.21, 48%). Upgrade: GPT-6.1 Sol high ($0.32, 52%).
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): GPT-6.1 Sol low ($0.13, 31%). Upgrade: GPT-6.1 Sol medium ($0.21, 48%).
- **Research and reasoning** (Analysis, tradeoffs, hard questions): GPT-6.1 Sol medium ($0.21, 50%). Upgrade: GPT-6 Astra max ($3.26, 55%), rarely worth it.
- **General agentic judgment** (Open-ended multistep tasks, planning): GPT-6.1 Sol medium ($0.21, 48). Upgrade: GPT-6.1 Sol high ($0.32, 50).

## Antigravity (Google Gemini)
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): Gemini 3.8 Flash low (index 33, cost per task not published). Upgrade: Medium ($0.93, 40).
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): Gemini 3.8 Flash medium ($0.93, 61%). Upgrade: None. High scores 60%.
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): Gemini 3.8 Flash medium (1426, $0.93). Upgrade: High adds 10 Elo, not worth it.
- **People, messages, money, records** (Customer and community messages, payments, exact names): Gemini 3.8 Flash medium ($0.93, 29), below Opus 5.5 low and Sol low.
- **Computer use and browser work** (Clicking through web apps, forms, portals): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging, repo work): Gemini 3.8 Flash medium ($0.93, 20%), weak for coding. Upgrade: High also scores 20%.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): Gemini 3.8 Flash medium ($0.93, 20%).
- **Research and reasoning** (Analysis, tradeoffs, hard questions): Gemini 3.8 Flash high ($1.24, 48%).
- **General agentic judgment** (Open-ended multistep tasks, planning): Gemini 3.8 Flash medium ($0.93, 40). Upgrade: High adds 1 point, not worth it.
- **Antigravity (Gemini)** (Antigravity agent loops): Gemini 3.8 Flash medium for loops, refactors, and hard bugs. Low (33) for deterministic scripts. Upgrade: High only for reasoning-heavy work (HLE 48% vs 42%).

## Local model (LM Studio)
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): Gemma 4 26B-A4B ($0). In-house test: classification 6/6, reformatting 8/8, instruction following 6/6 on all three runs. Upgrade: Use Haiku 5.5 low when output must be valid JSON. Gemma broke JSON on 1 to 2 of 6 extractions.
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): Light use only. Tool calls 3/4 in-house, AutomationBench 2% (AA estimate). Validate every call. Upgrade: Sonnet 5.5 low.
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): Reformatting only. GDPval 569 (AA estimate).
- **People, messages, money, records** (Customer and community messages, payments, exact names): Never for recall. AA-Omniscience -51. It did answer UNKNOWN to 8/8 made-up facts when offered that option.
- **Computer use and browser work** (Clicking through web apps, forms, portals): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging, repo work): Not yet evaluated on Terminal-Bench.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): Not yet evaluated.
- **Research and reasoning** (Analysis, tradeoffs, hard questions): Not suitable. HLE 8.7% (Google card), money math 4/6 in-house.
- **General agentic judgment** (Open-ended multistep tasks, planning): Not suitable (index 17).

## Best value across all vendors
- **Mechanical text work**: Gemma on a local LM Studio server ($0 cloud). In the cloud, Haiku 5.5 low ($0.02, index 29). Not worth it: Sonnet or Opus for pure mechanical work. Gemma for anything that calls tools (AutomationBench 2%).
- **Scripted relays and tool workflows**: GPT-6 Luna max ($0.07, AutomationBench 53%), which matches Opus 5.5 low at 13% of the cost. Not worth it: Haiku 5.5 at any effort (36% at xhigh). Opus 5.5 high and up, Sonnet 5.5 xhigh and max: 1 to 2 points per cost doubling.
- **Documents from supplied facts**: Haiku 5.5 xhigh (GDPval 1511, $0.12). GPT-6 Luna max (1432, $0.07) if cost matters more than polish. Not worth it: Opus 5.5 high (1705) adds 87 Elo for 8.7x the cost. Sonnet 5.5 max. Haiku hallucinates often (AA-Omniscience 6 to 11), so supply the facts and check names and numbers.
- **People, messages, money, records**: GPT-6.1 Sol high ($0.32, AA-Omniscience 41). Sol low ($0.13, 38) for a cheaper first pass with verification. Not worth it: Haiku 5.5 (3 to 11) and Sonnet 5.5 (19 to 32) at any effort.
- **Computer use and browser work**: Haiku 5.5 xhigh (OSWorld 67.5% at $0.30 per attempt). Only Anthropic and Luna are on this chart. Not worth it: Sonnet 5.5 max (+2.9 points for 2.5x). Haiku for steps that type names, accounts, or payments.
- **Agentic coding**: GPT-6.1 Sol medium (Terminal-Bench 48%, $0.21), about a sixth of Opus 5.5 medium's cost. Not worth it: Opus 5.5 xhigh (+3 for 1.9x) and max (+0). Sonnet 5.5 max ($5.46).
- **Small, clear coding fixes**: GPT-6.1 Sol low ($0.13, Terminal-Bench 31%). Haiku 5.5 max ($0.21, 33%) in Claude. Not worth it: Opus 5.5 low for this work, since Haiku 5.5 max scores higher for 38% of the cost.
- **Research and reasoning**: GPT-6.1 Sol medium (HLE 50%, $0.21). Not worth it: Opus 5.5 xhigh and max: 2 to 3 points per cost doubling.
- **General agentic judgment**: GPT-6.1 Sol medium (index 48, $0.21). Not worth it: Opus 5.5 xhigh and max (+2 per doubling). Sonnet 5.5 high (47, $0.88) trails Opus 5.5 medium on every test.
- **Antigravity (Gemini)**: Gemini 3.8 Flash medium ($0.93 list, index 40) for loops, refactors, and hard bugs. Not worth it: High for coding or automation: it ties medium (Terminal-Bench 20% vs 20%, AutomationBench 60% vs 61%) for 33% more.

## Sources
- https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-medium-vs-claude-opus-5-5-low
- https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-high-vs-claude-opus-5-5-medium
- https://artificialanalysis.ai/models/comparisons/claude-opus-5-5-high-vs-claude-opus-5-5-xhigh
- https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-vs-claude-opus-5-5
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-xhigh-vs-claude-sonnet-5-5-low
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-high-vs-claude-sonnet-5-5-xhigh
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-low-vs-claude-4-5-haiku
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-medium-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-vs-claude-opus-5-5-low
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-claude-sonnet-5-5-low
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol
- turn23view0
- turn23view2
- https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-8-flash-medium
- https://artificialanalysis.ai/models/comparisons/gemma-4-26b-a4b-vs-gemini-3-8-flash-low

## Review status
Updated is the build/review date. Each point has its own checked date. Inaccessible sources retain dated values. Vendor charts remain approximate, read 2026-10-08.
Pending source refresh: Haiku 5.5 low, Gemma 4 26B-A4B reasoning
