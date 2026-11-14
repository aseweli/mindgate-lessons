## Why it matters

Once you know two variables are linearly associated, the **regression line** turns that into predictions,
including for x values you never observed. It's the simplest machine-learning model and the foundation of
multiple regression.

`heights.csv` is **made-up practice data**: midparent height (average of the parents, inches) and an adult child's
height for 300 families.

## 1. In standard units the slope is r

If x is 1 SD above average, the regression line predicts y to be **r** SDs above average:
$\hat y_{su} = r \cdot x_{su}$. With $r < 1$ the prediction is less extreme than x ("regression toward the mean").

## 2. In original units

$$\text{slope} = r\,\frac{SD_y}{SD_x} \qquad \text{intercept} = \bar y - \text{slope}\cdot\bar x \qquad \hat y = \text{slope}\cdot x + \text{intercept}$$

```python
import numpy as np
import pandas as pd

h = pd.read_csv("heights.csv")
x, y = h["Midparent"], h["Child"]
r = np.corrcoef(x, y)[0, 1]
slope = r * np.std(y) / np.std(x)
intercept = np.mean(y) - slope * np.mean(x)
print(round(r, 3), round(slope, 3), round(intercept, 2))
print("predicted child height for a 72-inch midparent:", round(slope * 72 + intercept, 2))
```

```text
0.254 0.501 33.0
predicted child height for a 72-inch midparent: 69.11
```

## 3. Residuals and RMSE

A **residual** is actual − predicted. Positive: the line under-predicted; negative: it over-predicted.
Summarize all residuals with the **mean squared error** and its square root, the **root mean squared error**:

$$MSE = \text{mean of residual}^2 \qquad RMSE = \sqrt{MSE}$$

```python
predicted = slope * x + intercept
residuals = y - predicted
mse = np.mean(residuals ** 2)
print(round(mse, 3), round(np.sqrt(mse), 3))
```

```text
11.842 3.441
```

RMSE is in the units of y: a typical prediction is off by about that many inches.

## 4. Why this line? Least squares

Try any other line and its RMSE is bigger. The regression line is the **unique line with the smallest RMSE**
(the **least-squares line**).

```python
def rmse(a, b):
    return np.sqrt(np.mean((y - (a * x + b)) ** 2))

print(round(rmse(slope, intercept), 3))
print(round(rmse(1.0, 0.0), 3))
print(round(rmse(0.5, 32.0), 3))
```

```text
3.441
3.814
3.615
```
