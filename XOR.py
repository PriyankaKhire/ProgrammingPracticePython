#XOR
class XOR(object):

    def intToBinary(self, num):
        binary = []
        n = num
        while(n>0):
            binary.append(n%2)
            n = n/2
        binary.append(n)
        binary.reverse()
        return binary

    def binaryToInt(self, binary):
        binary.reverse()
        index = 0
        num = 0
        while(index < len(binary)):
            num = num + (binary[index]*(2**index))
            index = index+1
        return num

    def compute(self, binary, prev, index):
        if(index == len(binary)):
            print prev
            return
        if(binary[index] == prev):
            prev = 0
        else:
            prev = 1
        self.compute(binary, prev, index+1)

    def xorOf1Num(self, num):
        print "Xor of number ", num, " is ",
        binary = self.intToBinary(num)
        self.compute(binary, 0, 0)

    def truthTableTill(self, num):
        for i in range(num+1):
            binary = self.intToBinary(i)
            print binary, " = ", 
            self.compute(binary, 0, 0)

    def xorOf2Nums(self, a, b):
        binaryA = self.intToBinary(a)
        binaryB = self.intToBinary(b)
        #pad with 0s
        if(len(binaryA) < len(binaryB)):
            diff = len(binaryB) - len(binaryA)
            binaryA.reverse()
            for i in range(diff):
                binaryA.append(0)
            binaryA.reverse()
        elif(len(binaryB) < len(binaryA)):
            diff = len(binaryA) - len(binaryB)
            binaryB.reverse()
            for i in range(diff):
                binaryB.append(0)
            binaryB.reverse()
        #compute xor
        index = 0
        output = []
        while(index < len(binaryA)):
            if(binaryA[index] != binaryB[index]):
                output.append(1)
            else:
                output.append(0)
            index = index+1
        print "Xor of ",a," and ", b, " is " , self.binaryToInt(output)
        
        
        

#Main
obj = XOR()
obj.xorOf1Num(6)
obj.truthTableTill(6)
obj.xorOf2Nums(13,13)
