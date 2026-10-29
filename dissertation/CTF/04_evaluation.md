# Evaluation

[Back to overview](README.md)

## RQ2 -> detection

Use reproducible scripted scenarios for the primary comparison. Replay the same saved activity through access-only and combined-log configurations, using independently recorded actions and checked outcomes as ground truth.

Include:

- Ordinary successful logins and typing mistakes.
- Repeated failures with and without later success.
- Multi-account guessing, including a slower variation.
- Decoy use, reported separately.

Compare precision, recall, false alerts and missed attacks. Define event/episode boundaries and alert matching before evaluation. Develop thresholds on pilot activity, then freeze them.

Student CTF activity provides a separate exploratory dataset. Unexpected behaviour is useful, but uncertain cases must not be assigned attack labels from guesses, flag submissions or questionnaire answers alone.

## RQ3 -> response-plan quality

Proposed approach -> each participant completes different, matched unseen scenarios with equivalent alert evidence, with and without guidance. Counterbalance scenario allocation and order. Ask for response plans and assess technical appropriateness and completeness using predefined criteria.

I would score the plans using a supervisor-reviewed rubric. A second assessor or independent check of a subset would help; no assessor is confirmed yet.

The follow-up week is my preferred time for these tasks, subject to advice on feasibility and participant workload.

## Reflections and reports

Participants can explain mitigations for weaknesses they exploited and optionally submit a short findings report. Analyse these separately from the controlled response-plan comparison; participants already know the attacks they performed.

Pilot feedback can improve guidance before it is frozen. Formal-study responses will not be used to tune guidance during that evaluation. Difficulty, usefulness and confidence ratings are separate from measured detection accuracy and response-plan quality.
