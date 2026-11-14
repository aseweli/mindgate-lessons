## Why it matters

When you know what to repeat over (every item of a list, every number 1 to n), a `for` loop is the clean way:
**definite iteration**. Summing, counting and building tables are all for loops.

## 1. Looping over a collection

```python
for name in ['Rick', 'Summer', 'Morty']:
    print(name)
for index, pet in enumerate(["dusty", "aspen"]):
    print(index, pet)
for ch in "Tech":
    print(ch, end=" ")
print()
```

```text
Rick
Summer
Morty
0 dusty
1 aspen
T e c h 
```

## 2. range(start, stop, step)

Integers from `start` up to but **not including** `stop`. Defaults: start 0, step 1. All arguments must be ints.

```python
print(list(range(5)), list(range(5, 20, 3)), list(range(5, -5, -2)), list(range(5, -5)))
```

```text
[0, 1, 2, 3, 4] [5, 8, 11, 14, 17] [5, 3, 1, -1, -3] []
```

## 3. Accumulators

Start a total (0) or a product (1) **before** the loop, update it inside.

```python
n = 9
sum_odds = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        sum_odds += i
print(sum_odds)
```

```text
25
```

## 4. Nested loops

The inner loop runs completely for **each** pass of the outer loop. `print("*", end=" ")` stays on the line;
a bare `print()` ends it.

```python
r, c = 3, 5
for i in range(r):
    for j in range(c):
        print("*", end=" ")
    print()
for row in range(1, 5):
    print("* " * row)
```

```text
* * * * * 
* * * * * 
* * * * * 
* 
* * 
* * * 
* * * * 
```

`break` and `continue` work in for loops exactly as in while loops.
