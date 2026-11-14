import numpy as np

A = np.array([[1, 1], [0, 0]])        # TODO: second row holds the acid fractions 0.30 and 0.75
B = np.array([18, 0])                 # TODO: total acid = 0.45 * 18
x, y = np.linalg.solve(A + np.eye(2) * 1e-9, B)
print("30% solution:", round(x, 2), "oz")
print("75% solution:", round(y, 2), "oz")
