# Prompt for ChatGPT: build the ENGR 1330 course for MindGate

How to use it: start a new ChatGPT chat and attach

1. `AUTHORING.md` from this repository (download it from
   https://github.com/aseweli/mindgate-lessons/blob/main/AUTHORING.md, button "Download raw file"), and
2. every file in `Downloads/Engineering 1330` (syllabus, schedule, slides, notebooks, assignments, data files).

Then paste everything below the line as your message. When ChatGPT gives you the zip(s), unzip them into the
`mindgate-lessons` folder (so `courses/engr1330/` sits next to `courses/math1451/`), add `"engr1330"` to
`mindgate.json`, and run the checker (or ask Claude to). Fix whatever it reports, then push.

---

You are writing a complete course for **MindGate**, a Mac study app, for my class **ENGR 1330** (Computational Thinking
with Data Science, Texas Tech). Two kinds of files are attached:

- **`AUTHORING.md`**: the exact file format the app reads. Follow it exactly. Only the block types, answer types and
  fields it lists exist; anything else makes the app reject the whole course. Read all of it before writing anything,
  especially §1 Layout, §2 Text, §3 course.json, §4 lesson.json and §4.1 Code editor blocks, §5–6 Problems and answer
  types, §9 Quality bar.
- **My course files** (syllabus, schedule, lecture material, assignments, data). Use them as the source of truth for
  topics, order, dates, exams and grading. Read all of them first.

## What to produce

A folder `courses/engr1330/` laid out as in AUTHORING.md §1:

- `course.json`:
  - `"id": "engr1330"`, `"code": "ENGR 1330"`, the official title and term from the syllabus, `"icon": "code"`.
  - `units` in the order the class covers them, with `from`/`to` dates from the schedule. Each unit lists its lesson ids.
  - `exams` from the syllabus: real dates (`at`, `week_of`, or `opens` + `closes`), `after_unit`, `covers_units`,
    `covers_text`, `format_text` (length, format, what is allowed: notes, computer, etc.), and `practice` if the exam
    has a known size. Add every exam, quiz block or project deadline the syllabus calls an exam.
  - `notes`: a short course overview in Markdown (grading breakdown, late policy, what tools are used), in my words, not
    copied.
  - `textbook` and `resources` (only real links that appear in my files).
  - **Never invent a date, exam, or policy.** If something is missing from my files, leave it out and tell me in your
    final message.
- One folder per lesson, `courses/engr1330/lessons/<id>/`, with `lesson.json`, `.md` files for long text, `problems/`,
  and the starter code and data files its editors use. Ids like `py-01-variables`, `pandas-02-groupby`. Problem ids like
  `vars-01`.

## What each lesson contains

Follow AUTHORING.md §9, adapted for a programming course. Tabs, in this order:

1. **Learn**: why it matters, `terms`, the explanation built up from simple to exam level with short code snippets in
   fenced ```python blocks, `callout` blocks (`warn` for the 2–4 classic mistakes beginners make, `exam` for how this is
   tested in ENGR 1330).
2. **Examples**: 2–4 `worked_example` blocks, each step with a `why`, ending in the complete program.
3. **Code**: 1–3 `editor` blocks (§4.1), `"language": "python"`:
   - Starter code in a `.py` file in the lesson folder (`"files": [{"name": "main.py", "code": {"file": "starter.py"}}]`),
     with clear `# TODO` comments and enough scaffolding that a beginner can start.
   - The task in `md`, with the expected output for a sample input.
   - `stdin` when the program uses `input()`; `data` with a small CSV (under 5 MB) for pandas/matplotlib lessons. Make
     the CSV yourself or reuse a data file from my course files.
   - Put `"open": true` on the first editor of the tab.
   - Editors are **not graded**. Put the full solution in a `worked_example` in the Examples tab or a `callout` in the
     Exam review tab, never inside the starter file.
4. **Practice**: 6–10 graded problems (§5–6), easy → exam level (`difficulty` 1→5), each with 3 hints, a full
   `solution`, and `tests`. Good kinds for code:
   - "What does this program print?" → `text` (with `accept` spellings) or `number` or `list`.
   - "Which line causes the error?" / "Which change fixes it?" → `choice` with `explanations` for every option.
   - "What is the value of `x` after this loop?" → `number`, with random values via `vars` where it makes sense
     (§5.1), so the student gets a new version each time.
   - Output that is several lines: ask for one specific line or value instead of the whole block.
5. **Exam review**: `flashcards` for syntax and definitions, a `checklist` of "I can…" statements, 3–5 mixed exam-style
   problems.

## Rules

- Python 3. Use only the libraries my class uses (check my files; usually numpy, pandas and matplotlib). Every program
  must run as written, with the given `stdin` and data files, in under 10 seconds.
- Everything original: use my assignments and slides as the list of topics and the level to aim for, but don't copy
  their wording or their problems.
- Every answer correct. Mentally run every program and check every printed value. Compute `value`s from `vars`.
- JSON must be valid. Inside JSON strings, double every backslash and escape quotes. Put any long text or code in
  `.md` or `.py` files, which need no escaping.
- Use only the block types, answer types and fields in AUTHORING.md. Ids use only letters, digits, `-`, `_` and `.`.
- Every lesson id must appear in exactly one unit's `lessons` list in `course.json`.
- Videos: only include a `video` block if you are certain the YouTube id is real and on topic. Otherwise leave it out.

## How to deliver it

The course is large, so work in rounds:

1. **First reply:** don't write lessons yet. Give me the plan: the units with dates, the exams you found, the lesson list
   for each unit (id, title, one line on what it covers), and anything missing or unclear in my files. Wait for my OK.
2. **Then:** write `course.json`, then the lessons a unit at a time. Give each round as a **downloadable .zip** whose
   paths start at `courses/engr1330/`, so I can unzip each one into the same folder. Say which lessons are in each zip
   and which are still to come.
3. **Last:** a final message listing every lesson, every exam with its date, and anything I should check or fill in.

Before you send each zip, check it yourself against this list: valid JSON everywhere; every file a block or problem
references exists in the zip; every answer box `[___]{id}` has a matching answer and the other way round; every lesson
is listed in `course.json`; no fields that AUTHORING.md doesn't define.
