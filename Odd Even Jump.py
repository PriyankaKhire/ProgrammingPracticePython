# Odd Even Jump
# https://leetcode.com/problems/odd-even-jump/
'''
Notes: I tried to understand the monotonic stack solution, but couldn't.
'''
class Solution(object):
            
    def oddJump(self, A):
        oddJumps = [None for i in range(len(A))]
        for currElementIndex in range(len(A)-1):
            selectedElementIndex = None
            for nextElementIndex in range(currElementIndex+1, len(A)):
                # 1) you jump to the index j such that A[i] <= A[j]
                if(A[currElementIndex] <= A[nextElementIndex]):
                    # 2) A[j] is the smallest possible value.
                    if(selectedElementIndex == None or A[nextElementIndex] < A[selectedElementIndex]):
                        selectedElementIndex = nextElementIndex
                    # 3) If there are multiple such indexes j, you can only jump to the smallest such index j.
                    elif(A[nextElementIndex] == A[selectedElementIndex]):
                        selectedElementIndex = min(nextElementIndex, selectedElementIndex)
            oddJumps[currElementIndex] = selectedElementIndex
        return oddJumps

    def evenJump(self, A):
        evenJumps = [None for i in range(len(A))]
        for currElementIndex in range(len(A)-1):
            selectedElementIndex = None
            for nextElementIndex in range(currElementIndex+1, len(A)):
                # 1) you jump to the index j such that A[i] >= A[j]
                if(A[currElementIndex] >= A[nextElementIndex]):
                    # 2) A[j] is the largest possible value.
                    if(selectedElementIndex == None or A[nextElementIndex] > A[selectedElementIndex]):
                        selectedElementIndex = nextElementIndex
                    # 3) If there are multiple such indexes j, you can only jump to the smallest such index j.
                    elif(A[nextElementIndex] == A[selectedElementIndex]):
                        selectedElementIndex = min(nextElementIndex, selectedElementIndex)
            evenJumps[currElementIndex] = selectedElementIndex
        return evenJumps
                
    def oddEvenJumps(self, A):
        print "The array is",A
        odd = self.oddJump(A)
        even = self.evenJump(A)
        print odd
        print even
        goodStartingIndexCount = 0
        for i in range(len(A)-1):
            print "Starting from index",i
            # since we start with jump 1 we start with odd jump first
            jumpIndex = odd[i]
            print "With our first jump we are now at index",jumpIndex
            # already jumped once now we are on jump number 2
            jumpNumber = 2
            # this is to keep track of previous jumpIndex
            prevJumpIndex = None
            while(jumpIndex != None and jumpIndex < len(A)):
                prevJumpIndex = jumpIndex
                if(jumpNumber%2 == 0):
                    # even jump
                    jumpIndex = even[jumpIndex]
                    print "With EVEN jump we are at index",jumpIndex
                else:
                    # odd jump
                    jumpIndex = odd[jumpIndex]
                    print "With ODD jump we are at index",jumpIndex
                jumpNumber = jumpNumber + 1
            print "We have stopped at index",jumpIndex
            if(prevJumpIndex == len(A)-1):
                goodStartingIndexCount = goodStartingIndexCount + 1
                print "The current index was a good starting index"
            print "*"*30
        # the last index will always be a good index to jump from coz we are already there, so we add 1 to goodStartingIndexCount
        print "Total good starting indices are",goodStartingIndexCount+1
        """
        :type A: List[int]
        :rtype: int
        """
# Main
obj = Solution()
obj.oddEvenJumps([10,13,12,14,15])
print "\n"
obj.oddEvenJumps([2,3,1,1,4])
