# Binary Searchable Numbers
# https://leetcode.com/discuss/interview-question/352743/Google-or-Onsite-or-Binary-Searchable-Numbers
# tldr: "How many numbers are larger than all elements to their left and smaller than all elements to their right?"
class Solution(object):
    def findBinarySearchableNumbers(self, array):
        print "The array is", array
        # find all numbers that are larger than our current array element, from left to right
        largestSoFarFromLeft = [None for i in range(len(array))]
        # Populate the first element
        largestSoFarFromLeft[0] = array[0]
        # go through the array from left to right
        for i in range(1, len(array)):
            if(array[i] > largestSoFarFromLeft[i-1]):
                largestSoFarFromLeft[i] = array[i]
            else:
                largestSoFarFromLeft[i] = largestSoFarFromLeft[i-1]
        print "Numbers that are larger than all numbers to their left", largestSoFarFromLeft
        # find all numbers that are smaller than our current array element, from right to left
        smallestSoFarFromRight = [None for i in range(len(array))]
        # Populate the last element.
        smallestSoFarFromRight[-1] = array[-1]
        # go through the array from right to left
        for i in range(len(array)-2, -1, -1):
            if(array[i] < smallestSoFarFromRight[i+1]):
                smallestSoFarFromRight[i] = array[i]
            else:
                smallestSoFarFromRight[i] = smallestSoFarFromRight[i+1]
        print "Numbers that are smaller than all the numbers to their right", smallestSoFarFromRight
        # Now all we have to do is find numbers that are same on a particular index in these 2 lists
        sameNumbersOnAnIndex = 0
        for i in range(len(array)):
            if(smallestSoFarFromRight[i] == largestSoFarFromLeft[i]):
                sameNumbersOnAnIndex = sameNumbersOnAnIndex + 1
        print "The binary searchable numbers are", sameNumbersOnAnIndex

# Main
obj = Solution()
obj.findBinarySearchableNumbers([1, 3, 2, 4, 5, 7, 6, 8])
print "\n"
obj.findBinarySearchableNumbers([1, 3, 2])
print "\n"
obj.findBinarySearchableNumbers([2, 1, 3, 5, 4, 6])
print "\n"
obj.findBinarySearchableNumbers([1, 5, 7, 11, 12, 18])
print "\n"
obj.findBinarySearchableNumbers([3, 2, 1])
print "\n"
obj.findBinarySearchableNumbers([5, 4, 6, 2, 8])
