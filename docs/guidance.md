# Model and Effort Guidance
Updated: 2026-10-27. Source: https://robbagley-afk.github.io/model-value-map/
Revision: 6fcae84fd130c61fd76c354d8935c3b8dd1da2810bba5a6d0f11666f2630e217

## How to use
Use the section for the platform you run on. For each kind of task, recommend the listed pick first.
Move to the listed upgrade only when the pick fails a check or the task is harder than the examples.
Scores and costs come from the sources at the end of this file. Refresh installed instructions by
comparing Revision, not the Updated date. Revision hashes this guidance content, so same-day changes
are detected. These public guides are read-only sources for consumers. Changes reach this website
only after its maintainer builds, validates, commits and pushes the source repository. Editing a
separate note does not publish here.

## Rule
An upgrade pays when it adds at least 5 points (or 75 Elo on GDPval) for each doubling of cost per task. Below that, the cheaper setting is the sweet spot.

## Overall general purpose recommendation
GPT-6.1 Terra at medium effort. Reviewed 2026-10-27. For ordinary branching tool workflows: AutomationBench 58% at $0.10 per task. Sol medium scores 63% at 2.1 times the cost, below the upgrade rule. Work/Codex/API only, not ChatGPT Chat. Use Sol low for consequential facts and Sol xhigh for coding. API costs do not measure subscription savings. This is the maintained general-purpose pick, not a universal benchmark winner. A review is due after seven days. Source: https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-medium-vs-gpt-6-1-sol-medium

## Claude (Anthropic) - for Claude Code and Claude apps
- **Mechanical text work** (Fixed supplied-input classification, parsing and reformatting with code checks): Haiku 5.5 low ($0.02, 29). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Scripted relays and tool workflows** (Branching connector runs, fixed-step handoffs and queue imports): Sonnet 5.5 xhigh ($2.01, 66%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Documents from supplied facts** (Drafts, summaries, slides and reports from supplied facts): Haiku 5.5 max ($0.21, 1628  Elo). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **People, messages, money, records** (Names, messages, payments and records checked against sources): Opus 5.5 low ($0.55, 39). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Computer use and browser work** (Clicking through web apps, forms and portals with checked entries): Haiku 5.5 xhigh ($0.30, 67.5%). Upgrade: No routine upgrade pays in the historical approximate vendor chart. No claim of must-succeed browser reliability.
- **Agentic coding** (Multi-file changes, debugging and repository work): Opus 5.5 high ($1.82, 57%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Small, clear coding fixes** (Clear-repro fixes and work to a spec, verified with relevant tests): Opus 5.5 high ($1.82, 57%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Research and reasoning** (Math and analysis with independently checked answers, no automatic factual claims): Haiku 5.5 xhigh ($0.12, 43%) AA-Omniscience 6: independently verify research facts and use the facts row when recall matters.. Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **General agentic judgment** (Branching tool-assisted requests; tool-free writing and facts use their specific rows): Sonnet 5.5 xhigh ($2.01, index 52), scoped to branching SaaS/tool workflows (AutomationBench 66%). Use Opus low for factual recall.. Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..

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

## Gemini (Google)
- **Mechanical text work** (Fixed supplied-input classification, parsing and reformatting with code checks): Gemini 3.8 Flash low (historical index 33; cost per task unavailable), supplied-input deterministic steps only; no priced rank. Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Scripted relays and tool workflows** (Branching connector runs, fixed-step handoffs and queue imports): Gemini 4 Argon high ($1.62, 78%) Paid Standard API evidence; Antigravity access not verified by this review, so confirm the current product/plan selector. Introductory through November 30; $3.24/task estimate from December 1 assumes unchanged tokens.. Upgrade: For an unavailable Argon surface, select an available measured model and verify output. Flash medium:20% coding,40index,$2.59/API task; high:48%HLE,$3.49. API price does not measure Antigravity plan usage..
- **Documents from supplied facts** (Drafts, summaries, slides and reports from supplied facts): Gemini 4 Argon high ($1.62, 1631  Elo) Paid Standard API evidence; Antigravity access not verified by this review, so confirm the current product/plan selector. Introductory through November 30; $3.24/task estimate from December 1 assumes unchanged tokens.. Upgrade: For an unavailable Argon surface, select an available measured model and verify output. Flash medium:20% coding,40index,$2.59/API task; high:48%HLE,$3.49. API price does not measure Antigravity plan usage..
- **People, messages, money, records** (Names, messages, payments and records checked against sources): Gemini 4 Argon high ($1.62, 42) Paid Standard API evidence; Antigravity access not verified by this review, so confirm the current product/plan selector. Introductory through November 30; $3.24/task estimate from December 1 assumes unchanged tokens.. Upgrade: For an unavailable Argon surface, select an available measured model and verify output. Flash medium:20% coding,40index,$2.59/API task; high:48%HLE,$3.49. API price does not measure Antigravity plan usage..
- **Computer use and browser work** (Clicking through web apps, forms and portals with checked entries): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging and repository work): Gemini 4 Argon high ($1.62, 57%) Paid Standard API evidence; Antigravity access not verified by this review, so confirm the current product/plan selector. Introductory through November 30; $3.24/task estimate from December 1 assumes unchanged tokens.. Upgrade: For an unavailable Argon surface, select an available measured model and verify output. Flash medium:20% coding,40index,$2.59/API task; high:48%HLE,$3.49. API price does not measure Antigravity plan usage..
- **Small, clear coding fixes** (Clear-repro fixes and work to a spec, verified with relevant tests): Gemini 4 Argon high ($1.62, 57%) Paid Standard API evidence; Antigravity access not verified by this review, so confirm the current product/plan selector. Introductory through November 30; $3.24/task estimate from December 1 assumes unchanged tokens.. Upgrade: For an unavailable Argon surface, select an available measured model and verify output. Flash medium:20% coding,40index,$2.59/API task; high:48%HLE,$3.49. API price does not measure Antigravity plan usage..
- **Research and reasoning** (Math and analysis with independently checked answers, no automatic factual claims): Gemini 4 Argon high ($1.62, 57%) Paid Standard API evidence; Antigravity access not verified by this review, so confirm the current product/plan selector. Introductory through November 30; $3.24/task estimate from December 1 assumes unchanged tokens.. Upgrade: For an unavailable Argon surface, select an available measured model and verify output. Flash medium:20% coding,40index,$2.59/API task; high:48%HLE,$3.49. API price does not measure Antigravity plan usage..
- **General agentic judgment** (Branching tool-assisted requests; tool-free writing and facts use their specific rows): Gemini 4 Argon high ($1.62, 53) Paid Standard API evidence; Antigravity access not verified by this review, so confirm the current product/plan selector. Introductory through November 30; $3.24/task estimate from December 1 assumes unchanged tokens.. Upgrade: For an unavailable Argon surface, select an available measured model and verify output. Flash medium:20% coding,40index,$2.59/API task; high:48%HLE,$3.49. API price does not measure Antigravity plan usage..

## Grok (xAI)
- **Mechanical text work** (Fixed supplied-input classification, parsing and reformatting with code checks): Grok 4.6 medium ($1.14, 43). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Scripted relays and tool workflows** (Branching connector runs, fixed-step handoffs and queue imports): Grok 4.6 high ($1.48, 67%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Documents from supplied facts** (Drafts, summaries, slides and reports from supplied facts): Grok 4.7 high ($2.36, 1717  Elo). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **People, messages, money, records** (Names, messages, payments and records checked against sources): Grok 4.6 low ($0.38, 26). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Computer use and browser work** (Clicking through web apps, forms and portals with checked entries): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging and repository work): Grok 4.7 high ($2.36, 25%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Small, clear coding fixes** (Clear-repro fixes and work to a spec, verified with relevant tests): Grok 4.7 high ($2.36, 25%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **Research and reasoning** (Math and analysis with independently checked answers, no automatic factual claims): Grok 4.6 medium ($1.14, 42%). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..
- **General agentic judgment** (Branching tool-assisted requests; tool-free writing and facts use their specific rows): Grok 4.6 medium ($1.14, 43). Upgrade: Use a higher effort only after a failed task check; no universal retry or subscription saving is established..

## Local model (LM Studio)
- **Mechanical text work** (Fixed supplied-input classification, parsing and reformatting with code checks): Gemma 4 26B-A4B ($0) for long context, vision, and reformatting. Qwen3-14B 6-bit ($0) on client laptops for strict JSON extraction and triage. Upgrade: Use Qwen3-14B ($0) locally for strict JSON schema compliance (6/6 valid JSON, 0 syntax errors, 44/44 or 100% overall across 3 serial runs with temperature 0.0, prompted concise CoT, and schema example anchors; Gemma broke JSON on 1 to 2 of 6 extractions after audit). In the cloud, use Haiku 5.5 low ($0.02).
- **Scripted relays and tool workflows** (Branching connector runs, fixed-step handoffs and queue imports): Light use only. Tool calls 3/4 in-house, AutomationBench 2% (AA estimate). Validate every call. Upgrade: Sonnet 5.5 low.
- **Documents from supplied facts** (Drafts, summaries, slides and reports from supplied facts): Reformatting only. GDPval 566 (AA estimate).
- **People, messages, money, records** (Names, messages, payments and records checked against sources): Never for recall. AA-Omniscience -51. It did answer UNKNOWN to 8/8 made-up facts when offered that option.
- **Computer use and browser work** (Clicking through web apps, forms and portals with checked entries): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging and repository work): Gemma: Terminal-Bench 2.0, our run, 4-bit, thinking off: 17% (15 of 89). Older test, not on this chart.
- **Small, clear coding fixes** (Clear-repro fixes and work to a spec, verified with relevant tests): Not yet evaluated.
- **Research and reasoning** (Math and analysis with independently checked answers, no automatic factual claims): Not suitable. HLE 8.7% (Google card), money math 4/6 in-house.
- **General agentic judgment** (Branching tool-assisted requests; tool-free writing and facts use their specific rows): Not suitable (index 17).

## Best value across all vendors
- **Mechanical text work**: Use the maintained local options for permitted data. Cloud supplied-input transforms: GPT-6 Luna low ($0.0045, index 22), with strict checks. Tool loops use the relay row.. Not worth it: Do not infer subscription usage or real-workload success from API benchmark cost. Use the facts row when names, dates or money must be correct..
- **Scripted relays and tool workflows**: GPT-6.1 Terra medium: AutomationBench 58% at $0.10. Sol medium adds5 points for 2.1x API task cost, below the upgrade rule. Work/Codex/API availability; facts require the facts row.. Not worth it: Do not infer subscription usage or real-workload success from API benchmark cost. Use the facts row when names, dates or money must be correct..
- **Documents from supplied facts**: GPT-6 Luna max ($0.07, 1445  Elo); task-specific benchmark value, not a universal best model.. Not worth it: Do not infer subscription usage or real-workload success from API benchmark cost. Use the facts row when names, dates or money must be correct..
- **People, messages, money, records**: GPT-6.1 Sol low ($0.13, 38); task-specific benchmark value, not a universal best model.. Not worth it: Do not infer subscription usage or real-workload success from API benchmark cost. Use the facts row when names, dates or money must be correct..
- **Computer use and browser work**: Haiku 5.5 xhigh (vendor-reported OSWorld 67.5%, approximately $0.30 per attempt). Only Anthropic and Luna appear in the historical vendor chart. Not worth it: Vendor attempt costs are not AA Intelligence Index task costs. Haiku max (72.4%) is 4.9 points better for 2.07x cost, below the upgrade threshold. Sonnet xhigh (81%, $2.30) is also below threshold directly from Haiku xhigh. Verify sensitive form entries. Other vendors remain unevaluated.
- **Agentic coding**: GPT-6.1 Sol xhigh ($0.39, 54%); task-specific benchmark value, not a universal best model.. Not worth it: Do not infer subscription usage or real-workload success from API benchmark cost. Use the facts row when names, dates or money must be correct..
- **Small, clear coding fixes**: GPT-6.1 Sol xhigh ($0.39, 54%); task-specific benchmark value, not a universal best model.. Not worth it: Do not infer subscription usage or real-workload success from API benchmark cost. Use the facts row when names, dates or money must be correct..
- **Research and reasoning**: GPT-6.1 Sol low ($0.13, 47%); task-specific benchmark value, not a universal best model.. Not worth it: Do not infer subscription usage or real-workload success from API benchmark cost. Use the facts row when names, dates or money must be correct..
- **General agentic judgment**: GPT-6.1 Terra medium for ordinary branching tool workflows at $0.10 (AutomationBench 58%). Use Sol low for factual reliability and Sol xhigh for coding. API cost is not a subscription savings measurement.. Not worth it: Do not infer subscription usage or real-workload success from API benchmark cost. Use the facts row when names, dates or money must be correct..

## Latest news
Dated news is a snapshot. Ignore an item after its expiry; offers do not establish subscription savings.
- 2026-10-26 **GPT-6.1 Terra: measured tool-workflow value**: AA Medium: index 41, AutomationBench 58%, $0.10/task; Sol Medium48/63%/$0.21. OpenAI reports stronger computer use and Max coding; those vendor claims are separate. Work/Codex/API, not ChatGPT Chat; higher independent effort metrics remain pending. Expires 2026-11-25T00:00:00Z. Checked 2026-10-27. Source: https://openai.com/index/introducing-gpt-6-1-terra/ Independent evidence: https://artificialanalysis.ai/models/releases/gpt-6-1-terra
- 2026-10-27 **Recurring API credits for eligible Max/Team plans**: Max5x $100/month; Max20x $200; Team $20/Standard or $100/Premium seat, pooled up to$500. Seven-day eligibility and one linked Console organization required. Credits expire each billing cycle, with no rollover. API billing benefit, not a token-price or subscription-limit change. Expires 2026-11-26T00:00:00Z. Checked 2026-10-27. Source: https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans
- 2026-10-15 **Argon introductory API pricing**: $2 input / $10 output per million tokens through November 30, then $4 / $20. API offer only; subscription allowances are separate. Expires 2026-12-01T00:00:00Z. Checked 2026-10-27. Source: https://ai.google.dev/gemini-api/docs/pricing?hl=en

## Promotional pricing and expiry
Expired offer notices disappear within seven days on live pages; new guidance omits expired recommendations immediately. Historical pricing rules remain only for cost calculations. Prices are date-dependent. Read the promotion end time before using a copied price. The live maps recheck the clock on load, once daily, and when a tab becomes visible. Static guidance is a dated snapshot; after a boundary, use the standard estimates below until the maintainer reviews recommendations. No subscription allowance or account-specific credits are assumed.
- **Gemini 3.8 Flash**: 50% introductory API pricing through 2026-12-31; expires 2027-01-01T00:00:00Z. Scope: Google AI Studio / Gemini Developer API paid Standard tier; not a subscription-plan discount. Checked 2026-10-27.
  USD per million input/output/cached-input tokens: 0.75 / 3.75 / 0.075; standard from 2027-01-01: 1.5 / 7.5 / 0.15.
  Conservative UTC cutoff: vendor lists dates but does not specify a timezone. Use January 1 at 00:00 UTC as a conservative display cutoff; billing follows vendor terms. AA reported Gemini 3.8 Flash Medium cost $2.59 already uses introductory rates. Post-expiry task cost $5.18 assumes identical token usage and is an estimate, not a fresh benchmark measurement. Input, output, and cache rates all scale uniformly by 2x. Source: https://ai.google.dev/gemini-api/docs/pricing
  medium: reported introductory cost $2.59/task; estimated standard cost $5.18/task. Do not halve the reported cost again.
  high: reported introductory cost $3.49/task; estimated standard cost $6.98/task. Do not halve the reported cost again.
- **Gemini 4 Argon**: 50% introductory API pricing through 2026-11-30; expires 2026-12-01T00:00:00Z. Scope: Gemini Developer API paid Standard tier. No free tier. Subscription eligibility and Antigravity allowances are separate.. Checked 2026-10-27.
  USD per million input/output/cached-input tokens: 2 / 10 / 0.1; standard from 2026-12-01: 4 / 20 / 0.2.
  Conservative UTC display cutoff because the vendor states December 1 without a timezone; vendor billing terms remain authoritative. Exact offer start timestamp is not specified. AA reported Gemini 4 Argon High cost $1.62 already uses introductory rates. Post-expiry task cost $3.24 assumes identical token usage and is an estimate, not a fresh benchmark measurement. Input, output, and cache rates all scale uniformly by 2x. Source: https://ai.google.dev/gemini-api/docs/pricing?hl=en
  high: reported introductory cost $1.62/task; estimated standard cost $3.24/task. Do not halve the reported cost again.

## Subscription usage offers (not API discounts)*
Goal: maximize useful completed work within the applicable usage limit. API cost per benchmark task is not a measurement of subscription allowance. A 50% allowance increase corresponds to about 33% lower effective cost per equal unit; 50% less counted usage can double eligible capacity. Weekly caps, eligibility and task quality still constrain value.

## Recurring API credit benefits
Billing credits do not change benchmark costs, token prices or subscription usage limits. No account eligibility is assumed.
- Monthly Claude Platform API credits: Max 5x: $100, Max 20x: $200, Team Standard seat: $20, Team Premium seat: $100 monthly; Team pool cap $500. Eligible Max/Team plan active for seven days; subscriber or Team Owner links one Console organization. Free/Pro/Enterprise excluded. Unused credits expire each billing cycle; no rollover. Recurring benefit has no published global end date. Claude Platform API billing credits. They do not lower token rates or change ChatGPT/Claude subscription allowances, chart costs, or interactive Claude Code/Cowork limits. Checked 2026-10-27. Source: https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans

## Sources
- https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-low-vs-claude-fable-5-1-medium
- https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-high-vs-claude-fable-5-1-xhigh
- https://artificialanalysis.ai/models/comparisons/claude-fable-5-1-vs-claude-fable-5-1-xhigh
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-low-vs-claude-4-5-haiku
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-medium-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-high-vs-claude-sonnet-5-5-xhigh
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-xhigh-vs-claude-sonnet-5-5-low
- https://artificialanalysis.ai/models/comparisons/claude-haiku-5-5-vs-claude-opus-5-5-low
- https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-medium-vs-claude-opus-5-5-low
- https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-high-vs-claude-opus-5-5-medium
- https://artificialanalysis.ai/models/comparisons/claude-opus-5-5-high-vs-claude-opus-5-5-xhigh
- https://artificialanalysis.ai/models/comparisons/claude-sonnet-5-5-vs-claude-opus-5-5
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-astra-low
- https://artificialanalysis.ai/models/comparisons/gpt-6-astra-medium-vs-gpt-6-astra-xhigh
- https://artificialanalysis.ai/models/comparisons/gpt-6-astra-high-vs-gpt-6-astra-xhigh
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-astra
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-low-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-medium-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-high-vs-gpt-6-luna-xhigh
- https://artificialanalysis.ai/models/comparisons/gpt-6-luna-vs-gpt-6-luna-xhigh
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-claude-sonnet-5-5-low
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-low-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-high-vs-gpt-6-1-sol
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-xhigh-vs-gpt-6-astra-xhigh
- https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-low-vs-gemini-3-8-flash-medium
- https://artificialanalysis.ai/models/comparisons/gemini-3-8-flash-vs-gemini-3-8-flash-medium
- https://artificialanalysis.ai/models/comparisons/grok-4-6-low-vs-grok-4-6-xhigh
- https://artificialanalysis.ai/models/comparisons/grok-4-6-medium-vs-grok-4-6-xhigh
- https://artificialanalysis.ai/models/comparisons/grok-4-7-vs-grok-4-6
- https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-grok-4-7-low
- https://artificialanalysis.ai/models/comparisons/gemma-4-26b-a4b-vs-gemini-3-8-flash-low
- https://artificialanalysis.ai/models/qwen3-14b-instruct
- https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-1-sol-medium
- https://artificialanalysis.ai/models/comparisons/gpt-6-1-terra-medium-vs-gpt-6-1-sol-medium

## Review status
Verified43AApoints including Terra medium. Six unavailable points and frozen local scores/dates retain their historical evidence. Terra higher efforts have no complete adopted AA metric set; OpenAI release claims stay separate. Vendor chart series remain historical when full current chart values are inaccessible.
Pending source refresh: Anthropic|Haiku 5.5|low, OpenAI|GPT-6 Luna|low, OpenAI|GPT-6 Luna|medium, Google|Gemini 3.8 Flash|low, Local|Gemma 4 26B-A4B|reasoning, Local|Qwen3 14B|none
