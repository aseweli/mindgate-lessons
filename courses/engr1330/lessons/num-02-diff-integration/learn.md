## Why it matters

Measured data (positions every 0.1 s, temperatures every minute) have no formula to differentiate or integrate.
Finite differences and the trapezoid rule work directly on the numbers.

## 1. Finite differences

With step $h$:

- **Forward**: $f'(x) \approx \frac{f(x+h) - f(x)}{h}$
- **Backward**: $f'(x) \approx \frac{f(x) - f(x-h)}{h}$
- **Central**: $f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$ (usually far more accurate)

```python
f = lambda x: x**3
x, true = 3, 27                # f'(x) = 3x^2 = 27
for h in [0.1, 0.01]:
    fwd = (f(x + h) - f(x)) / h
    bwd = (f(x) - f(x - h)) / h
    cen = (f(x + h) - f(x - h)) / (2 * h)
    print(h, round(fwd, 4), round(bwd, 4), round(cen, 4))
    print("   errors %:", round(abs(fwd - true) / true * 100, 2), round(abs(bwd - true) / true * 100, 2), round(abs(cen - true) / true * 100, 4))
```

```text
0.1 27.91 26.11 27.01
   errors %: 3.37 3.3 0.037
0.01 27.0901 26.9101 27.0001
   errors %: 0.33 0.33 0.0004
```

Making $h$ ten times smaller cuts the forward/backward error about 10× but the central error about 100×.

On arrays, `np.diff(y) / h` gives forward differences (one fewer value) and `np.gradient(y, h)` mixes forward,
central and backward to keep the same length.

```python
import numpy as np

xs = np.arange(0, 1.01, 0.25)
ys = xs ** 2
print(np.diff(ys) / 0.25)
print(np.gradient(ys, 0.25))
```

```text
[0.25 0.75 1.25 1.75]
[0.25 0.5  1.   1.5  1.75]
```

## 2. The trapezoid rule

Split $[a, b]$ into $n$ strips of width $h = (b-a)/n$ and add trapezoid areas:

$$\int_a^b f\,dx \approx \frac h2\Big(f(x_0) + 2f(x_1) + \dots + 2f(x_{n-1}) + f(x_n)\Big)$$

```python
f = lambda x: x**2
a, b, n = 0, 3, 6
h = (b - a) / n
x = np.linspace(a, b, n + 1)
y = f(x)
I = h / 2 * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
print(I, "exact:", 3**3 / 3)
print(np.trapezoid(y, x))          # NumPy's version (np.trapz in older NumPy)
```

```text
9.125 exact: 9.0
9.125
```

More strips (smaller $h$) → closer to the exact value 9. The trapezoid rule is exact for straight lines.
