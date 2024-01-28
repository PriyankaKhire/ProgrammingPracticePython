# Given an array with unique elements, generate all sub arrays from that array
class Solution(object):
    
    # Basic Generate all sub arrays, but this implementation can also generate duplicates and duplicate in jumbled order
    def allSubArrays(self, array, subArray, count):
        print count, subArray
        if not array:
            return
        for i in range(len(array)):
            # remove the element at index i
            element = array.pop(i)
            # increase the count, this is to help us understand how many times is this function called
            count[0] += 1
            # add it to subArray
            self.allSubArrays(array, subArray+[element], count)
            # Backtrack by putting the element back in the array
            array.append(element)

    def run(self, nums):
        self.allSubArrays(nums, [], [1])

# Main
obj = Solution()
obj.run([1,2,3,4,5])
