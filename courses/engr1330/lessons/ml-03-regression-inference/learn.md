## Why it matters

A regression line can always be computed, even when it's the wrong model. Residual plots and a few formulas tell
you whether the line is trustworthy, and a bootstrap interval tells you whether the slope is real or just luck.

`trees.csv` is **made-up practice data**: trunk diameter (cm) and age (years) of 35 trees, where age grows faster
than linearly.

## 1. Residual plots

Plot **residuals against x**. A good linear fit shows a shapeless cloud around 0, evenly spread.

- **A curve (U or arch)**: the relation is non-linear; a straight line is not the best model.
- **A fan (spread grows with x)**: *heteroscedasticity*; the line is less accurate in some ranges than others.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fit(x, y):
    r = np.corrcoef(x, y)[0, 1]
    slope = r * np.std(y) / np.std(x)
    return slope, np.mean(y) - slope * np.mean(x)

t = pd.read_csv("trees.csv")
slope, intercept = fit(t["Diameter"], t["Age"])
res = t["Age"] - (slope * t["Diameter"] + intercept)
plt.scatter(t["Diameter"], res)
plt.axhline(0)
plt.xlabel("Diameter (cm)")
plt.ylabel("Residual (years)")
plt.show()
print("residuals at the ends:", round(res.iloc[0], 1), round(res.iloc[-1], 1))
print("residuals in the middle:", round(res.iloc[15], 1), round(res.iloc[17], 1))
```

```text
residuals at the ends: 5.7 7.9
residuals in the middle: -1.9 -3.9
```

Positive at both ends, negative in the middle: a U-shape, so the trees need a curved model.

## 2. Numerical facts about residuals

For the regression line, always:

- The **average residual is 0** (however bad the scatter plot is).
- $SD_{\text{residuals}} = \sqrt{1 - r^2}\; SD_y$. If $r = \pm1$ the residuals are all 0; if $r = 0$ the line is flat and
  the residuals are as spread out as y itself.
- $SD_{\text{fitted values}} / SD_y = |r|$.

```python
h = pd.read_csv("heights.csv")
x, y = h["Midparent"], h["Child"]
slope, intercept = fit(x, y)
fitted = slope * x + intercept
res = y - fitted
r = np.corrcoef(x, y)[0, 1]
print(round(np.mean(res), 6))
print(round(np.std(res), 4), round(np.sqrt(1 - r**2) * np.std(y), 4))
print(round(np.std(fitted) / np.std(y), 4), round(abs(r), 4))
```

```text
0.0
3.4413 3.4413
0.2541 0.2541
```

## 3. Is the slope real? Bootstrap it

Your scatter plot is one sample. Its slope might be positive just by chance while the **true** (population) line
is flat. Bootstrap the scatter plot: resample **rows** with replacement, refit, collect the slopes, take the middle
95%. **If that interval contains 0, don't trust a linear relationship.**

```python
np.random.seed(1330)
slopes = []
for i in range(2000):
    rs = h.sample(len(h), replace=True)
    slopes.append(fit(rs["Midparent"], rs["Child"])[0])
print("95% CI for the true slope:", round(np.percentile(slopes, 2.5), 3), round(np.percentile(slopes, 97.5), 3))
```

```text
95% CI for the true slope: 0.266 0.739
```

The whole interval is above 0, so the positive slope isn't a fluke.
