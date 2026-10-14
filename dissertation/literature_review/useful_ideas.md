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

## P01
Remembering that an alert is a common false positive
Always refer back to research questions -> when talking about the process you took (provides meaning to what you actually did, and why it was relevant to have done it / doing it)
Refer back to previous or future parts when speaking / comparing something -> and how it changes compared to this specific thing! -> plus refer to limitations!
Ensure that studies / data collected are consistent and referable!
Explain why something had to change / didn't happen the way it was intended or happened in a previous example!
Multiple studies -> try to use the same data -> providing comparable data + ensures that the original data was `true` -> allows for a comparison of data (another talking point)
When having two sources of `data` -> make them disjointed (unlinked) to provide different `sides of the street`
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
