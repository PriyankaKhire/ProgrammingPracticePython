#Expression Tree
#Given an expression, convert it into expression tree
#for that first you need to convert the expression into post fix expression
#then make the tree out of it.
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class expressionTree():
    def __init__(self, postFixExpression):
        self.exp = postFixExpression

    def inorder(self, root):
        if(root != None):
            self.inorder(root.left)
            print root.data,
            self.inorder(root.right)

    def createNode(self, data):
        node = TreeNode(data)
        return node

    def createTree(self):
        stack = []
        #Push all initial operands into the stack
        i = 0
        while i < len(self.exp):
            #create a node
            n = self.createNode(self.exp[i])
            if not self.exp[i].isalpha():                
                #Pop top 2 nodes from stack
                top1 = stack.pop()
                top2 = stack.pop()
                n.right = top1
                n.left = top2
            stack.append(n)
            i = i+1
        #return stack top that is the root
        return stack.pop()
            


#Main Program
#We assume that we are given post fix expression
o = expressionTree("ab+cde+**")
r = o.createTree()
o.inorder(r)
