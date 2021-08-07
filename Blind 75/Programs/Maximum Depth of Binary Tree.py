# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDepth(self, node, depth, maxDepth):
        if not node:
            maxDepth[0] = max(depth, maxDepth[0])
            return
        self.findDepth(node.left, depth+1, maxDepth)
        self.findDepth(node.right, depth+1, maxDepth)
            
    def maxDepth(self, root):
        maxDepth = [0]
        self.findDepth(root, 0, maxDepth)
        return maxDepth[0]
        """
        :type root: TreeNode
        :rtype: int
        """
        
