#IP to CIDR
class Solution(object):

    def addOneToIPArray(self, array, index):
        if(index == -1):
            return
        array[index] = array[index] + 1
        if(array[index] > 255):
            array[index] = 0
            self.addOneToIPArray(array, index-1)

    def getNextIP(self, ip):
        # convert ip address into array of int numbers.
        array = [int(addr) for addr in ip.split(".")]
        # add one to that address
        self.addOneToIPArray(array, len(array)-1)
        # convert array back to string for joining
        array = [str(addr) for addr in array]
        ip = ".".join(array)
        return ip

    def convertToBinary(self, num, output):
        if (num == 0):
            # return the zero padded output
            return '0'*(8-len(output))+output
        return self.convertToBinary(num/2, str(num%2)+output)

    def findCommonPrefix(self, ips):
        for i in range(len(ips)):
            ip = ips[i]
            print ip
            print [self.convertToBinary(int(num), "") for num in ip.split(".")]
            
        
    def ipToCIDR(self, ip, n):
        # first get all n ips
        ips = [ip]
        for i in range(1, n):
            ip = self.getNextIP(ip)
            ips.append(ip)
        print ips
        self.findCommonPrefix(ips)
        

# Main
obj = Solution()
obj.ipToCIDR("255.0.0.7", 10)
