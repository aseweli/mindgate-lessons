import numpy as np
import pandas as pd

h = pd.read_csv("pump_failures.csv")["Hours"]

mean = h.mean()
median = 0          # TODO: median of h
sd_numpy = 0        # TODO: np.std(h)
sd_pandas = 0       # TODO: h.std()
rng = 0             # TODO: max minus min
iqr = 0             # TODO: 75th percentile minus 25th percentile (np.percentile)

print("mean", round(mean, 1))
print("median", round(median, 1))
print("SD numpy", round(sd_numpy, 1))
print("SD pandas", round(sd_pandas, 1))
print("range", round(rng, 1))
print("IQR", round(iqr, 1))
