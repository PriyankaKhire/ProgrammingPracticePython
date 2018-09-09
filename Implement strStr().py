#Implement strStr()
#https://leetcode.com/problems/implement-strstr/description/
class Approch1(object):
    def strStr(self, haystack, needle):
        if needle == haystack:
            return 0
        for i in range(len(haystack)):
            j = 0
            k = i
            while(j < len(needle) and k < len(haystack) and haystack[k] == needle[j]):
                k = k+1
                j = j+1
            if(j == len(needle)):
                return i
        return -1
                
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
#Main
o1 = Approch1()
print o1.strStr("hello",  "ll")
