#Max Stack
#https://leetcode.com/problems/max-stack/
class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.mStack = []
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        self.stack.append(x)
        if(self.mStack and self.mStack[-1] > x):
            self.mStack.append(self.mStack[-1])
        else:
            self.mStack.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if not self.stack:
            return
        self.mStack.pop()
        return self.stack.pop()
        """
        :rtype: int
        """
        

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """
        

    def peekMax(self):
        return self.mStack[-1]
        """
        :rtype: int
        """
        

    def popMax(self):
        currentMax = self.peekMax()
        tempStack = []
        while(self.top() != currentMax):
            tempStack.append(self.pop())
        #pop the max
        self.pop()
        #add tempStack elements back onto stack
        for num in reversed(tempStack):
            self.push(num)
        return currentMax
        """
        :rtype: int
        """
        

#Main
obj = MaxStack()
obj.push(92)
print obj.peekMax()
obj.push(54)
print obj.peekMax()
obj.push(22)
print obj.pop()
print obj.pop()
obj.push(-57)
print obj.peekMax()
obj.push(-24)
print obj.popMax()
print obj.top()
print obj.stack, obj.mStack

