# IP to CIDR
#https://leetcode.com/problems/ip-to-cidr/
#https://translate.google.com/translate?hl=en&sl=auto&tl=en&u=https%3A%2F%2Fwww.cnblogs.com%2Fgrandyang%2Fp%2F8440087.html
#https://leetcode.com/problems/ip-to-cidr/discuss/151348/Java-Solution-with-Very-Detailed-Explanation-8ms

#Let us first try to understand what the problem is:
#Given an ip address as a string and an intiger n
#we need to find next n IP addressess such that:
#   the next ip address needs to start with same or higher value
#   the slash and number after that following the ip address ex: "255.0.0.7/32"
#   the number 32 represents prefix bits.
#   to understand this better 255.0.0.7 in binary is 11111111 00000000 00000000 00000111
#   the binary representation is in 32 bits. (just count all numbers in binary representation)
#   Now what do you mean when you say prefix ? here since prefix is of 32 bits it just simply means the whole binary representation
#   lets take a different example: 255.0.0.8/29 the binary is 11111111 00000000 00000000 00001000
#   now the prefix number is 29 which means 11111111 00000000 00000000 00001___000 we are only allowed to change the last 3 zeros
#   Note: we can only change 0 to 1 and not other way round meaning
#   if the address was 11111111 00000000 00000000 00001___111 we wouldnt be able to change anything so in that case 29 should have to be 32
#Now that we have this confusing problem statement out of the way let's reiterate what we have learnt so far
# given ip address and integer n we need to find next n ip addressess along with their prefixes so we know that ip address along with its prefix covers how many ip addressess.
class Solution(object):

    def return8bitBinary(self, num):
        binary = ""
        num = int(num)
        while num > 0:
            binary = str(num%2) + binary
            num = num/2
        return (8 - len(binary))*"0"+binary
    
    def convertIPToBinary(self, ip):
        binary = ""
        for num in ip.split("."):
            print num
            self.return8bitBinary(num)
        
    def ipToCIDR(self, ip, n):
        self.convertIPToBinary(ip)
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
#Main
obj = Solution()
obj.ipToCIDR("255.0.0.7", 10)
