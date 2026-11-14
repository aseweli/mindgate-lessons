## Why it matters

The same numbers can be shown four ways, and only one usually answers your question. Exam questions often describe
data and ask which plot fits best.

| Question | Plot | Matplotlib | pandas |
| --- | --- | --- | --- |
| How does it change over time? | **line** | `plt.plot` | `df.plot()` |
| Are two numeric variables related? | **scatter** | `plt.scatter` | `df.plot.scatter(x=..., y=...)` |
| How do categories compare? | **bar** | `plt.bar` | `df.plot.bar()` |
| How is one variable distributed? | **histogram** | `plt.hist` | `df["col"].plot.hist()` |

## 1. Line and scatter

```python
import numpy as np
import matplotlib.pyplot as plt

force = np.array([0, 5, 10, 15, 20, 25])            # N
extension = np.array([0, 2.1, 3.9, 6.2, 8.0, 10.1])  # mm
plt.scatter(force, extension)
plt.xlabel("Applied force (N)")
plt.ylabel("Extension (mm)")
plt.title("Spring force vs extension")
plt.show()
print(round(np.corrcoef(force, extension)[0, 1], 3))
```

```text
1.0
```

## 2. Bar charts for categories

```python
materials = ["Aluminum", "Steel", "Copper", "Titanium"]
density = [2700, 7850, 8960, 4500]                    # kg/m^3
plt.bar(materials, density, color="gray")
plt.ylabel("Density (kg/m³)")
plt.title("Density of engineering materials")
plt.show()
print(materials[np.argmax(density)])
```

```text
Copper
```

## 3. Histograms and bins

A histogram splits the range into **bins** and draws how many values fall in each. `bins=10` makes 10 equal bins;
`bins=[a, b, c, ...]` or `np.arange(start, stop, width)` sets the edges yourself. A value equal to an inner edge
goes into the bin to its **right**; the last bin includes its right edge. `plt.hist` returns the counts.

```python
lengths = np.array([49.6, 49.8, 49.9, 50.0, 50.0, 50.1, 50.1, 50.2, 50.3, 50.6])
counts, edges, bars = plt.hist(lengths, bins=[49.5, 49.9, 50.1, 50.3, 50.7], ec="black")
plt.xlabel("Bolt length (mm)")
plt.ylabel("Count")
plt.show()
print(counts)
```

```text
[2. 3. 3. 2.]
```

49.9 lands in the second bin [49.9, 50.1) and 50.1 in the third. Choosing bins changes how the shape looks: too few
hide detail, too many make noise.

## 4. pandas does the same

`df.plot.bar()`, `df.plot.scatter(x="A", y="B")`, `df["col"].plot.hist(bins=...)` call Matplotlib for you; finish
with the same `plt.xlabel`, `plt.title`, etc.
