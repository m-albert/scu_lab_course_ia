# Python Basics Cheat Sheet

A quick reference to core Python you’ll use in this course. Copy/paste and tweak in a notebook or a script.

## Getting started

- Run a REPL: `python`
- Run a script: `python my_script.py`
- Comments: `# this is a comment`

```python
# print to console
print("Hello, world!")
```

## Variables and basic types

- Numbers: `int`, `float`
- Text: `str`
- Boolean: `bool` (`True`/`False`)
- Empty: `None`

```python
x = 3            # int
pi = 3.1415      # float
ok = True        # bool
name = "Ada"     # str
nothing = None   # NoneType

# casting / conversion
int("5")      # 5
float("2.3")  # 2.3
str(42)        # "42"
bool(0)        # False
```

## Strings

```python
s = "image"
len(s)              # 5
s.upper()           # 'IMAGE'
s.replace('a','@')  # 'im@ge'

# indexing and slicing
s[0]        # 'i'
s[-1]       # 'e'
s[1:4]      # 'mag'
s[::-1]     # 'egami'

# f-strings (formatted)
w = 640; h = 480
msg = f"Size: {w}x{h}"
```

## Collections

- List: ordered, mutable `[]`
- Tuple: ordered, immutable `()`
- Dict: key-value `{}`
- Set: unique items `{}`; for non-empty literal: `{1, 2}`

```python
# lists
nums = [1, 2, 3]
nums.append(4)      # [1,2,3,4]
nums[0] = 10        # [10,2,3,4]
nums[:2]            # [10,2]

# tuples
pt = (10, 20)
pt[0]               # 10

# dicts
cfg = {"path": "data/", "verbose": True}
cfg["path"]            # 'data/'
cfg.get("missing", 0) # 0 default

# sets
seen = {"a", "b"}
seen.add("c")
"a" in seen            # True
```

## Comprehensions

```python
squares = [n*n for n in range(5)]
odd_squares = [n*n for n in range(10) if n % 2]
keys = [k for k in cfg]
inv = {v: k for k, v in cfg.items()}
unique = {c.lower() for c in "AaBb"}
```

## Control flow

```python
x = 7
if x > 10:
    print("big")
elif 5 <= x <= 10:
    print("medium")
else:
    print("small")
```

## Loops and iteration

```python
# for-loop
for i in range(3):           # 0,1,2
    print(i)

# enumerate and zip
items = ["a", "b", "c"]
for idx, item in enumerate(items):
    print(idx, item)

xs = [1, 2, 3]
ys = [10, 20, 30]
for x, y in zip(xs, ys):
    print(x, y)

# while-loop
count = 0
while count < 3:
    count += 1
```

## Functions

```python
def area(w: float, h: float = 1.0) -> float:
    """Rectangle area."""
    return w * h

area(3, 4)
area(5)             # uses default h=1.0

# *args and **kwargs

def show(*args, **kwargs):
    print(args, kwargs)

# lambda (small anonymous function)
double = lambda x: 2*x
```

## Exceptions

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")
    finally:
        pass  # runs either way
```

## Files

```python
# read all text
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

# write
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
```

## Imports and modules

```python
import math
from pathlib import Path
import json as js

math.sqrt(9)
Path("data").exists()
js.dumps({"a": 1})
```

## Handy built-ins

```python
len(nums)            # length
sum(nums)            # sum
min(nums), max(nums)
sorted(nums, reverse=True)
all([True, True, False])   # False
any([False, True])         # True

# unpacking
first, *rest = [1, 2, 3, 4]    # first=1, rest=[2,3,4]

# truthiness
bool("")   # False
bool([])   # False
bool(0)    # False
```

```{admonition} Tip
Prefer explicit and readable code. Follow PEP 8 style and use meaningful names. In notebooks, keep cells small and focused.
```

## Next steps

- Need Python installed? See the Install Python page in this book.
- For image analysis, you’ll soon meet NumPy, SciPy, and scikit-image in the notebooks section.
