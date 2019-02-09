#Unique Binary Search Trees II
#https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Approch1(object):

    def createCompleteBinarySearchTree(self, nodeSequence):
        output = ["null" for i in range(len(nodeSequence)**2)]
        output[0] = nodeSequence[0]
        for node in range(1, len(nodeSequence)):
            parentIndex = 0
            while(output[parentIndex] != "null"):
                #if current node > than root add it to right
                if(nodeSequence[node] > output[parentIndex]):
                    parentIndex = (2*parentIndex) + 2
                else:
                    # add it to left
                    parentIndex = (2*parentIndex)+1
            #add the node to parentIndex
            output[parentIndex] = nodeSequence[node]
        print output
                
                
            

    def permutation(self, array, output, count):
        if (len(output) == len(array)):
            print output
            self.createCompleteBinarySearchTree(output)
            return
        for i in range(len(array)):
            if(count[i] > 0):
                count[i] = count[i] - 1
                output.append(array[i])
                self.permutation(array, output, count)
                #backtrack
                output.pop()
                count[i] = count[i] + 1
        
        
    def generateTrees(self, n):
        self.permutation([i for i in range(1, n+1)], [], [1 for i in range(n)])

#Main
obj1 = Approch1()
obj1.generateTrees(3)
