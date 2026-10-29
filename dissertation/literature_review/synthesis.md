# Literature Review - Synthesis

## RQ1 - Literature and Design Justification

Compare limitations across papers -> record supporting evidence + relevant page / section -> explain what this means for SentinelIR -> identify what still needs evaluating!

| Paper | Limitation and supporting evidence | Implication for SentinelIR | What needs evaluating |
| --- | --- | --- | --- |
| P02 | Photo galleries and thumbnails caused false positives -> Section 5.5 | Include benign lookalikes -> investigate whether authentication context helps distinguish them from attacks | Compare false alerts and precision across access-only and combined-log conditions |
| P02 | Low-intensity attacks could be missed within the detection window -> Section 5.5 | Justify thresholds and time windows -> include slower attack scenarios | Test how threshold and window choices affect recall and false alerts |
| P02 + P03 | Both show why detection needs more than a headline result | P02 identifies normal lookalikes and missed low-intensity attacks; P03 reports high accuracy alongside lower recall | SentinelIR should test challenging scenarios and report false alerts + missed detections separately. |
| P04 | Evaluation focuses on generated-text alignment rather than users’ response-plan quality -> Section 4.3 | Keep guidance-output assessment separate from human response-plan assessment | Compare the appropriateness + completeness of users’ plans with and without guidance |
| P05 | Participants identified the burden of additional tools and the need for support usable under time pressure -> Section 5.4 | Consider concise prompts within SentinelIR’s existing alert workflow | Whether users can understand and apply the guidance without unnecessary effort |
| P05 | No summative evaluation establishing the aid’s effectiveness -> Discussion | Distinguish promising design + practitioner feedback from demonstrated performance improvement | Compare independently assessed response-plan quality with and without guidance |
| P06 | Filtering excluded known malicious activity -> Section 6.1; incomplete logs hindered compromise confirmation -> Section 8 | Include difficult scenarios + independently recorded ground truth; distinguish suspicion from confirmation | Recall / false-alert trade-offs and whether evidence supports each conclusion |
| P02 + P03 + P06 | Different input sources and evaluation labels -> their headline findings are not directly interchangeable | Explain each study's unit, data and limitations before comparing approaches | SentinelIR's own matched access-only and combined-log comparison |
| P07 | Experts rated `6/12 IACD + 5/12 NIST` playbooks insufficiently detailed; missing verification steps and communication were identified | Provide guidance explaining what to check, when response actions are appropriate + who needs informing | Assess response-plan completeness + technical appropriateness |
| P07 | Successful responses in the third exercise followed revised playbooks, practice + mentoring | Keep training and other support consistent when comparing guidance conditions | Whether guidance improves plans when both conditions receive equivalent evidence |

## RQ2 - Detection Using Combined Logs

P02 + P03 + P06 -> useful detection evidence from different inputs: flows, access logs and enriched authentication activity. Their results motivate a comparison; they do not answer SentinelIR's combined-log question.

P06 -> feature-removal analysis in Appendix C is useful context for asking what information contributes to detection. It is a different comparison from SentinelIR's proposed one.

For SentinelIR -> run both conditions against the same controlled activity, record ground truth separately + include benign mistakes and challenging attacks. Report precision + recall without assuming improvement.

## RQ3 - Investigation and Response Guidance

P01 + P04 + P05 -> address different aspects of supporting incident response. P01 examines investigation behaviour; P04 evaluates generated guidance; P05 develops a critical-thinking memory aid from practitioner needs.

P05 adds an important design consideration -> guidance should support critical thinking + consideration of the wider context, rather than encourage users to accept an alert or recommendation without checking it.

For SentinelIR -> consider prompts about supporting evidence, alternative explanations, missing information and the possible impact of response actions. These are proposed adaptations -> their value still needs testing.

Across these papers -> investigation support, generated-text alignment and formative feedback are different outcomes. They do not establish whether SentinelIR improves users’ response-plan appropriateness + completeness.

P06 -> possible addition to evidence-linked guidance: show why activity is suspicious + what still needs checking. This is my proposed design implication, not evidence that response plans improve. RQ3 still needs a direct human comparison.

P07 -> adds expert assessment of actual playbooks + observations of their use. Unlike P04's text-similarity measures and P05's formative feedback, it examines whether plans contain enough correct information for practical use.

P05 + P07 -> guidance needs to support critical thinking while providing enough practical detail. Positive opinions about a tool do not necessarily mean the resulting plans are complete or correct.

P07 separates `completeness` (covering the response from beginning to end) from `accuracy` (avoiding unnecessary or incorrect tasks) -> Sections 3.1.4 + 3.2.3. For SentinelIR -> adapt these into predefined criteria for checking evidence, appropriate conditional actions + relevant follow-up. These would be my adapted criteria, not an already validated SentinelIR scoring scale.

The third exercise was more successful after playbook revisions, practice + mentoring. These changed together -> the study does not isolate the effect of guidance alone.

For SentinelIR -> compare equivalent alert evidence with/without guidance, keep training comparable + assess response plans separately from questionnaire opinions. P07 informs this evaluation but does not directly answer RQ3.
