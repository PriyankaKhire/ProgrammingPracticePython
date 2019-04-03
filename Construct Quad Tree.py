#Construct Quad Tree
#https://leetcode.com/problems/construct-quad-tree/
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def createNode(self, val, isLeaf):
        return Node(val, isLeaf, None, None, None, None)
    
    def logic(self, grid, topLeft, bottomLeft, topRight, bottomRight):
        #print topLeft, bottomLeft, topRight, bottomRight
        if(topLeft == bottomLeft and topRight == bottomRight and topLeft == bottomRight):
            node = self.createNode(grid[topLeft[0]][topLeft[1]], True)
            return node
        #row mid and col mid
        colMid = (topLeft[1]+topRight[1])/2
        rowMid = (topLeft[0]+bottomLeft[0])/2
        #topLeft node
        topLeftNode = self.logic(grid, topLeft, [rowMid, bottomLeft[1]], [topRight[0], colMid], [rowMid, colMid])
        #bottomLeft node
        bottomLeftNode = self.logic(grid, [rowMid+1, topLeft[1]], bottomLeft, [rowMid+1, colMid], [bottomRight[0], colMid])
        #topRight node
        topRightNode = self.logic(grid, [topLeft[0], colMid+1], [rowMid, colMid+1], topRight, [rowMid, bottomRight[1]])
        #bottomRight Node
        bottomRightNode = self.logic(grid, [rowMid+1, colMid+1], [bottomLeft[0], colMid+1], [rowMid+1, topRight[1]], bottomRight)
        #take all 4 nodes and see if their valuse are equal if they are then create a node and call that leaf.
        if(topLeftNode.val == bottomLeftNode.val and topRightNode.val == bottomRightNode.val and topLeftNode.val == bottomRightNode.val):
            node = self.createNode(bottomRightNode.val, True)
        else:
            node = self.createNode("*", False)
            node.topLeft = topLeftNode
            node.topRight = topRightNode
            node.bottomLeft = bottomLeftNode
            node.bottomRight = bottomRightNode
        return node
    
    def construct(self, grid):
        node = self.logic(grid, [0,0], [len(grid)-1, 0], [0, len(grid)-1], [len(grid)-1, len(grid)-1])
        print node
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

#Main
grid1 = [
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0]
    ]
grid2 = [
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,1],
    [0,0,1,1]
    ]
grid3 = [
    [1,1,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0],
    [1,1,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,0,0],
    [1,1,1,1,1,1,0,0]]
obj = Solution()
obj.construct(grid3)
