# Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postOrder(self, node, p, q, answer):
        if not node:
            return 
        leftFound = self.postOrder(node.left, p, q, answer)
        rightFound = self.postOrder(node.right, p, q, answer)
        # if found in left subtree and right sub tree
        if (leftFound and rightFound):
            # then append to the answer
            answer.append(node)
            return
        # if one of the nodes is the value
        if (node == p or node == q):
            # then current node is lca
            if (leftFound or rightFound):
                answer.append(node)
                return
            # else return true since we found node in the sub tree.
            return True
        # if we find nothing, then we just propogate the answer from the below subtree to pass it to root.Ellipsis
        if (leftFound or rightFound):
            return True
        
            
    def lowestCommonAncestor(self, root, p, q):
        answer = []
        self.postOrder(root, p, q, answer)
        return answer[0]
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
