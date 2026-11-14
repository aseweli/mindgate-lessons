import numpy as np
import pandas as pd

df = pd.read_csv("bus_delays.csv")
np.random.seed(1330)          # keep this so your numbers match

for n in [20, 200, 2000]:
    sample = df["Delay"]      # TODO: replace with a random sample of n delays, with replacement
    share = 0                 # TODO: proportion of the sample that is > 10
    print(n, round(share, 3))

pop = 0                       # TODO: same proportion for the whole column
print("population", round(pop, 3))
