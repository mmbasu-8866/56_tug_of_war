# Lab 4 - Vibe Coding Submission

## Updated code

The runnable game is in the repository root (`main.py` and `game/`). The full source snapshot, including tests and README, is also supplied as `Updated_Code.zip`.

## Videos

- `videos/before.mp4` is the current baseline capture, recorded before code changes. Replace it with the student's own before video when provided.
- `videos/after.mp4` is the after-change recording supplied by the student.

The baseline capture is the game's actual pre-change window; it is already at game over because the computer opponent wins quickly when no player input is made. Automated regression tests cover overlapping A/D input and verify the fix. Sudden Death and panic-surge behavior are covered by automated tests.

## Chat record

`Chat_History.pdf` and `Chat_History.docx` contain the Lab 4 prompt and visible progress summary. They link to the Copilot session; this is a readable record, not a raw export of hidden tool traffic.

## Verification

Run the game with `python main.py`; run the tests with `python -m pytest`.

The final regression suite passes all 7 tests. The implementation is split across four commits in this repository's history, one per handout task.
