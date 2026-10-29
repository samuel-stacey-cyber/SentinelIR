# Scope and Contribution

## Already Established

- Established -> CLI-only SentinelIR, a separate authorised CTF-style application + the three current research questions.
- RQ1 = literature and design justification; RQ2 = detection using combined logs; RQ3 = response-plan quality with/without guidance.
- Established -> equivalent evidence for RQ3; automated response execution and a SentinelIR web UI are outside scope.
- Current preference -> repeated authentication failures + suspicious success; exact scenarios remain open.
- Earlier context: [open decisions](../research_question/open-decisions.md). This folder develops those choices; it does not silently replace earlier answers.
- Current wording: [research questions](../research_question/final_question.md).

Work in numbered order, but check ethics dependencies in file 07 early. Recommendations are suggestions, not your agreed decisions. Use `Open`, `Proposed`, `Decided` or `Needs supervisor input` in the blank status fields.

## Questions to Answer

### 1. Attack scope

- Thoughts:
  - So what I was thinking is
  - To create a vulnerable website (not sure how, whether through a service or making it myself)
  - Then potentially include the following exploits:
    - Brute-force:
      - Have a login page
      - Using a very easily guessable password
      - Which is within a standard brute-force password list like `10-million`
      - Then I want to be able to detect that the attack is then trying to exploit it!
      - Or either hide a password somewhere within a comment, but its incorrect and will let me know that someone
      - Is trying to use a password that (`honey-pot`)
      - Then after detecting whether they brute-forced the password or they used the `honey-pot` login
      - Then detecting once that IP address successfully logged in!
      - Could also potentially add a rate limit, with either:
        - Threshold set as a comment within the code
        - Or a comment for what limit is only acceptable!
    - SQL Injection:
      - So this could be another way of cracking this weak login
      - Allowing the user to be able to inject code into the login system
      - Giving the user a basic database if they do it correctly
      - Giving them both the `honey-pot` login (meaning that I can easily detect that they've used it!)
        - Potentially linking it back to their IP address if they have visited a specific page where
        - The commented `honey-pot` credentials are hidden
      - Then also if they try to use SQL injection in the incorrect format, then there is error handling
      - Letting them know that I know they are trying to use SQL injection :)
      - Database file however cannot be found through `SQLmap`!
        - Meaning that they actually have to manually use SQL injection
        - Rather than just running `SQLmap` in order to find
        - The database file!
      - Would like the database file somewhere which is basically impossible to find
      - But if you download it, it instead opens the following link :)
        - Using some funny trolling video :)
    - Path traversal:
      - I could add in one of the pages
      - A way to exploit path traversal
      - Which could be the only way to find the SQL database file
      - But you won't be able to download it!
      - They will only be able to view it by some way, not sure
    - Account forgery:
      - I could allow the user to be able to create an account
      - But within the code behind it (commented)
      - There are instructions (maybe in a different language)
      - On how they are able to create the account
      - Then I can then detect that they have created a new account
        - Plus log when there is a failed account creation (didn't follow the instructions!)
      - Then there is a file upload vulnerability for the profile picture they can add
      - I could also add in a vulnerability
        - Where when you log into your account
        - Using `Burp Suite`
        - You can capture that requests
        - Then change some parameters
        - To then use to be able to access the one of the valid account on the system
        - But not the `honey-pot` one!
    - File upload:
      - Once the user has created an account
      - They can upload a profile picture
      - Which is where they can do something not sure!
    - XSS:
    - Account escalation:
      - Once the user has found the database and is able to view it
      - I will have 3 different accounts:
        - `Honey-pot`
        - Account with admin controls
        - Account without admin controls
      - Then the user can use `Burp Suite` to be able to change the role
      - Of the `non-admin` account
      - Just by changing a `randomly-name` generated parameter
  - Basically I just want to mess with the attacker :)

### 2. Contribution

- Question: What useful knowledge will the study produce even if neither condition improves results?
- Options / trade-offs: Controlled comparison + design lessons / a new detection algorithm / a production deployment claim
- My recommendation: Position the contribution as controlled comparisons and evidence-based design lessons. Do not claim a novel algorithm or operational effectiveness unless the work demonstrates it.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 3. Success criteria

- Needed: `Before CW2 submission`
- Question: What deliverables establish project completion, separately from positive results?
- Options / trade-offs: Reproducible evaluation + explicit limitations / fixed improvement target
- My recommendation: Use documented comparisons, traceable labels, usable guidance and honest results. A null or negative result can still answer the questions.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 4. Scope changes and fallback

- Needed: `Before CW2 submission`
- Question: What happens if recruitment or implementation is not feasible?
- Options / trade-offs: Reduce scenarios while keeping comparisons / discuss a revised RQ3 with Kabiru
- My recommendation: Keep the core comparisons first. Technical guidance assessment can supplement RQ3 but cannot replace human evidence while retaining a claim about users’ plan quality.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

## Evidence or Supervisor Input Needed

[Synthesis](../literature_review/synthesis.md) + [working question](../research_question/work-question.md). Confirm any change to the authorised question with Kabiru.

## Completion Checklist

- [ ] Record core and excluded behaviours.
- [ ] State the contribution without assuming improvement.
- [ ] Define completion criteria + a supervisor-dependent fallback.

## CTF scope and contribution — Updated CTF Idea

- Detailed proposal -> [ctf_updated.md](ctf_updated.md).
- Needed: `Before CW2 submission`.
- Question -> Which authentication challenges form the core, and which optional challenges are genuinely needed?
- My recommendation -> Keep the existing RQs. Build the complete authentication route first; treat SQLi, traversal, IDOR and other additions as supplementary unless a scope change is agreed.
- My decision:
- Why:
- Status:
- Evidence / supervisor input needed -> confirm unresolved choices; the linked plan is a proposal, not approval.
- Completion checklist -> Core scenarios selected; optional exclusions recorded; each selected challenge has a research purpose.
