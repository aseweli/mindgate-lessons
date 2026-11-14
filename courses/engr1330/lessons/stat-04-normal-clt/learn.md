## Why it matters

The bell curve shows up whenever you **average** many random things, even when the things themselves are lopsided.
That fact, the central limit theorem, is why sample means are such good estimates and why confidence intervals
work. It also tells you exactly how much a bigger sample helps.

## 1. The normal (Gaussian) distribution

A normal distribution is symmetric and bell-shaped, described by its **mean** (center) and **SD** (spread). The SD
is the distance from the mean to the point where the curve changes from bending down to bending up (the inflection
point). `np.random.normal(mean, sd, size)` draws values from one.

```python
import numpy as np

np.random.seed(1330)
sleep = np.random.normal(7, 1.5, 10000)      # hours of sleep for 10,000 students
print(round(np.mean(sleep), 2), round(np.std(sleep), 2))
```

```text
6.99 1.5
```

## 2. The 68–95–99.7 rule

For a normal distribution, about **68%** of values lie within 1 SD of the mean, about **95%** within 2 SD, and
about **99.7%** within 3 SD.

```python
m, s = np.mean(sleep), np.std(sleep)
for k in [1, 2, 3]:
    inside = np.count_nonzero(np.abs(sleep - m) <= k * s) / len(sleep)
    print(k, "SD:", round(inside, 3))
```

```text
1 SD: 0.683
2 SD: 0.954
3 SD: 0.997
```

So with mean 7 h and SD 1.5 h, about 95% of students sleep between $7 - 3 = 4$ and $7 + 3 = 10$ hours.

**Standard units** (z-scores) say how many SDs a value is from the mean: $z = \frac{x - \text{mean}}{SD}$.
A value of 10 hours is $z = (10-7)/1.5 = 2$.

## 3. The central limit theorem (CLT)

> The distribution of the **means of large random samples** is roughly normal, **whatever the shape of the
> population** they are drawn from.

Below, the population of repair times is strongly right-skewed. Yet the 5,000 sample means (each from 400 times)
are symmetric around the population mean.

```python
np.random.seed(5)
population = np.random.exponential(20, 50000)        # right-skewed population
means = []
for i in range(5000):
    sample = np.random.choice(population, 400)
    means.append(np.mean(sample))
means = np.array(means)
print("population mean:", round(np.mean(population), 2))
print("mean of sample means:", round(np.mean(means), 2))
print("median of sample means:", round(np.median(means), 2))
```

```text
population mean: 20.02
mean of sample means: 20.01
median of sample means: 19.99
```

Mean ≈ median for the sample means: the skew is gone. `plt.hist(means)` shows a bell.

## 4. How spread out are the sample means?

$$SD \text{ of all possible sample means} = \frac{\text{population SD}}{\sqrt{\text{sample size}}}$$

This is the **square-root law**: multiply the sample size by $K$ and the SD of the sample means shrinks by a factor
$\sqrt K$. Four times the data → half the spread; nine times → one third.

```python
pop_sd = np.std(population)
for n in [100, 400, 900]:
    sim = [np.mean(np.random.choice(population, n)) for i in range(3000)]
    print(n, round(np.std(sim), 2), round(pop_sd / np.sqrt(n), 2))
```

```text
100 2.0 1.99
400 1.0 1.0
900 0.66 0.66
```

The simulated SDs (middle column) match $\text{pop SD}/\sqrt n$ (right column). Bigger samples give narrower,
taller bell curves: the estimate is more precise. The same is true for **sample proportions**: the proportion of
purple flowers in samples of 800 plants varies less than in samples of 200.
