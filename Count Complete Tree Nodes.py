# Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
'''
Still need to work on this approch, its incomplete. do it on leetcode.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.level = None
        
    def findLeftMostLevel(self, root):
        level = 0
        ptr = root
        while(ptr):
            level = level+1
            ptr = ptr.left
        return level
    
    def findRightMostLevel(self, root):
        level = 0
        ptr = root
        while(ptr):
            level = level + 1
            ptr = ptr.right
        return level
    
    def calculateTotalNodesInTreeGivenLevel(self, level):
        nodeCount = 0
        for i in range(level):
            nodeCount = nodeCount + (2**i)
        return nodeCount
    
    def numberOfNodesAtLevel(self, level):
        return (2**(level-1))-1
    
    def findNode(self, low, high, nodePosToFind, node, level):
        if(level == self.level-1):
            # either node exists
            if(low == nodePosToFind):
                return node.left
            if(high == nodePosToFind):
                return node.right
            #or it doesnt
            return None
        if(nodePosToFind-low > high-nodePosToFind):
            # go right
            return self.findNode((low+high)/2, high, nodePosToFind, node.right, level+1)
        elif(nodePosToFind-low < high-nodePosToFind):
            # go left
            return self.findNode(low, (low+high)/2, nodePosToFind, node.left, level+1)
    
    def binarySearch(self, low, high, root, lastFoundNodes):
        if(low >= high):
            print low
            return
        # goal to find first node who's right siblings are missing and all left are present.
        mid = (low+high)/2
        midNode = self.findNode(low, high, mid, root,1)
        if(midNode != None):
            lastFoundNodes.append(midNode)
            self.binarySearch(mid, high, root, lastFoundNodes)
        else:
            self.binarySearch(low, mid, root, lastFoundNodes)
        
    
    def countNodes(self, root):
        llevel = self.findLeftMostLevel(root)
        rlevel = self.findRightMostLevel(root)
        # tree is complete.
        if(llevel == rlevel):
            return self.calculateTotalNodesInTreeGivenLevel(llevel)
        self.level = llevel
        nodesSupposedToBeAtLastLevel = self.numberOfNodesAtLevel(llevel)
        self.binarySearch(0, nodesSupposedToBeAtLastLevel, root, [])
        """
        :type root: TreeNode
        :rtype: int
        """
        
