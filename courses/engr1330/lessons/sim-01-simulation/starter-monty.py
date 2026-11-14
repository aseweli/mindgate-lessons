import numpy as np

np.random.seed(1330)            # keep this so your numbers match
hidden = np.array(['car', 'first goat', 'second goat'])
goats = np.array(['first goat', 'second goat'])

def other_goat(x):
    if x == 'first goat':
        return 'second goat'
    return 'first goat'

def monty_hall_game():
    guess = np.random.choice(hidden)
    if guess == 'car':
        revealed = np.random.choice(goats)
        return [guess, revealed, other_goat(revealed)]
    # TODO: the guess is a goat: Monty reveals the other goat, and the car remains
    return [guess, guess, guess]

stay = 0
switch = 0
for i in np.arange(10000):
    guess, revealed, remaining = monty_hall_game()
    if guess == 'car':
        stay = stay + 1
    # TODO: add 1 to switch when the remaining door has the car

print("stay:", stay / 10000)
print("switch:", switch / 10000)
