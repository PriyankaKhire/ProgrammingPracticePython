# Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, node, low, high, s):
        if not node:
            return
        self.inorder(node.left, low, high, s)
        if (node.val >= low and node.val <= high):
            s[0] = s[0] + node.val
        self.inorder(node.right, low, high, s)
        
    def rangeSumBST(self, root, low, high):
        s = [0]
        self.inorder(root, low, high, s)
        return s[0]
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
