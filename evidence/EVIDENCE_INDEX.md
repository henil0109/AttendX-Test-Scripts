# Evidence Index

Only screenshots that really exist in this folder count as captured. Do not include passwords or tokens in any screenshot (the browser sign-in page should not be captured).

| ID | Filename | What the screenshot must show | How to capture |
|---|---|---|---|
| E01 | E01_git_setup.png | Git version and identity | VS Code terminal: `git --version`, `git config --global user.name`, `git config --global user.email`, `git config --local --get-regexp "^user\."` |
| E02 | E02_project_files.png | Project files in VS Code | VS Code Explorer with AttendX-Test-Scripts expanded |
| E03 | E03_initial_status.png | Untracked files | Not reproducible now; take it in a throwaway copy or use terminal output from the transcript (see note) |
| E04 | E04_first_commit.png | Staging and first commit | Same note as E03 |
| E05 | E05_github_push.png | GitHub page showing the three files | Browser: repository page (files list) |
| E06 | E06_second_commit_push.png | Second commit and push | GitHub commits page showing "Add empty-credential login validation", or terminal `git log --oneline --decorate` |
| E07 | E07_github_readme_edit.png | README with the new section on GitHub | **Captured** |
| E08 | E08_git_pull.png | `git pull --ff-only origin main` | Not reproducible (already up to date); screenshot the GitHub commits page instead, or note it |
| E09 | E09_git_log.png | `git log --oneline --decorate` | VS Code terminal: run the command, screenshot |
| E10 | E10_test_results.png | Both scripts passing | VS Code terminal: `python login_test.py -v` then `python attendance_marking_test.py -v` |

Note for E03, E04 and E08: those moments have already passed, and I will not recreate them as fake images. The exact real outputs are recorded in OBSERVATION_LOG.md. If you want genuine screenshots, show the same outputs from a throwaway clone, labelled as a re-run.
