# Detection Evaluation

## Already Established

- Established -> compare HTTP access logs alone against access + authentication logs for the same activity.
- Primary measures -> precision + recall; false alerts and missed detections must remain visible.
- Existing detection code has configurable thresholds/time windows and alert-state handling. Defaults are not automatically justified research settings.

## Questions to Answer

### 1. Scenario coverage

- Needed: `Before CW2 submission`
- Question: Which malicious and benign cases are essential, and what outcome is expected?
- Options / trade-offs: Only obvious attacks / balanced core with benign lookalikes + slow cases
- My recommendation: Include repeated guessing, known attacker success after guessing, ordinary password mistakes and legitimate success after failures. Add slower activity as a challenge case. Record account, actor, timing and independently known outcome for every scenario.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 2. Ground truth

- Needed: `Before CW2 submission`
- Question: Who or what records the actual activity independently of the detector?
- Options / trade-offs: Script/run manifest + verified application state / access status codes / participant recollection
- My recommendation: Use a separate scenario manifest and confirmation of the executed outcome. Participant recollection is supplementary. An HTTP 200/302 or successful authentication alone does not establish malicious compromise.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 3. Evaluation unit and alert matching

- Needed: `Before CW2 submission`
- Question: What is one positive/negative case, and when does an alert count as a match?
- Options / trade-offs: Predefined interaction episode / individual request / whole scenario run
- My recommendation: Start with predefined episodes carrying actor/account/time bounds. Define attack-class matching, timing tolerance and how duplicate alerts are handled before scoring. Separate brute-force recognition from compromise claims; do not count correlated events as independent replications.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 4. Fair comparison and tuning

- Needed: `Before CW2 submission`
- Question: What changes between configurations, what remains fixed and when are settings frozen?
- Options / trade-offs: Same detector logic with added evidence / separately tuned configurations
- My recommendation: Prefer matched logic/settings where feasible so the input evidence is the main change. Explain any unavoidable logic differences. Tune on separate pilot scenarios, reset detector state between runs and freeze settings before final evaluation.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 5. Measures and uncertainty

- Needed: `Before CW2 submission`
- Question: How will you aggregate results and handle undefined measures?
- Options / trade-offs: Per-scenario counts plus aggregate metrics / one headline accuracy figure
- My recommendation: Report TP, FP and FN with precision=TP/(TP+FP) and recall=TP/(TP+FN). Mark zero-denominator results undefined, not 100%. Report case mix, repeated runs and variability; use uncertainty estimates appropriate to independent units, without assuming synthetic repetition represents a population.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 6. Missing data and failed runs

- Needed: `During implementation`
- Question: When is a run invalid, and will it be repeated or retained as a failure?
- Options / trade-offs: Predefined exclusion/repeat rules / decisions after seeing results
- My recommendation: Record collection failures, missing records and reruns explicitly. Distinguish a capture failure from a detector miss; do not discard difficult cases merely because detection is poor.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

## Evidence or Supervisor Input Needed

[P02](../literature_review/reading_notes/P02_brute_force_web_app_investigation.md), [P03](../literature_review/reading_notes/P03_detection_apache_http_logs.md) + [P06](../literature_review/reading_notes/P06_discovering_password_guessing.md) support attention to lookalikes, missed activity and uncertain labels; none answers our combined-log comparison.

## Completion Checklist

- [ ] Define scenarios, labels and evaluation unit.
- [ ] Fix matching, tuning and exclusion rules.
- [ ] Specify metrics and fair comparison conditions.

## Decoys, flags and independent evidence — Updated CTF Idea

- Detailed proposal -> [ctf_updated.md](ctf_updated.md).
- Needed: `Before CW2 submission; verify during implementation`.
- Question -> How will I label attacks without using flag submissions or detector-visible challenge answers as ground truth?
- My recommendation -> Use independent scenario records and application-state checks. Declare decoy telemetry separately; compare identical activity and avoid treating an IP as a participant identity.
- My decision:
- Why:
- Status:
- Evidence / supervisor input needed -> confirm unresolved choices; the linked plan is a proposal, not approval.
- Completion checklist -> No answer-label leakage; benign and slow activity included; decoy evaluation and uncertain cases defined.
