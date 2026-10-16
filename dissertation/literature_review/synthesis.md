# Literature Review - Synthesis

## RQ1 - Literature and Design Justification

Compare limitations across papers -> record supporting evidence + relevant page / section -> explain what this means for SentinelIR -> identify what still needs evaluating!

| Paper | Limitation and supporting evidence | Implication for SentinelIR | What needs evaluating |
| --- | --- | --- | --- |
| P02 | Photo galleries and thumbnails caused false positives -> Section 5.5 | Include benign lookalikes -> investigate whether authentication context helps distinguish them from attacks | Compare false alerts and precision across access-only and combined-log conditions |
| P02 | Low-intensity attacks could be missed within the detection window -> Section 5.5 | Justify thresholds and time windows -> include slower attack scenarios | Test how threshold and window choices affect recall and false alerts |
| P02 + P03 | Both show why detection needs more than a headline result | P-2 identifies normal lookalikes and missed low-intensity attacks; P03 reports high accuracy alongside lower recall | SentinelIR should test challenging scenarios and report false alerts + missed detections separately. |
| P04 | Evaluation focuses on generated-text alignment rather than users’ response-plan quality -> Section 4.3 | Keep guidance-output assessment separate from human response-plan assessment | Compare the appropriateness + completeness of users’ plans with and without guidance |
| P05 | Participants identified the burden of additional tools and the need for support usable under time pressure -> Section 5.4 | Consider concise prompts within SentinelIR’s existing alert workflow | Whether users can understand and apply the guidance without unnecessary effort |
| P05 | No summative evaluation establishing the aid’s effectiveness -> Discussion | Distinguish promising design + practitioner feedback from demonstrated performance improvement | Compare independently assessed response-plan quality with and without guidance |

## RQ3 - Investigation and Response Guidance

P01 + P04 + P05 -> address different aspects of supporting incident response. P01 examines investigation behaviour; P04 evaluates generated guidance; P05 develops a critical-thinking memory aid from practitioner needs.

P05 adds an important design consideration -> guidance should support critical thinking + consideration of the wider context, rather than encourage users to accept an alert or recommendation without checking it.

For SentinelIR -> consider prompts about supporting evidence, alternative explanations, missing information and the possible impact of response actions. These are proposed adaptations -> their value still needs testing.

Across these papers -> investigation support, generated-text alignment and formative feedback are different outcomes. They do not establish whether SentinelIR improves users’ response-plan appropriateness + completeness.
