import numpy as np
import pandas as pd

suv = pd.read_csv("suv_specs.csv")

def standard_units(v):
    return v              # TODO: (v - mean) / SD

x = suv["MPG"]
y = suv["Price"]
r_mine = 0                # TODO: mean of the product of x and y in standard units
r_numpy = 0               # TODO: np.corrcoef(x, y)[0, 1]
print("mine:", round(r_mine, 4))
print("numpy:", round(r_numpy, 4))
