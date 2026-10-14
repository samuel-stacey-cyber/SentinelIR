# P04 — Enhancing Security Operations Center: Wazuh Security Event Response with Retrieval-Augmented-Generation-Driven Copilot

## Reference and Reading Status

- Authors: `Ismail`, `Rahmat Kurnia`, `Farid Widyatama`, `Ilham Mirwansyah Wibawa`, `Zilmas Arjuna Brata`, `Ukasyah`, `Ghitha Afina Nelistiani`, `Howon Kim`
- Year: 2025
- Venue: Sensors
- Source type: Peer-reviewed journal article
- DOI: `10.3390/s25030870`
- Reading status: `Read sufficiently for review`
- Sections read: `All sections completely read and highlighted / useful info pulled out and noted down!`
- Date notes last updated: 14/10/2026

## Discovery

- Search date: 13/10/2026
- Search platform / discovery method: Mendeley literature search
- Exact search terms, if applicable: `guidance response security incident security`
- Search log entry: 004

## Initial Screening — Is It Worth Reviewing?

Screening judgement updated after reading the full paper.

- Which part of SentinelIR does it relate to?
  - RQ1 — Literature and design justification     Relevance /10? 7
    - Useful to understand how security events + supporting knowledge are used to generate guidance!
    - Highlights an evaluation limitation -> similarity to reference responses does not prove technical correctness or improved user response plans.
    - Helps justify why SentinelIR should assess response-plan quality directly.
  - RQ2 — Detection using combined logs           Relevance /10? 2
    - Uses event data collected by `Wazuh` during simulated attacks.
    - `RAG` supports retrieval + guidance generation -> not a comparison of detection using different log sources.
    - Does not compare HTTP access logs alone against access + authentication logs.
    - Some useful ideas around scenario generation, but limited evidence for RQ2!
  - RQ3 — Investigation and response guidance     Relevance /10? 7
    - Useful example of connecting security events to contextual investigation + mitigation guidance.
    - Provides guidance-design ideas -> does not establish whether users produce better response plans.
    - Uses `cosine similarity` + `BERTScore` to assess generated text -> these do not directly measure technical appropriateness or completeness of users’ plans.
    - Generated the idea of building an assistant using an existing LLM to help users develop response plans -> potential implementation choice, not yet decided!
- Decision: `Keep as supporting material`
- Reason for decision:
  - Relevant to guidance design + evaluation limitations, even if SentinelIR does not use an LLM.
  - Useful for understanding how LLMs can support security workflows + where their evaluation falls short.
  - Need another paper focused on human evaluation -> comparing response decisions or plans with and without assistance!

---

## 1. What Problem Does It Address?

- Research question or aim:
  - Contributions:
    1. Enhance threat data extraction methods using `RAG`
    2. Embedding AI within `Wazuh` -> improved incident response using mitigation guidance
    3. Employing LLMs: `precise` + `context-driven` recommendations
    4. Comparison of the different models! [20] + [21]
  - Aim:
    - Further enhance `Wazuh's` capabilities using both AI and machine learning -> focused on incident response and threat intelligence
    - Use AI to both:
      - Automate complex analytical processes
      - To deliver `real-time` + `contextually relevant` insights
      - Improving:
        - Response accuracy
        - Decision-making
        - Mitigate fatigue
    - Address key challenges in incident responses
      - Alert fatigue
      - Data relevance
      - Through real-time data retrieval -> actionable intelligence
  - Proposed framework: `Wazuh Copilot`
    - Incorporating AI in Wazuh
    - Improving:
      - Deployments
      - Leveraging SIEM + XDR features
      - Combination of generative AI functionalities
- Claimed limitation in previous work:
  - Current integration of `Wazuh` lack direct connection with AI -> improving both accuracy + responsiveness!

## 2. How Did They Investigate It?

- Study approach:
  - Model Comparison of:
    - GPT-4
    - T5 (Text-to-Text Transfer Transformer)
    - `LLaMA`
    - `CyberBERT`
    - Pixtral 12B
    - Focusing on:
      - Log analysis
      - Incident response
      - Contextualizing threat intelligence
  - Went with GPT-4 + Pixtral 12B for their `SERC`
    - GTP-4o
      - Language understanding
      - Contextual reasoning
      - Processing of complex textual data
      - Effective for tasks like:
        - Intelligence repots
        - Actionable insights
        - Incident response guidance
    - Pixtral 12B
      - Multimodal data interpretation
      - Instruction following
        - Effective for inputs like:
          - Log data
          - System alerts
          - Visual representation of threats
- Setting: `Controlled attack simulation using Wazuh`
- Inputs:
  - Event logs in JSON format
  - MITRE ID -> retrieves correlating information from a server / database
  - AI prompts:
    - Initial enquiry
    - Follow-up interaction
- Inputs + outputs:
  - Attack actions
  - Detection and response
- Retrieval sources:
  - MITRE ATT&CK framework
  - General incident response guidelines
  - NIST Cybersecurity Framework (CSF) collection
  - Providing `precise` + `actionable` + `context-aware guidance`
  - Enhancing `real-time incident response` + `decision-making scenarios`
  - `SOCFortess Incident Response Plan` -> real-world threat scenarios (robust benchmark)
  - Simulated attacks -> `Red Atomic Attack Emulator`
- Dataset:
  - Simulation attack scenarios: -> all linked to their `MITRE ATT&CK technique`
    - Account Compromise
    - Data Loss
    - Malware
    - Phishing
    - Ransomware
- Comparison conditions:
  - AI generated responses vs curated ground truth
- What changed between conditions, and what stayed consistent?
  - Changed?
    - Modularization of documents within the database -> `Natural Language Toolkit (NLTK) splitter`
    - Unified indexing -> ensuring contextual integrity -> improved mitigation and incident responses

### Detection Method — If Applicable

- Detection approach: `Machine learning`
- Approach explanation:
  - Data is embedded using: `BAAI/bge-large-en-v1.5 model`
  - Vector storage + similarity search: `Qdrant`
  - Event logs are inputted in JSON format
    - Key metadata includes: -> enhancing accuracy + relevance
      - MITRE tactics
      - Alert severity
      - Compliance concerns
      - Detailed log descriptions
      - Ensures that all logs are transformed correctly -> no matter their original structure
  - Input is then parsed and encoded using an extractor powered by the `Pixtral` model
  - Finally encoded and embedded into storage + then retrieved from the vector database
  - Data refinement process:
    1. Raw JSON event logs are converted into encoded JSON format
    2. The encoded JSON is embedded into a user prompt -> `one-shot output approach`
    - Allows for more efficient `tokenisation` + `comptability` + `retrieval`
- Thresholds / parameters -> how were they chosen?
  - Fine-tuning the LLM -> retraining the model on `domain-specific data`
    - Limitations?
      - Computationally intensive
      - Frequent retraining
      - Struggles with incorporating the most recent threat intelligence
    - Benefits?
      - Able to understand `cybersecurity language`
    - Adaptations:
      - `RAG`
      - Retrieves relevant information from external knowledge sources during inference
      - More flexible + scalable solutions
      - More accurate + responsive decision-making
  - Parameters:
    - Temperature: Set to`0.1`
      - Ensures:
        - High determinism
        - Minimizing randomness -> `predictions`
    - Top-k: Configured to `50`
      - Restricting token sampling
      - Reduces the likelihood of low-probability tokens
    - Top-p (Nucleus Sampling): Set as `0.9`
      - Dynamic token selection
      - Considers tokens with a cumulative probability of `90%`
      - Balance between `determinism` + `contextual diversity`
    - Max Tokens: Defined as `4096`
      - Total number of tokens in the generated output
      - Applications requiring both `concise` + `comprehensive` responses
  - Metrics:
    - `Cosine similarity` -> `semantic alignment between the copilot’s recommendations and the ground truth`
    - `BERTScore` -> contextual accuracy
- Experiment:
  - Conducted a `end-to-end simulation of attack` + `defence mechanisms`
  - Evaluating the integration of `automated detection` + `mitigation procedures`
  - Utilizes `Atomic Red Team` to simulate predefined adversarial scenarios

## 3. What Did They Find?

### Finding 1

- Supporting finding:
  - GPT-4
    - Strengths:
      - Summarizing threat intelligence repots
      - Analysing phishing emails
    - Limitations:
      - Binary reverse engineering
      - Analysis of detailed logs
      - Handling of `nuanced` + `domain-specific` problems -> without fine-tuning
  - T5
    - Strengths:
      - Translating log data into actionable insights
      - Parsing security documentation
      - Generating attack scenario summarizes
      - Conducting vulnerability assessments
    - Limitations:
      - Needs optimization for improved speeds -> currently too slow!
  - `LLaMA`:
    - Strengths:
      - Reasoning
      - Analytical tasks
    - Limitations:
      - Requires significant configurations to be effective!
  - `CyberBERT`
    - Strengths:
      - Proficient in:
        - Malware classification
        - Log analysis
        - Phishing pattern identification
    - Limitations:
      - Generative capabilities -> report writing + threat scenario simulation
  - Pixtral 12B:
    - Strengths:
      - Image + text processing
    - Limitations:
      - Requires fine-tuning for:
        - Intrusion detection
        - Phishing email classification
      - Can be improved using `Low-Rank Adaptation (LoRA)`
- Main finding, in my own words:
  - OpenAI was a stronger model, but lack consistent performance across the 12 scenarios
  - Pixtral however produced `steadier` performance!
- Supporting result:
  - `Cosine Similaritry (%)`
    - OpenAI peaked at `75.81%` in `scenario 8`
    - While Pixtral peaked at `71.69%` in `scenario 9`
  - `Precision (%)`
    - Pixtral was the more dominant model -> maintained a higher precision average
      - Held a very small range -> `84.5% -> 87.0%`!!!
    - While OpenAI's was variable -> sometimes dipping or exceeding Pixtral `precision`
  - `Recall (%)`
    - Both models held very similar results in terms of both lowest and range achieved
    - However Pixtral was the more dominant model -> peaking at both a higher low and high values
      - Held a very small range -> `85.6% -> 87.5%`
    - While still very close, OpenAI still displayed greater variability!
      - With a range between `84.8% -> 86.9%` -> still very close to Pixtral!
  - `F1_Score (%)` (`BERTScore`)
    - Once again both models held very similar results
    - However Pixtral once again beat OpenAI by a small margin
      - Pixtral: `85.4% -> 87.2%`
      - OpenAI: `84.9% -> 86.5%`
- Measurements:
  - Cosine Similarity
  - Precision
  - Recall
  - F1 Score
- Relevant page / table / figure:
  - `Section 4.3: Performance Evaluation`
  - `Figure 9 -> 12`
- Main findings?
  - Pixtral was more consistent in terms of:
    - Reliability
    - Stable precision
    - Recall
    - F1 Score
    - However performance did plateau during certain scenarios!
  - Although OpenAI had a much broader range of performance metrics
    - Showcasing its `adaptability` + `strong contextual understanding`
    - But still had noticeable dips in `recall` + `F1 Score`
    - Presented the challenge of balancing both `precision` + `recall`!
  - Future:
    - Focus on fine-tuning both models
    - Improving contextual understanding -> aligning with the ground truth across scenarios
    - Particularly: `phishing` + `ransomware` scenarios!
    - Simulation framework:
      - Incorporate `Security Orchestration, Automation, and Response (SOAR) systems` -> end-to-end automation of the incident response lifecycle
      - Enhancing utility of AI assistance within SOC's
- How Convincing Is the Evidence?
  - Strength -> implemented an event-to-guidance workflow + compared generated outputs against reference responses.
  - Limitation -> text similarity does not establish technically correct or safe advice.
  - Limitation -> does not establish whether users produce better response plans with the guidance.
  - My interpretation -> useful design ideas, but SentinelIR needs its own assessment of response-plan appropriateness + completeness.

## 4. Implications for SentinelIR

### RQ1 — Literature and Design Justification

- Help in terms of the approach, measures used to gauge the LLM's, generate the potential idea of creating and using a LLM for SentinelIR's response plan assistant!

### RQ2 — Detection Using Combined Logs

- Doesn't go into detail around how they were detected, due to using `Wazuh` and just incorporating an assistant on the back of it!

### RQ3 - Investigation and Response Guidance

- Useful to understand some limitations of models, how to go around comparing them, what they found was the best and if I do go through with the LLM idea, then I can use this as either the responding behind which model I go for, or to follow the same approach they took?

## Final Takeaway and Next Action

- One-sentence takeaway: Useful to read, generated an idea, interesting to read up about LLM and work around it. Relevant to guidance design and its evaluation limitations; does not establish improved user response-plan quality.
- Role in my review: Can be comparable if the LLM idea goes through as well as if it doesn't get incorporated, then can be a reference for the future work / next steps for SentinelIR!
- Next action: Leave as reviewed, come back if necessary!
- Matrix updated: `Yes`
- Relevant connection added to synthesis notes: Yes / No / Not yet applicable
