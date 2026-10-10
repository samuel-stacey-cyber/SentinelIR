# Table of Contents

- [Table of Contents](#table-of-contents)
- [List of Tables](#list-of-tables)
- [List of Figures](#list-of-figures)
- [List of Abbreviations](#list-of-abbreviations)
- [Abstract](#abstract)
- [1. Introduction](#1-introduction)
- [2. Background and Literature Review](#2-background-and-literature-review)
  - [2.1 Web Authentication Attacks](#21-web-authentication-attacks)
  - [2.2 Security Logs and Log Evidence](#22-security-logs-and-log-evidence)
  - [2.3 Detection of Authentication Attacks](#23-detection-of-authentication-attacks)
  - [2.4 Security Alerts and Investigation](#24-security-alerts-and-investigation)
  - [2.5 Investigation and Response Guidance](#25-investigation-and-response-guidance)
  - [2.6 Evaluation Approaches](#26-evaluation-approaches)
  - [2.7 Literature Review Summary and Research Gap](#27-literature-review-summary-and-research-gap)
- [3. Methodology](#3-methodology)
  - [3.1 Research Design](#31-research-design)
  - [3.2 RQ1 Literature Review Approach](#32-rq1-literature-review-approach)
  - [3.3 RQ2 Detection Evaluation](#33-rq2-detection-evaluation)
  - [3.4 RQ3 Response-Plan Evaluation](#34-rq3-response-plan-evaluation)
  - [3.5 Data Collection and Analysis](#35-data-collection-and-analysis)
  - [3.6 Ethical Considerations](#36-ethical-considerations)
  - [3.7 Methodological Limitations](#37-methodological-limitations)
- [4. SentinelIR System Design and Implementation](#4-sentinelir-system-design-and-implementation)
  - [4.1 Requirements and Design Goals](#41-requirements-and-design-goals)
  - [4.2 System Architecture](#42-system-architecture)
  - [4.3 Log Collection and Parsing](#43-log-collection-and-parsing)
  - [4.4 Event Representation and Correlation](#44-event-representation-and-correlation)
  - [4.5 Detection Rules](#45-detection-rules)
  - [4.6 Alert Evidence](#46-alert-evidence)
  - [4.7 Investigation and Response Guidance](#47-investigation-and-response-guidance)
  - [4.8 Reporting and CLI Workflow](#48-reporting-and-cli-workflow)
  - [4.9 Testing and Validation](#49-testing-and-validation)
- [5. Evaluation and Results](#5-evaluation-and-results)
  - [5.1 Evaluation Environment](#51-evaluation-environment)
  - [5.2 RQ2 Results](#52-rq2-results)
  - [5.3 RQ3 Results](#53-rq3-results)
  - [5.4 Guidance Quality Results](#54-guidance-quality-results)
  - [5.5 Additional Findings](#55-additional-findings)
- [6. Discussion](#6-discussion)
  - [6.1 Answer to RQ1](#61-answer-to-rq1)
  - [6.2 Answer to RQ2](#62-answer-to-rq2)
  - [6.3 Answer to RQ3](#63-answer-to-rq3)
  - [6.4 Comparison with Previous Research](#64-comparison-with-previous-research)
  - [6.5 Contribution to Cybersecurity Practice](#65-contribution-to-cybersecurity-practice)
  - [6.6 Limitations](#66-limitations)
  - [6.7 Future Improvements](#67-future-improvements)
- [7. Conclusion and Future Work](#7-conclusion-and-future-work)
- [References](#references)
- [Appendices](#appendices)

# List of Tables

# List of Figures

# List of Abbreviations

# Abstract

Brief summary of the problem, research questions, methodology, main findings and contribution.

# 1. Introduction

- Background and motivation
- Problem statement
- SentinelIR overview
- Research aim
- Main research question
- Sub-questions
- Research objectives
- Scope and boundaries
- Expected contribution
- Dissertation structure

# 2. Background and Literature Review

## 2.1 Web Authentication Attacks

Discuss repeated authentication failures, successful authentication following failures and relevant benign behaviours.

## 2.2 Security Logs and Log Evidence

Discuss HTTP access logs, application authentication logs, their strengths, limitations and how they can be correlated.

## 2.3 Detection of Authentication Attacks

Review rule-based, statistical and other relevant detection approaches. Discuss precision, recall, false alerts and missed detections.

## 2.4 Security Alerts and Investigation

Discuss alert interpretation, contextual evidence, analyst investigation and uncertainty.

## 2.5 Investigation and Response Guidance

Review evidence-linked guidance, decision support, response planning and human-centred cybersecurity tools.

## 2.6 Evaluation Approaches

Discuss controlled environments, ground truth, detection evaluation, response-plan rubrics and participant-based studies.

## 2.7 Literature Review Summary and Research Gap

Summarise what the literature establishes, where studies disagree or have limitations, and what SentinelIR will investigate. Address RQ1 by linking supported limitations to design choices and evaluation needs.

# 3. Methodology

## 3.1 Research Design

Explain how the critical literature comparison answers RQ1 and informs the controlled evaluations for RQ2 and RQ3.

## 3.2 RQ1 Literature Review Approach

Describe the search, selection, critical appraisal and comparison of papers -> explain how supported limitations inform SentinelIR’s design and evaluation.

## 3.3 RQ2 Detection Evaluation

- Activity scenarios
- HTTP access-log condition
- Combined-log condition
- Ground truth
- Event matching and detection unit
- Precision and recall
- False alerts and missed detections

## 3.4 RQ3 Response-Plan Evaluation

- Participants
- Scenario design
- Evidence-equivalent conditions
- Guidance condition
- Response-plan tasks
- Assessment rubric
- Assessor consistency

## 3.5 Data Collection and Analysis

Explain how logs, detection outputs, response plans and supporting measures will be recorded and analysed.

## 3.6 Ethical Considerations

Discuss the controlled environment, participant consent, data handling, risks and ethics approval.

## 3.7 Methodological Limitations

Explain foreseeable limitations in the scenarios, participants, datasets and comparisons.

# 4. SentinelIR System Design and Implementation

## 4.1 Requirements and Design Goals

Link the requirements and design choices to the literature comparison in RQ1 -> explain what will be tested through RQ2 and RQ3.

## 4.2 System Architecture

## 4.3 Log Collection and Parsing

## 4.4 Event Representation and Correlation

## 4.5 Detection Rules

## 4.6 Alert Evidence

## 4.7 Investigation and Response Guidance

## 4.8 Reporting and CLI Workflow

## 4.9 Testing and Validation

Explain relevant implementation testing and distinguish work completed before the dissertation from work developed during it.

# 5. Evaluation and Results

## 5.1 Evaluation Environment

Describe the vulnerable application or CTF environment, logging configuration and scenarios.

## 5.2 RQ2 Results

Present detection results for both log configurations, including precision, recall, false alerts and missed detections.

## 5.3 RQ3 Results

Present response-plan results for the conditions with and without evidence-linked guidance.

## 5.4 Guidance Quality Results

Report whether the guidance was technically appropriate, evidence-supported and clear about uncertainty.

## 5.5 Additional Findings

Include usability, confidence or perceived usefulness if collected.

# 6. Discussion

## 6.1 Answer to RQ1

Explain which limitations identified in the literature informed SentinelIR’s design and evaluation, and which remain unresolved.

## 6.2 Answer to RQ2

Explain what the detection comparison shows.

## 6.3 Answer to RQ3

Explain what the response-plan comparison shows.

## 6.4 Comparison with Previous Research

Connect the findings to the literature review.

## 6.5 Contribution to Cybersecurity Practice

Explain what SentinelIR contributes within the defined scope.

## 6.6 Limitations

Discuss technical, methodological, participant and generalisability limitations.

## 6.7 Future Improvements

Discuss improvements that could be explored beyond the dissertation scope.

# 7. Conclusion and Future Work

- Restate the problem addressed.
- Answer the main research question.
- Answer RQ1, RQ2 and RQ3 directly.
- Summarise the contribution.
- State the key limitations.
- Identify future development and research.

# References

Use the required APA 7 format.

# Appendices

Possible appendices include:

- Research-question development
- Search strategy and search log
- Literature matrix
- Ethics approval information
- Scenario specifications
- Ground-truth records
- Detection rules
- Response-plan assessment rubric
- Participant information and consent materials
- Questionnaire
- Additional results
- Project plan or Gantt chart
