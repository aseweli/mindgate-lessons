import numpy as np

np.random.seed(1330)              # keep this line so your numbers match
n = int(input("Rolls per trial: "))
die = np.arange(1, 7)
trials = 10000
hits = 0

for i in np.arange(trials):
    rolls = np.random.choice(die, n)
    # TODO: if this trial contains at least one 6, add 1 to hits
    #       (hint: np.count_nonzero(rolls == 6) counts the sixes)

simulated = hits / trials
exact = 0                         # TODO: replace 0 with the exact formula 1 - (5/6)**n

print()
print("Simulated:", round(simulated, 4))
print("Exact:    ", round(exact, 4))
