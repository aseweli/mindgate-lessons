import numpy as np
import pandas as pd

fuel = pd.read_csv("fuel_test.csv")
fuel["Drop"] = 0                      # TODO: Before minus After
np.random.seed(1330)                  # keep this so your numbers match

boots = []
for i in range(5000):
    resample = fuel.sample(len(fuel), replace=True)
    boots.append(resample["Drop"].mean())
boots = np.array(boots)

left = 0                              # TODO: 2.5th percentile of boots
right = 0                             # TODO: 97.5th percentile of boots
print("95% CI:", round(left, 2), "to", round(right, 2))

# TODO: print "reject the null" if 0 is outside [left, right], else "do not reject the null"
