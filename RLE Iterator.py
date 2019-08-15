# RLE Iterator
# https://leetcode.com/problems/rle-iterator/solution/
class RLEIterator(object):

    def __init__(self, A):
        self.A = A
        """
        :type A: List[int]
        """
        
    def next(self, n):
        for i in range(n):
            print self.A
            while(self.A and self.A[0] == 0):
                self.A.pop(0)
                self.A.pop(0)
            if not self.A:
                return -1
            top = self.A[1]
            self.A[0] = self.A[0] - 1
        return top
        """
        :type n: int
        :rtype: int
        """
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
# Main
obj = RLEIterator([3,8,0,9,2,5])
print obj.next(2)
print obj.next(1)
print obj.next(1)
print obj.next(2)
