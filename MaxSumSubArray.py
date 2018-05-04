#Largest Sum Sub array
#https://leetcode.com/problems/maximum-subarray/description/

class windowApproach(object):
    def __init__(self, inputArray):
        self.inputArray = inputArray

    def add(self, leftIndex, rightIndex):
        array_sum = 0
        if(leftIndex == rightIndex):
            return self.inputArray[rightIndex]
        for i in range(leftIndex, rightIndex+1):
            array_sum = self.inputArray[i] + array_sum
        return array_sum
            
    def solution(self):
        #we use window approach here
        #Window from 0 to 0
        maxSum = -999
        left = 0
        right = 0
        #if at any given point of time, if the window is 1 then we return
        for rightIndex in range(len(self.inputArray)):
            windowSum = 0
            leftIndex = 0
            print "right Index "+str(rightIndex)
            while(leftIndex <= rightIndex):
                print "left index "+str(leftIndex)
                windowSum = self.add(leftIndex, rightIndex)
                print "window sum "+str(windowSum)                
                if(maxSum < windowSum):
                    maxSum = windowSum
                    left = leftIndex
                    right = rightIndex
                leftIndex = leftIndex+1
        print "max sum "+str(maxSum)
        print "left index "+str(left)
        print "right index "+str(right)
        print "This approach takes O(n^3) because of the way add function is written \n it can take O(n^2) if we modify the add function "

class kadnaneApproach(object):
    def __init__(self, inputArray):
        self.inputArray = inputArray

    #here instead of thinking that i want window from i to j, why not think that you want window from
    # 0 to j
    #that means we calculate sum from 0 to j at any given point of time.
    #if at any given point of time the sum becomes -ve we make it 0. because we dont care about -ve sum

    def solution(self):
        maxSum = 0
        sumFromZeroToj = 0
        right = 0
        for j in range(0, len(self.inputArray)):
            sumFromZeroToj = sumFromZeroToj + self.inputArray[j]
            print "Sum from 0th index to "+str(j)+"th index is "+str(sumFromZeroToj)
            if (sumFromZeroToj < 0):
                print "since sum is negative we make it 0"
                sumFromZeroToj = 0
            if(sumFromZeroToj > maxSum):
                maxSum = sumFromZeroToj
                right = j
        print "max sum "+str(maxSum)
        print "right Index "+str(right)

        #Now to find left index
        for i in range(right, -1, -1):
            maxSum = maxSum - self.inputArray[i]
            if(maxSum==0):
                print "left Index is "+str(i)
        print "This approach takes O(n) time"





#Main Program
wa = windowApproach([-2,1,-3,4,-1,2,1,-5,4])
wa.solution()
ka = kadnaneApproach([-2,1,-3,4,-1,2,1,-5,4])
ka.solution()
