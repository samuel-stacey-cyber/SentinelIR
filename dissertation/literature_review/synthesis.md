# Literature Review - Synthesis

## RQ1 - Literature and Design Justification

Compare limitations across papers -> record supporting evidence + relevant page / section -> explain what this means for SentinelIR -> identify what still needs evaluating!

| Paper | Limitation and supporting evidence | Implication for SentinelIR | What needs evaluating |
| --- | --- | --- | --- |
| P02 | Photo galleries and thumbnails caused false positives -> Section 5.5 | Include benign lookalikes -> investigate whether authentication context helps distinguish them from attacks | Compare false alerts and precision across access-only and combined-log conditions |
| P02 | Low-intensity attacks could be missed within the detection window -> Section 5.5 | Justify thresholds and time windows -> include slower attack scenarios | Test how threshold and window choices affect recall and false alerts |
| P02 + P03 | Both show why detection needs more than a headline result | P-2 identifies normal lookalikes and missed low-intensity attacks; P03 reports high accuracy alongside lower recall | SentinelIR should test challenging scenarios and report false alerts + missed detections separately. |
| P04 | Evaluation focuses on generated-text alignment rather than users’ response-plan quality -> Section 4.3 | Keep guidance-output assessment separate from human response-plan assessment | Compare the appropriateness + completeness of users’ plans with and without guidance |

## RQ3 - Investigation and Response Guidance

P01 + P04 -> support different parts of the evidence-to-guidance process. P01 examines analysts’ investigation behaviour; P04 examines generated guidance. Neither establishes whether SentinelIR’s guidance improves users’ response plans.

For SentinelIR -> provide equivalent alert evidence across conditions + assess technical appropriateness and completeness using predefined criteria. Collect perceived usefulness separately -> a positive rating does not prove a technically correct plan.
