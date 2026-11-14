import numpy as np
import pandas as pd

df = pd.read_csv("failures.csv")
a, p = df["Actual"], df["Predicted"]

TP = np.count_nonzero((a == 1) & (p == 1))
TN = 0      # TODO
FP = 0      # TODO
FN = 1      # TODO (1 so the starter runs without dividing by zero)

accuracy = (TP + TN) / len(df)
precision = TP / (TP + FP)
recall = 0  # TODO
f1 = 0      # TODO
print("TP", TP, "TN", TN, "FP", FP, "FN", FN)
print("accuracy", round(accuracy, 3))
print("precision", round(precision, 3))
print("recall", round(recall, 3))
print("F1", round(f1, 3))
