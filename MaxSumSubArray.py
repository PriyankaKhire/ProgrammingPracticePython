#Largest Sum Sub array
#https://leetcode.com/problems/maximum-subarray/description/

class windowApproach(object):
    def __init__(self, inputArray):
        self.inputArray = inputArray

    def solution(self):
        #we use window approach here
        #if at any given point of time, if the window is 1 then we return
        for rightIndex in range(len(self.inputArray)):
            for leftIndex in range(rightIndex):
                print leftIndex
                print rightIndex
            print "---"





#Main Program
wa = windowApproach([-2,1,-3,4,-1,2,1,-5,4])
wa.solution()
