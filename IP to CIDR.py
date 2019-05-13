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
    def __init__(self):
        self.binary = None

    def convertBinaryToInt(self, binary):
        index = len(binary) - 1
        intNum = 0
        powerOfTwo = 0
        while(index >= 0):
            intNum = intNum + (int(binary[index])*(2**powerOfTwo))
            powerOfTwo = powerOfTwo + 1
            index = index - 1
        return intNum

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
            binary = binary + " " + self.return8bitBinary(num)
        self.binary = binary

    '''
    def binaryToIntAddition(self, binary, intNum):
        binaryInt = self.convertBinaryToInt(binary)
        addition = int(binaryInt) + int(intNum)
        return addition
    '''

    def findZerosAtEnd(self, binary):
        numZeros = 0
        index = len(binary)-1
        while(index >= 0 and binary[index] != '1'):
            numZeros = numZeros + 1
            index = index - 1
        print numZeros

    def addToIPAddress(self, ip, num):
        #we want to circular add to ip address such that
        #255.255.255.255 + 1 = 0.0.0.1
        ip = ip.split(".")
        ip[-1] = str(int(ip[-1])+num)
        ipAddress = ""
        carry = 0
        for addrSpace in reversed(ip):
            if(int(addrSpace)+carry > 255):
                ipAddress = '0' + '.' + ipAddress
                carry = carry + (int(addrSpace) - 255)
            else:
                ipAddress = str(int(addrSpace)+carry) + '.' + ipAddress
                carry = 0
        ipAddress = ipAddress[:-1]
        if(carry > 0):
            ipAddress = ipAddress.split(".")
            print ipAddress
            ipAddress[-1] = str(int(ipAddress[-1]) + carry)
            ipAddress = '.'.join(ipAddress)
        print ipAddress
        

    def logic(self, n, ip):
        #find how many addressess spaces does the current address cover
        #self.binaryToIntAddition("00001011", 2)
        self.addToIPAddress("255.0.255.255", 2)
        
    def ipToCIDR(self, ip, n):
        self.convertIPToBinary(ip)
        self.logic(n, ip)
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
#Main
obj = Solution()
obj.ipToCIDR("255.0.0.7", 10)
