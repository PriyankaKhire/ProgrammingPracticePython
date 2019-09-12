class Solution(object):
    def __init__(self):
        self.hash = {
            0:[1,3],
            1:[4,0,2],
            2:[5,1],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
            }

    def logic(self, queue, visited):
        if not queue:
            return -1
        if(queue[0][-1] == "123450"):
            return len(queue[0])-1
        top = queue.pop(0)
        currStr = top[-1]
        #get index of zero
        zeroIndex = currStr.index('0')
        for nextMove in self.hash[zeroIndex]:
            currStr = list(currStr)
            currStr[zeroIndex], currStr[nextMove] = currStr[nextMove], currStr[zeroIndex]
            # if this state has been unvisited before.
            if(not "".join(currStr) in visited):
                queue.append(top+["".join(currStr)])
                visited.append("".join(currStr))
            #Backtrack
            currStr[zeroIndex], currStr[nextMove] = currStr[nextMove], currStr[zeroIndex]
        return self.logic(queue, visited)

    def slidingPuzzle(self, puzzle):
        #Convert it to string
        string = ""
        for row in puzzle:
            for col in row:
                string = string + str(col)
        print self.logic([[string]], [string])
            

# Main
obj = Solution()
obj.slidingPuzzle([[1,2,3],[4,0,5]])

obj = Solution()
obj.slidingPuzzle([[1,2,3],[5,4,0]])

obj = Solution()
obj.slidingPuzzle([[4,1,2],[5,0,3]])

obj = Solution()
obj.slidingPuzzle([[3,2,4],[1,5,0]])
