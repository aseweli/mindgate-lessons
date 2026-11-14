import numpy as np
import pandas as pd

h = pd.read_csv("heights.csv")
x, y = h["Midparent"], h["Child"]

r = np.corrcoef(x, y)[0, 1]
slope = 0              # TODO: r * SD of y / SD of x  (use np.std)
intercept = 0          # TODO: mean of y - slope * mean of x
pred66 = 0             # TODO: prediction for x = 66
rmse = 0               # TODO: sqrt of the mean of (y - (slope*x + intercept))**2

print("slope", round(slope, 3))
print("intercept", round(intercept, 3))
print("prediction at 66", round(pred66, 3))
print("RMSE", round(rmse, 3))
