## Why it matters

Engineering problems with several unknowns (currents in a circuit, amounts in a mixture, forces in a truss) become
$AX = B$. NumPy solves them in one line. Work is a dot product; torque is a cross product.

## 1. Dot product: a number

$\mathbf A\cdot\mathbf B = a_1b_1 + a_2b_2 + a_3b_3 = |A||B|\cos\theta$. Zero means perpendicular.

```python
import numpy as np

A = np.array([2, 3, 4])
B = np.array([5, 6, 7])
print(np.dot(A, B), np.dot([2, 0], [0, 2]), np.dot([2, 0], [-2, 0]))
force, move = np.array([10, 0]), np.array([5, 0])
print("work:", np.dot(force, move))
print("magnitude:", np.linalg.norm([3, 4]))
```

```text
56 0 -4
work: 50
magnitude: 5.0
```

## 2. Cross product: a vector

$\mathbf A\times\mathbf B = [a_2b_3 - a_3b_2,\; a_3b_1 - a_1b_3,\; a_1b_2 - a_2b_1]$, perpendicular to both
(right-hand rule). Order matters: $A\times B = -(B\times A)$. Torque $\tau = r\times F$.

```python
print(np.cross(A, B), np.cross(B, A))
print(np.cross([1, 0, 0], [0, 1, 0]))
print("torque:", np.cross([2, 0, 0], [0, 5, 0]))
```

```text
[-3  6 -3] [ 3 -6  3]
[0 0 1]
torque: [ 0  0 10]
```

## 3. Matrix multiplication

(m × n) @ (n × p) → (m × p): the **inner** dimensions must match. Entry (i, j) = row i of the first · column j of the
second. `A @ B` or `np.matmul(A, B)`; `A * B` is elementwise. In general $AB \ne BA$.

```python
P = np.array([[1, 2], [3, 4]])
Q = np.array([[5, 6], [7, 8]])
print(P @ Q)
print(P * Q)
print(Q @ P)
R = np.array([[1, 2, 3], [4, 5, 6]])
S = np.array([[1, 2], [3, 4], [5, 6]])
print((R @ S).shape, R @ S)
```

```text
[[19 22]
 [43 50]]
[[ 5 12]
 [21 32]]
[[23 34]
 [31 46]]
(2, 2) [[22 28]
 [49 64]]
```

## 4. Solving $AX = B$

If $A$ is square and invertible, $X = A^{-1}B$. `np.linalg.solve(A, B)` does it directly (more accurate than `inv`).
Mixture example: x oz of 20% acid + y oz of 70% acid make 20 oz of 50% acid: $x + y = 20$, $0.2x + 0.7y = 10$.

```python
A = np.array([[1, 1], [0.20, 0.70]])
B = np.array([20, 10])
print(np.linalg.solve(A, B))
print(np.linalg.inv(A) @ B)
C = np.array([[2, 1, 1], [1, 3, 2], [3, 2, 1]])
D = np.array([9, 13, 14])
print(np.round(np.linalg.solve(C, D), 6))
```

```text
[ 8. 12.]
[ 8. 12.]
[2.5 2.5 1.5]
```
