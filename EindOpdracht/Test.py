from ExpressionTrees_Template import *

a = Constant(-2)
b = Constant(300)
c = Constant(4)
x = Variable('x')
y = Variable('y')
d = a - (x * y + -b) + x - (y ** c / a)
print("print tree: " + str(d))
print("print evaluation in (x, y): " + d.evaluate())
print("print evaluation in (-1, y): " + d.evaluate({'x':-1}))
print("print evaluation in (2, 3): " + d.evaluate({'x':2, 'y':3}))
print("print expression from string: " + str(Expression.fromString("1+-x_0*-3")))
print("print expression from string: " + str(Expression.fromString("1-(1+6)*(2+3)")))

expr = Expression.fromString("1+1")
print(expr.evaluate())
expr = Expression.fromString("-x+1")
print(expr.evaluate())
print(expr.evaluate({"x":1}))

print(Expression.fromString("1").evaluate())
print(Expression.fromString("-x").evaluate())
print(Expression.fromString("x").evaluate({"x":5.1}))