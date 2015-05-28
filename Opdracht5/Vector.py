import math

class Vector:

    def __init__(self, n, arg = 0):
        self.elements = []
        if type(arg) is list:
            for i in range(0, n):
                self.elements.append(arg[i])
        else:
            for i in range(0, n):
                self.elements.append(arg)

    def __str__(self):
        s = ""
        for e in self.elements:
            s += str(e) + "\n"
        return s
        
    def lincomb(self, other, alpha, beta):
        c = Vector(0)
        for i in range(0, len(self.elements)):
            c.elements.append(self.elements[i] * alpha + other.elements[i] * beta)
        return c
        
    def scalar(self, alpha):
        c = Vector(0)
        for i in range(0, len(self.elements)):
            c.elements.append(self.elements[i] * alpha)
        return c
            
    def inner(self, other):
        c = 0
        for i in range(0, len(self.elements)):
            c += self.elements[i] * other.elements[i]
        return c
        
    def norm(self):
        c = 0
        for i in range(0, len(self.elements)):
            c += self.elements[i] ** 2
        c = math.sqrt(c)
        return c
        
    def substract(self, other):
        c = Vector(0)
        for i in range(0, len(self.elements)):
            c.elements.append(self.elements[i] - other.elements[i])
        return c

    def add(self, other):
        c = Vector(0)
        for i in range(0, len(self.elements)):
            c.elements.append(self.elements[i] + other.elements[i])
        return c
        
    def copy(vector):
        c = Vector(0)
        for i in range(0, len(vector.elements)):
            c.elements.append(vector.elements[i])
        return c

    def proj(v, u):
        c = Vector.copy(u)
        u0 = u.inner(u)
        if (u0 == 0): return Vector(len(V.elements))
        c = c.scalar(v.inner(u) / u0)
        return c
    
def GrammSchmidt(V):
    output = []
    u = []
    for i in range(0, len(V)):
        c = Vector.copy(V[i])
        for j  in range(0, i):
            c = c.substract(Vector.proj(V[i], u[j]))
        u.append(c)
        c = c.scalar(1 / c.norm())
        output.append(c)
    return output
            
        
        