# IP to CIDR
# https://leetcode.com/problems/ip-to-cidr/
class Solution(object):

    def findNextIp(self, ipArray, index):
        if(index == -1):
            return ipArray
        if(ipArray[index]+1 > 255):
            ipArray[index] = 0
            return self.findNextIp(ipArray, index-1)
        ipArray[index] = ipArray[index]+1
        return ipArray
        
    def convertToBinary(self, n, output):
        if(n == 0):
            return  "0"*(8-len(output))+output
        return self.convertToBinary(n/2, str(n%2)+output)

    def findNumberOfZerosInEndBits(self, ip):
        # convert ip to binary
        binary = ""
        for addrBlock in ip.split("."):
            binary = binary + self.convertToBinary(int(addrBlock), "")
        zeroCount = 0
        for i in range(len(binary)-1, -1, -1):
            if(binary[i] == '0'):
                zeroCount = zeroCount + 1
            else:
                return zeroCount

    def findAddresses(self, ip, n, output):
        originalIP = ip
        if(n == 0):
            print output
            return
        # find number of zeros in the end bits of binary representation of ip
        zeroCount = self.findNumberOfZerosInEndBits(ip)
        # the current address can cover 2^zeroCount addresses
        if((2**zeroCount) < n):
            print "Do nothing here"
        else:
            while(int(2**zeroCount) > n):
                zeroCount = zeroCount -1
        n = n - int(2**zeroCount)
        for i in range(int(2**zeroCount)):
            ipArray =  self.findNextIp([int(i) for i in ip.split(".")], len(ip.split("."))-1)
            ip = ".".join([str(i) for i in ipArray])
        output.append(originalIP+"/"+ str(32-int(zeroCount)))
        self.findAddresses(ip, n, output)
            
        
    def ipToCIDR(self, ip, n):
        # We need 'n' contigious ips.
        self.findAddresses(ip, n, [])
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """

# Main
obj = Solution()
obj.ipToCIDR("255.0.0.7", 30)

obj.ipToCIDR("238.104.165.250", 540)
