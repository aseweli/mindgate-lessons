import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1330)                        # keep this so your counts match
lengths = np.random.normal(50.0, 0.2, 500)
bins = [49.4, 50.6]                         # TODO: use np.arange(49.4, 50.61, 0.2)
counts, edges, bars = plt.hist(lengths, bins=bins, ec="black")
# TODO: x label with units, y label "Count", and a title
plt.show()
print(counts.astype(int))
