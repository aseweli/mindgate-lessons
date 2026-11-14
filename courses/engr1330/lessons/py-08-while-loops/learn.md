## Why it matters

Sometimes you don't know in advance how many repetitions you need: keep asking until the input is valid, keep
iterating until the error is small (numerical methods in Unit 9). That's **indefinite iteration**, the `while` loop.

## 1. while

The condition is checked **before** every pass; when it is False the loop ends. If it is False at the start, the
body never runs.

```python
n = 5
while n > 0:
    n -= 1
    print(n, end=" ")
print()
counter = 0
while counter <= 3:
    print("Counter =", counter)
    counter += 1
```

```text
4 3 2 1 0 
Counter = 0
Counter = 1
Counter = 2
Counter = 3
```

Something in the body must move toward making the condition False, or the loop runs forever (**infinite loop**).

## 2. break and continue

`break` leaves the loop immediately; `continue` skips the rest of this pass and goes back to the condition.

```python
n = 7
while n > 0:
    n -= 1
    if n == 4:
        break
    print(n, end=" ")
print("| loop ended")
n = 7
while n > 0:
    n -= 1
    if n == 4:
        continue
    print(n, end=" ")
print("| loop ended")
```

```text
6 5 | loop ended
6 5 3 2 1 0 | loop ended
```

## 3. Sentinel / validation loops

`while True:` with a `break` once the input is acceptable:

```py
while True:
    my_number = int(input("Please enter a number above 100: "))
    if my_number > 100:
        break
```

## 4. try / except

Code that might fail goes in `try`; what to do if it does goes in `except`. The program keeps running.

```python
x = 12.0
y = 2.0
while y >= -2.0:
    try:
        print(y, x / y)
    except ZeroDivisionError:
        print(y, "division by zero")
    y -= 1
```

```text
2.0 6.0
1.0 12.0
0.0 division by zero
-1.0 -12.0
-2.0 -6.0
```

A loop that works through a list: a list is True while it has items.

```python
a = ['R', 'E', 'D', 'R', 'U', 'M']
while a:
    print(a.pop(-1), end="")
print()
```

```text
MURDER
```
