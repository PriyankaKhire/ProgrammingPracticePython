#Add Binary
#Difficulty:Easy
#
#Given two binary strings, return their sum (also a binary string).
#
#The input strings are both non-empty and contains only characters 1 or 0.
#
#Example 1:
#
#Input: a = "11", b = "1"
#Output: "100"
#Example 2:
#
#Input: a = "1010", b = "1011"
#Output: "10101"

class AddBinary(object):
    def __init__(self):
        self.answer = ""

    #if one number is short then pad it with zeros by the difference of the 2 numbers
    def padWithZeros(self, num, numberOfZeros):
        for i in range(numberOfZeros):
            num = "0"+num
        return num

    def xor(self, str1, str2):
        return str(int(bool(int(str1)) ^ bool(int(str2))))

    def xnor(self, str1, str2):
        xor_answer = self.xor(str1, str2)
        return str(int(not int(xor_answer)))

    def addition(self, num1, num2, carry, i1, i2):
        if(i1 < 0 and i2 < 0):
            self.answer = carry+self.answer
            return
        binary1 = num1[i1]
        binary2 = num2[i2]
        i1 = i1-1
        i2 = i2-1
        if carry == "0":
            self.answer = self.xor(binary1, binary2)+self.answer
            if(binary1 == "1" and binary2 == "1"):
                carry = "1"
        else:
            #if carry = 1
            self.answer = self.xnor(binary1, binary2)+self.answer
            if(binary1 == "0" and binary2 == "0"):
                carry = "0"
        self.addition(num1, num2, carry, i1, i2)
            
        

    def solution(self, num1, num2):
        if(len(num1) < len(num2)):
            num1 = self.padWithZeros(num1, len(num2)-len(num1))
        elif(len(num2) < len(num1)):
            num2 = self.padWithZeros(num2, len(num1)-len(num2))
        self.addition(num1, num2, "0", len(num1)-1, len(num2)-1)
        print self.answer
        
#Main
o = AddBinary()
o.solution("1010", "1011")
o2 = AddBinary()
o2.solution("11", "11")
