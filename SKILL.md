# Repository Skill / Agent Instructions

Purpose
- Provide concise guidance for an AI coding agent working on this repository: editing code, adding small features, and running quick verification commands.

How to request changes
- State the goal and the target file(s) or directory.
- Include expected behavior and a short example of input → output when possible.
- Provide any constraints (Python version, style, tests to run).

What to include for reproducible edits
- Target path(s) (e.g., `python-basics/`, `MITx6001x/`).
- Sample input and expected output or test name to validate.
- Any files that must NOT be modified (configs, secrets).

Files / locations of interest
- [python-basics](python-basics)
- [MITx6001x](MITx6001x)
- [google-python-exercises](google-python-exercises)
- [CBT](CBT)

Typical agent capabilities
- Create, edit, and delete repository files.
- Run simple Python scripts or test commands and report output.
- Add small helper scripts, README updates, and lightweight tests.

Safety and secrets
- Never embed secrets (API keys, passwords, credentials) in prompts.
- If a change requires secrets, provide sanitized test credentials or run the step locally.

Testing and verification
- To run a script: `python path/to/script.py` using your Python 3.13+ environment.
- If a change includes tests, provide the test command or a small test script.

Commit / merge policy
- The agent can prepare changes and show diffs; commit only after explicit user approval.

If you'd like, ask the agent now to make a specific change and include the target file(s) and expected behavior.
