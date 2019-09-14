# Pyramid Transition Matrix
# https://leetcode.com/problems/pyramid-transition-matrix/
class Solution(object):
    def __init__(self):
        self.matrix = None
        self.chars = []

    def fillMatrix(self, allowed):
        self.matrix = [[[] for col in range(len(self.chars))] for row in range(len(self.chars))]
        for triplet in allowed:
            first = self.chars.index(triplet[0])
            second = self.chars.index(triplet[1])
            third = self.chars.index(triplet[2])
            # list(set(list))) prevents from adding duplicates
            self.matrix[first][second] = list(set(self.matrix[first][second] + [triplet[2]]))
        print "The matrix is"
        for r in range(len(self.matrix)):
            print self.matrix[r]

    # A recurrssive function to get all possible top layers for given bottom layer.
    def getTopLayers(self, bottom, index, currentTopLayer, topLayers):
        if(index == len(bottom)-1):
            topLayers.append(currentTopLayer)
            return
        first = self.chars.index(bottom[index])
        second = self.chars.index(bottom[index+1])
        for topTile in self.matrix[first][second]:
            self.getTopLayers(bottom, index+1, currentTopLayer+topTile, topLayers)
                        

    def dfs(self, bottom):
        if(len(bottom) == 1):
            return True
        # get top layers for current bottom layers
        topLayers = []
        self.getTopLayers(bottom, 0, "", topLayers)
        # do dfs with the topLayers
        for topLayer in topLayers:
            if(self.dfs(topLayer)):
                return True
        
        
    def pyramidTransition(self, bottom, allowed):
        if not allowed:
            return False
        # get all the chars
        self.chars = list(set("".join(allowed)))
        self.chars.sort()
        # fil the matrix where if we have a triplet such as abc
        # in matrix we fill matrix[a][b] =[c]
        self.fillMatrix(allowed)
        print self.dfs(bottom)
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
# Main
allowed = ["BCG", "CDE", "GEA", "FFF", "BCF"]
bottom = "BCD"
obj = Solution()
obj.pyramidTransition(bottom, allowed)

allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
bottom = "AABA"
obj = Solution()
obj.pyramidTransition(bottom, allowed)

# borrowed the idea for getTopLayers function from Pt1 written by me of the same program.
# borrowd the idea of filling the matrix from leetcode solution
print "1) So the first thing we do is construct the matrix"
print "If the allowed triplet is abc in matrix we append matrix[a][b] = [c]"
print "2) for a given bottom layer, we get all possible top layers for it"
print "3) with all the top layers for a given bottom layer, we do a simple dfs"
print "There is 2 layers of recurrssion in this program, 1 for gettin all top layers for a given bottom layer"
print "and another for doing dfs with them"
print "remember to separate out the 2 recurrssive funcitons"
