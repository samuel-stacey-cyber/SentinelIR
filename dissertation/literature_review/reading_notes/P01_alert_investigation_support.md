## P01 — A Field Study to Uncover and a Tool to Support the Alert Investigation Process of Tier-1 Analysts

- Authors: `Kersten, Leon`, `Beelen, Kim`, `Zambon, Emmanuele`, `Snijders, Chris`, `Allodi, Luca`
- Year: 2025
- Venue and source type: `USEC 2025 — conference paper`
- Search Date: 4/10/2026
- Search Terms: `alert investigation`
- Reading status: **Mostly Read**
- Relevance: RQ1 / RQ2 / Evaluation methods / Background

## 1. What Problem Does It Address?

- Research question or aim:
  - How effective is current alert investigation is? What does that consist of? How can it be improved? Current limitations? Are improvements through a support piece of software/system? How does it differ per investigation? How impactful is it per investigation?
- Claimed limitation in previous work:
- Main contribution, in my own words:

## 2. How Did They Investigate It?

- Study approach:
- Inputs / log sources:
  - By working with both T1 and T2 analysts. Main thing was investigating how T1 analysts worked, what they did and asked how the things they struggle with can be improved. T2 were used to verify whether the modifications to the tool were still within the original scope that an analyst would use.
- Dataset or participants:
  - Different types of alerts, number of alerts used with the experiment and their classification
  - Figures based on how successfully the T1 analysts were able to retrieve information, differred per category
  - ES1 Results:
    - During 223 investigations, out of them 160 of the investigations was assisted with external tools
    - But differed for other categorys of alerts
  - ES2 Results, due to time constraints:
    - Sample of alerts were reduced from 200 -> 18
    - Sample was created using a randomly selected alert from each injected attack from ES1
    - Plus another random sample of 8/178 NAtt alerts
- Sample size and unit of analysis:
  - Analysts
    - Five T1 analysts -> 400 investigations
    - Four T1 analysts -> 36 investigations
  - Alerts, created 200 total alerts for 10 total experiments used for the dataset for the development of the tool, all categoried as well:
    - 22 `Att` alerts
    - 178 `NAtt` alerts
  - Alerts were split into 2 scenarios (18 -> 9/9) + assigned their own subjects per split
- Baseline / comparison conditions:
  - Sample used + environment used, within ES2 was also in ES1, therefore there were comparable results
- Ground truth or assessment criteria:
- Evaluation measures:
- Relevant page / section:

If a field does not apply or is not reported, state that.

## 3. What Did They Find?

- Main finding:
  - Identified different types of information analysts retrieve + actions taken when coming across different types of alerts
    - Further findings found that when escalating dangerous alerts -> required larger amount of information + actions needing to be taken -> therefore an even more need for a tool to support them / reduce time / provide them the information without actions needed
  - These results imply the need for a `AISS` to support the analysts
  - Results from the support `AISS`, showed that `AISS` can aid analysts in reducing the complexity for all alerts -> except for the most trivial to analyse.
  - Results from ES2 were much stronger compared to ES1
- Supporting result, including what the number measures:
- My interpretation:
  - They found that when first reviewing how analysts work, what tools / actions they take in order to discover then analyse then escalate alerts, what strengths/limitations there are?
  - Then did some sample experiments with alerts, create a tool, got reviewed by more senior analysts
  - Then tested with the T1 analysts, first without the tools, discovering their limitations and what/how improvements can be made.
  - Then created the tool, and trialed it with the analysts against the same sample
  - Findings were that the support tool, made investigations overall less complex and was able to provide figures on how effective analysts truely are

## 4. How Convincing Is the Evidence?

### Strengths

- Used multiple different samples
- Repeated samples for comparable results
- Results changed the second time around
- Got a review from senior analysts for a review/improves of the tool
- Two different studies, with comparable results -> then discussed and compared how they differred
- Was able to pull data from the experiments, producing both tables + overall figures of the results

### Limitations acknowledged by the authors

- Had issues with the second study with time constraints
- SOC's operate differently + employ different techinques/technologies -> therefore the tool wont fit `perfect` for everyone
- T1 analysts had differring skills sets -> despite working within the same context
-

### My critical observations

- Strong investigation into something that is know information / common sense
- Interesting on the analysis of junior analysts
  - Differ samples used of alerts
  - Different types of alerts
  - How they are categorised
  - Process taken
- Process taken to carry out the experiment
- Repetition of samples/data for testing
  - Resulting in comparable results
  - Minimised time spent creating `training` data / data used within each experiment
- Structure/flow of the report
- Discussion session
- Use of lots of different references
- Use of a sample description before some paragraphs

### What the findings do not establish

- Not sure

## 5. Implications for SentinelIR

### RQ1 — Detection using combined logs

This paper does not resolve my access-log-only versus combined-log comparison. I still need detection literature and an experiment with independently established ground truth.

The alert taxonomy also requires care: detecting an unsuccessful malicious login attempt can still count as a correct detection in my study, even if the incident would not warrant escalation under another organisation’s procedures.

### RQ2 — Investigation and response guidance

I would use this paper to motivate investigating whether structured assistance helps users work with alert evidence.

For SentinelIR, a candidate guidance structure could be:

- What activity triggered the alert?
- What supporting evidence is available?
- What remains uncertain?
- What should the user verify next?
- Which response actions are appropriate if that verification confirms the suspected activity?


- Design or evaluation idea worth considering:
  - Short but meaningful `Abstract`
  -  Clearly present research questions
     -  Always referring them when possible, no matter the section
     -  Referring in both the `Discussion` and `Conclusion` sections
     -  Presented the research question
     -  Then actually explained and spoke through the experiments conducted
     -  Linked the experiments done to each research question
-  Gave an overall background of the paper / things done and used
-  Talks and compares relating work, but shows how their scope / goal differred to theirs
   -  Referring them
   -  Explaining them
   -  How they differred to what they ended up doing
   -  Loads of different examples used during comparisons
-  Then after speaking about related work, moved onto the studies done
-  Studies:
   -  First layed out the goal of the study
   -  Next an overview of methods used
   -  Subjects, more information
   -  Discussed different types of alerts
   -  Setup of the experiment
-  Techniques used to create the tool
   -  How they first created it
   -  Provided it to more senior analysts
   -  Recieved feedback
   -  Was able to compare how they different stages of the tools differred
   -
- Differences from my project that limit transfer: Not sure
- Connection or disagreement with another paper: `N/A`
- Possible use in my literature review:
  - Potentially useful in terms of understand what the different types of alerts are, how to identify / classificate them?
  - Overall layout -> useful to use as a template / pull ideas from

### Findings from Abstract

Goal: Discover how analyst conduct alert investigations
    Which information they considered and when

Through: Collaborating with commerical SOC and two `think-aloud experiments`

Experiments:
1. `Evaluate the alert investigation process followed by professional T1 analyst and identify crieteria within`
2. `Development of an alert investigation support system (AISS) -> integrated into a SOC environment -> evaluate its effectiveness against alert investigations with a cohort of T1 analysts`

Findings of experiments:
1. Five analysts: `400` investigations
2. Four analysts: `36` investigations

Results:
    Approach of analysts differed between them
    AISS aided them in terms of gathering more relevant information -> while performing fewer actions

### Main Research Question Breakdown

1. **RQ1**: `What type of information do T1 analysts consider when classifying alerts, what sources do they rely on to collect it, and to what extent does this depend on the type of investigated alert?`
2. **RQ2**: `To what extent does the analysis process followed by different T1 analysts vary between (a) alerts of different types and (b) analysts?`
3. **RQ3**: `Can the T1 analyst alert investigation process be improved by the addition of an alert investigation support system, and how doese that impact the collected information during an investigation?`

Answering them:
    **RQ1 + RQ2**: Five T1 analysts -> discover what information they consider when analysing 400 security alerts + identify inefficiencies in teh analysis process -> stability and considered information
    RQ3: Development of a AISS tool -> integrated into a SOC SIEM -> across 2 different teams -> evaluating the tools effectiveness + inefficiencies in the first team

### Coding Strategy and Coding Scheme - Section IV

Broke the research questions into two different concepts:

1. `input`: Information relevant to the security analysis -> `network log` / `malicious IP address`
2. `process`: Action aimed at processing relevant information -> `protocol-related logs` / `purpose of a domain`

#### Categorised

Four types:
1. `Relevance Indicators (RI)`
2. `Additional Alerts (AA)`
3. `Contextual Information (CI)`
4. `Attacker Evidence (AE)`

#### Strategy

Three brainstorming sessions -> through four authors + senior analyst (4+ years of experience)
They opted on an approach of `soley` relied on the senior analysts experience, to first identify:
    Main set of actions taken
    Relevant information to look for in data

#### Scheme

Refined through a coding process done in three rounds
Disagreements about codes were discussed -> lead to refinement of the coding scheme

After three refinements:
    Coding scheme was verified with T2 analysts
    Ensuring the accuracy after modifications were made
    Once verified by T2 analysts -> codebook was finalised

## Second Study - Section V


# Currently At:
C. ES2 Results
1) Types of information acquired when using the AISS (RQ3): Table V provides an overview of the number of investigations in which an analyst gathered information for Att and NAtt alerts in ES2.
