## Why it matters

Everything in Exam 3 rests on chance. A random sample, a bootstrap resample and a confidence interval are all
built from random draws, and probability is the language that says how likely each outcome is. In ENGR 1330 you
compute probabilities two ways: **by reasoning** (a formula) and **by simulation** (NumPy draws thousands of
random outcomes and you count). The two answers should agree.

## 1. Probabilities live between 0 and 1

A probability is a number from 0 (impossible) to 1 (certain), often written as a percent: 0.6 = 60%.
If outcomes are **equally likely** (a fair die, a well-shuffled box of tickets):

$$P(\text{event}) = \frac{\text{number of outcomes that make the event happen}}{\text{number of all possible outcomes}}$$

For one roll of a die: $P(\text{even}) = \#\{2,4,6\}/\#\{1,\dots,6\} = 3/6$.

```python
p_even = 3 / 6
p_multiple_of_3 = 2 / 6      # {3, 6}
print(p_even, round(p_multiple_of_3, 4))
```

```text
0.5 0.3333
```

## 2. The complement: "does not happen"

$$P(\text{not } A) = 1 - P(A)$$

If a weld passes inspection with chance 0.92, it fails with chance $1 - 0.92 = 0.08$.

```python
p_pass = 0.92
p_fail = 1 - p_pass
print(round(p_fail, 2))
```

```text
0.08
```

## 3. Multiplication rule: A **and** B

$$P(A \text{ and } B) = P(A) \times P(B \text{ given that } A \text{ happened})$$

A box holds four tickets: red, blue, green, yellow. Draw two **without replacement**.
$P(\text{green first}) = 1/4$. Once green is out, three tickets remain, so $P(\text{red second} \mid \text{green first}) = 1/3$:

$$P(\text{green, then red}) = \tfrac14 \times \tfrac13 = \tfrac{1}{12}$$

Multiplying by numbers $\le 1$ can only shrink the result: **every extra condition makes the event less likely.**

## 4. Addition rule: one of several ways

If an event can happen in exactly one of two ways (they can't both happen),

$$P(\text{event}) = P(\text{first way}) + P(\text{second way})$$

"One green and one red, in any order" happens as green-then-red **or** red-then-green:

$$P = \tfrac{1}{12} + \tfrac{1}{12} = \tfrac{2}{12} = \tfrac16$$

More ways to succeed make the event **more** likely.

## 5. "At least one": use the complement

"At least one six in 4 rolls" has many ways to happen (one six, two sixes, ...). Its complement has only one:
**no sixes at all**. Each roll misses a six with chance $5/6$, and the rolls don't affect each other, so

$$P(\text{at least one six in } n \text{ rolls}) = 1 - \left(\tfrac56\right)^n$$

```python
for n in [1, 2, 4, 10, 20]:
    p = 1 - (5/6)**n
    print(n, round(p, 3))
```

```text
1 0.167
2 0.306
4 0.518
10 0.838
20 0.974
```

As $n$ grows the chance climbs toward 1: with enough tries, even an unlikely event becomes almost certain.

## 6. Checking a probability by simulation

`np.random.choice(values, size)` picks `size` items **at random with replacement**, each equally likely.
Compare an array with a value to get True/False, and `np.count_nonzero` counts the Trues. The fraction of
trials where the event happened estimates its probability.

```python
import numpy as np

np.random.seed(1330)                       # same random numbers every run
die = np.arange(1, 7)                      # faces 1..6
rolls = np.random.choice(die, 10000)       # 10,000 rolls
print(np.count_nonzero(rolls == 6) / 10000)
print(round(1/6, 4))
```

```text
0.1687
0.1667
```

The simulated fraction is close to the exact $1/6 \approx 0.1667$ but not equal. Run it with a different seed and
the estimate changes a little; more repetitions make it steadier.

To draw **without replacement** (like pulling tickets out of a box), pass `replace=False`:

```python
import numpy as np

np.random.seed(7)
tickets = np.array(['red', 'blue', 'green', 'yellow'])
print(np.random.choice(tickets, 2, replace=False))
```

```text
['green' 'blue']
```
