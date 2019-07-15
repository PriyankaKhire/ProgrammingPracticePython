#Min Stack
#https://leetcode.com/problems/min-stack/
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mStack = []
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        self.stack.append(x)
        if(not self.mStack or x <= self.mStack[-1]):
            self.mStack.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        num = self.stack.pop()
        if(num == self.mStack[-1]):
            self.mStack.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.mStack[-1]
        """
        :rtype: int
        """
