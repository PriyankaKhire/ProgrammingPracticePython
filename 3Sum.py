#3Sum
#https://leetcode.com/problems/3sum/description/

class Approch1(object):
    def __init__(self, array):
        self.array = array
        #sort the array time O(n log n)
        self.array.sort()

    def twoSum(self, lowPtr, restSum):
        highPtr = len(self.array)-1
        while(lowPtr < highPtr):
            if(self.array[lowPtr]+self.array[highPtr] == restSum):
                return True, self.array[lowPtr], self.array[highPtr]
            if(self.array[lowPtr]+self.array[highPtr] > restSum):
                highPtr = highPtr-1
            else:
                lowPtr = lowPtr+1
        return False, -1, -1

    def solution(self):
        output = []
        for i in range(len(self.array)):
            firstNum = self.array[i]
            restNumSum = 0 - firstNum
            #find rest 2 numbers that add up to restNumSum
            flag, secondNum, thirdNum = self.twoSum(i+1, restNumSum)
            if flag:
                output.append([firstNum, secondNum, thirdNum])
        print output
            
            
                

#Main
o = Approch1([-1, 0, 1, 2, -1, -4])
o.solution()
