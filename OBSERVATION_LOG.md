# Observation Log - Version Control of Test Scripts for AttendX

Repository: https://github.com/henil0109/AttendX-Test-Scripts

> The tests simulate AttendX behaviour and do not connect to a real application.

## 1. Aim
To demonstrate Git-based version control and GitHub collaboration for the AttendX (student attendance app) QA automation test scripts shared by three QA engineers: tracking changes, committing, pushing, editing on GitHub, pulling, and reviewing history.

## 2. Software and tools
| Item | Details |
|---|---|
| Operating system | Windows 11 Pro (10.0.26200) |
| Git | git version 2.54.0.windows.1 (Git Credential Manager: manager) |
| Editor / terminal | Visual Studio Code, integrated PowerShell terminal |
| Python | Python 3.14.7 (built-in unittest only) |
| Remote hosting | GitHub (account henil0109), repository AttendX-Test-Scripts |
| Git identity (this repo) | Henil Patel <patelhenil0109@gmail.com> (repo-local config) |

## 3. Procedure
1. Task 1 - Create the local repository AttendX-Test-Scripts in VS Code and run git init.
2. Task 2 - Create login_test.py, attendance_marking_test.py and README.md; run both tests.
3. Task 3 - Check git status, stage the files with git add, and make the first commit.
4. Task 4 - Create an empty GitHub repository, connect it with git remote add origin, and push main.
5. Task 5 - Modify login_test.py (empty-credential validation), test, diff, stage, commit and push.
6. Task 6 - Edit README.md directly on GitHub (Version Control Workflow section) and git pull --ff-only.
7. Task 7 - Display and explain the history with git log.

Concept notes:
- **Working tree:** The project folder on disk where files are edited. Git compares it with the last commit to find changes.
- **Staging:** git add places chosen changes in the staging area, so a commit contains exactly the files you intended.
- **First commit:** The three files: login_test.py, attendance_marking_test.py and README.md (163 lines).
- **Commit message:** 'Add AttendX login and attendance test scripts' says what was added in plain language, which helps teammates scan history.

## 4. Command observation table
| Step | Actual command | Purpose | Actual output/result | Observation |
|---|---|---|---|---|
| 1 | `git --version` | Check Git is installed | git version 2.54.0.windows.1 | Git is installed and available in the terminal. |
| 2 | `git config --global user.name` | Check configured name | Henil Patel | Global name was already set. Config commands print nothing when they only set a value. |
| 3 | `git config --global user.email` | Check configured email | henilp@retailstat.com | Global email is a work address, so a repo-local identity was set (step 4). |
| 4 | `git config --local user.name "Henil Patel"<br>git config --local user.email "patelhenil0109@gmail.com"` | Use the personal GitHub identity for this repo only | (no output - success). Verified with git config --local --get-regexp "^user\.": user.name Henil Patel / user.email patelhenil0109@gmail.com | Commits in this repo are now linked to the GitHub account henil0109. |
| 5 | `python --version` | Check Python | Python 3.14.7 | Python is available. |
| 6 | `git status (in ST folder, before init)` | Check whether a repo exists | fatal: not a git repository (or any of the parent directories): .git | Expected: no repository existed yet. |
| 7 | `git init` | Create the repository | Initialized empty Git repository in C:/Users/HenilPatel/OneDrive - ProductSquads Technolabs LLP/ST/AttendX-Test-Scripts/.git/ | .git folder created; default branch was master. |
| 8 | `python login_test.py -v` | Run login tests | Ran 3 tests in 0.000s - OK (before improvement); after Task 5: Ran 4 tests in 0.001s - OK | All login tests pass. |
| 9 | `python attendance_marking_test.py -v` | Run attendance tests | Ran 5 tests in 0.000s - OK (re-run after Task 5: Ran 5 tests in 0.001s - OK) | All attendance tests pass. |
| 10 | `git status` | See file state before staging | On branch master / No commits yet / Untracked files: README.md, attendance_marking_test.py, login_test.py | Three files are untracked (not yet in Git). |
| 11 | `git add login_test.py attendance_marking_test.py README.md` | Stage the three files | Only LF-to-CRLF line-ending warnings (normal on Windows) | Files moved to the staging area. |
| 12 | `git status` | Confirm staging | Changes to be committed: new file: README.md, attendance_marking_test.py, login_test.py | Files are staged. |
| 13 | `git diff --cached --stat` | Review staged changes | 3 files changed, 163 insertions(+) | Staged content is exactly the three new files. |
| 14 | `git commit -m "Add AttendX login and attendance test scripts"` | First commit | [master (root-commit) 55c8ee5] ... 3 files changed, 163 insertions(+) | First commit created (hash later changed, see step 15). |
| 15 | `git commit --amend --reset-author --no-edit` | Re-author the unpushed first commit with the personal identity | [main 8892f49] Add AttendX login and attendance test scripts | Hash changed from 55c8ee5 to 8892f49 because the author changed. It had not been pushed, so no shared history was rewritten. |
| 16 | `git status` | Confirm clean tree | On branch main / nothing to commit, working tree clean | Working tree is clean. |
| 17 | `git branch -M main` | Rename branch to main | (no output - success) | git branch --show-current printed: main |
| 18 | `git remote add origin https://github.com/henil0109/AttendX-Test-Scripts.git<br>git remote -v` | Connect to GitHub | origin  https://github.com/henil0109/AttendX-Test-Scripts.git (fetch)<br>origin  https://github.com/henil0109/AttendX-Test-Scripts.git (push) | Remote origin points to the real repository. |
| 19 | `git push -u origin main` | First push (run by me in the VS Code terminal; browser sign-in) | Writing objects: 100% (5/5), 2.80 KiB ... To https://github.com/henil0109/AttendX-Test-Scripts.git<br> * [new branch] main -> main<br>branch 'main' set up to track 'origin/main'. | Verified: git ls-remote origin showed refs/heads/main at 8892f4997b3268e7b4dbedf5595f57106becba10. |
| 20 | `git diff` | Review unstaged change to login_test.py | login_test.py: replaced the password check with 'if not username or not password' returning 'Username and password are required'; added test_empty_credentials_are_rejected_with_validation_message (+11 / -1 lines) | Shows exactly what changed before staging. |
| 21 | `git status` | Check modified file | Changes not staged for commit: modified: login_test.py | Modified but not staged. |
| 22 | `git add login_test.py<br>git diff --cached --stat` | Stage and review | login_test.py \| 12 +++++++++++- / 1 file changed, 11 insertions(+), 1 deletion(-) | Only login_test.py is staged. |
| 23 | `git commit -m "Add empty-credential login validation"` | Second commit | [main 078a96e] Add empty-credential login validation / 1 file changed, 11 insertions(+), 1 deletion(-) | Second commit created. |
| 24 | `git push` | Push second commit | 8892f49..078a96e  main -> main | Verified: git status -sb showed ## main...origin/main and ls-remote showed 078a96e. |
| 25 | `(GitHub web) README.md > Edit > add 'Version Control Workflow' > Commit directly to main` | Remote change made on GitHub | Commit 'Document the shared Git workflow' (40c07e4) created on GitHub; see evidence E07 | Remote now has a commit the local repo does not have. |
| 26 | `git pull --ff-only origin main` | Download the GitHub edit safely | 078a96e..40c07e4  main -> origin/main / Updating 078a96e..40c07e4 / Fast-forward / README.md \| 3 +++ / 1 file changed, 3 insertions(+) | Fast-forward pull succeeded; histories had not diverged. |
| 27 | `git status` | Confirm synced | Your branch is up to date with 'origin/main'. nothing to commit, working tree clean | Local equals remote. |
| 28 | `findstr /n /c:"Version Control Workflow" README.md` | Confirm section is in local file | 51:## Version Control Workflow | The GitHub edit is present locally. |
| 29 | `git add README.md<br>git commit -m "Add GitHub repository URL to README"` | Record the real repo URL in the README | [main 00227d9] Add GitHub repository URL to README / 1 file changed, 1 insertion(+), 1 deletion(-) | Extra commit (README required the final URL). Pushed later together with the documentation commit. |
| 30 | `git log --oneline --decorate` | Show history | 40c07e4 (HEAD -> main, origin/main) Document the shared Git workflow<br>078a96e Add empty-credential login validation<br>8892f49 Add AttendX login and attendance test scripts<br>(captured before the URL commit 00227d9; see section 5 for final history) | Three practical commits visible, HEAD and origin/main aligned. |
| 31 | `git log --oneline --graph --all` | Show history graph | * 40c07e4 Document the shared Git workflow<br>* 078a96e Add empty-credential login validation<br>* 8892f49 Add AttendX login and attendance test scripts | Straight line, no branches or merge commits. |
| 32 | `git show --stat --oneline HEAD` | Inspect latest commit (at that time) | 40c07e4 Document the shared Git workflow / README.md \| 3 +++ / 1 file changed, 3 insertions(+) | The remote commit changed only README.md. |

Final history is shown by `git log --oneline --decorate` after the last commit and push (see the Word report / terminal).

## 5. Commit history
| Hash | Message | Author | Files | Explanation |
|---|---|---|---|---|
| 8892f49 | Add AttendX login and attendance test scripts | Henil Patel <patelhenil0109@gmail.com> | login_test.py, attendance_marking_test.py, README.md (new, 163 lines) | Initial commit with both test scripts and the README. Originally 55c8ee5 before re-authoring. |
| 078a96e | Add empty-credential login validation | Henil Patel <patelhenil0109@gmail.com> | login_test.py (+11, -1) | Added input validation and a test for empty/None credentials. |
| 40c07e4 | Document the shared Git workflow | HENIL (GitHub web, noreply address) | README.md (+3) | Made on GitHub using the Edit button, then pulled locally. |
| 00227d9 | Add GitHub repository URL to README | Henil Patel <patelhenil0109@gmail.com> | README.md (+1, -1) | Replaced the URL placeholder with the real repository URL. |
| (see git log) | Add observation log, evidence index and report | Henil Patel <patelhenil0109@gmail.com> | OBSERVATION_LOG.md, evidence/  | Practical record files. Its hash is shown by git log (it cannot name itself). |

## 6. Observations and conclusion
Git tracks every change to the test scripts as a snapshot (commit) made in three steps: edit in the working tree, stage with git add, then commit. Each commit keeps an author, message and hash, so the full history can be reviewed. GitHub holds the shared remote copy: git push uploads local commits, and an edit made on the GitHub website creates a commit that exists only on the remote. git pull --ff-only brought that commit into the local copy without creating merge commits and refused to proceed if histories had diverged, which keeps the three QA engineers synchronised safely. Note: the tests use simulated services and do not connect to a real or production AttendX application.

## 7. Deliverable checklist
- [x] GitHub repository link - https://github.com/henil0109/AttendX-Test-Scripts
- [x] Login automation test - login_test.py (4 tests pass)
- [x] Attendance-marking automation test - attendance_marking_test.py (5 tests pass)
- [x] README - README.md
- [x] Initial commit and subsequent commit - 8892f49 and 078a96e
- [x] Successful push - Both pushes verified with git ls-remote
- [x] Direct GitHub edit and successful pull - 40c07e4 pulled with fast-forward
- [x] Commit history - git log output in section 4/5
- [ ] Evidence screenshots - Only files that exist in evidence/ are listed below
- [x] Observation log - OBSERVATION_LOG.md

## 8. Evidence index
| ID | File | Shows | Status |
|---|---|---|---|
| E01 | `evidence/E01_git_setup.png` | Git version and identity (git --version, git config) | NOT YET CAPTURED |
| E02 | `evidence/E02_project_files.png` | VS Code Explorer showing AttendX-Test-Scripts files | NOT YET CAPTURED |
| E03 | `evidence/E03_initial_status.png` | Initial git status with untracked files | NOT YET CAPTURED |
| E04 | `evidence/E04_first_commit.png` | git add, git status, git commit output | NOT YET CAPTURED |
| E05 | `evidence/E05_github_push.png` | Push output and GitHub page showing the three files | NOT YET CAPTURED |
| E06 | `evidence/E06_second_commit_push.png` | Second commit and push output | NOT YET CAPTURED |
| E07 | `evidence/E07_github_readme_edit.png` | README on GitHub showing the added Version Control Workflow section | Captured |
| E08 | `evidence/E08_git_pull.png` | git pull --ff-only output | NOT YET CAPTURED |
| E09 | `evidence/E09_git_log.png` | git log --oneline --decorate | NOT YET CAPTURED |
| E10 | `evidence/E10_test_results.png` | Both test scripts passing | NOT YET CAPTURED |
