# P02 - Flow-Based Web Application Brute-Force Attack and Compromise Detection

## Reference and Reading Status

- Authors: `Hofstede, Rick`, `Jonker, Mattijs`, `Sperotto, Anna`, `Pras, Aiko`
- Year: 2017
- Venue: Journal of Network and Systems Management
- Source type: Peer-reviewed journal article
- DOI / link: https://doi.org/10.1007/s10922-017-9421-4
- Reading status: Basically completely read
- Sections read: All
- Date notes last updated: 11/10/2026 (template and research-question alignment)

## Discovery

- Search date: 04/10/2026
- Search platform / discovery method: Mendeley literature search
- Exact search terms, if applicable: `brute force web attack`
- Search log entry: 002

## Initial Screening — Is It Worth Reviewing?

Complete this before committing to a detailed read.

Understanding from the `Abstract` + `Background` + `Conclusion`:

- Which part of SentinelIR does it relate to?
  - RQ1 — Literature and design justification     Relevance /10? 8
    - Useful to understand their approach to log analysis
      - Through they way they analysed it
      - Datasets used / how that data was stored / how the data was collected
      - Samples sizes used / comparison of
      - How data was used then evaluated
      - Specific techniques / steps needing to be taken to complete something?
      - Specific terminology used -> useful facts to use / definitions / metrics
    - Layout of both presenting data + evaluation
    - Useful to understand the reasoning behind choosing `Flow-Based Web Application Brute-Force Attack`
      - Comparable with my `HTTP` attacks
      - Learn how to layout my reasoning behind my decisions
      - Present current limitations of these types of attacks
      - How they tackled `false positives`?
  - RQ2 — Detection using combined logs           Relevance /10? 7
    - Mentions one type of logs -> `brute-force attacks`
    - Invesitgation into `HTTP` logs
    - Conclusion:
      - Mention of how false positives and negatives are a clear industry standard issue
      - Mention of how different cipher suites and key exchanges protocols effect the size of HTTPs flows
        - Attackers attempt to remain invisible by using different cipher suites
      - Make detection approaches more resilient against `evasion techniques`
  - RQ3 — Investigation and response guidance     Relevance /10? 2
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
- Decision: `Keep - supporting background + evaluation context + comparable data/paper`
- Reason for decision:
  - Relevant due to the investigation into real data -> will be the same when for the CTF -> useful to compare the different types of detections
  - Process of using/handling real-world logs/data
  - Evaluates the detection of web application brute-force attacks
  - Useful comparison of log-based approach -> different types of logs
  - Not directly relevant to RQ3 -> no link to response plans / guidance
  - Useful background on encrypted traffic, evasion, and difficulties with distinguishing attacks

Judge relevance and evidence, rather than relying only on the title,
publication year, citation count or author reputation.

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

Distinguish the gap claimed by the authors from a gap I have independently
established through reading across the literature.

## 2. How Did They Investigate It?

- Study approach:
  - Built a flow-based detector using `packet-payload` histograms + clustering
  - Evaluated `brute-force` and `compromise` detection -> excluded the `scan` phase
  - Developed an Apache access log parser -> grouped records into `interactions`
  - Processed both datasets into comparable interactions -> compared detections against reference labels
  - Compared their approach against previous work `[24]`
- Setting: `Lab experiment + operational validation`
- Inputs / log sources:
  - Enhanced `IPXFIX flow data` -> detector input
  - Web server access logs -> ground-truth tables
- Dataset or participants:
  - Hosting 2GO production network -> one month during July/August 2015
  - ~`2500 hosting accounts` / `2603 vhosts`
  - Traffic datasets
- Sample size and unit of analysis:
  - `854945 interactions` -> processed ground truth
  - `Interaction` = consecutive sessions/connections towards a CMS backend
  - Flow sessions grouped when the idle gap is less than `5 minutes`
  - Gap choosen to accommodate short sessions + timing differences
- Baseline / comparison conditions: `Previous flow-based detection approach [24]`
- What changed between conditions, and what stayed consistent?
  - Changed? -> detection approach
  - Consistent? -> validation datasets + reference labels
  - Both? Compared at interaction level
- Ground truth or assessment criteria:
  - Consecutive POST requests to a CMS login page exceeding `N` -> `malicious interaction`
  - Validation used `N = 20`
  - Compromised labels depend on the CMS:
    - `WordPress` -> movement from `Login URl` -> `backend URL`
    - `Joolma` -> larger responses associated with the backend
    - `Drupal` -> redirect status code
    - Labels therefore depend on assumptions about application behaviour -> consider this when assessing reliability!
- Evaluation measures:
  - `TP`, `FP`, `TN`, `FN`
  - True positive rate -> `TP / (TP + FN)`
  - Accuracy -> `(TP + TN) / (TP + FP + TN + FN)`
  - Compromise evaluation restricted to correctly detected brute-force attacks
  - Unmatched detections recorded separately as `unclassified`
- Relevant page / section: `4`, `5`, `5.2 Datasets`, `5.3 Approach + Figure 9`, `5.4 Metrics`

Check whether repeated observations come from the same participants,
alerts, attacks or datasets.

For a review paper, record its search, selection, appraisal and synthesis
methods instead of an experimental setup.

Use “Not applicable”, “Not reported” or “Not yet checked” accurately.

### Detection Method — If Applicable

- Detection approach: `Thresholds` + `Classification rules` + `Hierarchical Cluster Analysis (HCA)`
- What information does the detector actually use?
  - IPFIX flows -> packet-payload-size histograms
  - Grouped traffic -> `source` + `destintation`
  - Access logs -> validation labels
- What triggers a detection?
  - Brute-force -> similar histograms within the largest cluster + additional checks
  - Compromise -> unusual return-traffic histogram -> after detected brute-force activity
- Thresholds / parameters -> how were they chosen?
  - `N = 20`
  - Due to covering roughly the upper 10% of attack sizes measured
  - `Number of clusters`
    - Expressed as the validity of clustering results
    - An `internal index` after every HCA step
  - Limitations?
    - Led to `failed login attempts` to be filtered out
  - Benefits?
    - Reduced the load on their prototype -> very small attacks + noise
  - Intra-cluster distance threshold `0`
  - Cluster relation size: `1:1`, `1:2`, `1:3`
  - Average distance between histograms in both clusters, `y`, at least `75`
- Was tuning separate from the final evaluation?
  - Separate held-out tuning/testing split wasn't reported!
- Main assumptions -> when might these fail?
  - Repeated attempts -> similar traffic
  - Normal traffic differs -> photo galleries -> `false positives`
  - Compromise changes return traffic

## 3. What Did They Find?

### Finding 1

- Main finding, in my own words:
  - Approach taken outperformed existing approaches
  - Number of `false positives` -> reduced to 10% of baseline/compared results
- Supporting result:
  - Large number of `TP + FN` / correctly detected malicious interactions -> `469 vs 237` compared results against baseline
- What does the number measure, and what is its denominator?
- Conditions under which the finding applies:

  - `False Negatives`
    - Caused by `low-intensity attacks` -> minimal traffic generation + < `N`
    - Distance between histograms exceeds `0` (threshold)
- Relevant page / table / figure: `5.5 Results` + `Table 2 + 3`
- Authors’ interpretation:
  - Argues that their approach improves detection compared to the evaluation baseline
- My interpretation:
  - They were able to produced more clean results
  - Beat previous results in terms of not detecting `false positives`
  - Better detection of `TP`

### Other Important Findings

- Mixed results, no detected improvement or unexpected outcomes:
- `False Positives`
  - Related to `photo galleries`
  - Thumbnails

## 4. Implications for SentinelIR

### RQ1 — Literature and Design Justification

- Normal photo-gallery traffic caused `false positives` -> `Section 5.5`
  - Include normal lookalikes when evaluting SentinelIR + test whether authentication context distinguish them!

### RQ2 — Detection Using Combined Logs

- Indirect evidence -> evaluates flow-based detection using access logs for validation -> doesn't compare access logs alone against combined + authentication logs -> test these!

## Final Takeaway and Next Action

- One-sentence takeaway:
  This paper supports flow-based brute-force detection under its evaluated conditions -> doesn't establish whether combining access and authentication logs improves detection!
- Role in my review: `Core evidence`
- Next action:
  - Use as a useful reference in terms of the results, approach and actions taken when handling both datasets and defining the rules, thresholds, and storage/collection of brute-force / web authentication logs/traffic
- Matrix updated: `Yes`
- Relevant connection added to synthesis notes: Yes / No / Not yet applicable
