# Quick Select Algorithm
# https://www.geeksforgeeks.org/quickselect-algorithm/
# https://en.wikipedia.org/wiki/Quickselect
'''
Quickselect is a textbook algorithm typically used to
solve the problems "find kth something": kth smallest, kth largest, kth most frequent, kth less frequent, etc.
Like quicksort, quickselect was developed by Tony Hoare and is also known as Hoare's selection algorithm.

It has O(N) average time complexity and is widely used in practice.
It is worth noting that its worst-case time complexity is O(N^2), although the probability of this worst-case is negligible.
'''
# Here we will try to return the Kth smallest element

def partition(array, left, right):
    pivot = right
    # shift the right by one so we can compare other elements
    right -= 1
    while(left < right):
        # bring left to a position where all elements behind left are smaller than pivot
        while (left < right and array[left] < array[pivot]):
            left += 1
        # bring right to a position where all elements in front of right are larger than pivot
        while (left < right and array[right] > array[pivot]):
            right -= 1
        # here array[left] > array[pivot] and array[pivot] > array[right] so we swap them
        if (array[left] > array[pivot] > array[right]):
            array[left], array[right] = array[right], array[left]
        # finally putting pivot in it's original position
        if (array[right] > array[pivot]):
            array[right], array[pivot] = array[pivot], array[right]
            pivot = right
    print array, pivot
    return pivot

def quicksort(array, k):
    print array
    pivot = None
    left = 0
    right = len(array) - 1
    while (left < right):
        print "pivot = ", pivot
        print "left", left, "right", right
        pivot = partition(array, left, right)
        print "pivot now is", pivot
        # Kth element is on the left side of the array
        if (pivot == k-1):
            return array[pivot]
        if (pivot > k-1):
            right = pivot - 1
        else:
            left = pivot + 1
    if (left == right == k-1):
        return array[left]


# Main
print quicksort([7, 10, 4, 3, 20, 15], 1)
#print quicksort([1,1,1,2,2,3], 2)