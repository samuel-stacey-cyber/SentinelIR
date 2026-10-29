# Hosting and logs

[Back to overview](README.md)

## Proposed setup

A small custom portal, with CTFd considered for flag submissions and progress. This is provisional; no CTF code has been written yet.

```text
Participant -> separate challenge instance -> HTTP + authentication logs
                       |                              |
                 flag submission                 CLI SentinelIR
                       |                              |
                separate scoring                saved replay data

Independent scenario/outcome records -> evaluation, not detector input
```

- Separate environment and flags per participant/run.
- Reset restores challenge state, preserves accepted progress and saved research logs, and records the reset.
- Keep scoring, research records and other participants outside the vulnerable environment.
- The shell bonus needs a separate containment assessment before implementation.

## Hosting remains open

I would like students to access the CTF remotely during a defined window. I am considering university hosting, restricted paid hosting or an isolated environment on my equipment, and would value advice.

My desktop has a Ryzen 7 7800X3D, 32 GiB RAM and approximately 2 TB internal storage. This is available for development; it has not been tested for participant hosting.

There are around 60 students in my year. That is a possible invitation pool, not a confirmed participant count or concurrent capacity target. Use queued/on-demand instances with a capacity limit if needed. A monetary hosting budget is not yet set.

## Required evidence

| Source | Required fields |
| --- | --- |
| HTTP access | Timestamp, request ID, method, sanitised path, status, run identifier |
| Authentication | Matching request ID, test-account identifier, event type, actual authentication outcome |
| Separate research records | Scenario outcomes, challenge progress, hints, resets and decoy activity |

No attempted passwords, session tokens or real personal data in detector logs. Keep answer manifests and ground-truth labels out of detector inputs. Record decoy signals separately so they are not mistaken for general detection improvement.

## Checks still needed

Inspect the existing SentinelIR implementation for multi-source capture, authentication parsing, correlation, replay, rotation and restart behaviour. Then test capture accuracy, flag validation, reset, participant isolation and capacity. These are requirements, not claims that the integration already works.
