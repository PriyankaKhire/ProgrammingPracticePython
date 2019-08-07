#Peak Index in a Mountain Array
#https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution(object):
    
    def binarySearch(self, A, low, high):
        if(low == high):
            return low
        mid = (low+high)/2
        if(mid-1 >= 0 and mid+1 < len(A)):
            if(A[mid-1] < A[mid] and A[mid] > A[mid+1]):
                return mid
            if(A[mid-1] < A[mid] and A[mid] < A[mid+1]):
                # go right
                return self.binarySearch(A, mid+1, high)
            if(A[mid-1] > A[mid] and A[mid] > A[mid+1]):
                # go left
                return self.binarySearch(A, low, mid-1)
        if(mid-1 < 0 and mid+1 < len(A)):
            if(A[mid] > A[mid+1]):
                return mid
            if(A[mid] < A[mid+1]):
                # go right
                return self.binarySearch(A, mid+1, high)
        if(mid-1 >= 0 and mid+1 >= len(A)):
            if(A[mid-1] < A[mid]):
                return mid
            if(A[mid-1] > A[mid]):
                # go left
                return self.binarySearch(A, low, mid-1)
            
        
    def peakIndexInMountainArray(self, A):
        return self.binarySearch(A, 0, len(A)-1)
        """
        :type A: List[int]
        :rtype: int
        """
        
