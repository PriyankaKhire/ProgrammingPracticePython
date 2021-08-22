# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    # python heaps are different, I want them to sort according to the value of the node so I created a tupel, where first value of tupel is the value of the node and next value is the node itself. This helps heap to sort according to the value of the node.
    def addToHeap(self, heap, node):
        heapq.heappush(heap, (node.val, node))
    
    # This function is to remove empty lists within our input list [[]]
    def removeEmptyListsFromInput(self, lists):
        answer = []
        for l in lists:
            if l:
                answer.append(l)
        return answer
        
    def mergeKLists(self, lists):
        # remove all empty lists in input.
        lists = self.removeEmptyListsFromInput(lists)
        # edge case
        if not lists:
            return
        # Create empty head node.
        head = ListNode()
        ptr = head
        # Create a heap
        heap = []
        # Add all first nodes to heap
        for l in lists:
            self.addToHeap(heap, l)
            # advance the node to it's next node.
            l = l.next
        # Add rest of the nodes to heap.
        while(heap):
            # pop the top node from heap
            (topVal, top) = heapq.heappop(heap)
            # add it to our linked list
            ptr.next = top
            # if this list has next node then add it to heap
            if (top.next):
                self.addToHeap(heap, top.next)
            # advance our list pointer.
            ptr = ptr.next
        # return list head
        return head.next
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
