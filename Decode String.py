#Decode String
#https://leetcode.com/problems/decode-string/
class Solution(object):
    #traverse backwards to get number
    def getNumber(self, string , index):
        i = index-1
        while(i >= 0):
            if(string[i].isdigit()):
                i = i - 1
            else:
                break
        return int(string[i+1:index]), len(string[i+1:index])
            
    def logic(self, s):
        stack = []
        i = 0
        while(i < len(s)):
            if(s[i] == '['):
                stack.append(i)
            elif(s[i] == ']'):
                number, numberLen = self.getNumber(s, stack[-1])
                #say the string is 2[ab] the length is len of abc + len of [ and ] + len of number (which is 1 in this case)
                oldStrLen = len(s[stack[-1]+1:i])+2+numberLen
                #the new string will be then abab so the length will change from 5 to 4
                newStrLen = number * len(s[stack[-1]+1:i])
                #so our i will change according to that 
                newI = i - (oldStrLen - newStrLen)
                expandedString = number * s[stack[-1]+1:i]
                s = s[0:stack[-1]-numberLen] + expandedString + s[i+1:]            
                stack.pop()
                i = newI
            i = i + 1
        print s
                
    def decodeString(self, s):
        self.logic(s)
        """
        :type s: str
        :rtype: str
        """
#Main
obj = Solution()
obj.decodeString("3[a]2[bc]")

obj = Solution()
obj.decodeString("3[a6[c]]")

obj = Solution()
obj.decodeString("2[abc]3[cd]ef")

obj = Solution()
obj.decodeString("100[leetcode]")
