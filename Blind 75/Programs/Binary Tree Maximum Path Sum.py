# Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postOrder(self, node, maxSum):
        if not node:
            # if the node doesn't exists we return 0 sum.
            return 0
        sumLeft = self.postOrder(node.left, maxSum)
        sumRight = self.postOrder(node.right, maxSum)
        print "Current node", node.val
        print "Current left sum", sumLeft
        print "Current right sum", sumRight
        print "*"*20
        sumSoFar = sumLeft + sumRight + node.val
        # calculate max sum
        # we need to chose max betwee, 
        # previous max, left+right sub tree (sumSoFar)
        # left sub tree, right sub tree, or just the current node.
        maxSum[0] = max(maxSum[0], sumSoFar, node.val+sumLeft, node.val+sumRight, node.val)
        # return sum of the path so far
        # just like above we need to chose between
        # just the left sub tree, just the right sub tree or just the current node.
        # Note: we can't chose the entire sub tree(sumSoFar) becasue then we are telling that the path ends there.
        return max(node.val+sumLeft, node.val+sumRight, node.val)
        
    def maxPathSum(self, root):
        maxSum = [-float('inf')]
        self.postOrder(root, maxSum)
        return maxSum[0]
        """
        :type root: TreeNode
        :rtype: int
        """
        
