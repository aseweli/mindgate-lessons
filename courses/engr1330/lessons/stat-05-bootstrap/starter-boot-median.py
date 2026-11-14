import numpy as np
import pandas as pd

sample = pd.read_csv("commute_times.csv")
np.random.seed(1330)                  # keep this so your numbers match

boots = []
for i in range(2000):
    resample = sample                 # TODO: a resample of the same size, WITH replacement
    boots.append(resample["Minutes"].median())
boots = np.array(boots)

print("sample median:", sample["Minutes"].median())
print("resamples:", len(boots))
print("smallest:", boots.min())       # all equal until the TODO is done!
print("largest:", boots.max())
