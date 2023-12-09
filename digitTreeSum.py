# digitTreeSum
# https://app.codesignal.com/interview-practice/question/2oxNWXTS8eWBzvnRB/description
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def inOrder(node, number, output):
    if not node:
        return
    if (not node.left and not node.right):
        output.append(number+str(node.value))
        return
    inOrder(node.left, number+str(node.value), output)
    inOrder(node.right, number+str(node.value), output)
    
def solution(t):
    output = []
    inOrder(t, "", output)
    addition = 0
    for digit in output:
        addition += int(digit)
    return addition
