## Why it matters

"What is x after this line?" is the most common Exam 1 question. Getting it right means knowing what each operator
does and in which order Python applies them.

## 1. Arithmetic operators

```python
a, b = 15, 2
print(a + b, a - b, a * b, a / b, a // b, a ** b, a % b)
```

```text
17 13 30 7.5 7 225 1
```

- `/` always gives a **float** (15 / 3 is 5.0).
- `//` is **floor division** (rounds down: −7 // 2 is −4). `%` is the **remainder**.
- `**` is power.

## 2. Precedence

`()` first, then `**`, then `* / // %` (left to right), then `+ -` (left to right).

```python
print(2 + 3 * 5 + 5)
print((2 + 3) * (5 + 5))
print(7 + 3 * 6 / 2 - 1)
print(2 % 2 + 2 * 2 - 2 / 2)
a, b = 3, 4
print(a*a + b*b**0.5, (a*a + b*b)**0.5)
```

```text
22
50
15.0
3.0
17.0 5.0
```

The hypotenuse needs the parentheses: `(a*a + b*b)**0.5`.

## 3. Comparisons and logic

`== != > >= < <=` give `True`/`False`. `and` is True only if both sides are; `or` if at least one is; `not` flips.
Precedence: comparisons, then `not`, then `and`, then `or`.

```python
x, y = 12, 6
print(x == y, x != y, x > y)
print(x < 15 and y == 6, 4 > 3 or 17 > 20, not 5 == 5)
print(True or False and False)
```

```text
False True True
True True False
True
```

The last line is `True or (False and False)` → True.

Augmented assignment: `n += 3` means `n = n + 3`; also `-=`, `*=`, `/=`.
