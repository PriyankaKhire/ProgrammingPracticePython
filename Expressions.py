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
        
    #Explanation: at first put the expression in ()
    #then as you are scanning the expression you first put ( in the bottom of the stack
    #then you start scanning the expression, if you encounter operand such as A, B etc you add it to output
    #if you encounter an operator such as + - * / then you put it in stack only if
    #the top of stack has an operator with less than or equal to precedence than the operator you are trying to put.
    #so if stack has + and you are trying to add * you can
    #in case if you are trying to add + and stack has * then you start popping till top of stack has something
    #that is less in precedence than the one you are currently trying to add
    #finally when you encounter ) pop the stack and add it to output till you reach (
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
        
