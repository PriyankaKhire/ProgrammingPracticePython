#The Great Tree-List Recursion Problem.
from Tree import node
from Tree import createNode
from Tree import addLeft
from Tree import addRight

head = node()
def foo(root, prev):
    global head
    if root == None:
        return
    foo(root.getLeft(), root)
    print prev.getData
    print root.getData()
    if(prev == None):
        print "prev is none so root is head"
        print root.getData()
        #Then current is head
        head = root
    else:
        print "Assigning root to right and prev to left"
        print root.getData()
        print prev.getData()
        root.setRight(prev) 
        prev.setLeft(root) 
    foo(root.getRight(), root)


#Main
root = createNode(1)
node1= addLeft(2, root)
node2 = addRight(3, root)
node3 = addLeft(4, node1)
node4 = addRight(5, node1)
node5 = addLeft(6, node2)
node6 = addRight(7, node2)
#Cannot create this inplace
foo(root, head)
