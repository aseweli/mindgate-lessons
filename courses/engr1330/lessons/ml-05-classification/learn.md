## Why it matters

Classification predicts a **category**: will this machine fail (1) or not (0)? Your class notebook compared
logistic regression, a decision tree and a random forest on a predictive-maintenance dataset. Whatever the model,
you judge it with the same few numbers, and picking the wrong one can make a useless model look great.

`failures.csv` is **made-up practice data**: for 400 machines, whether each actually failed and what a model predicted.

## 1. The confusion matrix

| | Predicted 0 | Predicted 1 |
| --- | --- | --- |
| **Actual 0** | TN (true negative) | FP (false positive) |
| **Actual 1** | FN (false negative) | TP (true positive) |

```python
import numpy as np
import pandas as pd

df = pd.read_csv("failures.csv")
a, p = df["Actual"], df["Predicted"]
TP = np.count_nonzero((a == 1) & (p == 1))
TN = np.count_nonzero((a == 0) & (p == 0))
FP = np.count_nonzero((a == 0) & (p == 1))
FN = np.count_nonzero((a == 1) & (p == 0))
print("TP", TP, "TN", TN, "FP", FP, "FN", FN)
```

```text
TP 21 TN 364 FP 7 FN 8
```

## 2. The four metrics

- **Accuracy** = (TP + TN) / all: fraction of predictions that are right.
- **Precision** = TP / (TP + FP): of the machines flagged as failing, how many really failed.
- **Recall** = TP / (TP + FN): of the machines that really failed, how many were caught.
- **F1** = 2·precision·recall / (precision + recall): one number balancing the two.

```python
accuracy = (TP + TN) / len(df)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * precision * recall / (precision + recall)
print(round(accuracy, 3), round(precision, 3), round(recall, 3), round(f1, 3))
```

```text
0.962 0.75 0.724 0.737
```

## 3. Why accuracy can mislead

Failures are rare here. A "model" that always predicts **no failure** is right for every working machine:

```python
lazy = np.zeros(len(df))
print("accuracy of always-0:", round(np.mean(lazy == a), 3))
print("its recall:", np.count_nonzero((a == 1) & (lazy == 1)) / np.count_nonzero(a == 1))
```

```text
accuracy of always-0: 0.928
its recall: 0.0
```

High accuracy, zero recall: it never catches a failure. With rare classes, look at precision, recall and F1.

## 4. With scikit-learn

The class notebook trains models and scores them like this (scikit-learn required):

```py
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

forest = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)
pred = forest.predict(X_test)
print(accuracy_score(y_test, pred), precision_score(y_test, pred), recall_score(y_test, pred), f1_score(y_test, pred))
```
