# largestValuesInTreeRows
# https://app.codesignal.com/interview-practice/question/m9vC4ALaAeudkwRTF/description

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    if not t:
        return []
    # Key = depth val = [list of all node values at that depth]
    hashTable = {}
    # the queue has [node, depth]
    queue = [[t,0]]
    while(queue):
        # get top node from queue
        top = queue.pop(0)
        # add the depth and node value to hash table
        if not top[1] in hashTable:
            hashTable[top[1]] = []
        hashTable[top[1]].append(top[0].value)
        # add top's children to queue with new depth
        if (top[0].left):
            queue.append([top[0].left, top[1]+1])
        if (top[0].right):
            queue.append([top[0].right, top[1]+1])
    # go through hash table to find max value at each depth
    output = []
    for key in hashTable:
        output.append(max(hashTable[key]))
    return output
