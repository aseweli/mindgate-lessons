## Why it matters

Data constantly show two things moving together. Deciding whether one **causes** the other is how engineers decide
whether a new design, material or treatment actually works.

## 1. Association first, causation second

A study has **individuals**, a **treatment** (the factor of interest) and an **outcome**. Any relation between
treatment and outcome is an **association**. Deciding about **causality** needs a more careful look.

## 2. Confounding factors

A **confounding factor** (lurking variable) is an underlying difference between the groups, other than the
treatment, that affects the outcome.

- In the 1960s coffee drinkers had more lung cancer. Coffee doesn't cause it: coffee drinkers were more likely to
  **smoke**, and smoking does. Smoking confounded the comparison.
- Flu cases and school attendance rise and fall together in winter; cold weather and indoor time affect both.

## 3. Randomized controlled experiments

To establish causality, **randomly assign** individuals to a **treatment group** or a **control group**, then treat
the groups identically except for the treatment. Randomization makes the groups alike on average in **every**
other way, including confounders you didn't think of. Python makes the random assignment:

```python
import numpy as np

np.random.seed(3)
volunteers = np.array(['Ana', 'Ben', 'Cy', 'Dee', 'Eli', 'Fay'])
groups = np.random.choice(['treatment', 'control'], len(volunteers))
for name, g in zip(volunteers, groups):
    print(name, g)
```

```text
Ana treatment
Ben treatment
Cy control
Dee control
Eli treatment
Fay treatment
```

`np.random.choice` with replacement can give unequal group sizes. To split exactly in half, shuffle and cut:

```python
np.random.seed(3)
shuffled = np.random.permutation(volunteers)
print("treatment:", shuffled[:3])
print("control:  ", shuffled[3:])
```

```text
treatment: ['Dee' 'Fay' 'Eli']
control:   ['Ben' 'Ana' 'Cy']
```

Without randomization (an **observational study**), you can show association but must be very careful claiming cause.
