## Why it matters

Usually you have **one** sample and no way to go back to the population for more. How far off might your sample's
median or mean be? The **bootstrap** answers this with nothing but the sample and a loop, and it is exactly how
ENGR 1330 builds confidence intervals in the next lesson.

## 1. Percentiles

The $p$th percentile is the value with about $p\%$ of the collection at or below it.
`np.percentile(collection, p)` computes it (interpolating between sorted values).

```python
import numpy as np

scores = np.array([12, 3, 18, 7, 9, 15, 5])
print(np.percentile(scores, 50), np.percentile(scores, 80))
```

```text
9.0 14.400000000000002
```

If your test score is at the 95th percentile, only about 5% of scores are higher.

## 2. Parameter, statistic, sampling distribution

- **Parameter**: a number about the **population** (the median commute of all students). Usually unknown.
- **Statistic**: the same kind of number computed from a **sample**. It estimates the parameter.
- **Sampling distribution**: how the statistic varies across different random samples.

## 3. The bootstrap

You can't draw new samples from the population, so you draw them from your sample:

1. Treat the original sample **as if it were the population**.
2. Draw a **resample** of the **same size**, at random **with replacement**.
3. Compute the statistic on the resample. Repeat many times (ENGR 1330 uses **10,000**).
4. The spread of those values estimates how much the statistic varies from sample to sample.

**Why with replacement?** Drawing all $n$ rows **without** replacement just gives back the original sample in a
different order, so every resample would have the same median. With replacement, some rows appear twice and
others not at all, mimicking a new random sample.

`commute_times.csv` is **made-up practice data**: a random sample of 300 students' commute times in minutes.

```python
import pandas as pd

sample = pd.read_csv("commute_times.csv")
print(len(sample), "students, sample median:", sample["Minutes"].median())

np.random.seed(1)
one = sample.sample(len(sample), replace=True)        # one bootstrap resample
print("resample median:", one["Minutes"].median())
print("distinct students in the resample:", one["Student"].nunique())
```

```text
300 students, sample median: 19.95
resample median: 20.4
distinct students in the resample: 195
```

About 63% of the original rows show up in a typical resample; the rest of its 300 rows are repeats. Now repeat:

```python
np.random.seed(2)
bootstraps = []
for i in range(10000):
    resample = sample.sample(len(sample), replace=True)
    bootstraps.append(resample["Minutes"].median())
bootstraps = np.array(bootstraps)
print(len(bootstraps))
print("middle 95% of the bootstrap medians:",
      np.percentile(bootstraps, 2.5), "to", np.percentile(bootstraps, 97.5))
```

```text
10000
middle 95% of the bootstrap medians: 18.4 to 21.3
```

`plt.hist(bootstraps)` draws the **bootstrap distribution** of the median. Its middle 95% is the range of plausible
values for the population median: that range is next lesson's confidence interval.

## 4. When the bootstrap works

- The original sample must be a **large, random** sample: the bootstrap can't fix a biased or tiny sample.
- Use **many** resamples (10,000) so the bootstrap distribution is smooth and stable.
- In the course demo (San Francisco salaries), about 95 out of 100 such middle-95% ranges contained the true
  population median.
