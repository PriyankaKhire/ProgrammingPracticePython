# IP to CIDR
# https://leetcode.com/problems/ip-to-cidr/
'''
https://freedomly.tk/2017/12/29/LeetCode-751-IP-to-CIDR/
Chinese translated explanation:
First explain the meaning of 29 in 255.255.0.8/29:
An IPv4 address has a total of 32 bits,
The 29 indicates that the first 29 bits of the IP are fixed, and the last three bits can be changed,
so 2^3 = 8 IPs can be overwritten.
So to make CIDR as small as possible, let the number of fixed IP bits be as small as possible, and ensure that the IP is contigious.

For example, we start with 255.0.0.7 and n = 30  so we need to cover 30 addresses, then there are:
255.0.0.7/32
Only one IP address remaining 30 - 1 = 29

The next IP address is 255.0.0.8, the last 8 digits are: 00001000, and 3 more bits can be changed.
Then there are 255.0.0.8/29 which can cover 8 IPs, and the remaining 29 - 8 = 21

The IP after 8 addresses is 255.0.0.16, the last 8 bits are: 00010000, and 4 bits can be changed.
Then there are 255.0.0.16/28 which can cover 16 IPs, and the remaining 21 - 16 = 5

The next IP after 16 addresses is 255.0.0.32, the last 8 bits are: 00100000, there are 5 bits that can be changed,
This covers 32 addresses and the remaining IP to be covered is only 5 (n=5),
32 exceeds the remaining n=5.
How about we change 4 bits instead of 5,  this covers 16 addresses, still too large
how about we change it to 3, this coveres 8 addresses, still too large
how about we change it to 2, this covers 4 addresses, 
Then there are 25.0.32/30 to cover 4 IPs, and the remaining 5 - 4 = 1

Then the last one to cover is 255.0.0.36/32, and the remaining 0 are to be overwritten.
At this point, you can get the least CIDR.
'''
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
        print "The binary representation of ip is", binary, "We are just omitting the periods for now coz there is no need for it"
        # count the number of zeros at the end.
        zeroCount = 0
        for i in range(len(binary)-1, -1, -1):
            if(binary[i] == '0'):
                zeroCount = zeroCount + 1
            else:
                return zeroCount

    def findAddresses(self, ip, n, output):
        # we save ip coz we are changing ip further.
        originalIP = ip
        print "The current IP is", originalIP, "Currently n is",n
        if(n == 0):
            print output
            return
        # find number of zeros in the end bits of binary representation of ip
        zeroCount = self.findNumberOfZerosInEndBits(ip)
        print "The number of zeros at the end are", zeroCount
        print "The current address can cover",(2**zeroCount),"addresses that have same",(32-zeroCount),"prefix bits"
        # the current address can cover 2^zeroCount addresses
        if((2**zeroCount) < n):
            print "Since ",(2**zeroCount),"<",n
        else:
            while(int(2**zeroCount) > n):
                print "Since ",(2**zeroCount),">=",n
                print "How about we increase 1 prefix bit by reducing the number of zeros"
                zeroCount = zeroCount -1
                print "The current address can cover",(2**zeroCount),"addresses that have same",(32-zeroCount),"prefix bits" 
        n = n - int(2**zeroCount)
        print "The new n is",n
        # find the next address that is NOT covered under our original ip.
        for i in range(int(2**zeroCount)):
            ipArray =  self.findNextIp([int(i) for i in ip.split(".")], len(ip.split("."))-1)
            ip = ".".join([str(i) for i in ipArray])
        # add cidr version of this ip
        output.append(originalIP+"/"+ str(32-zeroCount))
        print "-"*30
        self.findAddresses(ip, n, output)
        
    def ipToCIDR(self, IP, n):
        print "Let's understand the rules of the problem"
        print "1) We need 'n' contigious ips."
        print "2) We can only convert last bit zeros to 1 and not the other way round.\n"
        print "Rule 2 explanation:\n","*"*20
        print "Let's say the given IP is 255.0.0.7 "
        print "Then the binary representation of this is 11111111.00000000.00000000.00000111"
        print "For this IP address there are no zeros at the end, there are only 1s\n"
        print "Let's take another example 255.0.0.8"
        print "Then the binary representation of this is 11111111.00000000.00000000.00001000"
        print "There are 3 zeros at the end\n"
        print "Let's take another example 255.0.0.9"
        print "Then the binary representation of this is 11111111.00000000.00000000.00001001"
        print "There are no zeros at the end\n"
        print "Let's take another example 255.0.0.10"
        print "Then the binary representation of this is 11111111.00000000.00000000.00001010"
        print "There is 1 zero at the end\n"
        print "We need the number of contigious zeros at the end of binary representation of the IP"
        print "Why do we care so much about the zeros at the end ?"
        print "Let's take example 255.0.0.8"
        ip = "255.0.0.8"
        for i in range(8):
            print ip, "->", ".".join([self.convertToBinary(int(addrBlock), "") for addrBlock in ip.split(".")])
            ipArray =  self.findNextIp([int(i) for i in ip.split(".")], len(ip.split("."))-1)
            ip = ".".join([str(i) for i in ipArray])
        print "See anything in common?"
        print "They all have the first 29 bits in common"
        print "That is they all have 11111111.00000000.00000000.00001<end 3 bits> in common"
        print "Thus 255.0.0.8 can host 8 ip addresses (including it self) under it that have 29 bits common"
        print "Thust the CIDR 255.0.0.8/29 gives us 8"
        print "The CIDR 255.0.0.7/32 gives us only 1 (it self), "
        print "which means 255.0.0.7 can only host 1 ip address it with 32 bits in common"
        print "Comin back to CIDR 255.0.0.8/29 gives us 8, did you notice 2^3 = 8"
        print "And 3 is the number of zeros at the end of binary representation of 255.0.0.8"
        print "Let's see how we solve the problem with this information now\n"
        self.findAddresses(IP, n, [])
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """

# Main
obj = Solution()
obj.ipToCIDR("255.0.0.7", 30)

#obj.ipToCIDR("238.104.165.250", 540)
