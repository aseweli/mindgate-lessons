## Why it matters

Functions give a name to a reusable piece of logic: **abstraction and reusability**, **modularity** (break a big
task into small ones) and **namespace separation** (a function's variables don't clash with yours).

## 1. def, parameters, arguments

```python
def F2C(f):
    c = (f - 32) * 5 / 9
    return c

print(F2C(104), F2C(32))
```

```text
40.0 0.0
```

`f` is the **parameter**; 104 is the **argument**. Parentheses are needed even with no parameters: `f()`.

## 2. return vs print

`print` only shows a value; `return` hands it back to the caller. A function without `return` returns **None**.

```python
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

first = add_print(2.2, 3.3)
second = add_return(2.2, 3.3)
print(first, type(first))
print(second + 450.0)
```

```text
5.5
None <class 'NoneType'>
455.5
```

## 3. Default arguments

Parameters can have defaults; an argument you pass overrides it. Defaults must come **after** non-default ones.

```python
def sum_to(n=10):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_to(), sum_to(5))
```

```text
55 15
```

## 4. Local and global variables

A variable created inside a function is **local**: it doesn't exist outside. A function can read a global, but
assigning to the same name inside creates a new local one (unless declared `global`).

```python
x = "jojo"

def F2():
    print(x)            # reads the global

def F3():
    x = "not jojo"      # a new local x
    print(x)

F2()
F3()
print(x)
```

```text
jojo
not jojo
jojo
```

```python
def make():
    inside = 5
    return inside

make()
print(inside)
```

```text
NameError: name 'inside' is not defined
```
