from ExpressionTrees_Template import *

a = Constant(-2)
b = Constant(300)
c = Constant(4)
x = Variable('x')
y = Variable('y')
d = a - (x * y + -b) + x - (y ** c / a)
print("print tree: \n" + str(d))
print("print evaluation in (x, y): \n" + d.evaluate({}))
print("print evaluation in (-1, y): \n" + d.evaluate({'x':-1}))
print("print evaluation in (2, 3): \n" + d.evaluate({'x':2, 'y':3}))
print("print expression from string: \n" + str(Expression.fromString("1+-x_0*-3")))
print("print expression from string: \n" + str(Expression.fromString("1-(1+6)*(2+3)")))