from ExpressionTrees_Template import *

a = Constant(-2)
b = Constant(300)
c = Constant(4)
x = Variable('x')
y = Variable('y')
z = Variable('z')
d = x * y + c * z
f = d.makeFunction()
print(f(1,2,0))

expr = Expression.fromString("-x+1")
print(expr.evaluate())
print(expr.evaluate({"x": -1}))

d = a - (x * y + -b) + x - (y ** c / a)
print("print tree: " + str(d))
print("print evaluation in (x, y): " + d.evaluate())
print("print evaluation in (-1, y): " + d.evaluate({'x':-1}))
print("print evaluation in (2, 3):  " + d.evaluate({'x':2, 'y':3}))
print("print expression from string: " + str(Expression.fromString("1+-x_0*-3")))
print("print expression from string: " + str(Expression.fromString("1-(1+6)*(2+3)")))
print("print expression from string: " + str(Expression.fromString("1-(1+6)*(2+3)").evaluate()))
