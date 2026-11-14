## Why it matters

Every program stores data in variables. Most beginner errors on Exam 1 are about types: `input()` gives a string,
`"2" + "3"` is `"23"`, and an illegal name stops the program before it runs.

## 1. Variables

`name = value` stores a value; assigning again replaces it. Names may contain letters, digits and `_`, must not
start with a digit or contain symbols like `$`, and can't be **keywords** (`if`, `for`, `True`, `class`, `def`, ...).
Names are case-sensitive.

```python
exchange_rate = 0.1
my_name = "John"
name = my_name
my_name = "Brian"
print(name, my_name)
```

```text
John Brian
```

`name` still holds "John": it got the value at the moment of assignment.

## 2. Data types

| type | examples |
| --- | --- |
| `int` | 2045, 0, -87 |
| `float` | 140.75, -0.5, 2.0 |
| `str` | 'Hello', "Data Science" |
| `bool` | True, False |

```python
print(type(7), type(7.0), type("7"), type(True))
```

```text
<class 'int'> <class 'float'> <class 'str'> <class 'bool'>
```

## 3. Input is always a string

`input("prompt")` returns what the user typed **as a str**. Convert with `int()` or `float()` before doing math.

```python
a = "2"     # what input() returns when the user types 2
b = "3"     # ... and 3
print(a + b)
print(int(a) + int(b))
```

```text
23
5
```

## 4. print

`print(a, b)` separates items with a space; `sep=` and `end=` change that. Escape sequences: `\n` newline, `\t` tab,
`\\` backslash, `\"` quote. Comments start with `#`.

```python
x, y = 3, 4.5
print("x =", x, "and y =", y)
print(x, y, sep=" | ")
print("Line 1\nLine 2")
print("no newline", end="")
print(" ... continued")
```

```text
x = 3 and y = 4.5
3 | 4.5
Line 1
Line 2
no newline ... continued
```
