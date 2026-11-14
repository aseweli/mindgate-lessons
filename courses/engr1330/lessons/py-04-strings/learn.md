## Why it matters

Text is everywhere: file names, sensor IDs, user input. Indexing and slicing work the same way on lists and NumPy
arrays later, so this is also practice for Units 2 and 6.

## 1. Indexing

Positions start at **0**; negative indices count from the end (−1 is the last character).

```python
s = "he ate camel food"
print(s[0], s[3], s[-1], s[-4])
print(len(s))
```

```text
h a d f
17
```

## 2. Slicing `s[start:end:step]`

From `start` up to but **not including** `end`. Defaults: start 0, end the length, step 1. A negative step walks
backwards (`s[::-1]` reverses).

```python
print(s[0:2], "|", s[3:6], "|", s[:2], "|", s[7:], "|", s[::2])
print(s[::-1])
print("Light ray"[::-1])
```

```text
he | ate | he | camel food | h t ae od
doof lemac eta eh
yar thgiL
```

## 3. Strings are immutable

You can't change a character in place; build a new string instead.

```python
word = "cat"
word[0] = "b"
```

```text
TypeError: 'str' object does not support item assignment
```

```python
word = "b" + word[1:]
print(word)
```

```text
bat
```

## 4. Operators and methods

`+` joins, `*` repeats, `in` tests membership, comparisons are alphabetical (uppercase before lowercase). Methods
return **new** strings:

```python
t = "Texas Tech"
print(t.upper(), t.lower(), t.replace("Tech", "A&M"))
print("ab" * 3, "Tech" in t, t.find("Tech"), t.count("e"))
print("10,20,30".split(","))
print("hitchhiker".replace("hi", "ma"))
print(t)
```

```text
TEXAS TECH texas tech Texas A&M
ababab True 6 2
['10', '20', '30']
matchmaker
Texas Tech
```
