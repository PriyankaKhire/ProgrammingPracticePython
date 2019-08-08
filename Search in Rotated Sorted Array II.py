#Search in Rotated Sorted Array II
#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
'''
Essentially it's search in rotated sorted array but with duplicates.
In most cases you can apply the same logic but what about  cases like
[1, 3, 1, 1] in that case you move to the right to find the next larger value
but what about cases like [1, 1, 1, 1, 1] in that case if the element to be searched is not present
in the array then the time complexity would be O(n)
so for this problem, the average case time complexity is O(log n)
but worst case is O(n)
'''
