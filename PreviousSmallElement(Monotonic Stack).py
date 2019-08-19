# Find the nearest smaller numbers on left side in an array
# https://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/
# We use a data structure called Monotonic Stack.
# Monotonic Stack contains the elements which are either increasing only or decreasing only.
class Solution(object):
    def findPreviousLessElement(self, array):
        print "The given array is",array
        print "Here we use Monotonic stack to solve this porblem"
        stack = []
        answer = []
        print "Instead of directly pushing the element itself, here for simplicity, we push the index.\n"
        for i in range(len(array)):
            print "The stack is",stack
            print "Popping all elements that are greater than our current element",array[i]
            # remove all elements that are larger than current element.
            while(stack and array[stack[-1]] > array[i]):
                print "The stack top",array[stack[-1]],"is larger than",array[i]
                print "Popping",array[stack.pop()]
                print "The stack after popping is",stack
            # if stack is empty our current element does not have a previous minimum element
            if not stack:
                print "Since the stack is empty we dont have any previous small element to current element",array[i]
                answer.append(None)
            # else the top element is the previous small element.
            else:
                print "The previous small element to",array[i],"is",array[stack[-1]]
                answer.append(array[stack[-1]])
            # finally push current index on stack
            stack.append(i)
        print "The list of all previous small elements is",answer

# Main
obj = Solution()
obj.findPreviousLessElement([3, 7, 8, 4])
print "=-"*30,"\n"
obj.findPreviousLessElement([1, 6, 4, 10, 2, 5])
print "=-"*30,"\n"
obj.findPreviousLessElement([1, 3, 0, 2, 5])
