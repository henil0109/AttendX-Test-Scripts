# AttendX-Test-Scripts

## Objective
Demonstrate Git and GitHub version control for the automated test scripts of **AttendX**, a student attendance app, shared by three QA engineers.

> **Important:** The tests **simulate** AttendX behaviour using in-memory fake services. They do **not** connect to any real or production AttendX application.

## Problem this workflow solves
Three QA engineers editing the same test scripts by emailing files or copying folders leads to overwritten work, no history, and no way to see who changed what. Git tracks every change locally as commits, and GitHub acts as the shared remote copy so everyone can push their work and pull the others' changes.

## Repository files
| File | Description |
|---|---|
| `login_test.py` | `unittest` tests for login (valid and invalid credentials) against a simulated login service |
| `attendance_marking_test.py` | `unittest` tests for marking attendance, verifying status, and rejecting duplicates against a simulated service |
| `README.md` | This document |
| `OBSERVATION_LOG.md` | Practical record with actual command outputs |
| `evidence/` | Evidence checklist and screenshots |

## Prerequisites and setup
- Python 3.8+ (no third-party packages needed; only the built-in `unittest`)
- Git
- Clone and enter the repository:
  ```
  git clone <repository-url>
  cd AttendX-Test-Scripts
  ```

## Running the tests
```
python login_test.py -v
python attendance_marking_test.py -v
```

## Expected results
Every test should print `ok` and each script should end with `OK`. Login: valid credentials succeed; wrong password, unknown user (and later, empty credentials) are rejected. Attendance: Present/Absent are recorded correctly; duplicates and invalid statuses are rejected.

## Git workflow
```
git status                      # see changed/untracked files
git add <files>                 # stage changes
git commit -m "message"         # save a snapshot
git push -u origin main         # upload commits to GitHub (-u only the first time)
git pull --ff-only origin main  # download others' commits safely
git log --oneline --decorate    # view history
```

## GitHub repository
URL: _to be added after the remote repository is created_

## Version Control Workflow
Git tracks local changes as commits on the QA engineer's machine, while GitHub stores the shared remote repository that all three engineers push to and pull from.
