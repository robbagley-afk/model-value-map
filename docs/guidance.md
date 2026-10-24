# Model and Effort Guidance
Updated: 2026-10-24. Source: https://robbagley-afk.github.io/model-value-map/
Revision: 11d259d3736ede0670b2bcac0ef0e2de4e277958e1ae02f1f5f68db64107da10

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
GPT-6.1 Sol at medium effort. Reviewed 2026-10-24. Balanced capability and cost for everyday, multistep work. Use the task-specific picks below when your work needs something different. This is the maintained general-purpose pick, not a universal benchmark winner. A review is due after seven days. Source: https://artificialanalysis.ai/models/gpt-6-1-sol-medium

## Claude (Anthropic) - for Claude Code and Claude apps
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): Haiku 5.5 low ($0.02, 29). Upgrade: Haiku 5.5 medium ($0.05, 34) if low misses.
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): Sonnet 5.5 medium ($0.48, 55%). Opus 5.5 low ($0.55, 53%) when the run touches names or facts. Upgrade: Opus 5.5 medium ($1.34, 61%) when the workflow branches.
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): Haiku 5.5 max (pilot): 1619 at $0.21, near Sonnet 5.5 xhigh at a tenth of the cost. Upgrade: Rarely. Sonnet 5.5 xhigh (1728, $2.01) adds 110 Elo for 9.6x the cost.
- **People, messages, money, records** (Customer and community messages, payments, exact names): Opus 5.5 low ($0.55, 39). Upgrade: Rarely. Opus 5.5 max adds 7 points for 11x the cost.
- **Computer use and browser work** (Clicking through web apps, forms, portals): Haiku 5.5 xhigh (pilot, 67.5%, $0.30). Upgrade: Haiku 5.5 max (72.4%, $0.62) ties Sonnet 5.5 high (73%, $1.50). Sonnet 5.5 xhigh (81%, $2.30) for must-succeed runs.
- **Agentic coding** (Multi-file changes, debugging, repo work): Opus 5.5 high ($1.82, 57%). Upgrade: Rarely. Opus 5.5 xhigh ($3.46, 60%) adds 3 points for 1.90x the API task cost.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): Haiku 5.5 max (pilot, $0.21, 33%), ahead of Opus 5.5 low (31%, $0.55). Upgrade: Opus 5.5 high ($1.82, 57%) if the bounded fix fails its check.
- **Research and reasoning** (Analysis, tradeoffs, hard questions): Opus 5.5 medium ($1.34, 55%). Upgrade: Rarely. Opus 5.5 high ($1.82, 56%) adds 1 HLE point.
- **General agentic judgment** (Open-ended multistep tasks, planning): Opus 5.5 high ($1.82, 54). Upgrade: Rarely. Opus 5.5 xhigh ($3.46, 56) adds 2 index points.

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

## Gemini (Google)
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): Gemini 3.8 Flash low (index 33, cost per task not published), also for deterministic scripts. Upgrade: Medium ($0.93, 40).
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): Gemini 4 Argon high ($1.99, 78%) where available; paid API, eligible Antigravity App/CLI/extensions. Not available in Antigravity IDE. Upgrade: No measured higher effort. Antigravity IDE or ineligible plans: Gemini 3.8 Flash medium ($0.93). Argon API cost estimated $3.98 from December 1 assuming unchanged tokens; subscription usage is separate.
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): Gemini 4 Argon high ($1.99, 1624) where available; paid API, eligible Antigravity App/CLI/extensions. Not available in Antigravity IDE. Upgrade: No measured higher effort. Antigravity IDE or ineligible plans: Gemini 3.8 Flash medium ($0.93). Argon API cost estimated $3.98 from December 1 assuming unchanged tokens; subscription usage is separate.
- **People, messages, money, records** (Customer and community messages, payments, exact names): Gemini 4 Argon high ($1.99, 42) where available; paid API, eligible Antigravity App/CLI/extensions. Not available in Antigravity IDE. Upgrade: No measured higher effort. Antigravity IDE or ineligible plans: Gemini 3.8 Flash medium ($0.93). Argon API cost estimated $3.98 from December 1 assuming unchanged tokens; subscription usage is separate.
- **Computer use and browser work** (Clicking through web apps, forms, portals): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging, repo work): Gemini 4 Argon high ($1.99, 57%) where available; paid API, eligible Antigravity App/CLI/extensions. Not available in Antigravity IDE. Upgrade: No measured higher effort. Antigravity IDE or ineligible plans: Gemini 3.8 Flash medium ($0.93). Argon API cost estimated $3.98 from December 1 assuming unchanged tokens; subscription usage is separate.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): Gemini 3.8 Flash medium ($0.93, 20%) for a bounded Antigravity IDE fix; check the result. Upgrade: Gemini 4 Argon high ($1.99, 57%) in eligible App/CLI/extensions or API if the fix stalls; unavailable in Antigravity IDE.
- **Research and reasoning** (Analysis, tradeoffs, hard questions): Gemini 4 Argon high ($1.99, 57%) where available; paid API, eligible Antigravity App/CLI/extensions. Not available in Antigravity IDE. Upgrade: No measured higher effort. Antigravity IDE or ineligible plans: Gemini 3.8 Flash high ($1.24, 48%). Argon API cost estimated $3.98 from December 1 assuming unchanged tokens; subscription usage is separate.
- **General agentic judgment** (Open-ended multistep tasks, planning): Gemini 4 Argon high ($1.99, 53) where available; paid API, eligible Antigravity App/CLI/extensions. Not available in Antigravity IDE. Upgrade: No measured higher effort. Antigravity IDE or ineligible plans: Gemini 3.8 Flash medium ($0.93). Argon API cost estimated $3.98 from December 1 assuming unchanged tokens; subscription usage is separate.

## Grok (xAI)
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): Grok 4.6 low ($0.38, 35). Upgrade: Grok 4.6 medium ($1.14, 43).
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): Grok 4.6 high ($1.48, 67%).
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): Grok 4.6 medium (1612, $1.14). Upgrade: Grok 4.7 high (1707, $2.73).
- **People, messages, money, records** (Customer and community messages, payments, exact names): Grok 4.6 low ($0.38, 26), verify names and figures. Upgrade: Rarely. Grok 4.7 xhigh ($3.74, 32) adds 6 points.
- **Computer use and browser work** (Clicking through web apps, forms, portals): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging, repo work): Grok 4.6 high ($1.48, 21%). Upgrade: Rarely. Grok 4.7 high ($2.73, 25%) adds 4 points.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): Grok 4.6 high ($1.48, 21%). Upgrade: Rarely. Grok 4.7 high ($2.73, 25%) adds 4 points.
- **Research and reasoning** (Analysis, tradeoffs, hard questions): Grok 4.6 medium ($1.14, 42%). Upgrade: Rarely. Grok 4.6 xhigh ($1.75, 44%) adds 2 points.
- **General agentic judgment** (Open-ended multistep tasks, planning): Grok 4.6 medium ($1.14, 43). Upgrade: Rarely. Grok 4.7 high ($2.73, 46) adds 3 points.

## Local model (LM Studio)
- **Mechanical text work** (Classify, extract, reformat, dedupe, parse): Gemma 4 26B-A4B ($0) for long context, vision, and reformatting. Qwen3-14B 6-bit ($0) on client laptops for strict JSON extraction and triage. Upgrade: Use Qwen3-14B ($0) locally for strict JSON schema compliance (6/6 valid JSON, 0 syntax errors, 44/44 or 100% overall across 3 serial runs with temperature 0.0, prompted concise CoT, and schema example anchors; Gemma broke JSON on 1 to 2 of 6 extractions after audit). In the cloud, use Haiku 5.5 low ($0.02).
- **Scripted relays and tool workflows** (Fixed-step handoffs, connector runs, queue imports): Light use only. Tool calls 3/4 in-house, AutomationBench 2% (AA estimate). Validate every call. Upgrade: Sonnet 5.5 low.
- **Documents from supplied facts** (Drafts, summaries, slides, spreadsheets, reports): Reformatting only. GDPval 566 (AA estimate).
- **People, messages, money, records** (Customer and community messages, payments, exact names): Never for recall. AA-Omniscience -51. It did answer UNKNOWN to 8/8 made-up facts when offered that option.
- **Computer use and browser work** (Clicking through web apps, forms, portals): Not yet evaluated.
- **Agentic coding** (Multi-file changes, debugging, repo work): Gemma: Terminal-Bench 2.0, our run, 4-bit, thinking off: 17% (15 of 89). Older test, not on this chart.
- **Small, clear coding fixes** (Clear-repro bug fixes, UI polish, building to a spec): Not yet evaluated.
- **Research and reasoning** (Analysis, tradeoffs, hard questions): Not suitable. HLE 8.7% (Google card), money math 4/6 in-house.
- **General agentic judgment** (Open-ended multistep tasks, planning): Not suitable (index 17).

## Best value across all vendors
- **Mechanical text work**: Two-tier local offload ($0 cloud): Gemma on a local LM Studio server and Qwen3-14B on a local client workstation (44/44, 100% with 6/6 valid JSON and 4/4 tool calls). In the cloud, Haiku 5.5 low ($0.02, index 29). Not worth it: Sonnet or Opus for pure mechanical work. Gemma for anything that calls tools (AutomationBench 2%). Grok for mechanical work: Grok 4.6 low ($0.38, 35) costs 19x Haiku 5.5 low for 6 more points. Gemini 3.8 Flash medium ($0.93, 40) costs 13x GPT-6 Luna max for 2 more points. With Gemini, use Flash low (33) for deterministic scripts Newly measured Luna low ($0.0045, index 22) is a candidate for narrow supplied-input steps after a task check, not an established replacement for the maintained picks..
- **Scripted relays and tool workflows**: GPT-6 Luna max ($0.07, AutomationBench 53%), which matches Opus 5.5 low at 13% of the cost. Argon high (78%, $1.99 introductory through November 30) is the highest tracked AutomationBench score under $3; eligibility and task fit still need checking. Not worth it: Haiku 5.5 at any effort (36% at xhigh). Opus 5.5 high and up, Sonnet 5.5 xhigh and max: 1 to 2 points per cost doubling. Gemini 3.8 Flash high (60%) scores below medium ($0.93, 61%), which already trails GPT-6.1 Sol medium (63%, $0.21) Argon high costs $1.99 per AA task through November 30; estimated $3.98 from December 1 assuming unchanged tokens. Subscription caps and availability are separate..
- **Documents from supplied facts**: Haiku 5.5 max (GDPval 1619, $0.21). GPT-6 Luna max (1433, $0.07) if cost matters more than polish. Not worth it: Opus 5.5 high (1704) adds 86 Elo for 8.7x the cost. Sonnet 5.5 max. Haiku hallucinates often (AA-Omniscience 6 to 11), so supply the facts and check names and numbers. Grok 4.6 medium (1612, $1.14) roughly ties Haiku 5.5 max (1619, $0.21) at 5x the cost. Gemini 3.8 Flash medium (1423, $0.93) trails GPT-6 Luna max (1433, $0.07).
- **People, messages, money, records**: GPT-6.1 Sol high ($0.32, AA-Omniscience 41). Sol low ($0.13, 38) for a cheaper first pass with verification. Not worth it: Haiku 5.5 (3 to 11) and Sonnet 5.5 (19 to 32) at any effort. Grok (26 to 32) and Gemini 3.8 Flash (29 to 30) at any effort trail GPT-6.1 Sol low (38, $0.13) Argon high costs $1.99 per AA task through November 30; estimated $3.98 from December 1 assuming unchanged tokens. Subscription caps and availability are separate..
- **Computer use and browser work**: Haiku 5.5 xhigh (OSWorld 67.5% at $0.30 per attempt). Only Anthropic and Luna are on this chart. Not worth it: Sonnet 5.5 max (+2.9 points for 2.5x). Haiku for steps that type names, accounts, or payments.
- **Agentic coding**: GPT-6.1 Sol xhigh (Terminal-Bench 54%, $0.39). Opus 5.5 high scores 57% at $1.82; Argon high 57% at $1.99 introductory. The additional 3 points do not justify those multiples for general use. Not worth it: Opus 5.5 xhigh (+3 for 1.9x) and max (+0). Sonnet 5.5 max ($5.46). Grok at any effort (3 to 26%) trails Sol low (31%, $0.13). Gemini 3.8 Flash medium and high both score 20%; Argon high is the Google coding pick where available. Argon API price expires November 30; no subscription saving inferred.
- **Small, clear coding fixes**: GPT-6.1 Sol medium ($0.21, Terminal-Bench 48%) for a bounded first pass. Haiku 5.5 max ($0.21, 33%) is the Claude pilot; run a reproducible check. Not worth it: Opus 5.5 low for this work, since Haiku 5.5 max scores higher for 38% of the cost. Grok 4.7 low ($1.25, 16%) and Gemini 3.8 Flash medium ($0.93, 20%) trail Haiku 5.5 xhigh ($0.12, 29%).
- **Research and reasoning**: GPT-6.1 Sol low (HLE 47%, $0.13). Medium adds 3 points for 1.62x API task cost, below the rule. Use a task check. Argon high scores 57% at $1.99 where eligible. Not worth it: Opus 5.5 xhigh and max add only 2 to 3 HLE points per cost step. Grok tops out at 44%, below Sol low 47%. Argon high is $1.99 through November 30; estimated $3.98 thereafter with unchanged tokens. API cost is not subscription usage.
- **General agentic judgment**: GPT-6.1 Sol medium (index 48, $0.21). Not worth it: Opus 5.5 xhigh and max add only 2 index points per step. Sonnet 5.5 high (47, $0.88) trails Opus high (54, $1.82) on the task benchmarks. Grok 4.7 high/xhigh cost more than Sol medium for lower index scores. Gemini 3.8 Flash high adds 1 point over medium for 33% more; use Argon high where eligible. Fable high (51, $3.91) trails Opus high (54, $1.82) GPT-6 Astra low through xhigh are matched or beaten by cheaper Sol efforts on the index. Astra max (53, $3.26) adds only 1 point over Sol max (52, $0.72), below the value rule..

## Latest news
Dated news is a snapshot. Ignore an item after its expiry; offers do not establish subscription savings.
- 2026-10-15 **Argon introductory API pricing**: $2 input / $10 output per million tokens through November 30, then $4 / $20. API offer only; subscription allowances are separate. Expires 2026-12-01T00:00:00Z. Checked 2026-10-24. Source: https://ai.google.dev/gemini-api/docs/pricing?hl=en
- 2026-10-13 **Gemini 4 Argon broadly available**: Independent AutomationBench: 78% versus Sol Medium 63%, at $1.99 versus $0.21 per benchmark task. More capability comes at a higher task cost. Expires 2026-11-12T00:00:00Z. Checked 2026-10-15. Source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/ Independent evidence: https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-gpt-6-1-sol-medium
- 2026-10-07 **Sonnet 5.5 cache reads halved**: Cache reads fell to $0.10 per million tokens. Anthropic estimates about 20% lower cost on most agentic tasks; this is a vendor claim, not a measured subscription saving. Expires 2026-11-06T00:00:00Z. Checked 2026-10-24. Source: https://www.anthropic.com/claude-haiku-5-5

## Promotional pricing and expiry
Prices are date-dependent. Read the promotion end time before using a copied price. The live maps recheck the clock on load, once daily, and when a tab becomes visible. Static guidance is a dated snapshot; after a boundary, use the standard estimates below until the maintainer reviews recommendations. No subscription allowance or account-specific credits are assumed.
- **Gemini 3.8 Flash**: 50% introductory API pricing through 2026-12-31; expires 2027-01-01T00:00:00Z. Scope: Google AI Studio / Gemini Developer API paid Standard tier; not a subscription-plan discount. Checked 2026-10-24.
  USD per million input/output/cached-input tokens: 0.75 / 3.75 / 0.075; standard from 2027-01-01: 1.5 / 7.5 / 0.15.
  Conservative UTC cutoff: vendor lists dates but does not specify a timezone. Use January 1 at 00:00 UTC as a conservative display cutoff; billing follows vendor terms. AA reported medium/high costs already use introductory input/output/cache rates. Standard task estimates assume identical token usage; not a fresh benchmark run. Source: https://ai.google.dev/gemini-api/docs/pricing
  medium: reported introductory cost $0.93/task; estimated standard cost $1.86/task. Do not halve the reported cost again.
  high: reported introductory cost $1.24/task; estimated standard cost $2.48/task. Do not halve the reported cost again.
- **Gemini 4 Argon**: 50% introductory API pricing through 2026-11-30; expires 2026-12-01T00:00:00Z. Scope: Gemini Developer API paid Standard tier. No free tier. Subscription eligibility and Antigravity allowances are separate.. Checked 2026-10-24.
  USD per million input/output/cached-input tokens: 2 / 10 / 0.1; standard from 2026-12-01: 4 / 20 / 0.2.
  Conservative UTC display cutoff because the vendor states December 1 without a timezone; vendor billing terms remain authoritative. Exact offer start timestamp is not specified. AA high-effort cost $1.99 already includes introductory rates; post-expiry $3.98 assumes unchanged token usage and is an estimate, not a fresh benchmark measurement. Source: https://ai.google.dev/gemini-api/docs/pricing?hl=en
  high: reported introductory cost $1.99/task; estimated standard cost $3.98/task. Do not halve the reported cost again.

## Subscription usage offers (not API discounts)*
Goal: maximize useful completed work within the applicable usage limit. API cost per benchmark task is not a measurement of subscription allowance. A 50% allowance increase corresponds to about 33% lower effective cost per equal unit; 50% less counted usage can double eligible capacity. Weekly caps, eligibility and task quality still constrain value.
- **Claude artifact usage promotion***: 50% less five-hour session usage for eligible artifact work; approximately 2x eligible session capacity, not a blanket token discount. Ends October 15, 2026 at 11:59 PM Pacific (2026-10-16T07:00:00Z). Checked 2026-10-15.
Free (from October 7), Pro, Max and Team; excludes Enterprise. Eligible Claude chats and cloud tasks in the Claude app only.
Chat: next 10 messages after an artifact edit, up to the first 15 steps per reply. Cloud tasks in the Claude app: about 45 minutes when starting with Document, Presentation or Design, or up to 80 steps after an artifact edit.
For eligible document, slide and design work, consider Claude during this offer to stretch the five-hour allowance. Choose the lowest model and effort that passes your checks. API benchmark costs do not measure subscription allowance; no cross-vendor subscription winner is established.
* Does not apply to API use. No Claude API, Claude Code, local desktop tasks in the Claude app, scheduled/unattended tasks, usage-credit charges, older artifacts, standalone Claude Design, or Google Drive-created Docs/Sheets/Slides. Weekly allowance is unchanged. Source: https://support.claude.com/en/articles/17274727-artifact-usage-promotion
After expiry, standard usage applies; ignore this temporary recommendation.

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

## Review status
Analyst reviewed 2026-10-24. Unavailable and frozen rows retain historical dates. Material citation conflicts were corrected after direct source recovery. Independent API task costs, vendor-reported charts and subscription allowances remain separate. Local model scores and checked dates are unchanged. Recommendations were reviewed against the value rule with explicit task-specific exceptions and availability limits. The overall value leader remains Sol medium.
Pending source refresh: Google / Gemini 3.8 Flash / low — comparison omits cost/task; prior row and checked date preserved., Local / Gemma 4 26B-A4B / reasoning — frozen baseline; no refresh performed., Local / Qwen3 14B / none — comparison omits multiple fields and cost/task; prior row and checked date preserved., Grok 4.6 medium: collector candidate $1.35 rejected as token price; reopened AA comparison confirms $1.14 per task., Sol medium GDPval: reopened AA comparison confirms 1450, not collector candidate 1449., Argon low/medium: no complete independent effort evidence. Antigravity access is plan/product dependent; not available in Antigravity IDE., Expired Claude artifact offer: analyst source recovery unavailable; historical dates retained. No API or weekly-allowance effect., Recurring credits and account-specific offers require claim/eligibility checks and have no verified uniform token-price discount. They do not reduce chart costs.
