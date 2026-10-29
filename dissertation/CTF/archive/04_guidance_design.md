# Guidance Design

## Already Established

- Established -> evidence-linked investigation + conditional response suggestions; the user retains control.
- Current preference -> documented templates with limited contextual tailoring.
- An LLM assistant is an optional idea, not an agreed implementation requirement.

## Questions to Answer

### 1. Guidance content

- Needed: `Before CW2 submission`
- Question: What does every guidance item need to contain?
- Options / trade-offs: Short action list / evidence + checks + conditional actions + prevention
- My recommendation: Start with the relevant evidence, uncertainty, verification steps, conditional response and prevention suggestions. Explain why advice applies; suspicious activity must not be presented as confirmed compromise.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 2. Contextual tailoring

- Needed: `Before CW2 submission`
- Question: Which user inputs can change advice, and how will those inputs be controlled in RQ3?
- Options / trade-offs: Fixed scenario context / limited structured context / unrestricted dialogue
- My recommendation: Start with fixed scenario context and only add inputs that materially change recommendations. Both conditions need the same factual context; guidance must not reveal hidden labels or additional evidence.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 3. Implementation choice

- Needed: `Before CW2 submission`
- Question: Will the evaluated feature use templates or an LLM?
- Options / trade-offs: Templates / LLM-assisted generation
- My recommendation: Recommend templates for a reproducible first study. If an LLM is later chosen, revisit output verification, versioning, consistency, data transfer and scope before treating it as part of the experiment.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 4. Advice validation

- Needed: `Before participant research`
- Question: How will recommendations be checked, including false-positive scenarios?
- Options / trade-offs: Technical sources + scenario review / participant suggestions alone
- My recommendation: Check advice against relevant technical sources and lab behaviour, then seek a knowledgeable reviewer if available. Participant prevention suggestions are formative ideas, not proof that actions are correct.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 5. Freeze and presentation

- Needed: `Before participant research`
- Question: When will wording become fixed, and how much guidance will users see?
- Options / trade-offs: Pilot then freeze / revise during evaluation
- My recommendation: Pilot clarity and level of detail, then freeze/version the evaluated templates. Keep the evidence identical and the presentation comparable across conditions. Record later corrections separately and decide whether affected tasks need exclusion before analysis.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

## Evidence or Supervisor Input Needed

[P04](../literature_review/reading_notes/P04_wazuh_response_copilot.md): similarity is not correctness. [P05](../literature_review/reading_notes/P05_decsision_support_threat_incident.md): critical-thinking support. [P07](../literature_review/reading_notes/P07_how_ready_is_your_ready.md): practical detail, clear triggers and communication. These motivate testing, not guaranteed benefit.

## Completion Checklist

- [ ] Choose content, tailoring and implementation approach.
- [ ] Separate formative suggestions from evaluation data.
- [ ] Plan technical review, pilot and frozen version.

## CTF feedback and guidance development — Updated CTF Idea

- Detailed proposal -> [ctf_updated.md](ctf_updated.md).
- Needed: `Before participant research`.
- Question -> When will participant prevention suggestions be collected and how will they inform guidance?
- My recommendation -> Use pilot/development suggestions as inputs for technical review, then freeze guidance before the formal comparison. Keep playful detector feedback out of formal runs unless controlled.
- My decision:
- Why:
- Status:
- Evidence / supervisor input needed -> confirm unresolved choices; the linked plan is a proposal, not approval.
- Completion checklist -> Development and evaluation separated; equivalent alert evidence retained; suggestions checked rather than assumed correct.
