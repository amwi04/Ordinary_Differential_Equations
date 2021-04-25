

class forward_diff:
    def __init__(self,real = 0,img = 1):
        self.real = real
        self.img = img

    def __add__(self,other):
        if isinstance(other, int):
            real_part = self.real + other
            img_part = self.img
            return forward_diff(real_part,img_part)
        else:
            real_part = self.real + other.real
            img_part = self.img + other.img
            return forward_diff(real_part,img_part)

    def __str__(self):
        return f'x:{self.real}, dx:{self.img}'

    def __repr__(self):
        return f'x:{self.real}, dx:{self.img}'

    def __sub__(self, other):
        real_part = self.real - other.real
        img_part = self.img - other.img
        return forward_diff(real_part,img_part)

    def __mul__(self, other):
        if isinstance(other, forward_diff):
            real_part = self.real * other.real
            img_part = (self.img * other.real) + (self.real * other.img)
            return forward_diff(real_part,img_part)
        elif isinstance(other, int):
            real_part = self.real * other
            img_part  = self.img * other
            return forward_diff(real_part,img_part)

    def __truediv__(self, other):
        real_part = self.real / other.real
        img_part = ((self.img * other.real) - (self.real * other.img)) / (other.img^2)
        return forward_diff(real_part,img_part)

    def __floordiv__(self, other):
        real_part = self.real // other.real
        img_part = ((self.img * other.real) - (self.real * other.img)) // (other.img^2)
        return forward_diff(real_part,img_part)

    def __pow__(self, exponent):
        if isinstance(exponent, int):
            p = forward_diff(1,0)
            if exponent > 0:
                for i in range(exponent):
                    p = p*self
            elif exponent < 0:
                for i in range(-exponent):
                    p = p*self
                p = 1/p
            else:   # exponent == 0
                p = forward_diff(1,1)
            return p
        else:
            raise TypeError('exponent must int')

