import numpy as np

np.random.seed(1330)            # keep this so your output matches
people = np.arange(1, 13)
shuffled = people               # TODO: shuffle people with np.random.permutation
treatment = shuffled[:6]
control = shuffled             # TODO: the other 6
print("treatment:", sorted(treatment))
print("control:", sorted(control))
