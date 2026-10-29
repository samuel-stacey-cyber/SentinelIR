# CTF and Log Collection

## Already Established

- Established -> SentinelIR should analyse logs in the background while the CTF application runs.
- Implementation inspected -> file monitoring reads appended lines; live processing parses them and triggers detection checks.
- HTTP parsing currently maps some status codes to success/failure -> these are heuristics, not independent proof of authentication outcomes.
- Hosting, required application-log fields and source correlation remain undecided.

## Questions to Answer

### 1. Role of CTF activity

- Needed: `Before CW2 submission`
- Question: Will the primary detection comparison use scripted activity, participant activity or both?
- Options / trade-offs: Scripted matched scenarios / participant-only activity / scripted core plus participant exploration
- My recommendation: Use a repeatable scripted core and participant activity as supplementary evidence. Preserve the live-running goal, then replay the captured records through both detector configurations.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 2. Hosting and containment

- Needed: `Before CW2 submission`
- Question: Where can the application run, and how will participants reach only the authorised target?
- Options / trade-offs: Local isolated VM/container lab / university-managed environment / restricted remote hosting
- My recommendation: Prefer the simplest environment that recruitment can access safely. Document network boundaries, reset procedures, ownership permission and stop conditions; do not assume containerisation alone provides isolation.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 3. Evidence fields and correlation

- Needed: `Before CW2 submission`
- Question: Which fields are necessary, available in each source and permitted to collect?
- Options / trade-offs: Shared request/event identifiers / account + timestamp correlation / IP + time only
- My recommendation: Draft a field map: source, timestamp/timezone, method/path/status, test account code, application outcome and correlation identifier where available. Keep passwords/tokens out. Assess shared IPs and missing identifiers; record ambiguous matches rather than silently joining them.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 4. Live capture and replay checks

- Needed: `During implementation`
- Question: How will startup, buffering, rotation, duplicate lines, malformed records and out-of-order events be handled?
- Options / trade-offs: Controlled files per run / rotation-aware continuous capture
- My recommendation: Start with separate run files + preserved raw copies, timestamps and configuration versions. The existing monitor starts at file end, so explicitly test startup and pre-existing records. Specify how two sources arrive and how late records are reconciled.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

### 5. Pilot readiness

- Needed: `Before participant research`
- Question: How will you verify the full capture path before inviting participants?
- Options / trade-offs: Researcher-generated smoke scenarios / participant pilot after approval
- My recommendation: Verify that each known attempt can be traced through both logs to analysis output. Check an authorised success, a failed login and missing/duplicate records. Participant pilots require the appropriate approval.
- My decision:
- Why:
- Status:
- Evidence / supervisor input to resolve this:

## Evidence or Supervisor Input Needed

[P06](../literature_review/reading_notes/P06_discovering_password_guessing.md) motivates contextual authentication evidence, but does not validate our collection method. See [ethics decisions](07_ethics_and_data_management.md).

## Completion Checklist

- [ ] Choose the role of scripted and participant activity.
- [ ] Document hosting, permissions and fields.
- [ ] Specify how matching, capture and replay will be checked.

## CTF journey and flag service — Updated CTF Idea

- Detailed proposal -> [ctf_updated.md](ctf_updated.md).
- Needed: `Before CW2 submission; technical details during implementation`.
- Question -> Which platform/hosting arrangement, final goal, flag rules and reset method will I use?
- My recommendation -> Use the proposed journey as a starting point. Separate scoring from vulnerable data; prefer per-run instances/tokens, server-side progress checks and separate decoy events.
- My decision:
- Why:
- Status:
- Evidence / supervisor input needed -> confirm unresolved choices; the linked plan is a proposal, not approval.
- Completion checklist -> Core route is finishable; genuine/invalid/duplicate/decoy cases specified; live collection and replay specified.
