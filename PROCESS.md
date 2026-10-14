# How I plan the next work (Scrum-style)

This is the plan for the next sprints of **weld-defect-detection**. It is a planned way of working for a one-person project, not a record of past team work.

## Working agreement
- Sprint: one week. Sprint goal: one backlog item finished, with its numbers in `reports/` and the README.
- Planning on Monday (pick items), review on Friday (open the project page, check the numbers), a short retrospective note in the commit log.
- Board: one GitHub issue per backlog item, columns To do, In progress, Done (GitHub Projects).
- Branches: `main` stays working; each item gets its own branch and a pull request.

## Definition of done
1. The script runs in a fresh virtual environment from `requirements.txt`.
2. Every number in the README and on the page matches `reports/`.
3. The project page opens without console errors and works on a phone.
4. No secrets or personal data in the files or history.
5. Limits are stated next to the result.

## Product backlog
| # | User story | Acceptance |
|---|---|---|
| 1 | As a reviewer, I want the dataset source and licence recorded, so that the project is legally clean. | Source, licence, size in README. |
| 2 | As a reviewer, I want precision and recall per class on a held-out test set, so that the accuracy is measured. | Confusion matrix and per-class metrics in reports/. |
| 3 | As an inspector, I want a confidence threshold chosen from the data, so that defects are not missed. | Threshold picked from the precision-recall curve. |
| 4 | As a reviewer, I want an anomaly-detection comparison, so that missing defect types are covered. | One method (for example PatchCore) compared on the same test set. |
