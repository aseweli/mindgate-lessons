## Why it matters

Many engineering equations ($x^2 = 2$, $\cos x = x$, a pipe-flow friction equation) have no neat algebraic
solution. Numerical methods **approximate a root** of $f(x) = 0$ to any accuracy you need with a simple loop.

## 1. Lambda functions

`lambda arguments: expression` makes a small one-line function, handy for passing a formula to a method.

```python
f = lambda x: x**2 - 2
print(f(1), f(1.5))
double = lambda x: x * 2
print(list(map(lambda x: x**2, [1, 2, 3, 4])))
print(sorted([3, 1, 2], key=lambda x: -x))
```

```text
-1 0.25
[1, 4, 9, 16]
[3, 2, 1]
```

$f(1) < 0$ and $f(1.5) > 0$, so a root lies between 1 and 1.5.

## 2. The iteration pattern

Keep improving a guess **while** the approximate relative error is above a tolerance $e_s$:

$$e_a = \left|\frac{x_{new} - x_{old}}{x_{new}}\right| \times 100\%$$

Start `ea = 100` so the loop runs at least once.

## 3. Bisection (bracketed method)

Needs an interval $[x_l, x_u]$ where $f$ changes sign. Repeat: midpoint $x_m = (x_l + x_u)/2$; if
$f(x_l)\,f(x_m) > 0$ the root is in the right half (set $x_l = x_m$), otherwise in the left half ($x_u = x_m$).
Always converges, but slowly: the interval halves each step.

```python
f = lambda x: x**2 - 2
xl, xu = 0, 1.5
xm = (xl + xu) / 2
es, ea, i = 0.05, 100, 0
while ea > es:
    i = i + 1
    if f(xl) * f(xm) > 0:
        xl = xm
    else:
        xu = xm
    old = xm
    xm = (xl + xu) / 2
    ea = abs((xm - old) / xm) * 100
print(i, round(xm, 5))
```

```text
11 1.41394
```

## 4. Secant (open method)

Starts from **two guesses** (they need not bracket the root) and follows the line through the last two points:

$$x_{i+1} = x_i - f(x_i)\,\frac{x_{i-1} - x_i}{f(x_{i-1}) - f(x_i)}$$

Usually much faster than bisection, but it can diverge, so cap the iterations.

```python
xim1, xi = 1, 2
es, ea, i, maxiter = 0.05, 100, 0, 100
while ea > es and i < maxiter:
    i = i + 1
    xip1 = xi - f(xi) * (xim1 - xi) / (f(xim1) - f(xi))
    ea = abs((xip1 - xi) / xip1) * 100
    xim1, xi = xi, xip1
print(i, round(xip1, 6))
```

```text
4 1.414211
```

| | Bisection | Secant |
| --- | --- | --- |
| Inputs | interval with a sign change | two starting guesses |
| Always converges? | yes | no |
| Speed | slow (halves the interval) | fast near the root |
