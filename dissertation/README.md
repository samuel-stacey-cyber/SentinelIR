# SentinelIR - Dissertation Research and Planning

This directory contains the working research questions, project ideas, and planning notes for my SentinelIR dissertation.

SentinelIR is a Python command-line security-log analysis tool. The proposed research focuses on detecting selected web authentication attacks and providing evidence-linked investigation and response guidance.

The documents are work in progress and are being refined through literature review, feasibility checks and supervisor feedback.

## Current Research Question

```text
How does combining HTTP access and application authentication logs affect SentinelIR’s detection of selected web authentication attack behaviours, and how does evidence-linked guidance affect users’ response-plan quality in a controlled environment?
```

The study has three sub-questions:

1. **RQ1 - Literature and design justification**: critically compare limitations in existing approaches and explain how they inform SentinelIR’s design and evaluation.
2. **RQ2 - Detection**: HTTP access logs alone compared with HTTP access logs combined with application authentication logs.
3. **RQ3 - Response planning**: alerts containing equivalent contextual evidence, with and without investigation and response guidance.

## Suggested Reading Order

| Document | Purpose |
| --- | --- |
| [Current research questions](research_question/final_question.md) | Main question and three sub-questions |
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

- Follow up on Kabiru’s feedback from 8 October 2026 -> retain detection and guidance questions + add a literature and design justification question.
- Continue the literature review -> compare detection methods, log evidence, limitations and alert investigation support.
- Start drafting the introduction and literature review, linking claims to the papers reviewed.
- Define a small set of malicious and benign evaluation scenarios.
- Establish how detection results and response plans will be assessed.
- Develop CW1 and progress the required ethics application.
- Formal research activities will follow the university’s ethics approval requirements.
