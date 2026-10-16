# P05 - Developing decision support for cybersecurity threat and incident managers

## Reference and Reading Status

- Authors: `van der Kleij, Rick`, `Schraagen, Jan Maarten`, `Cadet, Beatrice`, `Young, Heather`
- Year: 2022
- Venue:
- Source type: `Journal article`
- DOI / link: `10.1016/j.cose.2021.102535`
- Reading status: To screen / Abstract screened / Partially read / Read sufficiently for review
- Sections read:
- Date notes last updated:

## Discovery

- Search date: 14/10/2026
- Search platform / discovery method: `Mendeley literature search` -> downloaded from `Locate`
- Exact search terms, if applicable: `incident response decision support user study`
- Search log entry: 005

## Initial Screening — Is It Worth Reviewing?

Complete this before committing to a detailed read.

- Which part of SentinelIR does it relate to?
  - RQ1 — Literature and design justification     Relevance /10? 7
    - Useful to understand the impact of usability of a new tool / any tool really
    - The problems with having to learn it, being able to replicate what you already know -> under time pressure specifically!
    - Therefore, SentinelIR needs simple, easy to use, and just streamlined!
    - Easy to remember -> hint where applicable!
  - RQ2 — Detection using combined logs           Relevance /10? 0
    - Not linked in terms of the detection / log analysis
    - Focused on the actions that people within SOC need support with!
  - RQ3 — Investigation and response guidance     Relevance /10? 9
    - Super useful to understand the process people have to take
    - Stages of gathering information -> using different approaches -> developing on them / what was discovered!

---

## 1. What Problem Does It Address?

- Research question or aim:
  - Abstract: Main aim is to develop decision support for cyber threats + incident management within the `financial sector`
  - Introduction:
    - Gauge whether decision support can improve performance + accuracy + initiate actions?
    - Aiming to speed up threat incident management
    - By providing relevant `cues` + `triggers` -> reducing flaws + mistakes!
  - Method:
    - Explore the `structural problems` + `dilemmas` SOC's face!
- Claimed limitation in previous work:
  - Introduction:
    - Previous work focuses on `decomposing` the job of cybersecurity experts
    - Broken up into `key task stages`
    - Role of `formal` + `informal` education -> `job performance`
    - Use of `Applied Cognitive Task Analysis` -> investigation into processes used by cyber professionals
  - Decision support in incident response:
    - Management decisions -> `limited` + sometimes `biased`
    - Create something to minimize / streamline the process!
    - Limitations of current decision support:
      - Linear
      - Procedural
      - Consume too many mental resources
      - Not tailored to unexpected + different cyberattacks
  - Method:
    - No combination of both a CTA and CWA
    - Lacks the goal of developing decision support for cybersecurity professionals -> without just adding a new system into the mix!
  - Discussion:
    - Focus solely on one organisation -> they did three!
- Main contribution, in my own words:
- Relevant page / section:

## 2. How Did They Investigate It?

- Study approach:
  - Abstract, interview:
    - Conducted a `two round` `indepth` (remote) interview with 10 `professionals`
    - From 3 institutions
  - Introduction:
    - Use of `Cognitive task analysis (CTA)`
    - Some element of `Cognitive work analysis (CWA)` is also used
    - Conducted 2 rounds of `in-depth` interviews with 10 experienced `CTIMs` from 3 different SOC's
    - Conducted workshops with SOC professionals
    - Results:
      - `CTA` + `CWA`
  - Decision support in incident response:
    - Merge both `CTA` + `CWA` together!
  - Method:
    - Used a `qualitative` research approach
    - Aiming at exploring the structural problems and dilemmas SOC's face!
    - From 10/4/2020 -> 2/9/2020 -> 10 participants
    - From three large financial institutions in the Netherlands
      - Organisation 1 & 2 provided 3 professionals each
      - Organisation 3 provided 4
      - All participants hold different skill sets + `tiers`
    - First round -> all 10
      - `Cognitive Task Analysis (CTA)`
      - Used to identify the main difficulties for SOC's
      - Main research question of the CTA: `What are the structural problems and dilemmas SOC's face when resolving threats and incidents?`
      - Following the `Applied Cognitive Task Analysis (ACTA) approach`
      - Consisting of three activities:
        - Task diagram
          - Asked to break down their work into three / six subtasks
          - Then to select the most cognitively demanding subtask -> used within the knowledge audit (next activity)
        - Knowledge audit
          - Used to provide details + examples of cognitive elements of expertise
          - Nailed down on the identified subtask
          - By asking eight `probe` questions
          - Identifying which `cues` + `strategies` they relied on + how it could be more difficult for a less experience person
        - Simulation interview
          - Asked to describe a particular threat / incident they had experienced
            1. List the major events that occurred
            2. Indicate the actions they would take
            3. Assessment of the situation
            4. Critical cues that led to this situation assessment + actions
            5. Potential errors an inexperienced person would make in this situation
        - Conducted a `thematic analysis` to categorise common cognitive difficulties
        - Text was then coded based on recurring words:
          - Confidence
          - Time
          - Critical thinking
        - These keywords were then used to create definitions for each category
        - Each interviewee's statements were then categorised
        - Finally modularised further into themes
        - Next the cognitive difficulties identified were presented to stakeholders -> who then prioritised them!
        - Finally, these were then chosen for further analysis using a CWA
    - Second round -> 2 from each organisation (6 total)
      - `CWA` -> tasked to broaden the scope of the general work domain
        - Finding out leverage points for their decision support
        - Being able to describe more `formally` the threat and incident decision-making process
        - Mostly bound by the highly influential approach
      - Used to explore requirements for a decision support system
      - CWA was tailored to their education + experience
      - Used a `work domain analysis`
      - Plus a CTA using the decision ladder as a representation
      - CWA process:
        1. Abstraction hierarchy:
           - Provides a representation of the functional structure of a given domain
           - Composed of:
             - Purposes
             - Values
             - Priorities
             - Purpose-related functions
             - Object-related processes
             - Physical objects
           - Used to provide constraints that everyone in a domain has to satisfy
        2. Work domain model:
           - They chose: `tabular abstraction hierarchy`
           - Showing levels of `abstraction of the constraints`
        3. Controlled task analysis:
           - Broken up into three stages:
             - Situation assessment
             - Options analysis
             - Planning
           - Limitation: Doesn't focus on how / who will carry out these activities
           - Yet important as: It is useful to shape the way in which decision support is done!
      - First version of, was created and refined through the two rounds of interviews:
        - Abstraction hierarchy
        - Decision ladder
      - Results of the CTA (workshop):
        - 1st Workshop:
          - Presented to the second-round interviewees
          - Used to receive feedback on `findings`
          - Plus discover which elements either need:
            - Further investigation
            - Solution concept
        - 2nd Workshop:
          - Consisted of `six` participates -> 2 from each organisation
          - Then split into two teams -> using the dialectical inquiry approach
          - Each team was tasked with:
            - Pitch + defend two out of four solutions
            - Prepare arguments for the other two not selected
          - Finally tasked with distributing `100 points` among the four solutions
          - Results were then used to distinguish which solution moved forward
          - Used to critically review the decision-support solutions
          - Plus understand integration requirements
        - Ideation session:
          - Invited colleagues from their organisation
          - Expertise in either `product design` + `cybersecurity`
          - Goal: What support could look like?
          - Resulted in `four concepts`:
            1. Critical thinking tool
              - Require someone to evaluate each piece of evidence in a tool
              - Deciding whether a piece of evidence correlates to either supporting or not supporting an initial hypothesis
              - For that specific stage of incident resolution
              - Providing analysts with an overview of the evidence both for and against the hypothesis
              - Ultimately helping lessen `confirmation biases`
            2. Micro-learnings
               - Can be a small reminder that `pops up` during low-workload periods
               - Being a more effective learning process
               - But will require `context-sensitivity` + `personalisation`
               - Alternative option: `scenario-based training`
                 - Focusing on particular learning objectives
                 - Critical events
                 - With collectable objective performance measurements
                 - Providing the user with feedback afterwards
            3. Improvements (redesign) to existing IR management procedures
               - Currently built around a focus from an engineer's `point of view` -> unpractical
               - Don't cover every `imaginable` instance
               - Current playbooks don't cover everything -> focused on compliance rather than a user's perspective
               - Meaning `end users` should be involved in the development of procedures!
            4. New SOC team member role
               - Someone who is not directly involved in the actual process
               - But is able to keep an overview of what everyone is doing!
               - Knowing what information is needed by everyone else
               - How the process is going (timewise)
               - Therefore `competencies` need to be defined!
            - Results: Throughout the stages of an IR team, they would benefit from either a tool or framework that will allow them to think:
              - Fast
              - Correctly
              - Evaluation of evidence
        - 100-points distribution exercise:
          - Results: Points distribution
            - Critical thinking tool: 55
            - Micro-learning: 115
            - Redesign of IR management process: 440
            - New role: 90
          - Resulting in the decision that:
            - Support should tackle the problem of considering the bigger picture and detail
            - Within a decision-making process
            - In order to improve the current IR management process!
            - As well as that critical-thinking should be integrated into incident managing procedures! Like:
              - CIP: Policies + procedures for incident managers to respond with
              - Playbooks
              - In the form of a `checklist`
      - Functional requirements from results of the workshops:
        1. Support should not be in the `form of another tool`, due to:
          - The abundance of tools already available
          - Resulting in higher workload -> less time available for actual cyber defence operations
          - Don't need something else when they are already under `time pressure`
          - Affects of having to learn + use it -> needs to `provide additional value`!!!
        2. Help `reactivate` existing knowledge structures
          - SOC's constantly learn -> adding to their `knowledge base`
          - Difficulty: Being able to activate that knowledge at the `right time`
        3. Enhancing the use of critical thinking skills in the process
        4. `TIME PRESSURE`!!!
           - Due to solutions needing to be implemented quickly without also adding to workload
    - All interviews took around 2 hours to complete
  - Results:
    - Discussion:
      - Using the list of ten cognitive difficulties
      - A group discussion was conducted
      - Involving a manager + member of the SOC -> from each institution
      - Participants then order the provided list
    - CWA:
      - Goal: Identify the functional requirements of a support system to aid SOC's in the triage process of threats + incidents
      - While taking both the `big picture` + details into account
      - Developed into:
        - Abstraction Hierarchy:
        - Controlled task analysis using a decision Ladder:
          - Six participants were presented a list of purposed-functions
          - In terms of `processes` + `knowledge states` -> within the decision
  - Critical thinking memory aid:
    - Seven process steps: Provide a high-level overview of IR management processes
      1. Observe -> incident is observed
      2. Triage -> identify the incident
      3. Investigate -> determine severity + urgency
      4. Contain -> prevent for further damage being caused
      5. Remediate -> treatment of a security breach
      6. Check -> evaluate the effectiveness of measures taken
      7. Post-incident evaluate -> reflect on the incident handling -> add lessons learnt into the playbook!
      - Follow the current NIST framework!
    - Purpose:
      - Support SOC's to be able to:
        - Balance the bigger picture
        - While `keeping the task at hand`
        - Using a `critical mindset`
        - Without just jumping to the conclusion
    - Critical for larger organisations! -> as synchronisation of activities becomes more difficult!
    - Being able to document the process in detail + communication of the current status (stakeholders)
    - Physical + digital format!
- Setting: `Interviews`
- Sample size and unit of analysis:
  - Interview: `10 people` + `3 locations`
  - 2 rounds: first all `10` then just `2` from each location
- Baseline / comparison conditions:
- Ground truth or assessment criteria:
  - Didn't focus on the following, due to time constraints:   (Limitations)
    - Strategy analysis
    - Social organisation
    - Cooperation analysis
    - Worker competencies analysis
    - All due to this study focusing on decision support rather than allocation
- Evaluation measures:
- Relevant page / section:

## 3. What Did They Find?

### Finding 1

- Main finding, in my own words:
  - Abstract: Development of a `critical-thinking memory aid`
  - Results:
    - Originally followed a six-phased thematic analysis approach -> split into `six codes` -> following `Braun and Clarke (2012)`
    - Results shifted it into `four themes` instead:
      1. Building up relevant experience and knowledge
         - Relates to the general knowledge and skills in the field of IT
         - Examples:
           - Threat landscape
           - Organisational + business matters
         - Feedback from interviewees:
           - Be driven by curiosity
           - Develop a network both inside + outside the company!
      2. Stakeholder communications
         - Refers to communication activities with external parties
         - Examples:
           - Threat intelligence networks
           - Outsourced service providers
           - Third parties
           - Internal stakeholders, ranging from: technical people + business / strategic actors
           - Team members to `get` + `deliver` information
         - Feedback from interviewees:
           - Building trusted connections across organisations!
         - Difficulties:
           - Having to deal with diverse backgrounds + use of different professional language
           - Answering unclear requests from stakeholders -> unable to identify the specific information needed!
      3. Analysis
         - Involves `paradoxical problems` -> feedback from the interviewees:
         1. Reliance on both facts + following strict application of processes
         2. While trying to:
            - Keep the big picture / broader context in mind
            - Thinking outside the box
            - Being critical of the information + verification of the decision made
         3. Juggling the idea of:
            - Future limitations
            - Needs + series of events
            - While discouraging use the of assumptions
         4. Being able to make comparisons + correlating them at the same time -> across different alerts and events!
      4. External stressors
        - Taking into account the effects of:
          - Environmental conditions
          - External stimulus
        - That will play affect on the quality of work
        - Types of stressors:
          1. Time pressure:
             - Caused by either `other people` / `the organisation`
             - Related to the impact an event has, for example:
               - Availability of the services -> `customers` + `internal parties`
               - Financial loss
          2. Limitations / failures of tools used
             - Requiring analysts to have a critical mindset at all times!
          3. Factors involved when trying to resolve an incident:
             - Amount of information
             - Systems involved
             - People needing to be considered
             - Resulting in processes being `cognitive heavy`
    - List of ten cognitive difficulties:
      - Results from the discussion: Being able to balance both the `bigger picture` with details
  - Discussion:
    - Three functional requirements of decision support:
      - Ability to `reactive` knowledge structures that they already know
      - Enhancement of critical thinking throughout processes
      - Tools need to be quickly implementable without adding extra workload!
      - Resulting in a critical thinking memory aid being created
        - Following cybersecurity IR processes
        - Adding bigger picture elements
        - With critical thinking steps
        - Broadening impacts of threats and incidents!
- Limitations?
  - Results:
    - Results: Ten cognitive difficulties were discovered from the thematic analysis:
      1. Application of applying knowledge to specific threats + incidents, linked to organisational processes
      2. Need to centralise information
      3. Being able to gauge how much information is truly needed
      4. Importance of communication with stakeholders + external parties
      5. Taking both details + the bigger picture into account at once
      6. Being able to perform procedures while keeping a critical mindset
      7. Being able to juggle lots of assets at once -> both people + machines
      8. Ability to be able to deal with `residual risk`
      9. Being able to compare situations when there is little expertise
      10. Being faced with new threats + incidents
  - Discussion:
    - Didn't carry out a summative evaluation
    - Focusing on the outcome or overall quality of the tool!
    - Evaluation (next steps): -> in the real-world!
      - Effectiveness?
      - Efficiency?
      - Usability?
    - Leading question: `Is a new role needed within a SOC?`
- Authors’ interpretation:
  - Memory aid:
    - `Promising way to address the problem of balancing the bigger picture with details`
- My interpretation:
  - Final Result: The biggest cognitive difficult within a SOC is:
    - Juggling the `bigger picture` + `details` while being under (time) pressure + involving multiple parties (departments / employees / waiting on others) at once
    - The need for something different to a playbook, described as:
      - Proceduralised
      - Rule-based
    - Need for something simple like a:
      - Decision table
      - Or workflow
      - All being able to fit every situation in `just a few words`

## Final Takeaway and Next Action

- One-sentence takeaway: Very useful paper to read, understand the process they took, things they keep in mind, the results of different approaches, how they then developed it even further / pulled over the results into a different/the next approach. Will be a good reference, didn't link completely to all research questions, but was focused and chosen to focus solely on RQ3, as previous literature reviews were very limited!
- Role in my review:
- Next action:
- Matrix updated: `Yes` / `No`
- Relevant connection added to synthesis notes: Yes / No / Not yet applicable
