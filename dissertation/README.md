# SentinelIR - Dissertation Research and Planning

This directory contains the working research questions, project ideas, and planning notes for my SentinelIR dissertation.

SentinelIR is a Python command-line security-log analysis tool. The proposed research focuses on detecting selected web authentication attacks and providing evidence-linked investigation and response guidance.

The documents are work in progress and are being refined through literature review, feasibility checks and supervisor feedback.

## Current Research Question

```text
To what extent can log evidence and evidence-linked response guidance improve the detection of web authentication attacks and the quality of response plans in a controlled environment?
```

The study currently proposes two comparisons:

1. **Detection**: HTTP access logs alone compared with HTTP access logs combined with application authentication logs.
2. **Response planning**: alerts containing equivalent contextual evidence, with and without investigation and response guidance.

## Suggested Reading Order

| Document | Purpose |
| --- | --- |
| [Working research question](research_question/work-question.md) | Current preferred question, sub-questions, definitions and proposed evaluation |
| [Questions for supervisor](research_question/questions_i_have.md) | Feedback requested on scope, evaluation and next steps |
| [Open decisions](research_question/open-decisions.md) | Current preferences and unresolved design decisions |
| [Feature brainstorming](brainstorming.md) | Proposed alert investigation and response-guidance feature |
| [Research-question shortlist](research_question/shortlist.md) | Alternative directions considered before selecting the current question |

## Earlier Ideas and Supporting Material

The research-question process directory records how the project direction developed:

- Initial brainstorming answers
- Candidate research questions
- Earlier refined options

Despite its filename, `process/final.md` is an earlier development document. The current preferred direction is recorded in `research_question/work-question.md`.

## Current Next Steps

- Obtain feedback on the research question and feasibility of the combined study.
- Begin a focused literature review covering authentication-log analysis and alert investigation support.
- Define a small set of malicious and benign evaluation scenarios.
- Establish how detection results and response plans will be assessed.
- Develop CW1 and progress the required ethics application.
- Formal research activities will follow the university’s ethics approval requirements.
