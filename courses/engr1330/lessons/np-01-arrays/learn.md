## Why it matters

NumPy arrays are the workhorse of scientific Python: up to ~50× faster than lists, no explicit loops, and code that
looks like the math. pandas, Matplotlib and scikit-learn are all built on them. A **2D array** is a matrix (a 4K
screen is a 3840 × 2160 grid of pixels).

## 1. Creating arrays

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape, b.shape, b.ndim, b.dtype)
print(np.zeros((2, 3)))
print(np.ones((2, 2)), np.eye(2))
print(np.arange(0, 2, 0.5), np.linspace(0, 100, 5))
```

```text
(3,) (2, 3) 2 int64
[[0. 0. 0.]
 [0. 0. 0.]]
[[1. 1.]
 [1. 1.]] [[1. 0.]
 [0. 1.]]
[0.  0.5 1.  1.5] [  0.  25.  50.  75. 100.]
```

`arange(start, stop, step)` is like range (stop excluded, floats allowed); `linspace(start, stop, num)` gives `num`
evenly spaced values **including** stop. `np.random.random((r, c))` fills with values in [0, 1);
`np.random.randint(lo, hi, size)` gives integers lo..hi−1. All elements of an array have **one type**.

## 2. Reshape

```python
x = np.array([[1, 4], [2, 3], [0, 6]])
print(np.reshape(x, (2, 3)))
print(np.arange(12).reshape(3, 4))
```

```text
[[1 4 2]
 [3 0 6]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

The total number of elements must stay the same (6 = 3·2 = 2·3).

## 3. Indexing and slicing: `arr[row, col]`

```python
arr = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr[1, 0], arr[1], arr[:, 0])
print(arr[1:3, 0:2])
print(arr[2, ::2])
```

```text
20 [20 25 30] [ 5 20 35]
[[20 25]
 [35 40]]
[35 45]
```

## 4. Boolean masks (conditional selection)

```python
v = np.arange(0, 11)
print(v > 5)
print(v[v > 5], v[v != 5], v[(v > 2) & (v < 6)])
```

```text
[False False False False False False  True  True  True  True  True]
[ 6  7  8  9 10] [ 0  1  2  3  4  6  7  8  9 10] [3 4 5]
```

## 5. Views vs copies

A slice is a **view**: changing it changes the original. `b = a` is the same array. Use `.copy()` for an independent one.

```python
x = np.array([1, 2, 3, 4, 5, 6])
y = x
z = x.copy()
s = x[0:2]
y[2:5] = 250
s[:] = 999
print(x, z)
```

```text
[999 999 250 250 250   6] [1 2 3 4 5 6]
```
