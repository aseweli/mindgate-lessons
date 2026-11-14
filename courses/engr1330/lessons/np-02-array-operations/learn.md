## Why it matters

"Apply this formula to every value" is one line in NumPy. Summaries per row or per column (`axis`) are how you
summarize experiments.

## 1. Elementwise arithmetic and ufuncs

```python
import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[10, 20], [30, 40], [50, 60]])
print(A + B)
print(A * 2, A ** 2)
print(np.sqrt(np.array([0, 1, 4, 9])))
print(np.round(np.sin(np.array([0, np.pi / 2, np.pi])), 3))
```

```text
[[11 22]
 [33 44]
 [55 66]]
[[ 2  4]
 [ 6  8]
 [10 12]] [[ 1  4]
 [ 9 16]
 [25 36]]
[0. 1. 2. 3.]
[0. 1. 0.]
```

## 2. Aggregates and axis

`axis=0` works **down the columns** (one result per column); `axis=1` **across the rows** (one per row). `argmax`
gives the position of the max (in the flattened array if no axis).

```python
M = np.array([[90, 31, 94, 75], [66, 45, 46, 75], [14, 28, 12, 16]])
print(np.sum(M), np.sum(M, axis=0), np.sum(M, axis=1))
print(np.max(M), np.argmax(M), np.mean(M, axis=1).round(2))
```

```text
592 [170 104 152 166] [290 232  70]
94 2 [72.5 58.  17.5]
```

## 3. Sorting

```python
d = np.array([[17, -6, 2], [86, -12, 0], [0, 23, 12]])
print(np.sort(d, axis=0))
print(np.sort(d, axis=1))
print(np.sort(d, axis=None)[::-1])
```

```text
[[  0 -12   0]
 [ 17  -6   2]
 [ 86  23  12]]
[[ -6   2  17]
 [-12   0  86]
 [  0  12  23]]
[ 86  23  17  12   2   0   0  -6 -12]
```

## 4. Stacking and transposing

`np.vstack((a, b))` stacks rows (same number of columns); `np.hstack((a, b))` stacks columns (same number of rows);
`A.T` or `np.transpose(A)` swaps rows and columns.

```python
a = np.ones((2, 3))
b = np.zeros((1, 3))
print(np.vstack((a, b)).shape, np.hstack((a, np.zeros((2, 2)))).shape)
print(A.T)
print(np.equal(A, B // 10), np.less_equal(A, 3))
```

```text
(3, 3) (2, 5)
[[1 3 5]
 [2 4 6]]
[[ True  True]
 [ True  True]
 [ True  True]] [[ True  True]
 [ True False]
 [False False]]
```
