from ExpressionTrees_Template import *

a = Constant(-2)
b = Constant(300)
c = Constant(4)
x = Variable('x')
y = Variable('y')
z = Variable('z')
d = x*y + c*z
f = d.makeFunction()
print(f(1,2,0))