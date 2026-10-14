# P03 — Detection of attack-targeted scans from the Apache HTTP Server access logs

Use this as a reading guide -> brief notes are enough where relevant!
Complete the sections that help answer my research questions -> mark unchecked details clearly.

## Reference and Reading Status

- Authors: `Baş Seyyar, Merve`, `Çatak, Ferhat Özgür`, `Gül, Ensar`
- Year: 2018
- Venue: Applied Computing and Informatics
- Source type: Journal article
- DOI / link: https://www.sciencedirect.com/science/article/pii/S2210832717300169?via%3Dihub
- Reading status: Read sufficiently for review
- Sections read: All
- Date notes last updated:

## Discovery

- Search date: 12/10/2026
- Search platform / discovery method: Mendeley literature search
- Exact search terms, if applicable: `authentication logs attack detection web evaluation http`
- Search log entry: 003

## Initial Screening — Is It Worth Reviewing?

Complete this before committing to a detailed read.

- Which part of SentinelIR does it relate to?
  - RQ1 — Literature and design justification     Relevance /10? 7
    - Super useful in terms of what type of website to build
    - What web application to use for the vulnerable website! -> `DVWA`
    - How to set it up + configurations
    - Techiques of detecting web app attacks
    - Limitations of detection -> how attacks can `mask` their attack
  - RQ2 — Detection using combined logs           Relevance /10? 9
    - Link to:
      - Detecting vulnerability scanning
      - `XSS` + `SQLI` attacks
      - Access log files
    - Learn how to detect `vulnerability scanners` -> useful to either incorporate / understand / link to!
    - Use of regular expressions to detect:
      - XSS:
        - HTML tags
        - `src` parameters of `img` tags
        - Javascript event handlers
      - SQL injection:
        - Existence of singlequotes
        - Doubledash
        - `#`
        - `exec()`
        - SQL keywords
    - Detection limitation considerations:
      - `URL obfuscation`
      - `Hex`
      - `UTF-8 encoding`
  - RQ3 — Investigation and response guidance     Relevance /10? 0
    - Irrelevant:
      - Bound to only two web app attacks + different scanners
      - No incorportation of preventions to them!
  - Evaluation methods
  - Background / definitions
    - Regular users (normal visit activity)
    - Automated visits -> `crawlers`, `bots`, `spiders`
    - `script kiddies and cyber terrorists`
    - Pentest standard -> `The Penetration Testing Execution Standard (PTES)`
    - Preferences for log files -> `easily available` + doesn't require expensive hardware!
    - Encrypted protocols -> `Secure Sockets Layer (SSL)`
    - Server Daemon -> `Secure Shell Daemon (SSHD)`
    - `Web Application Firewall (WAF)`
    - Previous works detection rules -> `HTTP header fields` + `Uniform Resource Identifier (URI)` + `strings` + `cookies`
    - `Open Systems Interconnection (OSI)` -> `Layer 3 + 4`
    - Previous / Compared Work:
      - Extracted `HTTP` info -> `host name` + `path` + `user agent` + `request method` + `response codes` + `referrer` + `content type fields`
      - Defined into three classes: `Repeated requests` + `HTTP scans` + `web crawlers`
      - Anomaly-detection methods: `Support Vector Data Description (SVDD), K-means, Density-Based Spatial Clustering of Applications with Noise (DBSCAN), Self-Organizing Map (SOM) and Local Outlier Factor (LOF)`
      - `Bayesian estimation technique` -> `Session Anomaly Detection (SAD)` -> `Cho and Cha`
      - Parameters -> `page sequences` + `frequency`

- What could this paper help me understand or decide?
  - Uses a `rule set` for detecting `SQL injection` + `XSS attacks` -> useful to understand the way they went around setting out the rules + detecting + anything else!
  - Understand their approach in terms of understanding:
    - Use of datasets
    - Analysis of results
    - Comparison of methods to `commonly` used detection techniques
  - Understand their suggestions on further development
  - Understand / incorporate the detection of attackers using `vulnerability scanners` -> within the CTF can try to detect both `Nmap` + `SQLmap` to see whether it works!
  - How to compare work which doesn't completely relate but still important in terms of data and info / definitions!
  - Use of `live data`
  - How to both present + explain the use and creation of a Python script based `log detector`
  - Presentation of different stages -> script + model evaluation + real testing on data
- Is it directly relevant, or would its findings need adapting?
  - Needs adapting to detect for all different types of web app attacks!
- Does it provide research evidence, a review of evidence, or guidance?
  - Holds comparable results
  - Understanding into a form of detection
  - Set-up of a vulnerable website
  - Can compare limitations
- Decision: `Keep as supporting material`
- Reason for decision:
  - Very useful paper, holds a lot of interesting and useful approaches, ways to set out rules, and mainly the way of setting up the CTF website!

---

## 1. What Problem Does It Address?

- Research question or aim:
  - Aim:
    - `Propose a method to detect attack-oriented scans and to distinguish them from other types of visits`
  - Objectives:
    - Detect vulnerability scans
    - Detect `XSS` + `SQLI` attacks
    - Examine access log files for detections
  - Analysis:
    - Based on `rule-based` detection strategy
    - Rule set was built around several features of log entries
- Claimed limitation in previous work:
  - Rule sets contained too many `features` -> making input data more complicated!
  - Limited to only `HTTP requests` -> additional could add `HTTP responses`
  - Limitation of using `data-mining techniques` -> simulations results obtain higher accuracy
  - Other work only detect for `user-agent header fields`
  - Use of `rule-based detection` -> compared to `machine learning` + `data-mining`
  - Use of combined log format -> larger number of `features` + more consistent results
- Main contribution, in my own words:
- Relevant page / section:

## 2. How Did They Investigate It?

- Study approach:
- Setting: Lab + Operational environment
- Inputs / log sources:
  - Separated by `visitor types`
    - Type 1 -> web application logs
    - Type 2 -> 3 different company website logs
    - Type 3 -> `DVWA Apache HTTP Server` web application logs
- Dataset or participants:
  - Type 1 (Normal traffic) dataset:
    - Web application running on `Tomcat` web server
    - Collected over 4 days from a `Jira Software` web application
    - File size: `16.3 MB`
    - `62,539` log entries -> `15` different IP addresses
  - Type 2 traffic:
    - From a companies website
    - Across 3 different log files
    - File size: `6.4 MB`
    - Collected over 13 days -> from requests of `web robots`
    - `28,804` log entries -> `143` different IP addresses
  - Type 3 (DVWA web application):
    - From a `DVWA Apache HTTP Server` web application
    - Configured to `low security`
    - Web vulnerability scanners used: `Acunetix, Netsparker and W3AF`
      - Acunetix: `22 mins and 22 seconds`
      - Netsparker: `19 mins and 56 seconds`
      - W3AF: `2 mins and 6 seconds`
- Sample size and unit of analysis:
  - All 3 different `Types` ran

### Detection Method — If Applicable

- Detection approach: `Rules`
- What information does the detector actually use?
  - Path
  - Query parts of the requested URI
  - XSS:
    - Regular expressions to recognise patterns
      - `HTML tags`
      - `src parameters` of the `img` tag
      - Javascript event handlers
  - SQL injection:
    - Existence of `singlequote`
    - Doubledash
    - `#`
    - `exec()`
    - SQL keywords
  - Considerations:
    - `URL obfuscation`
    - `Hex`
    - `UTF-8 encoding`
- What triggers a detection?
- Thresholds / parameters -> how were they chosen?
  - Request-count threshold -> needs checking against the algorithm -> confirm whether it is above or below 100 requests, the time window, and any additional conditions before using this rule!
  - Rules:
    - Static -> `blacklist` + `whitelist` approaches
    - Check the presence of HTTP requests + % of `404` requests
  - Limitations?
    - POST request bodies are not included in the access-log format used -> limits detection of attacks carried in the body -> does not mean POST requests or their bodies cannot be logged through other mechanisms! - Script unable to capture encoded data in other styles -> only uses 2
    - Bound to only two web app attacks + scannerse -> not prevention

## 3. What Did They Find?

### Finding 1

- Main finding, in my own words:
- Supporting result:
  - `99.38%` accuracy
  - `100.00%` precision
  - `75.00%` recall
  - `85.71%` F1 score
- Measurements:
  - Accuracy -> `(TN + TP) / (TN + FN + FP + TP)`
  - Precision -> `TP / (TP + FP)`
  - Recall -> `TP / (TP + FN)`
  - F1 score -> `2TP / (2TP + FP + FN)` -> harmonic mean of `precision` + `recall`
- Conditions under which the finding applies:
  - `Rule-based` approach
- Relevant page / table / figure:
- Limitations?
  - Ability to analyse other types of log files -> `audit` + `error` logs
  - Detection of other well-known web application attacks
- Authors’ interpretation:
  - `Very high probability of detection and low probability of false alarms`
  - Backed up by statistics!
  - That `static rules can detect successful web vulnerability scans`
  - Can handle both `large` and `live` data
- My interpretation:
  - Very strong and comparable results for mine!

## 4. Implications for SentinelIR

### RQ1 — Literature and Design Justification

- Super useful in terms of designing the CTF website
- Approaches and rules around detection
- Evidence of completed web app attack detection
- Structure / layout / representation of information!

### RQ2 — Detection Using Combined Logs

- Useful for setting out equations / figures / measurements
  - Learn, compare and apply to my own -> compare how mine needed to differ, if it did?
- Can pull and adjust their approach to XSS + SQLi and translate to mine
  - In terms of detection methods, rules + approaches

### RQ3 - Investigation and Response Guidance

- Unfortunately prevention was out of scope during this investigation!
- Therefore irrelevant

## Final Takeaway and Next Action

- One-sentence takeaway: Useful in terms of understanding how somewhat of a similar paper presents their approach, findings, results, limitations, and comparing other similar/no-so-similar work to their approach!
- Role in my review: Useful for comparisons, methods used, and report structuring!
- Next action: Find a paper on investigation and response guidance -> prioritise whether guidance helps users produce more technically appropriate and complete response plans -> RQ3!
- - Matrix updated: `Yes`
- Relevant connection added to synthesis notes: Yes
