#Expressions and conversion
#http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html

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

class helperFunctions(object):
    def reverse(self, string):
        '''
        for i in range((len(string))/2 ):
            print "Swapping "+string[len(string) - 1 - i]+" with "+string[i]
            temp = string[i]
            string[i] = string[len(string) - 1 - i]
            string[len(string) - 1 - i] = temp
        '''
        return string[::-1]

    def invertBrackets(self, string):
        s = ""
        for char in string:
            if char == "(":
                s = s+")"
            elif char == ")":
                s = s+"("
            else:
                s = s+char
        return s

#Convert infix to postfix and prefix
class infix(operatorPrecedence, helperFunctions):

    def __init__(self, infixExpression):
        #Call constructor of base class
        super(infix, self).__init__()
        #Put the infix expression in ()
        self.infixExpression = "("+infixExpression+")"

    #reverse the expression this means () will change to )(
    # convert it into postfix expression
    #reverse the expression again.
    def toPrefix(self):
        reversed_expression = self.reverse(self.infixExpression)
        inverted_brackets_expression = self.invertBrackets(reversed_expression)
        self.infixExpression = inverted_brackets_expression
        postFixed = self.toPostfix()
        reverse_postFixed = self.reverse(postFixed)
        return reverse_postFixed
        
        
        
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
        return output
                
                
        
        
        
    

#Main Program
#DONT use space in input expression
i = infix("(A-B/C)*(A/K-L)")
print i.toPostfix()
print i.toPrefix()    
