import numpy as np

f = lambda x: np.exp(x)
x, true = 1, np.e
for h in [0.1, 0.01, 0.001]:
    fwd = (f(x + h) - f(x)) / h
    cen = 0                       # TODO: central difference
    e_fwd = abs(fwd - true) / true * 100
    e_cen = 0                     # TODO: central error in percent
    print(h, round(e_fwd, 5), round(e_cen, 5))
