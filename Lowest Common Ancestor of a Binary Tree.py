#Lowest Common Ancestor of a Binary Tree
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#I am giving you inorder and preorder travarsals of the tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self, inorder, preorder):
        self.inorderStr = inorder
        self.preOrderStr = preorder
        self.inorderHash = {}
    '''    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorderStr.append(root.val)
            self.inorder(root.right)
    '''      
    def insertInorderHash(self):
        for i in range(len(self.inorderStr)):
            if not(self.inorderStr[i] in self.inorderHash):
                self.inorderHash[self.inorderStr[i]] = i
    '''
    def preOrder(self, root):
        if root:
            self.preOrderStr.append(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)
    '''
    #returns which side the child is of the parent in inorder travarsal
    def whichSide(self, parent, child):
        childIndex = self.inorderHash[child]
        parentIndex = self.inorderHash[parent]
        if(parentIndex == childIndex):
            return "Equal"
        if(parentIndex > childIndex):
            return "Left"
        else:
            return "Right"
        
    def lowestCommonAncestor(self, p, q):
        #self.inorder(root)
        #self.preOrder(root)
        self.insertInorderHash()
        print self.inorderHash
        
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

#Main
o = Solution([6, 5, 7, 2, 4, 3, 0, 1, 8], [3, 5, 6, 2, 7, 4, 1, 0, 8])
o.lowestCommonAncestor(5,1)

#Notes:
'''
no need for preorder travarsal we can just take the tree and inorder travarsal and the
travarsal hash and give the tree root and figure out.
very similar to deserilization of binary tree
not going to complete it.
'''
