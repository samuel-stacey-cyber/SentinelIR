# Challenge route

[Back to overview](README.md)

## Core -> two accounts, three flags

1. Find a test username in page source or a help page, then discover a disguised practice wordlist. Use bounded password guessing to access the first, low-privilege account -> **Flag 1**.
2. Follow clues to a file-reading feature. Path traversal reveals a seeded backup containing the second account's test credentials. Log into that account -> **Flag 2**.
3. Read its internal audit report. Identify the account linked to a suspicious change using the report's evidence table. A correct answer reveals **Flag 3**.

All three core flags complete the CTF. The second account contains the report; no third login is needed.

## Optional bonuses

| Branch | Proposed task | Reward |
| --- | --- | --- |
| Upload | Exploit an upload flaw to obtain a shell inside an isolated challenge environment | Independent bonus flag |
| Website administrator | Find the correct profile image, upload it to reveal a clue, then exploit an improperly trusted role parameter | Independent bonus flag |

The image is a clue mechanism; uploading the correct image is not itself a vulnerability. Website administrator does not mean operating-system root. Neither bonus is required to finish the core.

Exact upload mechanics, clue text and bonus prerequisites still need technical review. Bonus access must not expose scoring secrets or every core answer.

## Decoys and help

- Start with one decoy credential file and one decoy flag.
- Decoy credentials never authenticate successfully; record attempted use.
- Trying a planted password across several accounts is separate from a single decoy-use event.
- Invalid/decoy submissions -> neutral rejection. Duplicate flags -> no extra credit.
- Two or three progressively clearer hints per challenge -> record use, no points penalty.
- Optional beginner guide available to everyone, plus an unscored practice submission.
- Participants see CTF feedback, not live SentinelIR detections.

Manual/browser methods and tools such as Burp are allowed within the target boundaries. Login automation uses the bounded practice wordlist. Exact request limits and scanner permissions remain open.
