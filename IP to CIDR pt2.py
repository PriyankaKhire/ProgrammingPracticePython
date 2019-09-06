#IP to CIDR
class CIDR(object):
    def __init__(self, binary, ip):
        self.mainIP = ip
        self.binaryIp = binary
        self.placeOfAllOnes = []
        self.ipsUnderThis = []
        
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

    def findIfCurrentIpHasOneInAllRightPlaces(self, placeOfAllOnes, ip):
        for placeOfOne in placeOfAllOnes:
            if(ip[placeOfOne] != '1'):
                return False
        return True

    def findPlacesOfAllOnes(self, binaryIp):
        onePlaces = []
        for i in range(len(binaryIp)):
            if(binaryIp[i] == '1'):
                onePlaces.append(i)
        return onePlaces

    def createCIDRNode(self, ip):
        cidr = CIDR(ip[0], ip[1])
        cidr.placeOfAllOnes = self.findPlacesOfAllOnes(ip[0])[:]
        return cidr

    def convertToBinary(self, num, output):
        if (num == 0):
            # return the zero padded output
            return '0'*(8-len(output))+output
        return self.convertToBinary(num/2, str(num%2)+output)

    def findCommonPrefix(self, ips):
        binaryIps = []
        for i in range(len(ips)):
            ip = ips[i]
            print ip
            print ".".join([self.convertToBinary(int(num), "") for num in ip.split(".")])
            binaryIps.append([".".join([self.convertToBinary(int(num), "") for num in ip.split(".")]), ip])
        # array to hold all cidr blocks
        cidrs = []
        # create cidr for first ip
        cidrs.append(self.createCIDRNode(binaryIps[0]))
        for i in range(1, len(binaryIps)):
            binaryIp = binaryIps[i][0]
            ip = binaryIps[i][1]
            top = cidrs[-1]
            # if the current Ip has 1s in all the places as the main Ip of the top node then we can add it.
            if(self.findIfCurrentIpHasOneInAllRightPlaces(top.placeOfAllOnes, binaryIp)):
                top.ipsUnderThis.append(ip)
            else:
                # create cidr node of current ip and add it to cidrs.
                cidrs.append(self.createCIDRNode(binaryIps[i]))
        print [len(cidr.ipsUnderThis) for cidr in cidrs]
        
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
obj.ipToCIDR("238.104.168.0",21)
