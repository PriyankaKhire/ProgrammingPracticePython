# Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/
# took help from
# https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/
class Solution(object):

    def invertSignsOfArrayElements(self, A):
        for i in range(len(A)):
            A[i] = -A[i]
            
    def ifAllNegative(self, A):
        for num in A:
            if(num > 0):
                return False
        return True

    def kadane(self, A):
        maxEndingHere = [0 for i in range(len(A))]
        # initialize first element for max ending here
        if(A[0] > 0):
            maxEndingHere[0] = A[0]
        for i in range(1, len(A)):
            if(maxEndingHere[i-1]+A[i] > 0):
                maxEndingHere[i] = maxEndingHere[i-1]+A[i]
        return max(maxEndingHere)

    def circularMaxSum(self, A):
        # i) get sum of array
        arraySum = sum(A)
        # ii) invert signs of current array elements
        self.invertSignsOfArrayElements(A)
        # iii) find kadane for this new array
        kadaneSum = self.kadane(A)
        # iv) the max sum is
        return arraySum+kadaneSum
    
    def maxSubarraySumCircular(self, A):
        # 1) if all elements are negative
        if(self.ifAllNegative(A)):
            return max(A)
        # 2) if normal kadane gives the max sum
        maxSumSubArray = self.kadane(A)
        # 3) if max sum obtained by circular elements
        maxSumCircularSubArray = self.circularMaxSum(A)
        # which ever is the larger of the two is the answer
        print max(maxSumSubArray, maxSumCircularSubArray)
        """
        :type A: List[int]
        :rtype: int
        """

# Main
obj = Solution()
obj.maxSubarraySumCircular([11, 10, -20, 5, -3, -5, 8, -13, 10])
        
