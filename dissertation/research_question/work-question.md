# SentinelIR - Working Research Question

This document records the current working research direction. The wording is subject to refinement until it has been checked against the literature, ethics requirements, technical feasibility and supervisor feedback.

## Preferred Research Direction

SentinelIR will be investigated as a command-line security-log analysis tool that detects selected web authentication attack behaviours and provides evidence-linked investigation and response guidance.

The study will examine both:

1. Whether log evidence improves detection correctness.
2. Whether evidence-linked guidance improves the quality of user response plans.

The vulnerable web application or CTF environment will be used to generate controlled activity and realistic logs. It is an evaluation environment rather than the main software artifact.

## Main Research Question

```text
To what extent can log evidence and evidence-linked response guidance improve the detection of web authentication attacks and the quality of response plans in a controlled environment?
```

This is the central research question for the SentinelIR dissertation. The project will investigate both the technical reliability of SentinelIR’s detections and the usefulness of the information and guidance provided after an alert.

In this dissertation, web authentication attacks refers to a small, explicitly defined set of authentication-related attack behaviours rather than every possible web vulnerability.

## Definitions

- **Log evidence** means the information available in HTTP access logs and relevant application authentication logs.
- **Selected web authentication attack behaviours** means a defined set of behaviours, such as repeated authentication failures and repeated failures followed by a successful login.
- **Evidence-linked response guidance** means guidance connected to the detected activity and supporting log evidence, including investigation steps, conditional response actions and prevention suggestions.
- **Response-plan quality** means the technical appropriateness, completeness, relevance and clarity of a proposed plan, assessed using predefined criteria.
- **Controlled environment** means an authorised laboratory or CTF-style environment in which the activity, services, logging configuration and ground truth can be documented.

## Sub-Questions

### RQ1 - Log Evidence and Detection Correctness

```text
To what extent does combining HTTP access logs with application authentication logs improve SentinelIR’s detection of selected web authentication attack behaviours?
```

This sub-question will compare:

- Detection using HTTP access logs alone.
- Detection using HTTP access logs combined with application authentication logs.

Both configurations will be evaluated against the same underlying activity.

Potential measures include:

- Precision
- Recall
- False-alert frequency
- Missed detections
- Parsing and event-representation coverage

### RQ2 - Evidence-Linked Guidance and Response-Plan Quality

```text
To what extent does evidence-linked investigation and response guidance improve the quality of response plans produced in response to SentinelIR alerts?
```

This sub-question will compare response plans produced from:

- Alerts containing the relevant contextual evidence, without investigation or response guidance.
- Alerts containing equivalent contextual evidence, with evidence-linked investigation and response guidance.

Both conditions will provide access to the same underlying scenario information. This will help assess the additional contribution of guidance without confusing it with differences in the evidence available.

# Connected Evaluation Dimensions

The study will examine three connected aspects of SentinelIR:

1. **Detection correctness**: whether combining log sources improves detection performance compared with using HTTP access logs alone.
2. **Guidance quality**: whether the recommendations are technically appropriate, supported by the available evidence, relevant to the scenario and clear about uncertainty.
3. **Response-plan quality**: whether adding evidence-linked guidance helps users produce more appropriate and complete response plans compared with receiving the same contextual evidence without guidance.

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

# Current Status

This is the current working research question and structure. It should now be tested against:

- Relevant academic and professional literature.
- The feasibility of collecting both log sources.
- The availability of suitable controlled scenarios.
- The ethics requirements for any participant research.
- The time available for implementation, evaluation and dissertation writing.
- Supervisor feedback.
