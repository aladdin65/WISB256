import math

# check if a string represents a numeric value
def isnumber(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# check if a string represents an integer value        
def isint(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

class Expression():
    """A mathematical expression, represented as an expression tree"""
    
    """
    Any concrete subclass of Expression should have these methods:
     - __str__(): return a string representation of the Expression.
     - __eq__(other): tree-equality, check if other represents the same expression tree.
    """
    
    # operator overloading:
    # this allows us to perform 'arithmetic' with expressions, and obtain another expression
    def __add__(self, other):
        return OperatorNode(self, other, "+")
        
    def __sub__(self, other):
        return OperatorNode(self, other, "-")
        
    def __div__(self, other):
        return OperatorNode(self, other, "/")
        
    def __mul__(self, other):
        return OperatorNode(self, other, "*")
        
    def __pow__(self, other):
        return OperatorNode(self, other, "**")
        
    def __eq__(self, other):
        #if the evaluation is the same, the trees are considered the same
        return self.evaluate({}) == other.evaluate({})
        
    def __neg__(self):
        if isinstance(self, Constant): return Constant(-1 * self.value)
        elif isinstance(self, Variable):
            v = Variable(self.name)
            v.value = -1
            return v

    # basic Shunting-yard algorithm
    def fromString(string):
        # split into tokens
        tokens = tokenize(string)
        # stack used by the Shunting-Yard algorithm
        stack = []
        # output of the algorithm: a list representing the formula in RPN
        # this will contain Constant's, OperatorNodes and Variables
        output = []
        
        # list of operators
        oplist = ["+", "-", "*", "/", "**"]
        #dictionary containing precedence of operators:
        dictPrecedence = {"+":2, "-":2, "/":3, "*":3, "**": 4}

        for token in tokens:
            if isnumber(token):
                # numbers go directly to the output
                if isint(token):
                    output.append(Constant(int(token)))
                else:
                    output.append(Constant(float(token)))
            elif token in oplist:
                # pop operators from the stack to the output until the top is no longer an operator
                while (len(stack) != 0 and stack[-1] in oplist):
                    token2 = stack.pop()   #pop the next token from the stack
                    #compare the precedence of token with token2
                    if (token in "+-/*" and dictPrecedence[token] <= dictPrecedence[token2]) or (token in "^" and dictPrecedence[token] < dictPrecedence[token2]):
                        #push the new operator on the output stack:
                        output.append(token2)
                    else: 
                        #push the new operator on the stack:
                        stack.append(token2)
                        break
                stack.append(token)
            elif token == '(':
                # left parantheses go to the stack
                stack.append(token)
            elif token == ')':
                # right paranthesis: pop everything upto the last left paranthesis to the output
                while not stack[-1] == '(':
                    output.append(stack.pop())
                # pop the left paranthesis from the stack (but not to the output)
                stack.pop()
            else:
                # unknown token or Variable
                if token[0].isalpha() or (token[0] == "-" and token[1].isalpha()):      #check if the variable has the correct name or has the unary operator
                    check = True
                    for i in range(1, len(token)):
                        if not (token[i].isnumeric() or token[i].isalpha() or token[i] == "_"): #variable name should only contain letters or numbers
                            check = False
                            break
                    if (check):
                        #if correct name
                        output.append(Variable(token))
                    else:
                        raise ValueError('Unknown token: %s' % token)
                else:
                    raise ValueError('Unknown token: %s' % token)
        # pop any tokens still on the stack to the output
        while len(stack) > 0:
            output.append(stack.pop())
        
        # convert RPN to an actual expression tree
        for t in output:
            if t in oplist:
                # let eval and operator overloading take care of figuring out what to do
                y = stack.pop()
                x = stack.pop()
                stack.append(eval('x %s y' % t))
            else:
                # a constant, push it to the stack
                stack.append(t)
        # the resulting expression tree is what's left on the stack
        return stack[0]

class Constant(Expression):
    """Represents a constant value"""
    def __init__(self, value):
        self.value = value
        
    def __eq__(self, other):
        if isinstance(other, Constant):
            return self.value == other.value
        else:
            return False
        
    def __str__(self):
        return str(self.value)
        
    # allow conversion to numerical values
    def __int__(self):
        return int(self.value)
        
    def __float__(self):
        return float(self.value)

class Variable(Expression):
    """Represents a variable"""
    def __init__(self, name):
        self.name = name
        #hold a local variable for the unary operator:
        self.value = 1

    def __eq__(self, other):
        if isinstance(other, Variable):
            return self.name == other.name
        else:
            return False
            
    def __str__(self):
        if (self.value == 1):
            return self.name
        else:
            return "-" + self.name
        
    
        
class BinaryNode(Expression):
    """A node in the expression tree representing a binary operator."""
    
    def __init__(self, lhs, rhs, op_symbol):
        self.lhs = lhs
        self.rhs = rhs
        self.op_symbol = op_symbol
    
    # TODO: what other properties could you need? Precedence, associativity, identity, etc.
    #def __eq__(self, other):
        #if type(self) == type(other):
         #   return self.lhs == other.lhs and self.rhs == other.rhs
        #else:
         #   return False
            
    def __str__(self):
        lstring = str(self.lhs)
        rstring = str(self.rhs)
        
        # remove unnecessary parentheses by checking precedence and associativity:
        if self.op_symbol in "*/":   #left/right associative
            if isinstance(self.lhs, BinaryNode) and (self.lhs.op_symbol in "+-"):
                lstring = "(" + lstring + ")"
            if isinstance(self.rhs, BinaryNode) and (self.rhs.op_symbol in "+-"):
                rstring = "(" + rstring + ")"

        if self.op_symbol == "**":   #right associative
            if isinstance(self.lhs, BinaryNode) and (self.lhs.op_symbol in "+-*/"):
                lstring = "(" + lstring + ")"
            if isinstance(self.rhs, BinaryNode) and (self.rhs.op_symbol in "+-*/"):
                rstring = "(" + rstring + ")"
                
        # minus operator is left associative:
        if (self.op_symbol == "-" and (isinstance(self.rhs, BinaryNode) and self.rhs.op_symbol == "-")):
            rstring = "(" + rstring + ")"
        
        # return output:
        return "%s %s %s" % (lstring, self.op_symbol, rstring)
    
    def evaluate(self, values):
        # evaluate tree recursively
        output = self.eval_recursion(values)
        # remove unnecessary parentheses
        output = str(Expression.fromString(str(output)))
        # return output
        return output
            
    def eval_recursion(self, values):
        lC = self.lhs  #value left child
        rC = self.rhs  #value right child
        if (isinstance(self.lhs, Variable) and self.lhs.name in values): lC = values[self.lhs.name] * self.lhs.value
        if (isinstance(self.rhs, Variable) and self.rhs.name in values): rC = values[self.rhs.name] * self.rhs.value
        if (isinstance(self.lhs, OperatorNode)): lC = self.lhs.eval_recursion(values)
        if (isinstance(self.rhs, OperatorNode)): rC = self.rhs.eval_recursion(values)
        
        result = "(" + str(lC) + " " + str(self.op_symbol) + " " + str(rC) + ")"
        if isnumber(str(lC)) and isnumber(str(rC)):
            return int(eval(result))
        else:
            return result

        
class OperatorNode(BinaryNode):
    """Represents the operator"""
    def __init__(self, lhs, rhs, operator):
        super().__init__(lhs, rhs, operator)

# split a string into mathematical tokens
# returns a list of numbers, operators, parantheses and commas
# output will not contain spaces
def tokenize(string):
    splitchars = list("+-*/(),")
    
    # surround any splitchar by spaces
    tokenstring = []
    for c in string:
        if c in splitchars:
            tokenstring.append(' %s ' % c)
        else:
            tokenstring.append(c)
    tokenstring = ''.join(tokenstring)
    #split on spaces - this gives us our tokens
    tokens = tokenstring.split()
    
    #special casing for **:
    ans = []
    for t in tokens:
        if len(ans) > 0 and t == ans[-1] == '*':
            ans[-1] = '**'
        else:
            ans.append(t)
    
    #check for unary operators:    
    try:
        for i in range(0, len(ans)):
            #if token is minus operator and previous token is an operator:
            if (ans[0] == "-") or (i > 0 and ans[i] == "-" and ans[i - 1] in splitchars):
                #if next token is a variable name or a number:
                if i + 1 < len(ans) and not ans[i + 1] in splitchars:
                    #put in 1 slot:
                    ans[i] = str(ans[i]) + str(ans[i + 1])
                    #shift array by 1 step and remove last element:
                    for j in range(i + 1, len(ans)):
                        if j + 1 < len(ans): ans[j] = ans[j + 1]
                    ans.pop(-1)
    except:  #if end of the list, pass
        pass
    return ans