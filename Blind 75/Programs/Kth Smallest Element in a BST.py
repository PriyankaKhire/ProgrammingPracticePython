# Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self, node, k):
        if not node:
            return
        # see if kth element lies in left sub tree
        leftElement = self.inOrder(node.left, k)
        # reduce the value of k and see if k is 0. 
        k[0] = k[0]-1
        if (k[0] == 0):
            return node.val
        # see if kth element lies in right sub tree
        rightElement = self.inOrder(node.right, k)
        # if we found the element in any of the subtrees then return it.
        if (leftElement != None):
            return leftElement
        if (rightElement != None):
            return rightElement
        
    def kthSmallest(self, root, k):
        return self.inOrder(root, [k])
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
