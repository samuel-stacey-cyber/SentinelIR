# Questions for My Supervisor

I would appreciate feedback on the current research direction, particularly whether the combined detection and response-guidance study is feasible within the dissertation.

## Current Research Question

```text
How does combining HTTP access and application authentication logs affect SentinelIR’s detection of selected web authentication attack behaviours, and how does evidence-linked guidance affect users’ response-plan quality in a controlled environment?
```

My current proposal is to compare detection using HTTP access logs alone against detection using both access logs and application authentication logs.

For response planning, I propose presenting equivalent alert evidence with and without investigation and response guidance, then assessing the technical appropriateness and completeness of the resulting plans using predefined criteria.

## Priority Questions

### 1. Is the combined scope appropriate?

Is it realistic to investigate both detection correctness and response-plan quality within this dissertation?

Would you recommend using both sub-questions, or making detection the main investigation and evaluating guidance on a smaller scale?

### 2. Are the proposed comparisons suitable?

Would the two comparisons described above provide a sound basis for answering the research question?

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

- **Agreed research direction:**
- **Changes to the question or scope:**
- **Literature to investigate:**
- **Selected scenarios:**
- **Response-plan evaluation approach:**
- **Participant arrangements and fallback:**
- **CW1 actions:**
- **Ethics actions:**
- **Next milestone and date:**
