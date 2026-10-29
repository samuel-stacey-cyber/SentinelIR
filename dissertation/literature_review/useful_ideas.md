# Ideas to be used within Dissertation / Coursework

## Informative Table / Improved Abbreviation Table

When giving abbreviations, provide a table of not just the abbreviation but also the definition, order, and their reference:

| Information Type | Definition | Order | References |
| --- | --- | --- | --- |
| Additional Alerts (AA) | XYZ | 1 | [12], [14] |

## Tables

Have a table including some sort of `%`, providing the reader some sort of scale / data that they can view and understand, with comparable figures.

## Diagrams

Have some sort of diagram with plotted data -> then link back to within writing!

## Figures

Screenshots of the tool -> outputs + explanation of how it works

## Methodology

Include `study goals` -> referring back to the original research question!

## Appendices

# Notes

Making `HTTP log analyser` a big point -> main thing -> comparison against other `HTTP` log analysers as well as for other log analysers analysing other types of logs -> other types -> layout the different types of log analysers -> why I choose `HTTP`
Gantt chart
Risk assessment - presenting issues faced throughout + difficulties + risk matrix as well!

## P01
Remembering that an alert is a common false positive
Always refer back to research questions -> when talking about the process you took (provides meaning to what you actually did, and why it was relevant to have done it / doing it)
Refer back to previous or future parts when speaking / comparing something -> and how it changes compared to this specific thing! -> plus refer to limitations!
Ensure that studies / data collected are consistent and referable!
Explain why something had to change / didn't happen the way it was intended or happened in a previous example!
Comparable conditions -> use the same underlying activity where appropriate -> supports comparison, but does not prove the labels are correct!
RQ2 log sources -> corresponding evidence about the same activity; keep tuning and final evaluation data separate where possible!
Ethical considerations -> use the same throughout + explain them + link them back when another one is used!
Evaluation strategy -> referring back to the original research questions!
Comparison of tables / studies -> how they differed / similar
Results section!
Just before a new paragraph, have `ctrl+i`, a super brief description of what this paragraph is about / its aim: `Experimental setup and ethical considerations.`
Always refer back to the research question when speaking about results `Evaluation Strategy.`
Include a discussion section -> if that applies to a solo writer? -> refer back to each research question and talk about how it was done/wasn't done -> limitations and whatnot

## P02
Brute-force attacks are known as `flat traffic` -> `repeated authentication attempts` - `application-layer actions`
Limiting false positives - look for specific attack behaviour rather than only unusual traffic - investigate whether authentication context helps distinguish attacks from normal login mistakes
Labelling different types of metrics - `True Positive (TP)` - `False Positive (FP)` - `True Negative (TN)` - `False Negative (FN)`
`Brute-force thresholds` -> define exactly what SentinelIR counts + which events belong together + the time window -> explain why the threshold was chosen -> test several values to see how precision and recall change -> link to RQ2!
Comparable data -> group detections and ground truth into the same unit before comparing them -> decide whether SentinelIR evaluates individual attempts, attack sequences or scenarios -> avoid counting several alerts for one attack as several successfully detected attacks!
Ground truth -> record what actually happened in the controlled scenarios separately from SentinelIR's detection rules -> avoid defining an attack only by the same threshold the detector uses!
Authentication context -> a POST request or redirect does not automatically prove failed or successful authentication -> investigate whether application authentication logs provide clearer evidence -> directly relevant to RQ2!
Threshold testing -> use separate scenarios to choose thresholds, then evaluate on held-out scenarios -> avoid choosing the best threshold using the final evaluation results!
`TP`, `FP`, `TN`, `FN`
True positive rate -> `TP / (TP + FN)`
Accuracy -> `(TP + TN) / (TP + FP + TN + FN)`
Compromise evaluation restricted to correctly detected brute-force attacks
Unmatched detections recorded separately as `unclassified`
Literature justification -> compare limitations across papers + record the supporting evidence -> explain how each relevant limitation informs SentinelIR’s design and evaluation -> link to RQ1! -> do not assume SentinelIR resolves it before testing!
`an attack as a sequence of at least N ﬂows towards a CMS backend`
`an interaction as a set of consecutive sessions/connections towards a CMS backend within a certain time period`
Idea of `Preselection` -> minimizing false positives / web crawlers / calendar fetchers -> improving overall performance of the `detection phase` -> more than 7 times! `most computationally expensive component, so its use should be limited as much as possible by conﬁning the input dataset`
List options of approaches -> reason why that specific one was chosen! -> advantages/disadvantages of approach choose + other options out there!
Approach taken in this work: `In this work, we rely on single-linkage as the linkage method, and on MDPA as the distance metric, as discussed in Sect. 3`
State an approach someone else has done -> compare to then the one you've chosen!
Compare detection approaches -> find the gap and try to justify with evidence if and how it worked!

## P03
`script kiddies and cyber terrorists`
Pentest standard -> `The Penetration Testing Execution Standard (PTES)`
As of 2015 -> `web based and web application attacks` -> ranked number 2 and 3 in the cyber-threat environment
Speak about the rate of attacks over time and how they have changed (linked to specific types of vulnerability exploitations!)
Preferences for log files -> `easily available` + `no requirement for inexpensive hardware`
Encrypted protocols -> `Secure Sockets Layer (SSL)` + `Secure Shell Daemon (SSHD)`
Present a problem -> then how their solution solved it!
Nice little description of how the rest of the paper will flow / what info is in what section!
`paths requested for HTTP scans are also requested for brute-force attack as well`
Anomaly-detection methods: `Support Vector Data Description (SVDD), K-means, Density-Based Spatial Clustering of Applications with Noise (DBSCAN), Self-Organizing Map (SOM) and Local Outlier Factor (LOF)`
Research into different `data-mining techinques`
`Bayesian estimation technique` -> `Session Anomaly Detection (SAD)` -> `Cho and Cha`
Detection labelling -> `normal` + `abnormal` -> assigned by a threshold + parameters -> `page sequences` + `frequency`
`i-frame injection attacks` + `buffer overflow attacks`
Activity labelling: `human visitors, well- behaved web crawlers, malicious crawlers and unknown visitors`
`Rule-based detection`
Web vulnerability scanners: `Acunetix, Netsparker and W3AF`
Measurements:
- Accuracy -> `(TN + TP) / (TN + FN + FP + TP)`
- Precision -> `TP / (TP + FP)`
- Recall -> `TP / (TP + FN)`
- F1 score -> `2TP / (2TP + FP + FN)` -> mean of `precision` + `recall`
`sanitize, anonymized or modifie them in any way`
Section explaining: `tools` + `applications` + `VMs` -> installations + configurations explained!
`Apache is used by 51.2 percent of all web servers`
`DVWA design` -> `help web developers fin out critical web application security vulnerabilities by hands on activity `
Going to use `DVWA` for the website!
`Differently from the test environment; an extra module that directly accesses logs, or a script that analyses logs faster could be developed to use our approach in a live or real environment.`
`Observed method-field values`: `Track, Trace, Netsparker, Pri, Propfin and Quit`
Explain detection algorithm -> through pseudocode of the detection model -> `Algorithm XYZ. Pseudo-Code for Proposed Model` -> `Input:` + `Output:` ...
High accuracy does not tell the whole story -> 75% recall means 25% of actual positive cases were missed -> inspect `class balance` + confusion matrix before describing detection as very strong!

## P04
`Security Event Response Copilot (SERC)` -> system designed to assist analysts in responding to and mitigating security breaches more effectively
`Retrieval-Augmented Generation (RAG) methods` -> security event data extraction -> potential investigation?
`Wazuh` -> open-source SIEM platform -> potential investigation into / use? -> continuous development and innovation!
Split into three `vectorised data collections`:
- `incident response knowledge`
- `MITRE ATT&CK framework`
- `NIST Cybersecurity Framework (CSF) 2.0`
SOC limitations:
- Shortage of skilled personnel [1]
- limited automation [2]
- Inconsistent process integration [3]
- Balance of continuous staff training + retention requirements [4] + [5]
SIEM limitations:
- High false-positive rates [6]
- Manual analysis burdens [6]
Explanation of both NIST & MITRE frameworks -> how they work and whatnot
Potential talking point -> speak about how AI can enhance response plans! [13]
AI vs human response planning -> limitations: `scalability` + `accuracy` challenges!
`Wazuh` benefits: `flexibility, scalability, and powerful threat detection capabilities` -> [18]
Management of larger volume of generated data -> `event filtering` -> eliminating `false positives` + `benign activities` -> focusing on meaningful `security signals`
Event categorization: `severity` + `type` -> prioritizing `high-risk incidents`
Nice comparison of different tools, gauging: `cost` + `log management` + `FIM` + `integration` + `deployment` + `scalability` + `community` -> then explains why `Wazuh` was used!
`FIM` -> File Integrity Monitoring -> real-time detection of unauthorized changes -> system integrity + compliance
Was integrated with `Elastic Stack` [34] -> improving data visualization + analysis
`Wazuh` benefits and potential points for SentinelIR -> `customizable rule sets` + `strong community support` + `effective security monitoring`
Advisory strategic goals: `Initial Access, Privilege Escalation, or Defense Evasion`
`HTTPS traffic to obfuscate malicious communication`
`MITRE ATT&CK framework in categorizing tactics, techniques, and procedures (TTPs)`
`The NIST CSF comprises five functions: Identify, Protect, Detect, Respond, and Recover` -> `high-level taxonomy for organizing cybersecurity activities`
AI automation options: `malware detection, phishing prevention, and threat intelligence analysis`
Useful to do comparison to other sectors than just cybersecurity! If applicable!
Fortinet's Advisor
What are XDR features? -> relevant?
`Atomic Red Team` -> `providing security teams with a practical, accessible, and standardized approach to adversary emulation` -> `Red Atomic Attack Emulator, a tool capable of generating precise and controlled attack scenarios`
Potential additional parameter -> `MITRE ID`:
- MITRE tactics
- Alert severity
- Compliance concerns
- Detailed log descriptions
Critical findings: -> potential useful for the response guidance to a given scenario with SentinelIR + more!
- Risk assessments
- Recommended actions
- Contextual insights
`SOCFortess Incident Response Plan`
Potential attack scenarios to incorporate: -> map scenarios to their MITRE ATT&CK technique
- Account Compromise
- Data Loss
- Malware
- Phishing
- Ransomware
`Cosine similarity` -> `semantic alignment between the copilot’s recommendations and the ground truth`
`BERTScore` -> contextual accuracy
Need some `plotable` data! -> one thought:
- There are three stages of SentinelIR
  - Attack occurs
  - Detected
  - Incident response -> idea is creating an LLM using a dataset -> then within the CTF, will ask the participants to use the LLM and then let me review it, providing feedback, how their response plan differed and correctness, then I can pull figures out of it???
Another mention of `F1-score` will definitely need to try to incorporate this!
`Security Orchestration, Automation, and Response (SOAR) systems` -> end-to-end automation of the incident response lifecycle

## P05
First use case of `APA referencing`
`CDC` -> `Cyber Defence Centres` -> SOC
Major incidents:
- Data breaches
- DDoS attacks
- Malware campaigns -> new one!
SOC criteria:
- Threat intelligence
- Prioritization
- Resolution
- External communication
- Solution:
  - Adaptation of tools + methods -> improving both `performance` + `quality`
`TIBER-EU framework` -> ??? -> https://www.ecb.europa.eu/pub/pdf/other/ecb.tiber_eu_framework.en.pdf
`Cybersecurity Threat and Incident Managers (CTIMs)`
Aiming to speed up threat incident management -> providing relevant `cues` + `triggers` -> reducing flaws + mistakes!
- `Applied Cognitive Task Analysis` -> ???
- `Cognitive task analysis (CTA) ` -> Ooo really useful for gauging and comparing the differences in terms of both `knowledge` + `strategies`!!! + `Cognitive work analysis (CWA)`
Could potentially hold some interviews as well??? More data???
Potentially speak about how the dataset/knowledge of incident support can be turned into workshops employers can use???
Comparison / discussion around how `most` organizations focus on ISM!
SOC operator breakdown:
- Level 1 & 2:
  - First / second analysis of events
  - Tasked with:
    - Making the first assessment
    - Triage the problem
    - Generate context used for a `ticketing system`
    - Directly respond to `low-criticality incidents`
    - Determination of whether an incident is real or it is a `false positive`
    - Identify alerts that require a follow-up!
- Level 3:
  - Usually follows up on the alert identified by the lower operators
  - Due to having more experience with process + analytical tools
- Team within the SOC:
  - Investigation into the provided alert + from other sources: `vendors` + `external stakeholders`
  - Gauges whether action is required?
`Decision Support Systems (DSSes)` -> supporting + improving decision-making
Support decision processes:
- Security standards
- Training resources
- Vulnerability databases
- Best practices
- Catalogues of security controls
- Security checklists
- Benchmarks
- Threat information feeds + reports
`Personal DSSes`:
- Playbook:
  - Linear style checklist of required steps and actions required to successfully respond to specific incident types and threats
- Critical Incident Plans (`CIPs`):
  - Incident response policy and procedure for responders allowing them to have the capacity to respond appropriately in the event of a critical incident
  - Goal: Return to normal as quickly as possible after the incident; and to limit the effects of the incident on operations and any parties affected by the incident
`Applied Cognitive Task Analysis (ACTA) approach` -> used to understand methods and techniques for uncovering knowledge and cognitive strategies -> consisting of three activities:
- Task diagram
- Knowledge audit
- Simulation interview
`Thematic analysis`!
CWA is `mostly bound by the highly influential approach`
`tabular abstraction hierarchy`
`dialectical inquiry approach`
`Decision ladder`
Playbooks are insufficient for the needs of SOC's
SOC's deal with so many factors -> difficult to balance them all at once!
`Is a new role needed within a SOC?`

## P06
Papers to review from this paper:
- https://ieeexplore.ieee.org/abstract/document/8806735
- https://www.usenix.org/conference/usenixsecurity22/presentation/sanusi-bohuk
Password guessing -> an important account-compromise threat; avoid claiming it is the single most effective cause!
Credential stuffing -> use of previously breached credentials on other applications
`User risk profiles`
`Gossamer`
`Arana`
`Agglomerative clustering`
`attack campaigns` -> set of login request likely to be submitted by the same attacker
`Low and slow` approach -> by submitting a low number of requests per day at a slow rate
- `Use a small number of guesses per target account (low)`
- `Per unit time (slow)`
Don't just focus on the high volume of IPs / same IP -> look for `low volume, targeted attacks`
`Breach alerting APIs` -> Most compromised users, also had their passwords in known breaches -> `[22, 27, 43, 45]`
Ways of tackling compromise -> consider `rate limiting` + `2FA`
Changing the destination URL -> attacker targeting behaviour, not a prevention technique!
`Distributed attacks` -> requests spread across multiple IPs
`Low-and-slow attacks` -> fewer requests over long periods
`natural lanaguage processing techniques`
`Credential tweaking attacks` -> submitting slight variants of breached passwords
`Schechter et al. [39]` -> `StopGuessing: Using Guessed Passwords to Thwart Online Guessing`
`Privacy-preserving data structures` -> `Binomial ladder filter`
Attackers can `spoof push-based 2FA` -> can hide it by sending them soon after the victim has logged in!
Have a look into their previous work + maybe be able to pull over points for SentinelIR! -> `Gossamer` `Gossamer: Securely Measuring Password-based Logins`
Secure storage techniques:
- Submitted passwords:
  - Encrypted
  - Stored in a `in-memory database`
  - Then cryptographically erased every 24 hours
- Usernames
  - Deterministically encrypted
`used a machine only accessible to a subset of researchers logging in from a specific computer in the university network and requiring a strong password and 2FA for acces`
What is a `Client user agent string` -> `a short piece of text that a web browser or client application automatically sends to a web server in every HTTP request`
Ways the used to try to predict maliciousness:
- Linear regression -> poor precision in this experiment with imperfect proxy labels -> not a general judgement about the method!
- Decision tree
- Random forest
- Logistic regression
- SVM models
`Silhouette score` -> `a metric used to evaluate the quality of clustering models like K-Means by measuring how well each data point fits its assigned cluster compared to other clusters`
Non-existent username -> possible suspicious signal, but legitimate typing mistakes can also cause it!
`Horizontal attack`
Preventions: disallow both popular + weak passwords!
`BlackBox API`
`HIBP`
Minimising false positives:
- Choose aggressive thresholds
- Evaluating threshold's effect

P06 -> implications for SentinelIR:
- Test benign lookalikes -> mistyped usernames + repeated legitimate failures
- Record scenario ground truth separately from detection rules
- Distinguish `suspicious activity` from `confirmed compromise` in alerts + guidance
- Test added authentication fields -> do not assume more data automatically improves detection
- Thresholds -> evaluate missed attacks as well as false alarms
- Password-storage notes above describe Gossamer -> not a plan to collect participants' passwords in SentinelIR
- Keep clustering as literature context unless justified within scope -> no requirement to rebuild `Araña`!

## P07
Playbook benefits, potentially good ideas for the response-guidance part:
- Checklists are useful!
- Communication templates!
`CISA`
`The NIST Computer Security Incident Handling Guide` - emphasize speed of recovery and restoration of availability
`Integrated Adaptive Cyber Defense` - asks users to consider how tasks could be automated
`SOTER` - wasn't selected as other two were more common!
`Honey-words` - usernames + password for valid but fictional accounts - detecting credential misuse
`Playbook designers must be concise yet descriptive terms to cue defender actions`
Evidence-linked response plans, must include:
- TOC
- Boldface titles
- Summaries!
