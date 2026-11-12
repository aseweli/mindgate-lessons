# Writing MindGate lessons and problems

This repository holds the lessons for the **MindGate** study app (code: `aseweli/mindgate`). The app downloads this
repository, checks every file, and shows the lessons. A pull that has **any** error is not installed: the app keeps the
previous lessons and lists the errors in Settings. So check your work before pushing (see "Before you push").

Who reads this: the person studying, and any model asked to write lessons. **Follow this file exactly.** Only the block
types, answer types and fields listed here exist. Anything else is an error.

Courses:

| Folder | Course | Textbook | Exams |
| --- | --- | --- | --- |
| `courses/math1451` | MATH 1451 Calculus I with Applications (TTU, Fall 2026) | Smith, Strauss, Toda, *Calculus*, 8th ed. | Written, timed, **no calculator** → exact answers |
| `courses/chem1307` | CHEM 1307 Principles of Chemistry I (TTU, Fall 2026) | Vining, Young, Day, Botch, *General Chemistry*, 1st ed. (MindTap) | Online **multiple choice**, calculator + Fact Sheet |

---

## 1. Layout

```
mindgate.json                         {"schema": 1, "courses": ["math1451", "chem1307"]}   (course order)
courses/<course>/course.json          syllabus: units (in teaching order), exams, rules, resources
courses/<course>/lessons/<lesson-id>/
    lesson.json                       the lesson: tabs made of blocks
    *.md                              long text, referenced from lesson.json as {"file": "intro.md"}
    *.png | *.svg | *.jpg ...         figures used by "figure" blocks
    problems/<problem-id>.json        one problem: variables, answers, hints, tests
    problems/<problem-id>.md          (optional) its statement, then "## Hint" and "## Solution" sections
```

Rules:

- **IDs** (folder and file names) use letters, digits, `-`, `_`, `.` only, at most 80 characters. A lesson's folder name **is**
  its id; a problem's file name (without `.json`) **is** its id.
- Suggested ids: math `m-3.5-chain-rule`, chem `ch08-vsepr`. Problems: `chain-01`, `vsepr-03`.
- **A lesson only appears if its id is listed** in a unit's `"lessons"` array in `course.json`, in the order you want.
- Anything outside `courses/` (drafts, notes, source PDFs you keep for reference) is ignored by the app. Lesson folders
  whose name starts with `_` are ignored too (handy for drafts).

## 2. Text: Markdown + LaTeX

Every text field accepts any of:

- an inline string: `"md": "The derivative of $x^2$ is $2x$."`
- a list of lines (joined with newlines): `"md": ["# Heading", "", "A paragraph with $x^2$."]`
- a file next to the JSON: `"md": {"file": "explain.md"}`  ← **preferred for anything longer than a sentence**

Inside text:

| Write | Shows |
| --- | --- |
| `$...$` / `$$...$$` (also `\(...\)` / `\[...\]`) | inline / display math (KaTeX: nearly all of LaTeX math mode) |
| `$\ce{2H2 + O2 -> 2H2O}$`, `$\ce{SO4^2-}$`, `$\ce{A ->[\Delta] B}$` | chemical formulas and equations (mhchem) |
| `$\pu{40.7 kJ/mol}$`, `$\pu{1.20e3 g}$` | numbers with units (mhchem) |
| Markdown | `**bold**`, `*italic*`, lists, tables, `> quotes`, `## headings`, `[links](https://...)` |

**JSON escaping:** inside a JSON string every backslash is doubled: `"$\\frac{1}{2}$"`, `"$\\ce{H2O}$"`. In `.md` files you
write LaTeX normally (`$\frac{1}{2}$`). That is why long text belongs in `.md` files.

---

## 3. course.json (already written for both courses; edit only to add lessons or fix dates)

```json
{
  "id": "chem1307", "code": "CHEM 1307", "title": "Principles of Chemistry I", "term": "Fall 2026",
  "accent": "#f85149",
  "textbook": {"title": "...", "authors": "...", "edition": "1st", "publisher": "..."},
  "rules": {"calculator": true, "exact_answers": false, "fact_sheet": true, "notes": "shown on the overview"},
  "notes": "Markdown shown on the course overview",
  "units": [ {"id": "ch07", "title": "Ch. 7 · ...", "from": "2026-11-02", "to": "2026-11-09", "summary": "optional",
              "lessons": ["ch07-configurations", "ch07-trends"]} ],
  "exams": [ {"id": "exam3", "title": "Exam 3", "opens": "2026-11-19T20:00", "closes": "2026-11-21T20:00",
              "after_unit": "ch09", "covers_text": "Chapters 7–9", "format_text": "30 multiple choice · 90 min"} ],
  "fact_sheet": "Markdown (periodic table notes, constants) shown on the overview and in fact_sheet blocks",
  "resources": [ {"title": "...", "url": "https://...", "note": "optional"} ]
}
```

Exams take one of `"week_of"`, `"at"`, or `"opens"` + `"closes"` (ISO dates). `"after_unit"` places the exam marker in the sidebar.

---

## 4. lesson.json

```json
{
  "id": "ch08-vsepr",
  "title": "Molecular shapes (VSEPR) and polarity",
  "short": "VSEPR & polarity",
  "section": "8.x",
  "chapter": 8,
  "minutes": 75,
  "difficulty": 3,
  "objective": "Predict electron-domain geometry, molecular geometry, bond angles and polarity from a Lewis structure.",
  "requires": ["ch08-lewis"],
  "tags": ["exam3"],
  "tabs": [
    {"id": "learn",    "title": "Learn",    "blocks": [ ... ]},
    {"id": "watch",    "title": "Watch",    "blocks": [ ... ]},
    {"id": "examples", "title": "Examples", "blocks": [ ... ]},
    {"id": "practice", "title": "Practice", "blocks": [ ... ]},
    {"id": "review",   "title": "Exam review", "blocks": [ ... ]}
  ]
}
```

- Required: `title`, and either `tabs` or `blocks`. A flat `"blocks": [...]` makes one **Learn** tab; adding
  `"problems": ["p1", "p2"]` then adds a **Practice** tab.
- Tabs are fully up to you (ids, titles, order, how many). The app always adds a **Notes** tab at the end for the student.
- `short` is the sidebar label (≤ 28 characters). `section` (math) or `chapter` (chem) shows in the header.

### Blocks

| `type` | Fields | What it shows |
| --- | --- | --- |
| `markdown` | `md` | Prose with math |
| `callout` | `style`: `key` \| `tip` \| `warn` \| `exam` \| `ok`; `title` (optional); `md` | A highlighted box. Use `exam` for "how this shows up on the TTU exam", `warn` for common mistakes |
| `terms` | `items`: `[["term", "definition"], ...]`; `title` (optional, `false` hides it) | Definition list |
| `video` | `youtube` (video id) or `url`; `title`; `channel`; `start`, `end` (`"12:40"` or seconds); `focus` | Embedded YouTube player at the right timestamp, plus "Open on YouTube" |
| `worked_example` | `title`; `problem` (md); `steps`: `[{"title"?, "md", "why"?}]`; `answer` (md); `reveal`: `"step"` (default) or `"all"` | Step-by-step solution the student reveals one step at a time |
| `formulas` | `title`; `items`: `[{"label", "latex", "note"?}]` (`latex` is raw LaTeX without `$`) | A formula sheet |
| `figure` | `src` (image file in the lesson folder); `alt`; `caption`; `width` | An image (png, jpg, gif, svg, webp) |
| `checklist` | `id`; `title`; `items`: `["md", ...]` | Self-check boxes (remembered on the Mac) |
| `flashcards` | `title`; `cards`: `[["front md", "back md"], ...]` | Click-to-flip cards |
| `lewis_demo` | `title`; `formula`; `structure` (see §8); `caption` | A read-only Lewis structure drawing |
| `problem` | `id` (a problem in `problems/`) | One problem inline (good inside Learn/Examples, right after the idea it practices) |
| `problem_set` | `problems`: `["id", ...]`; `title`; `intro` | Several problems in order |
| `fact_sheet` | (none) | The course's `fact_sheet` text |
| `divider` | (none) | A horizontal rule |

Video rules: **use only real video ids you have verified** (the 11-character id after `watch?v=`). Never guess an id.
Prefer short, focused segments using `start`/`end` over whole hour-long videos. Good channels: The Organic Chemistry Tutor,
Khan Academy, Professor Dave Explains, Tyler DeWitt (chem), Professor Leonard, PatrickJMT, 3Blue1Brown (calc).
Always fill `focus` with what to watch for. If you can't verify a video, leave the block out.

---

## 5. Problems (WeBWorK style)

A problem is `problems/<id>.json`, optionally with `problems/<id>.md` for the statement.

```json
{
  "title": "Chain rule with a power",
  "difficulty": 2,
  "minutes": 4,
  "tags": ["3.5", "chain-rule"],
  "exact": true,
  "vars": {
    "a": {"int": [2, 6]},
    "b": {"pick": [-3, -1, 1, 2]},
    "n": {"int": [3, 6]},
    "f": {"formula": "(a*x^2 + b)^n"}
  },
  "where": ["a + b != 0"],
  "answers": {
    "fp":  {"type": "formula", "value": "n*(a*x^2+b)^(n-1)*2*a*x", "vars": {"x": [-2, 2]},
            "feedback": [{"answer": "n*(a*x^2+b)^(n-1)", "message": "Multiply by the derivative of the inside, 2·[$a]x."}]},
    "fp1": {"type": "number", "value": "n*(a+b)^(n-1)*2*a"}
  },
  "hints": ["Which function is inside which?", "Let $u = [$a]x^2 + [$b]$. What is $du/dx$?", "$f'(x) = n u^{n-1} \\cdot u'$"],
  "tests": {"fp": {"right": ["2*[$a]*[$n]*x*([$a]x^2+[$b])^([$n]-1)"], "wrong": ["[$n]*([$a]x^2+[$b])^([$n]-1)"]}}
}
```

`problems/chain-01.md`:

```markdown
Let $f(x) = [$f]$.

a) $f'(x) =$ [__________]{fp}

b) $f'(1) =$ [_____]{fp1}

## Hint
(optional; hints may also be written here instead of in JSON, one "## Hint" section each)

## Solution
Let $u = [$a]x^2 + [$b]$, so $f = u^{[$n]}$ and $u' = [$a]\cdot 2x$. By the chain rule ...
```

### Fields

| Field | Meaning |
| --- | --- |
| `statement` | The problem text (or put it in `<id>.md`). Contains the answer boxes |
| `answers` | `{answer_id: spec}`; every box in the text needs one, and every answer needs a box |
| `parts` | Instead of `statement` + `answers`: `[{"id": "a", "title"?, "statement", "answers", "hints"?, "solution"?}]` |
| `scaffold` | `true`: part 2 unlocks only after part 1 is correct (WeBWorK scaffolding) |
| `vars`, `where` | Random variables (§5.1) |
| `hints` | List of up to ~4 hints, revealed one at a time: 1 = the idea, 2 = a guiding question/setup, 3 = the next concrete step |
| `solution` | Full worked solution (shown after a correct answer or "Give up") |
| `show_solution` | `"after_correct"` (default) or `"never"` (then only "Give up" shows it) |
| `exact` | `true` makes every `number` answer reject decimals (use for MATH 1451) |
| `difficulty` 1–5, `minutes`, `tags`, `title` | Shown in the header; tags are free text |
| `tests` | `{answer_id: {"right": [...], "wrong": [...]}}` entries that must be accepted / rejected (§9). `[$var]` works inside |

### 5.1 Random variables

| Spec | Value |
| --- | --- |
| `{"int": [lo, hi]}`, optional `"step"`, `"not": [values]` | random integer |
| `{"real": [lo, hi], "step": 0.1}` or `{"real": [lo, hi], "decimals": 3}` | random decimal |
| `{"pick": [v1, v2, ...]}` | one of the list. Items may be objects: `{"pick": [{"name": "water", "f": "H2O", "M": 18.02}, ...]}` → use `[$m.name]`, and `m.M` inside expressions |
| `{"formula": "expr"}` | a formula built from other variables, displayed simplified with `[$f]` (e.g. `(3x^2 - 1)^4`) |
| `{"expr": "expr", "round": 2}` | a number computed from other variables |
| a plain number or string | a constant |

`"where": ["a != b", "a*c > 0"]` re-draws until every condition holds (comparisons: `== != < > <= >=`).

### 5.2 Showing variables in text

`[$a]` → value of `a` (integers print without decimals; formulas print as simplified LaTeX, so use them inside `$...$`).
`[$a:.2f]` → Python format spec. `[$a:3sf]` → 3 significant figures. `[$m.name]` → a field of a picked object.

Write expressions with formula variables instead of pasting numbers into LaTeX (`$[$f]$`, not `$([$a]x^2 + [$b])$`,
which would show `+ -3` when b is negative).

### 5.3 Answer boxes

`[_____]{id}`: the number of underscores sets the width. `[_]{id}` for choice, multi and lewis answers. Boxes must be
**outside** `$...$`.

### 5.4 Expressions (in `value`, `expr`, `formula`, and what students type)

`+ - * / ^` (or `**`), parentheses, implied multiplication (`2x`, `3(x+1)`, `x sin(x)`), `pi`, `e`, `sqrt()`, `abs()` or `|x|`,
`sin cos tan sec csc cot`, `arcsin arccos arctan` (also `asin`…, `sin^-1(x)`), `sinh cosh tanh`, `ln`, `log` (= natural log,
as in WeBWorK), `log10`, `exp`, `n!`. `sin^2(x)` means `(sin x)^2`. Students get the same syntax and a live preview.

---

## 6. Answer types

Common options for any answer: `"feedback": [{"answer": "<a typical wrong answer>", "message": "..."}]` (shown when the
student's entry matches that wrong answer, checked the same way as the real answer) or `{"contains": "text", "message": "..."}`;
`"width"`.

| `type` | Required | Options | Student enters | Checked by |
| --- | --- | --- | --- | --- |
| `number` | `value` (expression or `"DNE"`/`"INF"`/`"-INF"`) | `exact` (reject decimals), `tol` (default 0.001), `tol_type` (`relative`/`absolute`), `allow`: `["DNE","INF"]` | `sqrt(3)/2`, `-7/4`, `DNE`, `inf` | value within tolerance |
| `formula` | `value` | `vars`: `{"x": [lo, hi], "y": [lo, hi]}` (test ranges; keep inside the domain!), `tol`, `points` | `24x(3x^2-1)^3` | equal at 12 random points |
| `formula_c` | `value` (without +C) | `vars`, `constant` (default `"C"`) | `x^3/3 + 2x + C` | differs by a constant; `+ C` required |
| `choice` | `choices` (md list), `correct` (0-based index) | `display`: `radio` (default) / `dropdown`; `shuffle` (default true); `fixed_last`: n keeps the last n in place ("None of these"); `explanations`: md per choice (shown after checking) | picks one | index |
| `multi` | `choices`, `correct`: [indexes] | `shuffle`, `partial` (partial credit) | picks several | exact set |
| `order` | `items` (in the correct order) | `separators`, `case_sensitive` (default true), `allow_reverse` (accept `>` order), `show_items` (default true) | `Cl < S < Mg < Na` | sequence |
| `text` | `accept`: [accepted spellings] | `case_sensitive`, `ignore_punctuation` | `bent` | normalized match (prefer `choice` when possible) |
| `list` | `values`: [expressions] | `ordered`, `element`: an answer spec for each item (default `{"type": "number"}`), `partial`, `allow_none` | `-2, 1/3` | each item matched once |
| `interval` | `value`, e.g. `"(-inf, -2) U [1, 3]"` (`[$a]` allowed) | `tol` | `(-inf,-2) U [1,3]` | endpoints + brackets |
| `quantity` | `value` (expression, in `units`), `units` | `tol` (default 0.01 relative), `sigfigs`: n, `sigfig_mode`: `warn` (default) / `require` | `3.20e2 torr`, `0.421 atm`, `4.5*10^-3 mol` | converted to `units`, then tolerance; sig figs counted from what was typed |
| `chem_formula` | `value` | `exact_form` (require the same writing order) | `Fe2O3`, `Ca(OH)2`, `SO4^2-`, `CuSO4*5H2O` | element counts + charge |
| `coefficients` | `values`: [ints] | `lowest` (default true) | `1, 5, 3, 4` | proportional; lowest whole numbers |
| `econfig` | `value`, e.g. `"[Ar]3d5 4s1"` | | `[Ar]4s1 3d5` or the full form | same subshell filling (any order, noble-gas core expanded) |
| `lewis` | `formula` and `structures`, or `"mode": "rules"` | `charge`, `allow`, `palette`, `start`, `mismatch_message`, `min_formal_charge` | builds it in the Lewis editor | §8 |

Units known to `quantity`: g kg mg µg, L mL, mol mmol, M (mol/L), atm torr mmHg Pa kPa bar psi, J kJ cal kcal Cal eV,
K and °C (temperature: only K ↔ °C conversion), m cm mm nm pm Å, s min h, Hz, amu/u/Da, C, V, W, N, and "molecules"/"atoms"
(as counts, 1 mol = 6.022e23). Combine with `*`, `/` and `^`: `kJ/mol`, `L*atm/(mol*K)`, `g/mol`, `J/(g*K)`, `m/s^2`.
Ions: write the charge with `^` for numbers (`SO4^2-`, `Fe^3+`); a bare `+`/`-` means 1 (`NH4+`, `OH-`).

---

## 7. Course-specific rules

**MATH 1451** (no calculators on exams): set `"exact": true` on problems with numeric answers and use exact values
(`sqrt(3)/2`, `pi/6`, `ln(2)`). Use `formula` for derivatives, `formula_c` for antiderivatives, `interval` for
domains/increasing/concavity, `list` for critical numbers and solutions, `number` with `"allow": ["DNE", "INF"]` for limits.
Match the textbook section numbering (`"section": "3.5"`). The course overview already lists the suggested textbook exercises.

**CHEM 1307** (multiple-choice exams with a calculator): end every lesson with exam-style `choice` problems (4–5 options,
plausible distractors built from real mistakes, `explanations` for each choice). Use `quantity` with `sigfigs` for
calculations, `lewis` for structures, `econfig` for configurations, `order` for periodic and IMF trends, `coefficients`
for balancing. The instructor's study-guide outline for each chapter lists exactly what's tested; cover every point of it.

---

## 8. Lewis structures

A structure is atoms and bonds; positions are optional (the app lays it out):

```json
{"atoms": [{"el": "C", "lp": 0}, {"el": "O", "lp": 2}, {"el": "O", "lp": 2}],
 "bonds": [[0, 1, 2], [0, 2, 2]]}
```

`lp` = number of lone **pairs**; `"e": 1` = one unpaired electron (NO, NO₂); a bond is `[atom index, atom index, order 1–3]`.
Formal charges are computed, never written.

Answer spec:

```json
{"type": "lewis", "formula": "NO3-",
 "structures": [ {...resonance form 1...}, {...form 2...}, {...form 3...} ],
 "allow": [], "mismatch_message": "Close: which oxygen carries the double bond doesn't matter, but N needs an octet."}
```

- `"structures"` (match mode): accepted if the drawing is the same as **any** listed structure (atom labels, lone pairs and
  bond orders compared as a graph, so atom order doesn't matter). List every acceptable resonance form.
- `"mode": "rules"`: accepted if atoms match the formula, the electron count is right, every atom has an octet (duet for H)
  and formal charges sum to the charge. Add `"min_formal_charge": true, "max_abs_fc": 0` to also demand the lowest formal
  charges.
- `"allow"`: `"expanded_octet"` (period 3+ central atoms like PCl5, SF6), `"incomplete_octet"`, `"odd_electron"`.
- When wrong, the student sees the first problem found: wrong atoms, wrong electron total, which atom lacks an octet,
  formal-charge sum, or `mismatch_message`.
- `palette` sets the element buttons (default: the elements in `formula`); `start` pre-draws a partial structure.

---

## 9. The quality bar ("high detail")

Each lesson should contain, in this order:

1. **Learn**: why it matters (one short paragraph), key terms, the explanation built up from simple to exam-level with
   small examples, a `formulas` block for anything to memorize, `callout` blocks: `warn` for the 2–4 most common mistakes,
   `exam` for how TTU tests it (format, typical wording, what is given: e.g. the CHEM Fact Sheet).
2. **Watch**: 1–3 verified videos with start/end and a `focus` each.
3. **Examples**: 2–4 `worked_example` blocks, from basic to exam-level, every step with a `why`.
4. **Practice**: 6–12 problems, easy → exam-level (`difficulty` 1→5). Randomize numbers. Multi-part problems where
   steps build. `feedback` entries for the classic wrong answers. 3 hints each. A full step-by-step `solution` each.
5. **Exam review**: `flashcards` for definitions/trends, a `checklist` of "I can…" statements, and 3–5 mixed exam-style problems.

Rules:

- Everything original: don't copy textbook, WeBWorK, MindTap or study-guide problems or prose verbatim. Use the study guide
  as the list of topics to cover.
- Every claim correct; every number checked; every `value` computed from the variables (never typed in as a number).
- Keep test ranges for `formula` answers inside the function's domain (e.g. `{"x": [0.5, 3]}` for `ln(x)`).
- Add `tests` for the important answers: at least one `right` (a different but equivalent form) and one `wrong` (the
  classic mistake).

## 10. Before you push

From a clone of the app repo (`aseweli/mindgate`), next to this repo:

```bash
python3 tools/check_content.py ../mindgate-lessons
```

It must end with `RESULT: ALL OK`. It loads everything, creates 25 random copies of every problem, confirms each answer
key is accepted by its own checker, and runs your `tests`. To see the lessons in the app before pushing:

```bash
./run.sh --lessons ../mindgate-lessons
```

Then push to `main`. The app checks for new lessons every 2 hours while it's open, or immediately with
**Settings → Pull questions**.
