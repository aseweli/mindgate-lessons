## Why it matters

Real outcomes depend on more than one thing: a house price depends on the area's income, the age of the houses and
the population. **Multiple linear regression** uses several features at once, and building it by hand shows the
pieces every machine-learning model has: data split, a model, a cost, an optimizer and an evaluation.

## 1. What is machine learning?

A program **learns** from experience E with respect to a task T and performance measure P if its performance on T,
measured by P, improves with E. (Spam filter: T = classify emails, E = watching you label emails, P = fraction
classified correctly.)

- **Supervised learning**: labeled input–output pairs. **Regression** predicts a number (price); **classification**
  predicts a category (fail / no fail).
- **Unsupervised learning**: no labels; find structure (clustering, PCA).
- **Reinforcement learning**: an agent learns by trial and error from feedback (Q-learning).

`housing.csv` is **made-up practice data**: area income, average house age, population and price for 600 areas.

## 2. Features in standard units

**Feature scaling** puts every feature in standard units (mean 0, SD 1) so that income (tens of thousands) doesn't
swamp house age (single digits). It makes gradient descent converge much faster.

```python
import numpy as np
import pandas as pd

data = pd.read_csv("housing.csv")
features = ["Income", "HouseAge", "Population"]
for f in features:
    data[f + "_su"] = (data[f] - np.mean(data[f])) / np.std(data[f])
print(data[[f + "_su" for f in features]].describe().round(2).loc[["mean", "std"]])
```

```text
      Income_su  HouseAge_su  Population_su
mean        0.0          0.0            0.0
std         1.0          1.0            1.0
```

## 3. Training and test sets

Shuffle the rows, use about **2/3 for training** (fit the model) and **1/3 for testing** (evaluate on data the model
has never seen).

```python
np.random.seed(1330)
shuffled = data.sample(len(data), replace=False)
train = shuffled.iloc[0:400]
test = shuffled.iloc[400:]
print(len(train), len(test))
```

```text
400 200
```

## 4. The model (hypothesis function), vectorized

$$h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 = \theta^T x$$

Stack a **row of ones** on top of the features so $\theta_0$ is handled like the others. With features as rows:
`X` has shape (4, m), `theta` has shape (4, 1), and `theta.T @ X` gives all m predictions at once.

```python
su = [f + "_su" for f in features]
X_train = np.vstack((np.ones((1, len(train))), train[su].values.T))
y_train = train["Price"].values.reshape(-1, 1)
X_test = np.vstack((np.ones((1, len(test))), test[su].values.T))
y_test = test["Price"].values.reshape(-1, 1)
print(X_train.shape, y_train.shape)
```

```text
(4, 400) (400, 1)
```

## 5. Cost function and gradient descent

The **cost** measures how wrong the predictions are: $J(\theta) = \frac{1}{2m}\sum (h_\theta(x) - y)^2$.
**Gradient descent** starts at $\theta = 0$ and repeatedly steps downhill, updating **all** θ's at the same time:

$$\theta := \theta - \alpha \cdot \frac1m X (h - y)$$

$\alpha$ is the learning rate (step size).

```python
theta = np.zeros((4, 1))
alpha = 0.05
m_train = y_train.shape[0]
costs = []
for i in range(2000):
    h = (theta.T @ X_train).T                      # predictions, shape (m, 1)
    costs.append(np.sum((h - y_train) ** 2) / (2 * m_train))
    theta = theta - alpha * (X_train @ (h - y_train)) / m_train
print(np.round(theta.ravel()))
print("cost went from", f"{costs[0]:.3e}", "to", f"{costs[-1]:.3e}")
```

```text
[380545. 212895. 173493. 142582.]
cost went from 1.310e+11 to 4.864e+09
```

## 6. Evaluate with RMSE on both sets

```python
def rmse(X, y):
    return np.sqrt(np.mean(((theta.T @ X).T - y) ** 2))

print("train RMSE:", round(rmse(X_train, y_train)))
print("test RMSE: ", round(rmse(X_test, y_test)))
```

```text
train RMSE: 98626
test RMSE:  98734
```

Similar train and test RMSE means the model generalizes; a much larger test RMSE would mean it memorized the
training data.

## 7. The same model with scikit-learn

In class you also fit it in a few lines with scikit-learn (install it if your Mac doesn't have it):

```py
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = StandardScaler().fit_transform(data[features])
x_train, x_test, y_train, y_test = train_test_split(x, data["Price"], test_size=1/3)
lm = LinearRegression().fit(x_train, y_train)
print(lm.intercept_, lm.coef_)
```
