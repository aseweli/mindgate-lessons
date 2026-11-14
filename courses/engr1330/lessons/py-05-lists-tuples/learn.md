## Why it matters

Lists hold collections of data (sensor readings, names, results of a simulation). You'll index, slice and loop
over them in almost every program in this course.

## 1. Lists are ordered, mutable and can mix types

```python
crew = ["Walter", "Jesse", "Gus", "Mike", 8, True, 342.232]
print(len(crew), crew[0], crew[-1], crew[0:3])
crew[-1] = "Hello"
del crew[2]
crew.append("hi")
print(crew)
```

```text
7 Walter 342.232 ['Walter', 'Jesse', 'Gus']
['Walter', 'Jesse', 'Mike', 8, True, 'Hello', 'hi']
```

## 2. Changing lists

`append(x)` adds at the end, `insert(i, x)` at position i, `pop(i)` removes and returns item i (last if no i),
`del lst[i]` deletes, `remove(x)` deletes the first x. `sorted(lst)` returns a new sorted list; `lst.sort()` sorts in place.

```python
v = [2.3, 4.6, 6.9]
v.insert(1, "hello")
last = v.pop()
print(v, last)
print(list(range(0, 21, 5)), sum(range(0, 21, 5)), max([3, 9, 1]), min([3, 9, 1]))
```

```text
[2.3, 'hello', 4.6] 6.9
[0, 5, 10, 15, 20] 50 9 1
```

## 3. Nested lists

Index step by step from the outside in.

```python
m = [2.3, 4.6, [1, 3, 5], ["science", "engineering"]]
print(m[2][1], m[3][0], m[3][0][0])
deep = [1, 2, 3, [4, 5, ["target"]]]
print(deep[3][2][0])
```

```text
3 science s
target
```

## 4. Tuples are immutable

A tuple `(a, b, c)` is like a list that can't change after it's created. Use it for fixed records; unpack it into variables.

```python
point = (3, 4)
x, y = point
print(x, y, len(point))
point[0] = 5
```

```text
3 4 2
TypeError: 'tuple' object does not support item assignment
```
