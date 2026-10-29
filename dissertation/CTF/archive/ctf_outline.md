# SentinelIR — CTF Idea and Plan

## Overall Idea

- Create a deliberately vulnerable website -> a fictional staff portal with test accounts and fake information.
- Give less experienced participants some achievable challenges -> then include harder optional routes for those who want to continue!
- Use clues, decoy credentials and decoy flags to make it interesting.
- Keep the challenges fair -> participants should be able to work out what went wrong and what to try next.
- The aim is to study detection and response guidance -> finishing the CTF is not a measure of whether someone is a `true hacker`.
- SentinelIR remains `CLI-only` -> the CTF website and flag submission page are separate research infrastructure.
- These are proposed additions -> not claims that they are already implemented or approved.

## How This Fits the Research Questions

- `RQ1` -> use the literature to justify the scenarios, logging, detection limitations and guidance design.
- `RQ2` -> compare access logs alone against access + authentication logs for the same selected authentication scenarios.
- `RQ3` -> compare users' response plans with equivalent alert evidence, with or without investigation and response guidance.
- The CTF provides activity and useful participant feedback -> the questionnaire alone cannot establish improved response-plan quality.
- SQL injection, traversal and other challenges are optional extensions -> their results must not be presented as answers to the authentication-focused RQ2 without an agreed scope change.

## 1. Recommended Starting Scope

### Core -> build and evaluate first

- A login page with seeded test accounts.
- One deliberately weak test password -> included in a small supplied practice wordlist.
- Repeated failed logins -> followed by either failure or successful authentication.
- A decoy credential hidden in a client-visible comment -> triggers a decoy-use event when submitted.
- A normal account area containing the first genuine flag.
- A final authentication challenge -> identify and access a second seeded test account using the supplied clues.
- A protected flag submission page -> progress tracking and a final completion flag.
- Both HTTP access and application authentication logs -> monitored live by SentinelIR and saved for replay.
- Benign activity -> ordinary browsing, successful logins and genuine typing mistakes.

### Optional -> add only after the core works

- `IDOR` -> accessing another test account's object by changing an identifier.
- `Broken authorisation / mass assignment` -> changing a role field that the server incorrectly trusts.
- `SQL injection` -> a separate route into seeded application data.
- `Path traversal` -> retrieving a seeded clue outside the intended document folder, inside an isolated challenge file system.
- Upload or XSS challenges -> only if their research value justifies the extra implementation and containment work.

## 2. Proposed Journey and End Goal

- Story -> investigate a fictional company portal and recover a final audit report.
- Start page -> explains the permitted targets, available tools, time limit, hints and that some clues/flags may be decoys.
- Practice area -> learn how to submit a flag without affecting the formal evaluation.
- First challenge -> weak login -> normal account dashboard -> `Flag 1`.
- Second challenge -> inspect clues and distinguish a genuine account route from the decoy -> `Flag 2`.
- Core end goal -> submit both genuine flags -> unlock the fictional audit report and completion flag.
- This core route must remain `finishable` without implementing every optional vulnerability.
- Expanded version, if time allows -> `IDOR` reveals a clue, traversal reveals a seeded document, and a role-control flaw opens an admin area containing an additional flag.
- SQL injection can be an alternative branch -> it should not accidentally expose every flag and bypass the whole exercise.
- Hints can unlock gradually -> record their use, keep the policy consistent and do not treat asking for help as failure.
- Any leaderboard should be optional and use aliases -> completion time is not the main dissertation outcome.

## 3. Vulnerabilities and What SentinelIR Could Detect

Approximate order -> easiest to observe under this proposed logging setup. Detecting suspicious activity is different from proving successful exploitation!

| Order | Weakness / scenario | What to build | Observable evidence | Important limit |
| --- | --- | --- | --- | --- |
| 1 | Weak password + missing effective login throttling | Seeded account + bounded wordlist | Repeated authentication failures in a time window | Mistyped passwords can look similar; a weak password itself is not revealed by request counts |
| 2 | Exposed decoy credential | Unique fake credentials in a visible comment | Application records use of that decoy without recording the password | This is a deliberately planted signal, not general brute-force detection |
| 3 | Failures followed by successful login | Account that can eventually be accessed | Correlated failure and success events for the test account/run | Success does not by itself establish malicious compromise |
| 4 | Exposed backup / sensitive test file | Fake backup or configuration clue | Request to the seeded resource + server outcome | Access can be legitimate; do not put real secrets in it |
| 5 | Path traversal | Restricted challenge file-reading route | Suspicious path input + actual file-access outcome | Encoded requests and benign path strings complicate signature detection |
| 6 | SQL injection | Isolated vulnerable query against fake data | Request indicators, query errors and relevant application outcomes | POST bodies are not normally in access logs; indicators do not prove injection succeeded |
| 7 | `IDOR` / broken object access control | Change object ID to access another test account's item | Acting account, requested object, owner and access outcome | Access logs alone usually lack the ownership context needed |
| 8 | Role escalation / mass assignment | Server trusts an editable role field | Actor, previous/new role and permission-change outcome | A role change may be authorised; distinguish it from admin activity |
| 9 | Unsafe uploads handling | Bounded file-type validation challenge | Upload metadata, validation outcome and storage outcome | Accepting a file does not prove code execution; avoid executing uploaded code |
| 10 | XSS | Optional isolated reflection/rendering challenge | Suspicious input + controlled browser observation if available | Server logs alone cannot confirm JavaScript executed |

- Password spraying is another authentication-focused option -> a few guesses across several accounts.
- Slow guessing is useful for testing threshold limitations -> more directly relevant to RQ2 than adding lots of unrelated vulnerabilities.
- Username enumeration could be an optional response-difference challenge -> detecting probing does not establish that enumeration succeeded.
- My recommendation -> choose a small core, then at most one or two extensions initially. This is a proposed workload limit, not a requirement.

## 4. Adjustments to My Original Ideas

- `Brute-force` -> use a bounded wordlist and request budget rather than requiring millions of requests.
- `Rate limits` -> decide whether the challenge deliberately lacks them or uses a fixed limit. Freeze this before evaluation -> changing it also changes the activity being measured.
- `Honey-pot login` -> more precisely a decoy credential / `honeytoken`. Prefer rejection plus a private event; a fake authenticated area would add more complexity.
- A visit to the comment-containing page followed by decoy use supports a sequence -> it does not prove that the visitor read the comment.
- Do not log attempted passwords -> recognise the seeded decoy inside the application and record a category/event.
- `SQLmap` -> hiding a database filename cannot make a SQL-injectable application manual-only. `SQLmap` can enumerate database contents through the injection itself. A manual-only practice rule is possible, but it is not a technical guarantee. [`SQLmap` features](https://github.com/sqlmapproject/sqlmap/wiki/features)
- A page displaying database contents can be saved -> do not rely on `viewable but impossible to download`. Use a fake document or selected seeded records instead of exposing the actual database file.
- `Account forgery` -> following hidden registration instructions is a puzzle. Changing another user's identifier is `IDOR`; changing a protected role through ordinary input is broken authorisation / potentially mass assignment. [OWASP `IDOR`](https://community.owasp.org/attacks/insecure_direct_object_reference)
- Funny feedback -> use an optional joke page or local message. Do not make a download automatically open an external video or run anything.
- Avoid telling participants that SentinelIR caught them during formal activity -> this changes their behaviour. Keep any playful feedback fixed across conditions, or reserve it for practice/debriefing.
- Uploads -> keep files non-executable, size-limited and isolated from application code. A contained validation flaw is sufficient for a puzzle. [OWASP upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

## 5. Flags and Submission Page

- Use the website for checking flags -> the questionnaire is for feedback, not the main flag validator.
- Genuine flags -> one per challenge, plus a final completion flag.
- Prefer separate participant instances / run-specific flags -> reduces copying and accidental interference.
- Keep flag validation and progress separate from the vulnerable database and challenge file system.
- Store validation values securely, such as hashes of unpredictable tokens -> never expose the full answer list to the browser.
- Validate required progress server-side -> changing a request parameter must not mark a challenge as complete.
- Duplicate genuine submission -> `Already completed` -> no repeated points.
- Invalid submission -> neutral message -> no unnecessary hints about valid tokens.
- Decoy submission -> no progress; record that a decoy was submitted, then explain it in the debrief.
- Keep a decoy flag different from a decoy login -> separate events and separate interpretations.
- Bound submission attempts and input length -> the scoring service should not itself be a vulnerable challenge.
- Record challenge ID, run ID, time and submission category -> avoid storing raw flags in research logs.
- Flag completion is supporting evidence of progress -> it is not an independent label for every attack attempt.

## 6. Logs, Ground Truth and Detection

- Access logs -> timestamp, request ID, method, sanitised path, response status and relevant response metadata.
- Authentication logs -> matching request ID, test account identifier, event type and genuine authentication outcome.
- Use run/instance identifiers for research correlation -> an IP address alone is not a reliable participant identity.
- Do not put real credentials, authentication tokens or personal free-text into logs.
- Optional challenge instrumentation -> record object access or role-change outcomes separately if those challenges are selected.
- Ground truth -> separate scripted scenario records + independent checks of application state. Participant activity may need manual verification; mark uncertain cases rather than guessing.
- Keep challenge answers, flag manifests and ground-truth labels out of detector input -> otherwise the evaluation becomes circular.
- Decoy events require special care -> report them separately or explicitly declare their availability in each comparison; do not claim their easy detection proves general authentication detection improved.
- Start collection before tasks begin -> confirm both log streams are captured and timestamps align.
- Save the same activity for replay -> evaluate both RQ2 configurations against identical episodes.
- Freeze thresholds using pilot activity -> do not tune against the final evaluation dataset.
- Include benign mistakes and slower attacks -> inspect false positives and missed attacks, not just successful demonstrations.
- Current live-monitoring code is a starting point -> multi-source collection, correlation and replay still need verifying/implementing.

## 7. Participants, Guidance and Questionnaire

- Participation starts only after the required ethics approval and participant materials are ready.
- CTF tasks -> generate activity and gather feedback about difficulty, clues and the attacks attempted.
- Ask what participants would investigate, contain and prevent -> useful qualitative feedback, not automatically technically correct guidance.
- Check suggestions against technical evidence before incorporating them into guidance.
- Any guidance development feedback should come from a pilot/development stage -> freeze guidance before the formal RQ3 comparison.
- RQ3 tasks -> give equivalent evidence with/without guidance and ask users to write response plans.
- Use unseen scenarios for response planning where possible -> someone who performed an attack already knows its cause.
- Choose task allocation and counterbalancing before recruitment -> do not infer the effect of guidance from satisfaction ratings alone.
- Score technical appropriateness and completeness using predefined criteria; record usefulness/confidence separately.
- Names/emails for contact are personal data -> hold them separately from task responses.
- Linked participant codes are pseudonymous, not fully anonymous. Decide whether the questionnaire is genuinely unlinked or needs a code before promising anonymity.
- Hosting, Microsoft Forms settings, retention and withdrawal arrangements remain decisions -> a protected PC alone does not settle the complete data flow.

## 8. Detailed Delivery Plan

### Phase 1 -> settle the experiment

- Select the authentication behaviours, benign scenarios and optional challenges.
- Agree what counts as an episode, correct alert and successful login.
- Choose the core completion route and write a short challenge specification for each step.
- Output -> scenario table + expected evidence + independent ground-truth method.
- Move on when -> every core task supports the RQs and can be evaluated without extra vulnerabilities.

### Phase 2 -> prepare the environment

- Compare a small custom app with adapting an existing training platform -> choose based on logging control, isolation, reset support and development time.
- Decide local / university-managed / restricted remote hosting -> do not assume public hosting is required.
- Keep the vulnerable app isolated from personal files, real accounts and other participants' instances.
- Separate the vulnerable content from scoring, research records and administrative controls.
- Define reset and backup procedures; restrict outbound connectivity where practical.
- Output -> environment diagram, data flow and reset procedure.
- Move on when -> a test instance can be started, stopped and reset without exposing real data.

### Phase 3 -> build the smallest complete CTF

- Implement seeded accounts, the login challenge, one decoy, the genuine flags and final report.
- Implement server-side flag checks and progress tracking.
- Add access + authentication events with request correlation.
- Output -> a complete beginner-to-final route, even if no optional branches exist yet.
- Move on when -> genuine, invalid, duplicate and decoy submissions behave as intended.

### Phase 4 -> connect and verify SentinelIR

- Verify live capture, restart behaviour, log rotation and missing/malformed events.
- Run scripted benign and attack scenarios -> independently confirm their outcomes.
- Replay the same logs through access-only and combined-log configurations.
- Output -> reproducible run records and a pilot detection table.
- Move on when -> capture failures can be distinguished from detector misses and no answer labels leak into detection.

### Phase 5 -> add selected optional branches

- Add only extensions that fit the available time and have a clear learning/research purpose.
- Check that shortcuts do not expose scoring secrets or bypass every stage.
- Check each branch's logged indicators against actual application outcomes.
- Output -> extra challenge specifications and documented detection limitations.
- Stop adding features if -> the core evaluation, ethics materials or report are slipping.

### Phase 6 -> pilot and freeze

- Obtain required approval before involving participants, including pilots where applicable.
- Trial instructions, difficulty, hints, session timing and response-plan scoring.
- Check whether the final task is achievable without excessive guessing or unexplained obstacles.
- Revise using pilot evidence -> record changes, then freeze formal scenarios, thresholds, guidance and scoring criteria.
- Output -> versioned study pack + final procedure + analysis plan.

### Phase 7 -> run the study

- Confirm consent and boundaries -> issue test access -> check logging -> run tasks.
- Record departures from the procedure, hints, technical failures and incomplete tasks.
- Run the planned RQ3 comparison with equivalent evidence and controlled task allocation.
- Collect questionnaire responses -> debrief decoys and explain withdrawal arrangements.
- Export and check data -> remove unnecessary identifiers -> store according to the agreed plan.

### Phase 8 -> analyse and write up

- RQ2 -> precision, recall and error counts under both log configurations; report uncertain labels and capture problems.
- RQ3 -> appropriateness/completeness scores under both conditions; discuss experience, order effects and assessor limitations.
- Questionnaire -> perceived usefulness, difficulty and participant suggestions, reported separately.
- Discuss what the controlled CTF does and does not establish about real operational attacks.
- Preserve reproducible configuration and sanitised examples -> no personal research data in the public repository.

## Decisions Still Open

- Exact attack set + maximum optional scope.
- Custom app or adapted platform; hosting and participant isolation.
- Core final challenge and flag rules.
- Which decoy information is available to the detector and how it is evaluated.
- Participant numbers, session duration, task allocation and scoring assessors.
- Ethics materials, data handling, retention and withdrawal process.
- Schedule and resource limits -> place agreed milestones into the 24-week Gantt chart.

My decision:

Why:

Status:

## Where These Decisions Belong

- [01 — Scope](01_scope_and_contribution.md) -> which challenges are in/out and what they contribute.
- [02 — CTF and logs](02_ctf_and_log_collection.md) -> hosting, routes, flags and collection.
- [03 — Detection](03_detection_evaluation.md) -> ground truth, decoys and fair comparisons.
- [04 — Guidance](04_guidance_design.md) -> development feedback and freezing guidance.
- [05 — Participants](05_participants_and_tasks.md) -> difficulty, tasks and prior knowledge.
- [06 — Scoring](06_response_plan_scoring.md) -> response-plan quality versus CTF progress.
- [07 — Ethics](07_ethics_and_data_management.md) -> decoys, participant information and data flows.
- [08 — Timeline](08_timeline_resources_and_risks.md) -> build gates and contingency.
- [09 — CW2 readiness](09_cw2_readiness.md) -> what the proposal must explain before submission.
