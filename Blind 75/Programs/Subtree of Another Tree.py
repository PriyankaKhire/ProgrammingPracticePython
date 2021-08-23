# Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sameTrees(self, t1, t2):
        # if we reach null node of both trees then return true
        if (not t1 and not t2):
            return True
        # if one tree has nodes, but another doesn't we return false
        if ((not t1) and t2):
            return False
        if (t1 and (not t2)):
            return False
        # if left sub tree is not the same we return False and early terminate.
        if not(self.sameTrees(t1.left, t2.left)):
            return False
        # if values are not same we reutrn false and early terminate without checking further.
        if (t1.val != t2.val):
            return False
        # if right sub tree is not the same we return false and early terminate
        if not(self.sameTrees(t1.right, t2.right)):
            return False
        # else we return true to keep looking further.
        return True
    
    def findSubTree(self, root, subRoot):
        # if it's a null node, we return back.
        if not root:
            return 
        # if we find current node value = subTree root value we check if they are same or not
        if (root.val == subRoot.val):
            if (self.sameTrees(root, subRoot)):
                return True
        # if sub tree found in left sub tree we return true and early terminate.
        if (self.findSubTree(root.left, subRoot)):
            return True
        # if sub tree found in right sub tree we return true and early teminate
        if (self.findSubTree(root.right, subRoot)):
            return True
        
    def isSubtree(self, root, subRoot):
        return self.findSubTree(root, subRoot)
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
