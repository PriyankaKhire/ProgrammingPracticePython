# Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        # Key: depth Val: [list of values]
        self.traversal = {}
    
    def iterativeBFS(self, root):
        queue = [[root, 0]]
        while(queue):
            [topNode, depth] = queue.pop(0)
            # Add it to travarsal tree
            if (depth not in self.traversal):
                self.traversal[depth] = []
            self.traversal[depth].append(topNode.val)
            # add left and right childern to queue.
            if(topNode.left):
                queue.append([topNode.left, depth+1])
            if(topNode.right):
                queue.append([topNode.right, depth+1])
        
    def levelOrder(self, root):
        if not root:
            return root
        self.iterativeBFS(root)
        # fill the list of lists from the hash table.
        traversalList = [self.traversal[key] for key in self.traversal]
        return traversalList
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
