# Lab 4 - Vibe Coding Submission

## Updated code

The runnable game is in the repository root (`main.py` and `game/`). The full source snapshot, including tests and README, is also supplied as `Updated_Code.zip`.

## Videos

- `videos/before.mp4` is the student's recording of the original game.
- `videos/after.mp4` is the student's recording of the updated game.

The before recording shows the original static game before any changes. The after recording shows the updated game with its timer, tension meter, animated rope, and leaning pullers. Automated regression tests verify overlapping A/D input, panic surges, Sudden Death, and reset behavior.

## Chat record

`Chat_History.pdf` and `Chat_History.docx` contain the Lab 4 prompt and visible progress summary, including that the student supplied both video recordings. They link to the Copilot session; this is a readable record, not a raw export of hidden tool traffic.

## Verification

Run the game with `python main.py`; run the tests with `python -m pytest`.

The final regression suite passes all 7 tests. The implementation is split across four commits in this repository's history, one per handout task.
