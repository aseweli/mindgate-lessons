## Why it matters

You almost never get to measure a whole **population** (every bus arrival, every chip, every student). You take a
**sample** and use it to say something about the population. How the sample is chosen decides whether that is
trustworthy, and comparing samples to each other is the idea behind the bootstrap and confidence intervals later
in this unit block.

The examples use `bus_delays.csv`, a **made-up practice dataset** of 2,000 campus bus arrivals with the delay in
minutes (negative = early).

```python
import pandas as pd

df = pd.read_csv("bus_delays.csv")
print(df.shape)
print(df.head(3))
```

```text
(2000, 3)
   Bus  Route  Delay
0    1    Red     -2
1    2    Red      2
2    3  Green      2
```

## 1. Deterministic samples: no chance involved

If you simply say which rows you want, the sample is **deterministic**: running the code again gives the same rows.
Selecting by position or by a condition are both deterministic.

```python
first_five = df.iloc[0:5]                 # rows by position
red = df.loc[df["Route"] == "Red"]        # rows by a condition
print(len(first_five), len(red))
```

```text
5 687
```

## 2. Probability samples and random samples

A **probability sample** is one where, before drawing, you can compute the chance that any group of elements ends
up in the sample. The chances don't have to be equal. Example: choose 2 of A, B, C by always taking A and then
flipping a coin between B and C. The sample $\{A, B\}$ has chance 1/2, $\{A, C\}$ has 1/2, $\{B, C\}$ has 0.

A **random sample** is drawn with chance at every step:

- **with replacement**: a drawn row goes back and can be drawn again;
- **without replacement**: each row can appear at most once.

In pandas, `df.sample(n)` is **without** replacement by default; `df.sample(n, replace=True)` is with replacement.

```python
import numpy as np

np.random.seed(4)
s = df.sample(5)                          # without replacement
print(s["Bus"].tolist())
t = df.sample(5, replace=True)            # with replacement
print(len(t))
```

```text
[1894, 899, 1579, 560, 89]
5
```

## 3. Probability distribution vs empirical distribution

The **probability distribution** of a die gives each face chance 1/6. An **empirical distribution** is what you
actually observe: the proportions in the data you collected. Roll 10 times and the proportions are bumpy; roll
10,000 times and they settle near 1/6.

**Law of averages:** if a chance experiment is repeated independently under the same conditions, the proportion of
times an event happens gets closer and closer to its theoretical probability.

The same holds for sampling from a population: the histogram of a **large** random sample closely resembles the
histogram of the population; a small sample's histogram can look quite different.

```python
np.random.seed(11)
for n in [10, 100, 1000]:
    sample = df["Delay"].sample(n, replace=True)
    share_late = np.count_nonzero(sample > 10) / n
    print(n, round(share_late, 3))
print("population:", round(np.count_nonzero(df["Delay"] > 10) / len(df), 3))
```

```text
10 0.2
100 0.19
1000 0.201
population: 0.192
```

## 4. The empirical distribution of a statistic

A **statistic** is a number computed from a sample, such as the sample median. Different random samples give
different values. Repeat "take a sample, compute the median" many times and collect the results: that collection
is the **empirical distribution of the statistic**, and it shows how much the estimate can vary.

```python
np.random.seed(21)
medians = []
for i in range(1000):
    m = df["Delay"].sample(200, replace=True).median()
    medians.append(m)
medians = np.array(medians)
print("population median:", df["Delay"].median())
print("sample medians range from", medians.min(), "to", medians.max())
```

```text
population median: 2.0
sample medians range from 0.0 to 4.0
```

The sample medians cluster around the population median, so a single large random sample gives a sensible estimate
of it. `plt.hist(medians)` would draw that empirical distribution.
