# Lab 4 - Vibe Coding Submission

## Project

**Tug of War Repair Lab** — Pygame
**Assigned repository:** `ruturajshedbale/56_tug_of_war`
**Working fork:** `mmbasu-8866/56_tug_of_war`

## Submission contents

| Deliverable | Files |
|---|---|
| Lab report | `Lab_4_Report.docx`, `Lab_4_Report.pdf` |
| Task prompts | `VibeCoding_Prompts.docx` |
| Original and updated code | `code/` and `Updated_Code.zip` |
| Before/after videos | `videos/before.mp4`, `videos/after.mp4` |
| Before/after evidence frames | `Before_Changes_Screenshot.png`, `After_Changes_Screenshot.png` |
| Chat record | `Chat_History.docx`, `Chat_History.pdf` |

## Updated code

The runnable game is in the repository root (`main.py` and `game/`). A copy of the complete source and tests is included in `code/` and `Updated_Code.zip`.

## Videos

- `videos/before.mp4` is the student's recording of the original game.
- `videos/after.mp4` is the student's recording of the updated game.

The before recording shows the original static game before any changes. The after recording shows the updated game with its timer, tension meter, animated rope, and leaning pullers. Automated regression tests verify overlapping A/D input, panic surges, Sudden Death, and reset behavior.

## Chat record

`Chat_History.pdf` and `Chat_History.docx` contain the Lab 4 prompt and visible progress summary, including that the student supplied both video recordings. They link to the Copilot session; this is a readable record, not a raw export of hidden tool traffic.

## Verification

Run the game with `python main.py`; run the tests with `python -m pytest`.

The final regression suite passes all 7 tests. The implementation is split across four commits in this repository's history, one per handout task.

## Task commits

- `f7da3d0` — fix alternating-input deadlock
- `55da0c1` — add panic-surged AI
- `6a7ed7f` — animate rope tension and pullers
- `8618dc8` — add timer and Sudden Death
- `9e5e3a3`, `12c7f01` — add and finalize Lab 4 evidence and reports
