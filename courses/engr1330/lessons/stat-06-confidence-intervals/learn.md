## Why it matters

A single number ("the mean drop is 1.7") hides how uncertain it is. A **confidence interval** gives a range of
plausible values for the unknown population parameter together with how confident you can be in the method that
produced it. It is also the simplest way to test a claim like "the true average change is 0".

## 1. From bootstrap to interval

After bootstrapping a statistic (previous lesson), take the **middle** part of the bootstrap distribution:

| Confidence level | Left end | Right end |
| --- | --- | --- |
| 80% | 10th percentile | 90th percentile |
| 90% | 5th | 95th |
| 95% | 2.5th | 97.5th |
| 99% | 0.5th | 99.5th |

For a $c\%$ interval, cut $(100 - c)/2$ percent off each end.

The examples use `fuel_test.csv`, **made-up practice data**: fuel use (L/100 km) of 24 trucks before and after a
new engine tune. The column of interest is the **drop** = Before − After.

```python
import numpy as np
import pandas as pd

fuel = pd.read_csv("fuel_test.csv")
fuel["Drop"] = fuel["Before"] - fuel["After"]
print("sample mean drop:", round(fuel["Drop"].mean(), 3))

np.random.seed(1330)
boots = []
for i in range(10000):
    resample = fuel.sample(len(fuel), replace=True)
    boots.append(resample["Drop"].mean())
boots = np.array(boots)

print("95% CI:", round(np.percentile(boots, 2.5), 2), round(np.percentile(boots, 97.5), 2))
print("80% CI:", round(np.percentile(boots, 10), 2), round(np.percentile(boots, 90), 2))
print("99% CI:", round(np.percentile(boots, 0.5), 2), round(np.percentile(boots, 99.5), 2))
```

```text
sample mean drop: 1.754
95% CI: 1.06 2.51
80% CI: 1.29 2.24
99% CI: 0.88 2.76
```

**More confidence → wider interval.** The 99% interval contains the 95% one, which contains the 80% one. To be more
sure you've caught the parameter, you cast a wider net.

## 2. What "95% confident" means (and doesn't)

Reported as: *based on this sample of 24 trucks, with 95% confidence the average drop for all such trucks is between
the two ends.*

| Statement | Right? |
| --- | --- |
| The **procedure** captures the true parameter in about 95 of every 100 samples | ✓ |
| We are 95% confident the population mean drop is in the interval | ✓ |
| 95% of the individual trucks' drops are in the interval | ✗ (it is about the **mean**, not individuals) |
| There is a 95% chance the parameter is in **this** interval | ✗ (the parameter is fixed; it is in or out) |
| 95% of bootstrap samples have their mean in the interval, so the parameter must be too | ✗ |

In the course demo, 100 intervals from 100 different samples were built and about 95 of them contained the true
population median: that is what the 95% refers to.

## 3. Using a CI to test a hypothesis

- **Null hypothesis**: the population average drop is 0 (the tune does nothing).
- **Alternative**: the population average drop is not 0.

Build a 95% CI. **If 0 is not inside it, reject the null** (using a 5% cut-off). The cut-off and the confidence
level are complementary: a 95% CI ↔ 5% cut-off, a 99% CI ↔ 1% cut-off.

```python
left, right = np.percentile(boots, 2.5), np.percentile(boots, 97.5)
if left <= 0 <= right:
    print("0 is inside the 95% CI: don't reject the null")
else:
    print("0 is outside the 95% CI: reject the null at the 5% cut-off")
```

```text
0 is outside the 95% CI: reject the null at the 5% cut-off
```

The interval is more informative than a yes/no test: it also estimates **how big** the drop is.
