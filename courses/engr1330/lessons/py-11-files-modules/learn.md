## Why it matters

Data arrives in files, and results must be saved. Modules bring in tools you didn't write: math, random, and
soon NumPy, pandas and Matplotlib.

## 1. CRUD with open()

Three steps: **open** a connection, **read or write**, **close**.

| mode | meaning |
| --- | --- |
| `'r'` | read (file must exist) |
| `'w'` | write: creates the file or **erases** it first |
| `'a'` | append: adds to the end (creates if missing) |

```python
f = open("bottle.txt", "w")
f.write("message in a bottle")
f.close()

f = open("bottle.txt", "a")
f.write("\nsecond line")
f.close()

f = open("bottle.txt", "r")
text = f.read()
f.close()
print(text)
print(len(text.split("\n")), "lines")
```

```text
message in a bottle
second line
2 lines
```

`with open(...) as f:` closes the file automatically. `f.readlines()` gives a list of lines.

```python
with open("bottle.txt", "r") as f:
    lines = f.readlines()
print(lines)

import os
print("bottle.txt" in os.listdir("."))
os.remove("bottle.txt")
print(os.path.exists("bottle.txt"))
```

```text
['message in a bottle\n', 'second line']
True
False
```

`os.getcwd()` is the current folder; `pathlib.Path('.').iterdir()` lists its contents.

## 2. Modules

`import math` then `math.sqrt(2)`; `from math import fsum` imports one name; `import math as ma` renames it.
Install new packages with `pip install name` (Anaconda already has NumPy, pandas, Matplotlib).

```python
import math
from math import fsum
import math as ma
import random

print(math.pi, fsum([1.0, 6.0, 9.23]), ma.sqrt(16))
random.seed(1)
print(random.randint(1, 6), random.randrange(1, 7))
```

```text
3.141592653589793 16.23 4.0
2 5
```

A file you write yourself, e.g. `amodule.py` with `def subs(a, b): return a - b`, can be imported the same way:
`import amodule` then `amodule.subs(6, 10)`.
