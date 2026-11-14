## Why it matters

Before modeling anything, an engineer summarizes the data: where is the center, how spread out is it, is it
lopsided? Two numbers for center (mean, median) and a few for spread (range, IQR, SD) tell you most of the story,
and the bootstrap and confidence intervals that come next are built on these same statistics.

## 1. Center: mean, proportion, median, mode

The **mean** is the sum divided by the count: $\bar x = \frac1n \sum x_i$. It has the same units as the data, lies
between the min and max, and need not be one of the values.

```python
import numpy as np

loads = np.array([5, 6, 6, 12])
print(np.mean(loads))
```

```text
7.25
```

The mean depends only on **which values occur and in what proportions**: $5\cdot\tfrac14 + 6\cdot\tfrac24 + 12\cdot\tfrac14 = 7.25$.
Doubling every value's count gives the same mean.

A **proportion** is the mean of 0s and 1s: if 1 = defective, the mean is the fraction defective.

```python
defective = np.array([1, 0, 0, 1, 0, 0, 0, 1, 0, 0])
print(np.mean(defective))
```

```text
0.3
```

The **median** is the middle of the sorted values (odd count) or the average of the two middle values (even count).
It ignores how far away the extreme values are, so an outlier barely moves it. The mean, however, gets dragged.

```python
a = np.array([5, 5, 6, 6, 8, 12, 12])
b = np.array([5, 5, 6, 6, 8, 12, 1200])     # one huge outlier
print(np.median(a), np.median(b))
print(round(np.mean(a), 2), round(np.mean(b), 2))
```

```text
6.0 6.0
7.71 177.43
```

The **mode** is the most frequent value. It is a poor summary of the center for numeric data (it can sit far from
the middle), but it is the only one that works for categories.

## 2. Spread: percentiles, range, IQR

The $p$th **percentile** is the value with about $p\%$ of the data below it. `np.percentile(data, p)` interpolates
between sorted values when needed. Quartiles: $Q_1$ = 25th, $Q_2$ = 50th (median), $Q_3$ = 75th percentile.

- **Range** = max − min: quick, but ruined by one outlier.
- **Interquartile range** IQR = $Q_3 - Q_1$: the spread of the middle 50%, not affected by outliers.

```python
data = np.array([3, 7, 8, 10, 13, 15, 21, 40])
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
print(q1, q3, q3 - q1)
print(np.max(data) - np.min(data))
```

```text
7.75 16.5 8.75
37
```

## 3. Spread: variance and standard deviation

Deviations from the mean always cancel out (they sum to 0), so square them first.

- **Variance** = mean of squared deviations: $\frac1N\sum (x_i - \bar x)^2$ (`np.var`).
- **Standard deviation** SD = $\sqrt{\text{variance}}$ (`np.std`), back in the data's units: "how far a typical value
  is from the mean".

```python
loads = np.array([5, 6, 6, 12])
print(loads - np.mean(loads))                  # deviations
print(np.var(loads), round(np.std(loads), 4))
```

```text
[-2.25 -1.25 -1.25  4.75]
7.6875 2.7726
```

**NumPy and pandas don't agree by default.** `np.std` divides by $N$; pandas' `.std()` and `.describe()` divide by
$N-1$ (the *sample* SD), so pandas gives a slightly bigger number.

```python
import pandas as pd

s = pd.Series([5, 6, 6, 12])
print(round(np.std(s), 4), round(s.std(), 4), round(np.std(s, ddof=1), 4))
```

```text
2.7726 3.2016 3.2016
```

## 4. Shape: symmetric or skewed

- **Symmetric**: mean ≈ median (a bell curve).
- **Right-skewed** (long tail to the right, e.g. failure times, delays, salaries): mean **>** median.
- **Left-skewed** (long tail to the left): mean **<** median.

pandas' `df.skew()` gives the **skew factor** $s$. Rule of thumb: $|s| < 0.5$ roughly symmetric, $0.5$–$1$ moderately
skewed, $> 1$ highly skewed; positive = right, negative = left.

`describe()` gives most of this in one call (`std` is the $N-1$ version; `50%` is the median).
The file `pump_failures.csv` is **made-up practice data**: hours until each of 80 pumps failed.

```python
pumps = pd.read_csv("pump_failures.csv")
print(pumps["Hours"].describe().round(1))
print("skew:", round(pumps["Hours"].skew(), 2))
```

```text
count      80.0
mean      995.1
std       778.0
min        40.0
25%       487.2
50%       815.0
75%      1397.0
max      3449.0
Name: Hours, dtype: float64
skew: 1.23
```
