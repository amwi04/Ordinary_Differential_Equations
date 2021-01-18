## Forward-Mode Automatic Differentiation

- Taken from Julia version https://mitmath.github.io/18337/lecture8/automatic_differentiation.html
- proof https://github.com/amodwani/18337


```python

from auto_diff import forward_diff

def h(x):
    return x**2 + 2

xx = forward_diff(3,1)

h(xx)
Number:11, ε:6

```

Where ε is the diff value of the equation
