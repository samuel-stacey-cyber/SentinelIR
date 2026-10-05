# SentinelIR - Working Research Question

## Preferred Research Direction

SentinelIR will be investigated as a command-line security-log analysis tool that detects selected web authentication attack behaviours and provides evidence-linked investigation and response guidance.

The study will examine both:

1. How combining log sources affects detection precision and recall.
2. How evidence-linked guidance affects the technical appropriateness and completeness of user response plans.

The vulnerable web application or CTF environment will be used to generate controlled activity and realistic logs. It is an evaluation environment rather than the main software artifact.

## Main Research Question

```text
How does combining HTTP access and application authentication logs affect SentinelIR’s detection of selected web authentication attack behaviours, and how does evidence-linked guidance affect users’ response-plan quality in a controlled environment?
```

## Definitions

- **Log evidence** means the information available in HTTP access logs and relevant application authentication logs.
- **Selected web authentication attack behaviours** means a defined set of behaviours, such as repeated authentication failures and repeated failures followed by a successful login.
- **Evidence-linked response guidance** means guidance connected to the detected activity and supporting log evidence, including investigation steps, conditional response actions and prevention suggestions.
- **Response-plan quality** means the technical appropriateness and completeness of a proposed plan, assessed using predefined criteria. Relevance and clarity may be included as supporting criteria.
- **Controlled environment** means an authorised laboratory or CTF-style environment in which the activity, services, logging configuration and ground truth can be documented.

## Sub-Questions

### RQ1 - Log Evidence and Detection Correctness

```text
How does combining HTTP access logs with application authentication logs affect the precision and recall of SentinelIR’s detection of selected web authentication attack behaviours compared with using HTTP access logs alone?
```

This sub-question will compare:

- Detection using HTTP access logs alone.
- Detection using HTTP access logs combined with application authentication logs.

Measures include:

- Precision (primary measure)
- Recall (primary measure)
- False-alert frequency
- Missed detections
- Parsing and event-representation coverage

### RQ2 - Evidence-Linked Guidance and Response-Plan Quality

```text
How does providing evidence-linked investigation and response guidance alongside SentinelIR alerts affect the technical appropriateness and completeness of users’ response plans compared with presenting equivalent alert evidence without guidance?
```

This sub-question will compare response plans produced from:

- Alerts containing the relevant contextual evidence, without investigation or response guidance.
- Alerts containing equivalent contextual evidence, with evidence-linked investigation and response guidance.

The response plans produced by users will be assessed for technical appropriateness and completeness using predefined criteria.

# Connected Evaluation Dimensions

The study will examine three connected aspects of SentinelIR:

1. **Detection correctness**: how combining log sources affects detection precision and recall compared with using HTTP access logs alone.
2. **Guidance quality**: whether the recommendations are technically appropriate, supported by the available evidence, relevant to the scenario and clear about uncertainty.
3. **Response-plan quality**: how adding evidence-linked guidance affects the technical appropriateness and completeness of users’ response plans compared with receiving the same contextual evidence without guidance.

# Proposed Evaluation Structure

The study will use controlled scenarios involving selected web authentication behaviours and activity.

The evaluation will:

1. Generate predefined normal and malicious activity.
2. Record independent ground truth describing what occurred.
3. Capture HTTP access and application authentication logs.
4. Analyse comparable activity using the selected SentinelIR configurations.
5. Compare detection results against the ground truth.
6. Present selected alerts with equivalent contextual evidence, with and without investigation and response guidance.
7. Assess the resulting response plans using predefined criteria.
8. Analyse correct detections, missed detections, false alerts, guidance quality and response-plan quality.

# Scope Boundaries

The dissertation will:

- Focus on selected web authentication attack behaviours.
- Evaluate SentinelIR as the main software artifact.
- Use a controlled application or CTF environment to generate realistic evidence.
- Treat alerts as indicators requiring investigation rather than automatic proof of compromise.
- Leave operational response decisions with the user.
- Keep automated response execution as future work.
- Keep the web UI, database, multi-user accounts, phone integration and multi-node deployment outside the dissertation implementation.
- Avoid claiming that SentinelIR detects all web vulnerabilities.
