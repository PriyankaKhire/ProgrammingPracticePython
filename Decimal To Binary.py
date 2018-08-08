#Decimal to Binary

def decimalToBinary(decimalNum):
    array = []
    while(decimalNum > 0):
        binaryBit = decimalNum%2
        array.append(binaryBit)
        decimalNum = decimalNum/2
    #reverse the array and convert it to string
    binaryNumber = ""
    for num in reversed(array):
        binaryNumber = binaryNumber+str(num)
    return binaryNumber

#Main
print decimalToBinary(10)
