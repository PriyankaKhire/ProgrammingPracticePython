# Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/
class Solution(object):
    def __init__(self):
        self.chars = None
        self.matrix = None
        self.indegree = None

    def bfs(self):
        # letters with indegree 0 can be potential roots of trees so add them to queue
        queue = [[self.chars[i]] for i in range(len(self.indegree)) if self.indegree[i] == 0]
        # so after this if queue was empty that means every one had indegree of 1
        # so there was a cycle.
        visited = [False for i in range(len(self.chars))]
        result = []
        while(queue):
            topList = queue.pop(0)
            #print topList
            top = topList[-1]
            if(visited[self.chars.index(top)] != True):
                # mark top visited
                visited[self.chars.index(top)] = True
                # add it to result
                result.append(top)
            # add all adjacent unvisited nodes to queue
            for i in range(len(self.matrix)):
                if(self.matrix[self.chars.index(top)][i] == 1):
                    if(self.chars[i] in topList):
                        #print "There is a cycle"
                        return ""
                    queue.append(topList+[self.chars[i]])
        # we couldn't cover all vertices that means there is something wrong.
        if(len(result) != len(self.chars)):
            return ""
        return "".join(result)
            

    def fillMatrix(self, words):
        for i in range(len(words)-1):            
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
        print words
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
        print self.bfs()
        
        

# Main
obj = Solution()
obj.alienOrder(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"])

obj = Solution()
obj.alienOrder(["ac","ab","b"])

obj = Solution()
obj.alienOrder(["z", "x", "z"])

obj = Solution()
obj.alienOrder(["z", "x"])

obj = Solution()
obj.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])

obj = Solution()
obj.alienOrder(["dvpzu","bq","lwp","akiljwjdu","vnkauhh","ogjgdsfk","tnkmxnj","uvwa","zfe","dvgghw","yeyruhev","xymbbvo","m","n"])
