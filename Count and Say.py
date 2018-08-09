#Count and Say
#https://leetcode.com/problems/count-and-say/description/
class Solution(object):
    
    def say(self, n):
        string = str(n)
        count = 1
        sayCount = ""
        i = 0
        for i in range(1, len(string)):
            if(string[i] != string[i-1]):
                sayCount = sayCount+str(count)+str(string[i-1])
                count = 1
            else:
                count = count +1
        sayCount = sayCount+str(count)+str(string[i])
        return sayCount
        
    def countAndSay(self, n):
        count = 1
        #count
        for i in range(1, n):
            count = self.say(count)
        return str(count)
    
#Main
o = Solution()
print o.countAndSay(5)
