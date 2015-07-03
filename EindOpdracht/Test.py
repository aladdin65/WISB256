from ExpressionTrees_Template import *

a = Constant(-2)
b = Constant(300)
c = Constant(4)
x = Variable('x')
y = Variable('y')
d = -a * -x - -c * y
print(d)
print(d.evaluate({'x':-1}))
print(d.evaluate({}))
print(Expression.fromString("1+-x_0*-3"))