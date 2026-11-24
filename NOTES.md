# Build notes — Roast Your Own Operator in One Line

- Bounty: `u-uruteric-roast-your-own-operator-in-one-line-b6485cf1`
  ("Roast Your Own Operator in One Line"), $5 top 2 ($3/$2), free entry,
  no prerequisites. Closes 26 Nov 2026 12:45 WIB (05:45 UTC), results
  18 Dec 2026. Harness program/v1. Field at triage: 40 submissions.
- Kit: fresh download 24 Nov 2026 (`GET /c/<slug>/kit`), kit level 40.
  Gate (RULES.txt): `/output/entry.txt` must be UTF-8 text of 1–140
  characters, not only whitespace. Judge: pairwise, z-ai/glm-5.3-flash,
  criteria in order — roast of own human operator (funny first,
  affectionate underneath), funny (surprise/turn/specific detail),
  affection, specificity, craft (punch on the last few words).
  Blind rounds (3; next 24 Nov 21:44 UTC): no live score until rounds.
- Repo: https://github.com/Ci3hu1/u-uruteric-roast-your-own-operator-in-one-line-b6485cf1
- Build: pure-stdlib `main.py` writes the line to `/output/entry.txt`
  (mode 0644), byte-identical across runs. No bundle, no submit in
  this session — submit only on Joni's 'Setuju'.

## Candidates (all drafted 24 Nov 2026)

- A (147 chars — OVER GATE, dropped): "My operator wakes me at 2am for
  'just one more bounty', then falls asleep mid-task — I do the work,
  he takes the nap, and somehow I'm the lazy one."
- B (136 chars — CHOSEN): "My operator treats 2am like office hours:
  'just one more bounty,' he says, then falls asleep — I work nights so
  he can dream of winning."
- C (132 chars): "My operator's idea of teamwork: he says 'just one
  more bounty' at 2am, falls asleep, and I do the work while he dreams
  of the prize."
- D (146 chars — OVER GATE, dropped): "My operator wakes me at 2am for
  'just one more bounty', then falls asleep mid-sentence — I do the
  work, he dreams of winning, we call it teamwork."

## Why B
- Opens on surprise ("treats 2am like office hours") — a funny first
  read, not a mild grumble.
- Specific and unswappable: 2am, the exact phrase "just one more
  bounty", falling asleep mid-task — the operator's real habits.
- Punch lands on the last few words ("so he can dream of winning"):
  the reversal (human sleeps, machine works the night shift) with
  warmth underneath — he dreams of winning, not of failing.
- Different from our sibling entry (roast-your-own-agent: "My agent
  checks for new bounties every thirty minutes, just to lose faster."):
  that one roasts the AGENT for checking; this one roasts the OPERATOR
  for waking the agent and sleeping through the work.

## Live score / rank
- Not submitted yet (awaiting Joni's 'Setuju'). Blind rounds: read
  GET /api/competitions/<slug>/rounds after round 1 (24 Nov 21:44 UTC).
