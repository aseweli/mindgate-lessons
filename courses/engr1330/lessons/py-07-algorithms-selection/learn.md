## Why it matters

Before coding, describe the solution as a **flowchart** or **pseudocode**: you catch logic errors early and can
explain the plan to non-programmers. **Selection** (if/else) is how a program makes decisions.

## 1. Algorithms, flowcharts and pseudocode

An **algorithm** is a finite sequence of well-defined steps. A **flowchart** draws it: ovals for start/end,
parallelograms for input/output, rectangles for processing, diamonds for decisions, arrows for flow.
**Pseudocode** writes it in plain language using six constructs (in capitals): SEQUENCE, IF-THEN-ELSE, CASE,
WHILE, REPEAT-UNTIL, FOR; one statement per line, indent nested parts, close with ENDIF / ENDWHILE.

```text
GET number from user
CONVERT number to an integer
COMPUTE remainder of number divided by 5
DISPLAY remainder
```

## 2. Sequence

Statements run one after another, top to bottom; order matters (you can't use `x` before assigning it).

```python
x = 5
y = x * 2
z = y / 3
print(x, y, z)
```

```text
5 10 3.3333333333333335
```

## 3. Selection

`if condition:` runs the indented block only when the condition is True. The colon and the indentation are required.

```python
n = 144
if n % 2 == 0:
    print("even")
else:
    print("odd")

x, y = 15, 12
if x == y:
    print("equal")
elif x > y:
    print("x is greater")
else:
    print("x is smaller")
```

```text
even
x is greater
```

`elif` conditions are checked **in order** and only the **first** true branch runs.

Nested ifs and the inline if:

```python
marks = 75
if marks >= 55:
    if marks <= 69:
        print("D grade")
    elif marks <= 79:
        print("C grade")
    else:
        print("B grade or better")
else:
    print("Fail")

my_int = 3
num1 = 12 if my_int == 0 else 13
print(num1, 'Present' if 'bob' in ['sam', 'bob'] else 'Absent')
```

```text
C grade
13 Present
```
