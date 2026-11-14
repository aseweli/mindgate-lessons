## Why it matters

A good plot shows in a second what a table hides. Engineering plots follow conventions: labeled axes with units, a
title, a legend when there's more than one line. Missing labels are the most common way to lose points.

`motor_temps.csv` is **made-up practice data**: the temperature (°C) of two motors every 5 minutes.

## 1. A first plot

`import matplotlib.pyplot as plt`, then `plt.plot(x, y)`. Add `plt.xlabel`, `plt.ylabel`, `plt.title`,
`plt.grid()` and finish with `plt.show()`.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)       # 1000 points from -10 to 10
y = x ** 3
plt.plot(x, y)
plt.title("The y = x**3 plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
print(len(x), x[0], x[-1])
```

```text
1000 -10.0 10.0
```

## 2. Two lines, a legend and styles

Give each line a `label=` and call `plt.legend()`. Style with `color=`, `linestyle=` (`'--'`, `':'`), `linewidth=`,
`marker=` (`'o'`, `'s'`, `'*'`) and `markersize=`. Limit the view with `plt.xlim(lo, hi)` / `plt.ylim(lo, hi)`.

```python
import pandas as pd

df = pd.read_csv("motor_temps.csv")
plt.plot(df["Minute"], df["MotorA"], color="red", marker="o", label="Motor A")
plt.plot(df["Minute"], df["MotorB"], color="blue", linestyle="--", label="Motor B")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Motor temperature comparison")
plt.legend()
plt.show()
print(df.tail(2))
```

```text
    Minute  MotorA  MotorB
11      55    57.9    56.7
12      60    56.5    60.6
```

## 3. Subplots

`plt.subplot(nrows, ncols, index)` picks one panel of a grid (index starts at **1**). The object-oriented
`fig, axes = plt.subplots(nrows, ncols)` returns all axes at once; label them with `ax.set_xlabel`, `ax.set_title`,
and call `plt.tight_layout()` so they don't overlap.

```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
axes[0].plot(df["Minute"], df["MotorA"], "red")
axes[0].set_title("Motor A")
axes[1].plot(df["Minute"], df["MotorB"], "blue")
axes[1].set_title("Motor B")
for ax in axes:
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Temp (°C)")
plt.tight_layout()
fig.savefig("motors.png", dpi=100)
print(type(axes), axes.shape)
```

```text
<class 'numpy.ndarray'> (2,)
```

## 4. Figure vs Axes

The **Figure** is the whole page; an **Axes** is one plot area on it, with its own x and y axis. `figsize=(w, h)`
is in inches, `dpi` is dots per inch, and `fig.savefig("name.png")` writes the file (png, jpg, svg, pdf).
