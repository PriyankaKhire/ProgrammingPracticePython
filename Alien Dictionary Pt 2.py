# Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
class Solution(object):
    def __init__(self):
        self.chars = None
        self.matrix = None
        self.indegree = None

    def bfs(self):
        # letters with indegree 0 can be potential roots of trees so add them to queue
        queue = [self.chars[i] for i in range(len(self.indegree)) if self.indegree[i] == 0]
        visited = [False for i in range(len(self.chars))]
        while(queue):
            top = queue.pop(0)
            if(visited[top] == True):
                print "there is a cycle"
                return ""
            # mark top visited
            

    def fillMatrix(self, words):
        for i in range(len(words)-1):
            print words[i], words[i+1]
            for letter in range(min(len(words[i]), len(words[i+1]))):
                # we only care about the first different letter
                if(words[i][letter] != words[i+1][letter]):
                    r = self.chars.index(words[i][letter])
                    c = self.chars.index(words[i+1][letter])
                    self.matrix[r][c] = 1
                    # letter at index r has a directed edge going from it to letter at index c
                    # so letter at index c has indegree of +1
                    self.indegree[c] = self.indegree[c] + 1
                    break
        
    def alienOrder(self, words):
        # get all the alphabets
        self.chars = list(set("".join(words)))
        # sort them.
        self.chars.sort()
        # create a graph matrix
        self.matrix = [[0 for col in range(len(self.chars))] for row in range(len(self.chars))]
        # currently the indegree of all nodes of matrix is zero
        self.indegree = [0 for i in range(len(self.chars))]
        # fill the graph matrix
        self.fillMatrix(words)
        # perform a simple bfs
        self.bfs()
        
        

# Main
obj = Solution()
obj.alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"])
