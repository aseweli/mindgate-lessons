import numpy as np

np.random.seed(1330)                       # keep this line so your numbers match
population = np.random.exponential(12, 40000)
pop_sd = np.std(population)

for n in [16, 64, 256]:
    means = []
    for i in range(2000):
        sample = population[:n]            # TODO: replace with a random sample of size n
        means.append(np.mean(sample))
    sd_sim = 0                             # TODO: SD of the list means
    sd_formula = 0                         # TODO: pop_sd divided by the square root of n
    print(n, round(sd_sim, 2), round(sd_formula, 2))
