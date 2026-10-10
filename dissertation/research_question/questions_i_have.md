# Questions for My Supervisor

I would appreciate feedback on the current research direction, particularly how the literature comparison should inform the detection and response-guidance evaluations.

## Current Research Question

```text
How does combining HTTP access and application authentication logs affect SentinelIR’s detection of selected web authentication attack behaviours, and how does evidence-linked guidance affect users’ response-plan quality in a controlled environment?
```

RQ1 will examine limitations in existing approaches and how they inform SentinelIR’s design and evaluation.

For RQ2, my current proposal is to compare detection using HTTP access logs alone against detection using both access logs and application authentication logs.

For RQ3 response planning, I propose presenting equivalent alert evidence with and without investigation and response guidance, then assessing the technical appropriateness and completeness of the resulting plans using predefined criteria.

## Priority Questions

### 1. Is the literature comparison sufficiently focused?

Does the new RQ1 capture the limitations review and justification discussed in our meeting?

What limitations in existing approaches to web authentication attack detection and alert investigation can inform the design and evaluation of SentinelIR?

How much depth should the comparison cover across detection methods and alert investigation approaches?

### 2. Are the proposed comparisons suitable?

Would the two experimental comparisons described above provide a sound basis for answering RQ2 and RQ3?

Are there particular assumptions or sources of bias I should address before developing the experimental design?

### 3. What contribution should I establish through the literature?

Which aspects of this project appear most promising as a research contribution?

What would distinguish a sufficiently original and insightful investigation from a straightforward implementation and demonstration of existing techniques?

### 4. How should response-plan quality be assessed?

Would a rubric with technical appropriateness and completeness as the primary criteria, and relevance and clarity as supporting criteria, be suitable?

How should I justify and validate the criteria, account for multiple acceptable responses, and reduce subjectivity when scoring plans?

### 5. Is a participant study practical?

Would cybersecurity students be an appropriate participant group, and what recruitment and sample-size justification would be expected?

Could controlled response-planning exercises provide sufficient evidence, or would a different evaluation method be more appropriate?

## Scope and Feasibility

### 6. Which scenarios would provide enough depth?

I am considering repeated authentication failures and suspicious successful authentication, alongside benign mistakes and other legitimate activity that might trigger alerts.

Would this be sufficient, or is another behaviour needed? Should directory enumeration remain outside the main study?

### 7. What role should the CTF play?

Would a small controlled application with scripted activity be sufficient for the main detection experiment?

Could participant CTF activity and a questionnaire provide useful supplementary evidence without becoming a separate major study?

### 8. What fallback would be acceptable if recruitment is unsuccessful?

Could the guidance be assessed technically against defined scenarios and authoritative recommendations?

If so, how should I revise the response-planning sub-question to avoid claiming improvements in user performance without participant evidence?

## Approvals and Assessment

### 9. What are the next steps for CW1 and ethics approval?

When should I submit CW1 for feedback and marking so that a passing attempt is confirmed before CW2?

What should the ethics application cover, and which development or pilot activities may I undertake before approval?

### 10. How should I document my existing implementation?

I developed much of SentinelIR over the summer. How should I distinguish that earlier work from the development and research completed during the dissertation?

### 11. What should I prioritise before our next review?

What are the main weaknesses or missing pieces in the current proposal?

Are there particular papers, research areas or methodological approaches you recommend investigating first?

## Notes Following Feedback

- **Agreed research direction:** Meeting on 8 October 2026 -> Kabiru advised retaining the two existing questions and adding a third covering limitations in other papers and the reasoning behind SentinelIR.
- **Changes to the question or scope:** Literature and design justification becomes RQ1, detection becomes RQ2 and response guidance becomes RQ3. Exact new wording drafted after the meeting -> still to confirm with Kabiru.
- **Literature to investigate:** Continue reviewing relevant papers and comparing limitations -> use these to justify design and evaluation choices. Kabiru advised that I can begin the introduction and literature review.
- **Selected scenarios:**
- **Response-plan evaluation approach:**
- **Participant arrangements and fallback:**
- **CW1 actions:**
- **Ethics actions:**
- **Next milestone and date:**
