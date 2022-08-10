# Remove All Adjacent Duplicates in String II
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution(object):
    def popKFromStack(self, k, stack):
        for i in range(k):
            stack.pop()
            
    def stackApproach(self, s, k):
        stringStack = [s[0]]
        # stack to keep track of duplicates
        dupStack = [1]
        index = 1
        while (index < len(s)):
            # if the top of stack has k same chars then pop them
            if (dupStack[-1] == k):
                # pop k items from string stack
                self.popKFromStack(k, stringStack)
                # pop dupStack
                dupStack.pop()
            # if the top of stack and curr char in string are same
            if (stringStack and s[index] == stringStack[-1]):
                # then just increment the duplicate count
                dupStack[-1] += 1
            else:
                # else put 1 on duplicate stack. 
                dupStack.append(1)
            # put current letter in stack
            stringStack.append(s[index])
            # increment the index
            index += 1
        # check one last time in dup stack
        if (dupStack[-1] == k):
            self.popKFromStack(k, stringStack)
            dupStack.pop()
        return stringStack
        
    def removeDuplicates(self, s, k):
        stack = self.stackApproach(s, k)
        return "".join(stack)
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
