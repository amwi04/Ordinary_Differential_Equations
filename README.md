## Forward-Mode Automatic Differentiation

- Taken from Julia version https://mitmath.github.io/18337/lecture8/automatic_differentiation.html
- proof https://github.com/amodwani/18337
    - We want to calculate f'(x) where x ε R
    - and f: R -> R
    - But f(x) is analytic (means it is differentiable)
    - Take Taylor series expansion
    -   f(x + iy) = f(x) + iyf'(x) + O(y^2)
    -   if'(x) =  f(x + iy) - f(x) + O(y^2) / y
    - as f:R -> R
    - f'(x) = Im[f(x + iy) - f(x)] /y + O(y)
    - and imaginary part of f(x)/h will be 0 as f:R -> R
    - f'(x) = Im[f(x + iy)]/y + O(y)
    - To find derivative of a function will be img part of f(x + iy)/y

    - That is implamented in forward_diff


```python

from auto_diff import forward_diff

def h(x):
    return x**3 + x**2 + x + 2

xx = forward_diff(3,1)

h(xx)
 x:41, dx:34
```

Where ε is the diff value of the equation
