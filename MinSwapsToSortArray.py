# Minimum number of swaps required to sort an array
# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
'''
My initial thought was also BFS, but that's coz I misunderstood the problem, I thought you can only swap with adjacent elements.
But here all you need to do is to swap the element and put it in its right position.
So I looked at the time and space complexity with which they have solved it on https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
They used O(nlogn) time and O(n) space.
Cool so I guess I can solve with that.
First you sort the array and put it in a different variable
array   = [1, 3, 5, 2, 4, 6, 7]
sorted =  [1, 2, 3, 4, 5, 6, 7]
See the elements 1, 6, 7 they are already in their correct sorted position.
The rest of the elements that are not in their correct position, let's call them NotInTheirCorrectPositionElements
the total number of swaps required to put these NotInTheirCorrectPositionElements elements is
length(NotInTheirCorrectPositionElements) - 1
I even checked with examples given here -> https://www.hackerrank.com/challenges/minimum-swaps-2/problem
and thats the answer.
But this is wrong, see the example 3
'''
class Solution(object):
    def Approch1(self, array):
        print "The array is", array
        # sort array and put it in different variable.
        sortedArray = [element for element in sorted(array)]
        # go through both the arrays and find elements that are not in their correct position
        numberOfElementsNotInTheirCorrectPosition = 0
        for i in range(len(array)):
            if(array[i] != sortedArray[i]):
                numberOfElementsNotInTheirCorrectPosition = numberOfElementsNotInTheirCorrectPosition + 1
        print "The number of elements not in their correct sorted position is", numberOfElementsNotInTheirCorrectPosition
        print "Thus the total number of swaps required to sort this arrya is", numberOfElementsNotInTheirCorrectPosition-1
        
        
# Main
obj = Solution()
obj.Approch1([1, 3, 5, 2, 4, 6, 7])
print "\n"
obj.Approch1([1, 2, 3, 4])
print "\n"
obj.Approch1([3, 4, 1, 2])
print "But you see the answer you give is 3 but the real answer is 2"
print "[3, 4, 1, 2] -> [1, 4, 3, 2] -> [1, 2, 3, 4]"
