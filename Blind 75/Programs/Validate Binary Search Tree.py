# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # inorder traversal of BST is alwasy sorted in ascending order.
    def inOrder(self, node, traversal):
        if not node:
            return
        self.inOrder(node.left, traversal)
        traversal.append(node.val)
        self.inOrder(node.right, traversal)
    
    # validate if the traversal is in ascending order or not.
    def validate(self, traversal):
        for i in range(1, len(traversal)):
            if (traversal[i-1] >= traversal[i]):
                return False
        return True
        
    def isValidBST(self, root):
        traversal = []
        self.inOrder(root, traversal)
        return self.validate(traversal)
        """
        :type root: TreeNode
        :rtype: bool
        """
        
