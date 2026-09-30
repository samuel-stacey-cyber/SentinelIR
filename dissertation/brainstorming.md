# Brainstorming

When SentinelIR generates an alert, it should also help the user understand what happened and decide what to do next.

The alert should provide supporting evidence, explain why the activity was flagged, and suggest investigation and response steps. The user could then provide additional context to tailor these suggestions into a practical plan.

The intended workflow is:

Detection → supporting evidence → investigation guidance → user context → tailored response plan.

# Revised Version

## Proposed Feature: Alert Investigation and Response Guidance

SentinelIR will aim to support users beyond the initial detection of suspicious activity by providing evidence-based investigation and response guidance alongside selected alerts.

Detection correctness remains the main research priority. The guidance feature will build on those detections, helping users interpret the available information and make informed decisions about further investigation, response and prevention.

The intended audience includes SOC analysts, cybersecurity students and IT staff responsible for monitoring systems. The dissertation evaluation will identify which user groups are represented and limit its conclusions accordingly.

## Information Provided with an Alert

For each supported alert type, SentinelIR should aim to provide:

- **A summary:** what activity was detected and why it triggered the rule.
- **Supporting evidence:** relevant log events, timestamps, sources, affected services and accounts where available.
- **Uncertainty and alternative explanations:** what the evidence establishes, what remains unknown, and whether legitimate activity could explain the alert.
- **Investigation steps:** checks the user could perform to determine the nature and extent of the activity.
- **Possible response actions:** conditional suggestions appropriate to the findings and environment.
- **Prevention guidance:** relevant measures that could reduce the likelihood or impact of similar activity.

An alert will indicate suspicious behaviour requiring assessment. It will not automatically establish that an attack succeeded or that a system was compromised.

## Tailoring the Response Plan

Users should be able to provide relevant context to refine the suggested plan. For example, they might confirm whether a source belongs to an authorised scanner, whether an affected account is expected to be active, or whether the activity is still occurring.

The plan should explain why a suggested action is relevant and identify any conditions that need to be checked before taking it. Where information is insufficient, SentinelIR should identify what further evidence is needed.

The initial implementation will cover a small set of selected alert types. The mechanism used to produce and tailor guidance will be decided after reviewing feasibility and relevant literature.

## Relationship to the Dissertation

The project will investigate detection correctness and assess the supporting guidance separately.

Controlled experiments will examine whether SentinelIR identifies the selected activity accurately. Evaluation of the guidance will consider its technical correctness, relevance to the scenario, clarity and usefulness.

Positive feedback about the guidance will not be treated as proof that the detector is accurate. Similarly, a correct detection will not automatically establish that its recommended response is appropriate.

## Potential CTF Participant Research

Subject to ethics approval, participants completing controlled CTF scenarios could provide additional research data through a questionnaire.

Questions could explore:

- What participants attempted and what outcomes they observed.
- How they would investigate, respond to and prevent the activity.
- What information they would need to make those decisions.
- What they found useful, unclear, missing or inappropriate in SentinelIR’s guidance.

Participants’ own defensive suggestions should be collected before showing them SentinelIR’s recommendations. Their suggestions will be treated as research responses and checked against relevant technical sources before informing the tool’s guidance.

Participant feedback may support development or evaluation. These uses will be distinguished so that feedback used to improve the feature is not presented as an independent evaluation of the revised version.

## Scope and Future Work

The dissertation implementation will provide information and suggested actions while leaving operational decisions and execution with the user.

Automatically executing response actions after user approval is a potential future extension. It is outside the current dissertation implementation scope.

The immediate priority is a manageable feature that connects selected detections with clear evidence and appropriate guidance, supported by an evaluation that can be completed within the available time.
