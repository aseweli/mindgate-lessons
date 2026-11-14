import numpy as np
import pandas as pd

t = pd.read_csv("trees.csv")
np.random.seed(1330)                 # keep this so your numbers match

def slope_of(df):
    r = np.corrcoef(df["Diameter"], df["Age"])[0, 1]
    return 0                         # TODO: r * SD of Age / SD of Diameter

slopes = []
for i in range(2000):
    resample = t                     # TODO: resample rows, same size, with replacement
    slopes.append(slope_of(resample))

left = np.percentile(slopes, 2.5)
right = np.percentile(slopes, 97.5)
print("95% CI:", round(left, 3), round(right, 3))
print("contains 0:", left <= 0 <= right)
