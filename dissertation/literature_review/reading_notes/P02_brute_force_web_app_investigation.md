# P02 - Flow-Based Web Application Brute-Force Attack and Compromise Detection

## Reference and Reading Status

- Authors: `Hofstede, Rick`, `Jonker, Mattijs`, `Sperotto, Anna`, `Pras, Aiko`
- Year: 2017
- Venue: Journal of Network and Systems Management
- Source type: Peer-reviewed journal article
- Reading status: Partially read
- Sections read: `Abstract`, `Background and Related Work`, `Conclusion`
- Date notes last updated: 04/10/2026

## Discovery

- Search date: 04/10/2026
- Search platform / discovery method: Mendeley literature search
- Exact search terms, if applicable: `brute force web attack`
- Search log entry: 002

## Initial Screening — Is It Worth Reviewing?

Understanding from the `Abstract` + `Background` + `Conclusion`:

- Which part of SentinelIR does it relate to?
  - RQ1 — Detection using combined logs           Relevance /10? 7
    - Mentions one type of logs -> `brute-force attacks`
    - Invesitgation into `HTTP` logs
    - Conclusion:
      - Mention of how false positives and negatives are a clear industry standard issue
      - Mention of how different cipher suites and key exchanges protocols effect the size of HTTPs flows
        - Attackers attempt to remain invisible by using different cipher suites
      - Make detection approaches more resilient against `evasion techniques`
  - RQ2 — Investigation and response guidance     Relevance /10? 2
    - Mentions three existing host-based defence approaches:
      - Log file analysis -> `SentinelIR`
      - `Host-based intrusion detection systems`
      - `Firewalls`
    - No super relevant -> runs through the different types of alerts, not how to prevent them!
  - Evaluation methods
    - Dataset is from a real company
      - Useful to understand how to use real logs when talking about analysis, or throughout the report
      - My generated data will be from CTF / syntehtically generated
  - Background / definitions
  - Ideas generated:
    - Mention how attacks are done, compare them with the data provided from the CTF questionnaire
    - Explain the process they took, how its differred to others
    - Finally circle back and speak about how to prevent the common ones and more complex ones
    - Explain each and every attack that can be detected, the process and just an overview -> background?
    - Mention the difficulties with `HTTP` protocol -> vast!
      - TLS/SSL
    - Mention the different networking layers!
    - References with other papers how mine differes in terms of research / aims!

- What could this paper help me understand or decide?
  - Get some general/professional progress of collecting, storing, understanding, analysing, then using as evidence
  - Limitations of false positives and negatives
  - Real data
  - Understanding into some of the factors that affect HTTP logs
  - Useful to understand how the analyse logs -> useful for SentinelIR?
  - Way the structure investigating the logs
  - Use of cluster methods -> `attack traffic` vs `non-attack traffic`
- Is it directly relevant, or would its findings need adapting?
  - I'd say relevant, not completely but some parts will be useful!
- Does it provide research evidence, a review of evidence, or guidance?
  - Primary research using real-world network-flow data to evaluate brute-force and compromise detection methods
- Is the full text available to assess its methods and findings?
  - Yes
- Decision: `Keep - supporting background and evaluation context`
- Reason for decision:
  - Relevant due to the investigation into real data -> will be the same when for the CTF
  - Process of using/handling real-world logs/data
  - Evaluates the detection of web application brute-force attacks
  - Useful comparison of log-based approach -> different types of logs
  - Not directly relevant to RQ2 -> no link to response plans / guidance
  - Useful background on encrypted traffic, evasion, and difficulties with distinguishing attacks

---

## 1. What Problem Does It Address?

- Research question or aim:
  - `Can network-based IPFIX monitoring detect buret-force attacks on Web applications?`
  - `Can compromises be identified from flow data?`
  - `Does the approach work in encrypted environments?`
- Claimed limitation in previous work:
  - Brute-force detection is not a new research area -> previous studies often focus on login-restrictive protocols such as `SSH`
  - `HTTP` supports many activities beyond logging in -> harder to distinguish authentication attempts from other web traffic
  - `HTTPS` encrypts sessions -> makes inspecting the traffic contents harder for network-based detection
  - Some previous HTTP(S) detection approaches rely on individual packets -> differs from this study's use of `flow data`
  - Authors identify a previous flow-based approach [24]:
    - Extracts attack signatures from brute-force tools
    - Assumes brute-force attacks produce many small flows -> few packets and bytes
    - Limitation: legitimate applications can produce similar traffic -> `calendar fetchers` and `web crawlers`
    - Can therefore incorrectly classify legitimate activity as attacks -> `false positives`
  - How this study aims to address the limitation:
    - Also assumes traffic during the brute-force phase is relatively `flat`
    - Uses `histograms` to help distinguish attacks from benign traffic with similar packet counts, byte counts and durations
    - Need to check the results -> how successfully does this reduce false positives, and under what conditions?
- Main contribution, in my own words:
- Relevant page / section: `Background and Related Work`

## 2. How Did They Investigate It?

- Study approach:
  - Developed an Apache access log parser that `aggregates` log records - sorting by number of `interactions`
  - 
- Setting: Lab / Operational environment / Other
- Inputs / log sources:
- Dataset or participants:
- Sample size and unit of analysis:
- Baseline / comparison conditions:
- What changed between conditions, and what stayed consistent?
- Ground truth or assessment criteria:
- Evaluation measures:
- Relevant page / section:

Check whether repeated observations come from the same participants,
alerts, attacks or datasets.

For a review paper, record its search, selection, appraisal and synthesis
methods instead of an experimental setup.

Use “Not applicable”, “Not reported” or “Not yet checked” accurately.

## 3. What Did They Find?

### Finding 1

- Main finding, in my own words:
- Supporting result:
- What does the number measure, and what is its denominator?
- Conditions under which the finding applies:
- Relevant page / table / figure:
- Authors’ interpretation:
- My interpretation:

### Other Important Findings

- Mixed results, no detected improvement or unexpected outcomes:

Only add further findings that matter to my research.

Mark claims taken only from the abstract until checked against the results.
Keep exact quotations in quotation marks with a page reference.

## 4. How Convincing Is the Evidence?

### Strengths

- Strength:
- Why it makes the evidence more convincing:

### Limitations Acknowledged by the Authors

- Limitation:
- How it affects the conclusions:
- Relevant page / section:

### My Critical Observations

- Observation:
- Evidence or example supporting it:
- Why it matters:

Consider whichever questions apply:

- Is the comparison fair?
- Could something other than the intervention explain the result?
- Are the labels or assessment criteria trustworthy?
- Do the measures actually capture the claimed benefit?
- Are the data, scenarios or participants suitable for the question?
- Do repeated observations or reused datasets affect the interpretation?
- Are important details missing that would make replication difficult?

### What the Findings Do Not Establish

-

Do not assume that detection accuracy, fewer actions, faster completion,
greater confidence and better response plans mean the same thing.

## 5. Implications for SentinelIR

### RQ1 — Detection Using Combined Logs

- What does this contribute to my log-source comparison?
- Does it directly compare relevant sources, or provide indirect evidence?
- What could inform my detection rules, scenarios or evaluation?

### RQ2 — Investigation and Response Guidance

- What does this contribute to guidance design or evaluation?
- Does it assess investigation, decisions, response plans or another outcome?
- What could inform my response-plan assessment criteria?

Complete only the relevant subsection(s).

### Application and Limits

- Design or evaluation idea worth considering:
- Evidence supporting that idea:
- Differences from SentinelIR that limit transfer:
- What I would still need to test myself:

Separate the paper’s demonstrated findings from my proposed application.

## 6. Connections Across Papers

- Related paper ID:
- Where do the findings agree, differ or complement each other?
- Could differences in inputs, methods, participants or measures explain this?
- Theme this could contribute to in my literature review:
- Unanswered question worth investigating further:

If this is too early to judge, write “Revisit after further reading”.

## Final Takeaway and Next Action

- One-sentence takeaway:
  This paper provides evidence that ___ under ___ conditions,
  but does not establish ___.

- Role in my review: Core evidence / Supporting evidence / Background / Exclude
- Next action:
- Matrix updated: Yes / No
- Relevant connection added to synthesis notes: Yes / No / Not yet applicable
