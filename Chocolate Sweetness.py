#Chocolate Sweetness
#https://leetcode.com/discuss/interview-question/350800/Google-or-Onsite-or-Chocolate-Sweetness
'''
Given an array chocolate of n non-negative integers,
where the values are sweetness levels of the chocolate.
You are also given a value k which denotes the number of
friends you will share this chocolate with.
Your friends are greedy so they will always take the highest sweetness chunk.
Find out what is the maximum sweetness level you could get.

tltr: Split the array into k non-empty continuous subarrays.
Write an algorithm to maximize the minimum sum among these k subarrays.

Example:

Input: chocolate = [6, 3, 2, 8, 7, 5], k = 3
Output: 9
Explanation:
The values in array are sweetness level in each chunk of chocolate. Since k = 3, so you have to divide this array in 3 pieces,
such that you would get maximum out of the minimum sweetness level. So, you should divide this array in
[6, 3] -> 6 + 3 = 9
[2, 8] -> 2 + 8 = 10
[7, 5] -> 7 + 5 = 12
Your other two friends will take the sweetest chunk, so they will take 12 and 10. The maximum sweetness level you could get is 9.
'''
# Variation of https://leetcode.com/problems/split-array-largest-sum/
class Solution(object):
    def __init__(self):
        self.minSweetness = None
        
    def canWeSplitIntoSubArrayWithGreaterOrEqualGivenSum(self, array, k, givenSum, output, index):
        if(index == len(array)):
            if(len(output) == k):
                return True
            return
        subArray = []
        for i in range(index, len(array)):
            subArray.append(array[i])
            if(sum(subArray) >= givenSum):
                output.append(subArray)
                if(self.canWeSplitIntoSubArrayWithGreaterOrEqualGivenSum(array, k, givenSum, output, i+1)):
                    return True
                output.pop()

    def binarySearch(self, array, k, low, high):
        if(low > high):
            return
        mid = (low+high)/2
        print "Testing for sweetness",mid,"is is possible?",bool(self.canWeSplitIntoSubArrayWithGreaterOrEqualGivenSum(array, k, mid, [], 0))
        if(bool(self.canWeSplitIntoSubArrayWithGreaterOrEqualGivenSum(array, k, mid, [], 0))):
            self.minSweetness = mid
            # Try to go on the higher side
            self.binarySearch(array, k, mid+1, high)
        else:
            self.binarySearch(array, k, low, mid-1)
                
    def splitChocolate(self, array, k): 
        # Here the lowes sweetness one could get is
        lowSweetness = min(array)
        # The highest sweetness one could get is
        highSweetness = sum(array)
        # Checking for all sweetness levels
        # Hint: run this program to see a trend.
        for i in range(lowSweetness, highSweetness+1):
            print "Can we split chocolate to at least",i,"sweetness?",bool(self.canWeSplitIntoSubArrayWithGreaterOrEqualGivenSum(array, k, i, [], 0))
        print "We can also do the above using binary search"
        self.binarySearch(array, k, lowSweetness, highSweetness)
        print "I'll get bar of sweetness",self.minSweetness,"that's the best I can do"
        """
        :type array: List[int]
        :type k: int
        :rtype: int
        """

#Main
array = [6, 3, 2, 8, 7, 5]
obj = Solution()
obj.splitChocolate(array, 3)
