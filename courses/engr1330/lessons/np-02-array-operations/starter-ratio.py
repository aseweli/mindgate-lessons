import numpy as np

np.random.seed(1330)                  # keep this so your numbers match
ratios = []
for trial in range(5):
    arr = np.sort(np.random.randint(5, 106, 25))
    evens = 0                         # TODO: number of even values (use a mask)
    odds = 1                          # TODO: number of odd values
    ratios.append(evens / odds)
ratios = np.array(ratios)
print(np.round(ratios, 2))
print(round(np.mean(ratios), 3))
