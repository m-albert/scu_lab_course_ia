---
title: Python Basics
kernelspec:
  name: python
  display_name: Python
---

# Python Basics

This page is a browser-runnable version of the Python basics material. Use the power button at the top of the page to start the in-page JupyterLite kernel, then run the code cells directly in the page.

## Hello World

```{code-cell} python
print("Hello, World!")
```

## Python as a Calculator

```{code-cell} python
2 + 2
```

```{code-cell} python
(2 + 3) * 4 / 5**2
```

## Variables

```{code-cell} python
a = 3 - 2**4
a
```

```{code-cell} python
b = a * 5
b
```

## Types

```{code-cell} python
type(a)
```

```{code-cell} python
b = 1.3
type(b)
```

## Strings

```{code-cell} python
"Hello, " + "World!"
```

```{code-cell} python
age = 27
f"I am {age} years old!"
```

## Lists

```{code-cell} python
squares = [1, 4, 9, 16, 25]
squares[0], squares[-1]
```

```{code-cell} python
squares[1:5:2]
```

```{code-cell} python
squares[1] = 10
squares[2:5] = [50, 60, 70]
squares.append(100)
squares
```

## Dictionaries

```{code-cell} python
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
car["color"] = "red"
car
```

```{code-cell} python
list(car.items())
```

## Conditionals

```{code-cell} python
a = 42
if a % 2 == 0:
    print("a is even!")
else:
    print("a is odd!")
```

## Loops

```{code-cell} python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

```{code-cell} python
for i in range(0, 5, 2):
    print(i)
```

## Functions

```{code-cell} python
def maximum(a, b):
    """Returns the maximum of two numbers."""
    if a >= b:
        return a
    return b

maximum(5, 7)
```

## NumPy

```{code-cell} python
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
a
```

```{code-cell} python
b = np.array([[1, 2, 3], [4, 5, 6]])
b
```

```{code-cell} python
a = np.arange(11, 20)
indices, = np.where(a > 15)
a[indices]
```

## Matplotlib

```{code-cell} python
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="y(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y = cos(x)")
ax.legend()
```
