# Model Value Map

Score against cost per task for Anthropic, OpenAI, Google, and a local Gemma model at every effort level, with the cheapest good choice for each kind of work.

- Live page: https://robbagley-afk.github.io/model-value-map/
- Text version for AI tools: [docs/guidance.md](docs/guidance.md) and [docs/guidance.json](docs/guidance.json)
- Refreshed on the 1st and 15th of each month.

## Use it in Claude Code or Codex

Add this line to your instructions file (`~/.claude/CLAUDE.md` for Claude Code, `~/.codex/AGENTS.md` for Codex):

> Before you recommend a model or effort level, read https://robbagley-afk.github.io/model-value-map/guidance.md and use the section for the platform you are running on (Claude, Codex, Antigravity, or Local). Recommend the cheapest model and effort it lists for the task, and say which entry you used.

To keep your copy current, create a scheduled task that runs every two weeks with the prompt in [share.json](share.json) (`task_prompt`), or copy it from the "Use this guide in Claude Code or Codex" section of the live page.

## Data

- `model_data.json`: every model and effort point with its source URL. Independent scores come from Artificial Analysis. Vendor chart points are read from launch-page images and are approximate.
- `sweetspots.json`: the pick for each kind of work, best value from any vendor first, then each vendor.
- `frontier.py`: prints the cost frontier for each benchmark. Run `python3 frontier.py model_data.json`.
- `gemma_eval/run_eval.py`: a 44-item test of a local Gemma model on LM Studio. Set `LMSTUDIO_URL` and run it. It never loads or swaps models.

Rule: an upgrade pays when it adds at least 5 points (or 75 Elo on GDPval) for each doubling of cost per task.

Scores change often. Check the date at the top of guidance.md before relying on a number.
