from ExpressionTrees_Template import *

a = Constant(-2)
b = Constant(300)
c = Constant(4)
x = Variable('x')
y = Variable('y')
d = a - (x * y + -b) + x - y
print(d)
print(d.evaluate({}))
print(d.evaluate({'x':-1}))
print(d.evaluate({'x':2, 'y':3}))
print(Expression.fromString("1+-x_0*-3"))
print(Expression.fromString("1-(1+6)*(2+3)"))