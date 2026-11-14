## Why it matters

Some chance questions are hard to work out on paper but easy to **simulate**: let the computer play the game
thousands of times and count. Simulation is the engine behind everything in Units 11–13 (sampling, the bootstrap,
confidence intervals).

## 1. Random choices

`np.random.choice(array)` picks one item uniformly at random; `np.random.choice(array, n)` picks `n` items **with
replacement**. Unlike the other functions you know, it doesn't give the same result every time (unless you fix the
seed with `np.random.seed`).

```python
import numpy as np

np.random.seed(1330)
groups = np.array(['treatment', 'control'])
print(np.random.choice(groups))
print(np.random.choice(groups, 5))
die = np.arange(1, 7)
print(np.random.choice(die, 10))
```

```text
control
['control' 'treatment' 'control' 'control' 'control']
[1 2 6 5 2 6 6 1 3 2]
```

## 2. A function for one play

A dice bet: 1 or 2 spots → lose 1 dollar; 3 or 4 → nothing; 5 or 6 → win 1 dollar.

```python
def bet_on_one_roll():
    x = np.random.choice(np.arange(1, 7))
    if x <= 2:
        return -1
    elif x <= 4:
        return 0
    else:
        return 1

print(bet_on_one_roll())
```

```text
0
```

## 3. Iteration: repeat and collect

To repeat something `n` times, loop over `np.arange(n)`. Collect results in an array with `np.append`, which
returns a **new** array (so assign it back).

```python
outcomes = np.array([])
for i in np.arange(300):
    outcomes = np.append(outcomes, bet_on_one_roll())

print(len(outcomes))
print("losses:", np.count_nonzero(outcomes == -1))
print("ties:  ", np.count_nonzero(outcomes == 0))
print("wins:  ", np.count_nonzero(outcomes == 1))
print("net gain:", sum(outcomes))
```

```text
300
losses: 89
ties:   113
wins:   98
net gain: 9.0
```

Each outcome has chance 1/3, so each count is near 100.

## 4. The simulation recipe

1. **What to simulate**: the quantity (for example, the number of heads in 100 tosses).
2. **Simulate one value**: code that produces one such number.
3. **Number of repetitions**: decide how many times (for example, 10,000).
4. **Code the simulation**: a loop that repeats step 2 and collects the results.

```python
coin = np.array(['Heads', 'Tails'])

def one_value():                                         # step 2
    tosses = np.random.choice(coin, 100)
    return np.count_nonzero(tosses == 'Heads')

heads = np.array([])
for i in np.arange(10000):                               # steps 3 and 4
    heads = np.append(heads, one_value())
print(np.min(heads), np.max(heads), round(np.mean(heads), 2))
```

```text
30.0 67.0 50.03
```

The number of heads is rarely exactly 50 but is centered there.

## 5. Monty Hall

Three doors: a car and two goats. You pick a door; the host opens a **different** door with a goat. Should you switch?

```python
import pandas as pd

goats = np.array(['first goat', 'second goat'])
hidden = np.array(['car', 'first goat', 'second goat'])

def other_goat(x):
    if x == 'first goat':
        return 'second goat'
    elif x == 'second goat':
        return 'first goat'

def monty_hall_game():
    guess = np.random.choice(hidden)
    if guess == 'car':
        revealed = np.random.choice(goats)
        return [guess, revealed, other_goat(revealed)]
    return [guess, other_goat(guess), 'car']

games = pd.DataFrame([monty_hall_game() for i in range(10000)], columns=['Guess', 'Revealed', 'Remaining'])
print("stay wins:  ", np.count_nonzero(games['Guess'] == 'car') / 10000)
print("switch wins:", np.count_nonzero(games['Remaining'] == 'car') / 10000)
```

```text
stay wins:   0.3379
switch wins: 0.6621
```

Your first guess is right 1/3 of the time; the remaining door has the car the other 2/3. **Switching doubles your chance.**
