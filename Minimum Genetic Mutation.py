# Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
class Solution(object):
    
    # returns true if 2 words are different by 1 string
    def isOneAway(self, word1, word2):
        if(word1 == word2):
            return False
        if(len(word1) != len(word2)):
            return False
        oneAway = False
        for i in range(len(word1)):
            if(word1[i] != word2[i]):
                if(oneAway == False):
                    # if one away flag has not been set, then set it.
                    oneAway = True
                else:
                    # the flag was already set, that means the string has more than 1 char different.
                    return False
        return True
                
    def formMatrix(self, bank):
        matrix = [[0 for col in range(len(bank))] for row in range(len(bank))]
        for i in range(len(bank)):
            for j in range(i, len(bank)):
                if(i !=j and self.isOneAway(bank[i], bank[j])):
                    #print "word",bank[i],bank[j],"are one away"
                    matrix[i][j] = 1
                    matrix[j][i] = 1
        return matrix

    def bfs(self, startIndex, endIndex, matrix, bank):
        # the path also includes the start, so we need to subctract 1 from the final min pathLength.
        queue = [[startIndex]]
        pathLength = float("inf")
        while queue:
            topPath = queue.pop(0)
            top = topPath[-1]
            if(top == endIndex):
                pathLength = min(pathLength, len(topPath))
            # get all unvisited neighbors of top
            for n in range(len(bank)):
                if(n != top and matrix[top][n] == 1 and not(n in topPath)):
                    queue.append(topPath+[n])
        if(pathLength == float('inf')):
            return -1
        return pathLength-1
        
    def minMutation(self, start, end, bank):
        if not bank:
            return -1
        # if end is not in bank then we cannot change any string to end
        if not (end in bank):
            return -1
        bank = bank + [start, end]
        bank.sort()
        # remove duplicates
        bank = list(set(bank))
        matrix = self.formMatrix(bank)
        return self.bfs(bank.index(start), bank.index(end), matrix, bank)
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
# Main
start = "AAAAACCC"
end =  "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
obj = Solution()
print obj.minMutation(start, end, bank)

start = "AACCGGTT"
end =  "AACCGGTA"
bank = []
obj = Solution()
print obj.minMutation(start, end, bank)

start = "AAAAAAAA"
end = "CCCCCCCC"
bank = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
obj = Solution()
print obj.minMutation(start, end, bank)
