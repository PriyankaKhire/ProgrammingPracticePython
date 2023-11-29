# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, left, right):
        if (left == None and right == None):
            return True
        if (not left and right):
            return False
        if (not right and left):
            return False
        if (left.val != right.val):
            return False
        side1 = self.inOrder(left.left, right.right)
        side2 = self.inOrder(left.right, right.left)
        return (side1 and side2)

    def isSymmetric(self, root):
        return self.inOrder(root.left, root.right)
        """
        :type root: TreeNode
        :rtype: bool
        """
        
