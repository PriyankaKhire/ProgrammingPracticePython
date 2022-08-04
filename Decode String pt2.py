# Decode String
# https://leetcode.com/problems/decode-string/
class Solution(object):
    def decodeString(self, s):
        stack = []
        index = 0
        while(index<len(s)):
            if (s[index] == ']'):
                # start popping until you reach [ 
                string = ''
                while(stack[-1] != '['):
                    string = stack.pop() + string
                # pop [ from stack
                stack.pop()
                # next build your number
                num = ''
                # start popping until 1) stack empty 2) reach alphabet or string
                while(stack and stack[-1].isnumeric()):
                    num = stack.pop() + num
                # multiply string with num and add it back to stack
                decodedString = string*int(num)
                stack.append(decodedString)
            else:
                stack.append(s[index])
            index += 1
        return ''.join(stack)        
        """
        :type s: str
        :rtype: str
        """
        
