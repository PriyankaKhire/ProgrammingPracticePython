# Basic Calculator III
# https://leetcode.com/problems/basic-calculator-iii/

class Calculator(object):
    def __init__(self):
        self.operators = ['+', '-', '*', '/']
    
    def addition(self, a, b):
        return a+b
    
    def subtraction(self, a, b):
        return a-b
    
    def multiplacation(self, a, b):
        return a*b
    
    def division(self, a, b):
        if (a == 0 or b == 0):
            return 0
        return a/(b)
    
    def operation(self, a, b, operator):
        expressions = {
            '+': self.addition(a, b),
            '-': self.subtraction(a, b),
            '*': self.multiplacation(a, b),
            '/': self.division(a, b)
        }
        return expressions[operator]
    
    def precedence(self, operator):
        precidence = {
            '*':1,
            '/':1,
            '+':0,
            '-':0,
        }
        return precidence[operator]
    
        
class Solution(object):
    
    def convertInToList(self, s):
        newList = []
        number = ""
        for char in list(s):
            if char.isnumeric():
                number = number + char
            else:
                if (number != ""):
                    newList.append(int(number))
                    number = ""
                newList.append(char)
        return newList
        
    def calculate(self, s):
        s = s+')'
        s = self.convertInToList(s)
        numStack = []
        operatorStack = ['(']
        calculator = Calculator()
        for char in s:
            print numStack, operatorStack
            if(char == '('):
                operatorStack.append(char)
            elif(char == ')'):
                while(operatorStack and operatorStack[-1] != '('):
                    n2 = numStack.pop()
                    n1 = numStack.pop()
                    op = operatorStack.pop()
                    print "number1", n1, "number2", n2, "operator", op
                    ans = calculator.operation(n1, n2, op)
                    numStack.append(ans)
                # pop "("
                if operatorStack:
                    operatorStack.pop()
            elif(char in calculator.operators):
                operatorStack.append(char)
            else:
                ans = char
                while(operatorStack and operatorStack[-1] == '*' or operatorStack[-1] == '/'):
                    op = operatorStack.pop()
                    num = numStack.pop()
                    print "current num", ans, "top of stack", num, "operator", op,
                    ans = calculator.operation(num, ans, op)
                    print "answer", ans
                numStack.append(ans)
        return int(numStack[-1])
        """
        :type s: str
        :rtype: int
        """
        
