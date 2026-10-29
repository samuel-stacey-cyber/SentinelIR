# SentinelIR — CTF Chat Handoff

## What I Want From This Chat

- Help me finalise the CTF as a whole -> ideas, challenge progression, flags, detection, hosting and then development.
- Start by reviewing the existing plan and helping me make the outstanding decisions.
- Do not treat the previous assistant's recommendations as choices I have already made!
- Keep it collaborative -> suggest practical options, explain the trade-offs and help me choose.
- Use short explanations, bullets, arrows and `backticks` when writing planning notes.
- Ask focused questions, preferably using the available pop-up question tool -> do not overwhelm me with every decision at once.
- Preserve my existing notes. Clearly separate `Established`, `Preference`, `Proposed` and `Open`.
- Do not immediately implement the entire proposed CTF. Agree the scope and design with me first, then develop the agreed stages.

## Project Context

- My name is Sam -> Coventry University cybersecurity research project, supervised by Kabiru.
- SentinelIR is a `CLI-only` security log analysis tool.
- The vulnerable CTF website is separate from SentinelIR -> a website for generating controlled activity and hosting challenges is allowed; a SentinelIR dashboard is not the project direction.
- I want SentinelIR running in the background while the CTF is used -> collecting/analysing logs live, with saved activity available for repeatable comparisons.
- Fellow cybersecurity students are the intended participants -> recruitment, numbers, session length and ethics arrangements still need finalising.
- The dissertation needs defensible detection and response-plan evaluation, not just a collection of fun vulnerabilities.

## Current Research Questions — Preserve These

### Main Question

How does combining HTTP access and application authentication logs affect SentinelIR’s detection of selected web authentication attack behaviours, and how does evidence-linked guidance affect users’ response-plan quality in a controlled environment?

### RQ1 — Literature and Design Justification

What limitations in existing approaches to web authentication attack detection and alert investigation can inform the design and evaluation of SentinelIR?

### RQ2 — Detection Using Combined Logs

How does combining HTTP access logs with application authentication logs affect the precision and recall of SentinelIR’s detection of selected web authentication attack behaviours compared with using HTTP access logs alone?

### RQ3 — Investigation and Response Guidance

How does providing evidence-linked investigation and response guidance alongside SentinelIR alerts affect the technical appropriateness and completeness of users’ response plans compared with presenting equivalent alert evidence without guidance?

- RQ1 -> critical literature comparison informs design/evaluation.
- RQ2 -> same authentication activity, two log configurations, independent ground truth.
- RQ3 -> equivalent alert evidence, with/without guidance, response plans assessed using predefined criteria.
- Extra vulnerabilities do not automatically expand RQ2 -> discuss any proposed change with me rather than silently changing the question.

## My CTF Idea

- Make it fun -> clues, branching routes, some misleading information and decoys!
- Beginners should have achievable early challenges; more experienced participants should have harder optional challenges.
- There needs to be a clear final goal -> I have not finalised the story or exact completion route.
- Include genuine flags and a submission page that tells participants whether their flag is accepted.
- Include `honey-pot flags` -> more precisely decoy flags, plus potentially decoy credentials.
- I originally suggested:
  - Weak passwords / brute-force login.
  - A fake credential in an HTML comment -> detect when someone uses it.
  - Detect repeated failures followed by successful login.
  - SQL injection as an alternative way into the application/data.
  - Path traversal to discover a hidden file.
  - Registration clues, changing account identifiers and changing roles through requests.
  - Profile-picture upload and possibly XSS.
  - Funny messages or a joke page.
- This is brainstorming -> the final challenge list is still open.

## Current Assistant Proposal — Not Yet My Final Decision

- Fictional staff portal -> recover a final audit report.
- Core -> weak login, decoy credential, a second authentication challenge, genuine flags and a final completion flag.
- Complete the core route before adding optional vulnerabilities.
- Possible extensions -> IDOR, role escalation, SQL injection or traversal.
- Keep upload/XSS optional because they add complexity and need different evidence to confirm exploitation.
- Consider slow guessing or password spraying -> these may contribute more directly to RQ2 than unrelated vulnerabilities.
- Prefer a bounded practice wordlist and resource budget over requiring millions of login attempts.
- Separate flag validation/progress from the deliberately vulnerable application data.
- Prefer per-run instances or tokens to limit copying/interference -> exact arrangement remains open.
- A small custom app versus an adapted training platform has not been chosen.

## Technical Corrections Already Discussed

- Hiding a database filename does not prevent SQLmap from exploiting SQL injection and enumerating data.
- A manual-only challenge rule is possible -> not a guarantee that automation cannot work.
- If database content is displayed, it can be saved -> do not promise `viewable but impossible to download`.
- Hidden registration instructions are a puzzle, not inherently an account-forgery vulnerability.
- Changing another account/object identifier without an ownership check -> `IDOR / broken object access control`.
- Changing a protected role through ordinary input -> broken authorisation, potentially mass assignment depending on implementation.
- A successful login does not prove compromise; a suspicious request does not prove successful exploitation.
- IP addresses alone do not reliably identify participants -> use appropriate request/run correlation.
- Ordinary access logs usually do not include POST bodies or authoritative authentication outcomes.
- Server logs alone cannot confirm XSS execution, and an accepted upload does not establish code execution.
- Use an optional joke page rather than a download that automatically opens something or executes code.

## Research Design Constraints

- Capture ordinary benign activity as well as attacks -> include genuine login mistakes and slower attempts.
- Compare both RQ2 configurations against the same saved activity.
- Keep independent ground-truth records -> do not feed challenge answers, scoring manifests or attack labels into SentinelIR.
- Flag completion measures progress -> it does not label every attack attempt or establish detection accuracy.
- Decoy events are unusually easy signals -> declare how they are used and avoid presenting them as proof of general detection improvement.
- Pilot thresholds and scenarios separately -> freeze them before formal evaluation.
- Do not alter participant behaviour with live `we caught you` feedback unless that is explicitly part of a controlled design.
- The end questionnaire can ask about difficulty, usefulness and how participants would prevent attacks.
- Participant prevention suggestions need technical review before they become guidance.
- Use development/pilot feedback to improve guidance, then freeze it before evaluating it.
- RQ3 needs assessed response plans -> opinions and confidence ratings are separate outcomes.
- Someone who performed an attack knows its cause -> plan unseen response scenarios or another way to control prior knowledge.
- Automated execution of response actions is outside the agreed dissertation scope.

## Ethics and Data — Outstanding, Not Approved by This Handoff

- The environment must use fake accounts/data and explicitly authorised targets.
- Hosting is undecided -> local, university-managed or restricted remote arrangements need comparing.
- Names/emails may be collected for contacting participants and feedback -> hold these separately from task responses.
- Microsoft Forms is a preference for the questionnaire, not a finalised data-handling arrangement.
- Storage on my protected PC is a preference -> access, backups, retention, withdrawal and platform data flows need documenting.
- Linked codes mean pseudonymous data -> do not promise fully anonymous responses if they can be linked back.
- Participant materials should explain the presence of decoys without giving away placements, followed by a debrief.
- Do not claim ethics approval or recruitment approval without checking the actual records.
- No participant collection before the necessary approval/materials are in place.

## Existing Code — Inspect Before Making Promises

Repository: `/home/ss-mint/Projects/SentinelIR`

Earlier inspection found existing HTTP parsing, rule-based detection, automated tests and a single-file live monitoring starting point. This is context, not confirmation that the full CTF or multi-source pipeline already works.

Check the current implementation before choosing an architecture:

- `app/parsers/http_parser.py`
- `app/monitoring/file_monitor.py`
- `app/monitoring/live_event_processor.py`
- `app/detection/detection_engine.py`

- Verify multi-source support, authentication outcomes, request correlation, replay, rotation and restart behaviour.
- Existing web-related code or a legacy branch name does not override the CLI-only scope.
- Read applicable repository instructions and check current changes before editing.
- Do not commit or push unless I ask; do not overwrite unrelated changes.

## Read These Files First

All paths below are relative to `/home/ss-mint/Projects/SentinelIR`:

1. `dissertation/decisions/ctf_outline.md` -> current detailed proposal; previously called `ctf_updated.md` in the conversation. Use the actual current file.
2. `dissertation/decisions/01_scope_and_contribution.md` -> my original brainstorming + scope decisions.
3. `dissertation/decisions/02_ctf_and_log_collection.md` -> infrastructure and collection decisions.
4. `dissertation/decisions/03_detection_evaluation.md` -> fair comparison, scenarios and ground truth.
5. `dissertation/research_question/final_question.md` -> authoritative current question wording.

Then consult the remaining decision files as needed:

- `04_guidance_design.md`
- `05_participants_and_tasks.md`
- `06_response_plan_scoring.md`
- `07_ethics_and_data_management.md`
- `08_timeline_resources_and_risks.md`
- `09_cw2_readiness.md`

These seven filenames are also under `dissertation/decisions/`.

Literature context -> `dissertation/literature_review/reading_notes/`, `matrix.md`, `synthesis.md` and `useful_ideas.md`.

- P01–P07 contain reviewed work -> inspect the relevant notes before attributing findings.
- P02/P03/P06 help with detection limitations; P01/P04/P05/P07 help distinguish investigation support, guidance output and human evaluation.
- Do not treat adapted ideas as already validated for SentinelIR.
- If this chat cannot access these local paths, ask me to attach the current outline and relevant files. Do not pretend to have read them.

## How to Organise Further Work

- Keep `01` for scope/contribution -> detailed CTF design belongs in `ctf_outline.md` and related decisions in `02`–`08`.
- No README requested for this folder.
- Preserve original brainstorming; update resolved decisions clearly rather than replacing everything.
- Use `Open`, `Proposed`, `Decided` and `Needs supervisor input`.
- Cross-check filenames before adding links -> the outline has already changed name since the previous response.
- No timetable, participant count, technology stack or final challenge selection has been approved by this handoff.

## Suggested First Conversation

Start by summarising the current idea briefly, then help me decide:

1. What is the story and concrete final goal?
2. Which authentication challenges are essential, and which optional branches do I actually want?
3. How should beginners progress while harder tasks remain available?
4. What should genuine flags and decoys do, including hints and scoring?
5. What architecture best supports those choices, isolation, reset and live logging?

Ask the first few questions together, then work through the dependencies -> do not turn this into another long literature review before making design progress.

## What a Finalised Design Should Contain

- Agreed scope -> core, optional and excluded features.
- Challenge map -> entry points, alternative routes, hints and end goal.
- Challenge specifications -> prerequisites, intended weakness, task outcome, flag, evidence, benign comparison, independent success check and reset method.
- Architecture -> vulnerable app, scoring, logs, SentinelIR and research records.
- Logging contract -> fields, correlation, sensitive-data exclusions and replay.
- Study procedure -> participant activity, separate response-plan tasks and questionnaire.
- Acceptance checks -> challenge works, score cannot be forged, logs match events, reset works and no real data is exposed.
- Phased implementation backlog -> smallest complete route first, then selected extensions.
- Open issues -> clearly listed for me or Kabiru, rather than silently decided.

First priority -> finalise a coherent, achievable CTF that I am excited to build and that produces usable research evidence!

## Lecturer Feedback Before Implementation

- Once I have finalised a complete draft of the CTF plan -> send it to three lecturers:
  - Kabiru -> my supervisor.
  - Two lecturers who have created CTFs we have completed throughout university.
- Purpose -> check the research relevance, challenge progression, difficulty and feasibility before building everything.
- This will be a design-review draft -> still open to changes based on feedback!

### What I Will Send

- A short overview -> purpose, intended participants and connection to SentinelIR.
- The full CTF plan -> core challenges, optional branches and exclusions.
- A challenge map -> starting point, clues, flags, decoys and final goal.
- Logging + evaluation plan -> what activity is recorded and what it can demonstrate.
- Proposed hosting, isolation and reset arrangements.
- Outstanding decisions -> clearly identify where their advice would help.

### Questions to Ask

1. Does the CTF support the research questions, or are any challenges unnecessary?
2. Is the progression suitable for students with different experience levels?
3. Are the clues, decoys and final goal fair and understandable?
4. Are there unintended shortcuts or technical problems I have overlooked?
5. Will the proposed logs and independent checks provide enough evidence for evaluation?
6. Is the scope achievable, and what would you remove or prioritise?
7. What is the most important change you would recommend before implementation?

### Feedback or Research Data?

- My current preference -> structured written feedback first.
- If I want to analyse their responses as research evidence -> discuss this with Kabiru before collecting them.
- Confirm whether this requires changes to the ethics application and participant documents.
- Do not assume that being a lecturer or supervisor replaces consent.
- Obtain permission before attributing comments or including direct quotations.
- Do not promise anonymity -> three lecturers with identifiable roles may be recognisable.

### How I Will Use the Feedback

- Keep a decision record:
  - Feedback received -> proposed change -> my decision -> reasoning.
- Record disagreements too -> explain why I followed one suggestion over another.
- Separate expert opinions from findings established through testing.
- Revise the CTF plan -> then agree the first implementation stage.
- Lecturer feedback does not replace pilot testing or the RQ2/RQ3 evaluations.
