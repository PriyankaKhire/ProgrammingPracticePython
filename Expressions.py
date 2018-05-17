#Expressions and conversion

#Getting the operator precedence from wikipedia
#https://en.wikipedia.org/wiki/Order_of_operations
class operatorPrecedence(object):
    def __init__(self):
        self.precedence_levels = {
            ")": 4,
            "exponents": 3,
            "roots": 3,
            "*": 2,
            "/": 2,
            "+": 1,
            "-": 1,
            "(" : 0
            }

    def getPrecedence(self, operator):
        return self.precedence_levels[operator]

#Convert infix to postfix and prefix
class infix(operatorPrecedence):

    def __init__(self, infixExpression):
        #Call constructor of base class
        super(infix, self).__init__()
        #Put the infix expression in ()
        self.infixExpression = "("+infixExpression+")"
        
    def toPostfix(self):
        stack = []
        output = ""
        for char in self.infixExpression:
            if char == "(":
                stack.append(char)
                continue
            if char == ")":
                #Pop stack till you reach "("
                while stack[-1] != "(":
                    top = stack.pop()
                    output = output + top
                #Pop "("
                stack.pop()
                continue
            if char.isalpha():
                output = output + char
            else:
                if (self.getPrecedence(char) >= self.getPrecedence(stack[-1])):
                    stack.append(char)
                else:
                    while stack and self.getPrecedence(stack[-1]) > self.getPrecedence(char):
                        top = stack.pop()
                        output = output + top
                    stack.append(char)
        print output
                
                
        
        
        
    

#Main Program
#DONT use space in input expression
i = infix("A+B+C+D")
i.toPostfix()
        
