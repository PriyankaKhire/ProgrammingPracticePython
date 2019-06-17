#Find Anagram Mappings
#https://leetcode.com/problems/find-anagram-mappings/
class Solution(object):
    def __init__(self):
        self.hashTable = {}
        
    def putInHash(self, B):
        for i in range(len(B)):
            self.hashTable[B[i]] = i
    
    def logic(self, A):
        output = []
        for i in range(len(A)):
            output.append(self.hashTable[A[i]])
        return output
        
    def anagramMappings(self, A, B):
        self.putInHash(B)
        return self.logic(A)
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
#Main
obj = Solution()
print obj.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
