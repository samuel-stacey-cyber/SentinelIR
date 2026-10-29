# Ideas

## System-style CLI output

When providing information, errors, logs or progress updates -> make the output feel like a system running!

- `[*]` => Processing / currently running
- `[+]` => Success / completed
- `[i]` => Information / supporting evidence
- `[!]` => Warning / suspicious activity
- `[-]` => Error / failed operation
- `[?]` => User input / confirmation needed

Example:

[*] Reading HTTP access and authentication logs...
[+] Loaded 1,250 log entries.
[*] Checking for repeated authentication failures...
[!] Potential brute-force activity detected.
[i] Evidence: 25 failed login attempts within 60 seconds.
[i] Suggested investigation: Check whether this activity was expected.
[?] View the supporting evidence and response guidance?

Keep the symbols consistent -> include clear wording, so the meaning does not depend on colour alone!
