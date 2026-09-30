# SentinelIR — Refined Research Question Options

## Option 1: Log Evidence and Detection Correctness

**To what extent does combining HTTP access logs with application authentication logs improve the precision and recall of SentinelIR’s detection of web authentication attacks compared with using HTTP access logs alone?**

This question investigates whether additional authentication information improves detection correctness. Both configurations would be evaluated against the same underlying benign and malicious activity, using independently recorded ground truth.

## Option 2: Evidence and Response Planning

**To what extent does adding contextual evidence and investigation guidance to SentinelIR alerts improve the appropriateness and completeness of response plans produced by cybersecurity students compared with basic alert summaries?**

This question investigates whether alerts help users make better response decisions. Participants would receive comparable scenarios, with response plans assessed against predefined criteria. Perceived usefulness would be collected separately from the assessment of plan quality.

## Option 3: Technical Quality of Response Guidance

**How effectively can SentinelIR use log evidence and user-provided context to produce technically appropriate investigation and response guidance for suspected web authentication attacks in a controlled environment?**

This question examines the guidance itself: whether its recommendations are supported by the evidence, relevant to the scenario, and explicit about uncertainty and conditions requiring further investigation.

It would include benign scenarios that trigger alerts, so that the guidance is assessed on its ability to support verification as well as response.


# Combined Research Question

## Main Research Question

**To what extent can log evidence and evidence-linked response guidance improve the detection of web authentication attacks and the quality of response plans in a controlled environment?**

## Sub-Questions

**RQ1: TO what extent does combining HTTP access logs with application authentication logs improve SentinelIR's detection of selected web authentication attacks?**

**RQ2: To what extent does evidence-linked investigation and response guidance improve the quality of response plans produced by SentinelIR alerts?**

The study would examine three connected aspects:

1. **Detection correctness:** whether combining log sources improves precision and recall compared with access-log-only detection.
2. **Guidance quality:** whether recommendations are technically appropriate, supported by evidence, and clear about uncertainty.
3. **Response-plan quality:** whether contextual evidence and guidance help participants produce more appropriate and complete plans than basic alert summaries.

---
