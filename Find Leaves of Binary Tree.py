# Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteLeaves(self, root, leaves):
        if not root:
            return
        self.deleteLeaves(root.left, leaves)
        if (root.left in leaves):
            root.left = None
        if (root.right in leaves):
            root.right = None
        self.deleteLeaves(root.right, leaves)
        
    def getLeaves(self, root, leaves):
        if not root:
            return
        self.getLeaves(root.left, leaves)
        if((not root.left) and (not root.right)):
            leaves.append(root)
        self.getLeaves(root.right, leaves)
        
    def findLeaves(self, root):
        listLeaves = []
        while (root.left or root.right):
            leaves = []
            self.getLeaves(root, leaves)
            leavesValue = [leaf.val for leaf in leaves]
            listLeaves.append(leavesValue)
            self.deleteLeaves(root, leaves)
        listLeaves.append([root.val])
        return listLeaves
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
