#Mini Parser
#https://leetcode.com/problems/mini-parser/
class Solution(object):
    def deserialize(self, s):
        outterList = []
        currentList = outterList
        currDigit = -1
        for i in range(len(s)):
            char = s[i]
            if(char == "[" and i != 0):
                currentList.append([])
                currentList = currentList[-1]
            elif(char.isdigit()):
                if(currDigit == -1):
                    currDigit = 0
                currDigit = (currDigit*10)+int(char)
            elif(char == ","):
                currentList.append(currDigit)
                currDigit = -1
            elif(char == "]" and currDigit > 0):
                currentList.append(currDigit)
                currDigit = -1
        if(currDigit > -1):
            outterList.append(currDigit)
        print outterList
            
        
        """
        :type s: str
        :rtype: NestedInteger
        """
#Main
obj = Solution()
obj.deserialize("[123,[456,[789]]]")

obj = Solution()
obj.deserialize("324")
