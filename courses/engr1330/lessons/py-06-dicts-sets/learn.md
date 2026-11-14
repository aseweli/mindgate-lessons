## Why it matters

A dictionary is a lookup table: give it a **key**, get the **value**, like a phone book. It's the natural structure
for inventories, settings and word counts. Sets keep only unique items.

## 1. Creating and looking up

```python
d1 = dict(A=123, B=222, C="Lubbock")
d2 = {"A": 123, "B": 222, "C": "Lubbock"}
print(d1 == d2, d2["C"], len(d2))
d2["D"] = 4.5            # add
d2["A"] = 0              # update
print(d2)
print(d2.get("Z", "missing"))
```

```text
True Lubbock 3
{'A': 0, 'B': 222, 'C': 'Lubbock', 'D': 4.5}
missing
```

A missing key with `d[key]` raises **KeyError**; `d.get(key, default)` doesn't.

## 2. Nested data

```python
inventory = {'ford': {'mustang': [2022, 2000, 2013], 'escape': [1999, 2021]},
             'chevy': {'blazer': [2014, 2019], 'camaro': [2019, 2000]}}
print(inventory['ford']['mustang'])
print(inventory['chevy']['camaro'][1])
d3 = {'key': [20, 25, 25, {'innerkey': [11, 22, 33]}]}
print(d3['key'][3]['innerkey'][1])
```

```text
[2022, 2000, 2013]
2000
22
```

## 3. Looping and counting

```python
shopping = {"apples": 4, "milk": 1, "eggs": 12}
for item, qty in shopping.items():
    print(item, qty)
print("total items:", sum(shopping.values()), "unique:", len(shopping))

counts = {}
for w in "the cat and the hat and the bat".split():
    counts[w] = counts.get(w, 0) + 1
print(counts)
```

```text
apples 4
milk 1
eggs 12
total items: 17 unique: 3
{'the': 3, 'cat': 1, 'and': 2, 'hat': 1, 'bat': 1}
```

## 4. Sets

```python
s = {3, 1, 3, 2, 1}
print(s, len(s))
a, b = {1, 2, 3}, {2, 3, 4}
print(a & b, a | b, a - b)
print(sorted(set("mississippi")))
```

```text
{1, 2, 3} 3
{2, 3} {1, 2, 3, 4} {1}
['i', 'm', 'p', 's']
```
