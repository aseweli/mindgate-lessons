## Why it matters

Prediction is the core of data science: use one variable to predict another. Before predicting, check whether the
two variables move together and how tightly. The **correlation coefficient** $r$ puts a single number on that, and
it is the slope of the regression line in the next lesson.

`suv_specs.csv` is **made-up practice data** on 40 SUVs: acceleration (km/h gained per second), fuel economy
(MPG) and price (dollars).

## 1. Scatter plots and association

Always plot **y (the variable to predict) against x**. If y tends to rise with x, the association is **positive**;
if it tends to fall, **negative**; if there's no trend, none.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

suv = pd.read_csv("suv_specs.csv")
plt.scatter(suv["Acceleration"], suv["Price"])
plt.xlabel("Acceleration (km/h per s)")
plt.ylabel("Price (dollars)")
plt.title("Price vs acceleration")
plt.show()
print(suv.head(3))
```

```text
    Model  Acceleration   MPG  Price
0  SUV-01         10.60  35.0  36030
1  SUV-02         12.41  25.4  35320
2  SUV-03         13.09  25.6  34660
```

## 2. Standard units and r

Put each variable in **standard units** (how many SDs from its mean), multiply the pairs, and average:

$$r = \text{mean of } \left(\frac{x - \bar x}{SD_x}\right)\left(\frac{y - \bar y}{SD_y}\right)$$

Points up-right or down-left of the center give positive products; the other two quadrants give negative products.

```python
def standard_units(v):
    return (v - np.mean(v)) / np.std(v)

x = suv["Acceleration"]
y = suv["Price"]
r = np.mean(standard_units(x) * standard_units(y))
print(round(r, 4))
print(np.corrcoef(x, y))
print(round(np.corrcoef(x, y)[0, 1], 4))
```

```text
0.8712
[[1.         0.87120082]
 [0.87120082 1.        ]]
0.8712
```

`np.corrcoef(x, y)` returns a 2×2 matrix; the off-diagonal entry `[0, 1]` is $r$. pandas: `suv[["Price", "MPG"]].corr()`.

## 3. Reading r

- $-1 \le r \le 1$. $r = 1$: perfect straight line sloping up; $r = -1$: sloping down; $r = 0$: no **linear** trend.
- $r$ has **no units** and doesn't change if you change units (dollars → thousands of dollars) or swap x and y.

```python
print(round(np.corrcoef(suv["MPG"], suv["Price"])[0, 1], 4))
print(round(np.corrcoef(suv["MPG"], suv["Price"] / 1000)[0, 1], 4))
print(round(np.corrcoef(suv["Price"], suv["MPG"])[0, 1], 4))
```

```text
-0.6664
-0.6664
-0.6664
```

## 4. What r does not tell you

- **Correlation is not causation.** A third variable (a confounder) can drive both.
- **r measures only linear association.** A perfect curve can have $r$ near 0.
- **r is sensitive to outliers.** One point can create or hide a correlation.

```python
x = np.arange(-3, 4)
y = x ** 2                     # a perfect U-shape
print(round(np.corrcoef(x, y)[0, 1], 4))
```

```text
0.0
```
