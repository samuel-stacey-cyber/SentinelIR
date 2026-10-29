# Scope and purpose

[Back to overview](README.md)

## Current direction

- Fictional company staff portal -> fake accounts, documents and data.
- Achievable core route -> three flags in around 45–60 minutes.
- Two optional bonus challenges -> up to around 90 minutes with exploration.
- Clues and decoys throughout -> playful, but still professional and fair.
- Personal progress tracking -> no leaderboard planned.

## Research purpose

- `RQ1` -> use the literature to justify the design and evaluation.
- `RQ2` -> compare HTTP access logs alone with access + authentication logs for the same selected authentication activity.
- `RQ3` -> compare response plans produced from equivalent alert evidence, with and without guidance.

The extra web vulnerabilities make the CTF more varied. They do not extend RQ2 beyond authentication detection. Completing a flag does not establish that SentinelIR detected the attack correctly.

## Deferred

SQL injection, IDOR, XSS, SSRF and the full mail/bot/Git pipeline idea are deferred for this version. Automated response actions and a SentinelIR dashboard are outside scope.

The upload-to-shell bonus is subject to a containment and feasibility check. If it adds too much work, I will simplify or defer it after review.
