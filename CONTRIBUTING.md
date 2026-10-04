# Contributing (workshop labs)

This repository is a **training sandbox**. Use it to practice GitHub Copilot safely.

## Ground rules
- **Synthetic data only.** Never commit customer data, secrets, or production logs.
- **Work on a branch.** Create a disposable branch for every lab exercise.
- **Keep changes small.** One focused change per pull request so it is easy to review.
- **Add a test.** Every behavior change should come with a pytest test.

## Typical lab flow
1. Create a branch: `git checkout -b lab/<your-name>`
2. Make a small change (or let Copilot make it).
3. Run the tests: `pytest`
4. Open a pull request and request a **Copilot code review**.
5. Discard or merge the branch when the lab is done.
