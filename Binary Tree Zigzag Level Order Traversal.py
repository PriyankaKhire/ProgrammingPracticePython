# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def logic(self, root):
        q = [[root,0]]
        hashTable = {}
        while(q):
            topArray = q.pop(0)
            top = topArray[0]
            level = topArray[1]
            if not(level in hashTable):
                hashTable[level] = [top.val]
            else:
                hashTable[level].append(top.val)
            print top.val
            if(top.left):
                q.append([top.left, level+1])
            if(top.right):
                q.append([top.right, level+1])
        return hashTable
                
    def zigzagLevelOrder(self, root):
        if not root:
            return
        ht = self.logic(root)
        print ht
        output = []
        for key in ht:
            if(key%2 != 0):
                ht[key].reverse()
            output.append(ht[key])
        return output
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
