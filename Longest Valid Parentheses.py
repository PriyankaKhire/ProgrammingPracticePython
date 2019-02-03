#Longest Valid Parentheses
#https://leetcode.com/problems/longest-valid-parentheses/
#essentially we need longest parenthesis that is consequitive
#so in this example
#()((((((()()()(((((((()()()()() the longest valid parentheses is the last 5 parentheses. and the first 4 are not counted.
class StackApproch(object):

    def logic(self, s):
        isPartOfValidParentheses = [False for i in range(len(s))]
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack and s[stack[-1]] == "(":
                    isPartOfValidParentheses[i] = True
                    isPartOfValidParentheses[stack[-1]] = True
                    stack.pop()
                else:
                    stack.append(i)
        #Now just find out which is longest consequitive one
        i =0
        j = i
        maxLength = 0
        while(i < len(s) and j < len(s)):
            while(j < len(s) and isPartOfValidParentheses[j] == True):
                j = j+1
            if(maxLength < (j-i)):
                maxLength = (j-i)
            i = j+1
            j = i
        return maxLength
                    
    
    def longestValidParentheses(self, s):
        print self.logic(s)
        """
        :type s: str
        :rtype: int
        """

#Main
obj1 = StackApproch()
obj1.longestValidParentheses("())((())")

obj2 = StackApproch()
obj2.longestValidParentheses(")()())")

obj3 = StackApproch()
obj3.longestValidParentheses("())((())")

obj4 = StackApproch()
obj4.longestValidParentheses("())(()())")
