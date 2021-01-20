## Forward-Mode Automatic Differentiation

- Taken from Julia version https://mitmath.github.io/18337/lecture8/automatic_differentiation.html
- proof https://github.com/amodwani/18337
    - We want to calculate f'(x) where x ε R 
    - and f: R -> R
    - But f(x) is analytic (means it is differentiable)
    - Take Taylor series expansion
    -    $ f(x + iy) = f(x) + iyf'(x) + O(h^2) $
    -    $ if'(x) = \frac{ f(x + iy) - f(x) + O(h^2)}{y}  $
                        
 

```python

from auto_diff import forward_diff

def h(x):
    return x*x + 2

xx = forward_diff(3,1)

h(xx)
Number:11, ε:6

```

Where ε is the diff value of the equation
