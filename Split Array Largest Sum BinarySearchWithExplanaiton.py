# Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/
class SolutionWtihExplanation(object):
    def __init__(self):
        self.givenSums = []
        self.possibleToSplitArray = []
        self.recordLowestSum = None

    def binarySearchToGetMinSumOfLargestSumOfSubArrays(self, array, m, low, high):
        if(low > high):
            return
        print "The low is",low,"The high is", high
        mid = (low+high)/2
        print "The mid is", mid,"this mid now acts as our given sum"
        canWeSplitIntoMSubArrays = bool(self.splitArrayToSubArraysWithLessOrEqualGivenSum(array, m, mid, [], 0))
        print "Can we split the array into",m,"subArrays, when given sum is", mid,"?",canWeSplitIntoMSubArrays
        if(canWeSplitIntoMSubArrays):
            print "Recording ",mid," as the lowest sum we have seen so far"
            self.recordLowestSum = mid
            self.binarySearchToGetMinSumOfLargestSumOfSubArrays(array, m, low, mid-1)
        else:
            self.binarySearchToGetMinSumOfLargestSumOfSubArrays(array, m, mid+1, high)

    def splitArrayToSubArraysWithLessOrEqualGivenSum(self, array, m, givenSum, output, index):
        # doesn't this funciton look oddly similar to findAllSubArraysOfSizeM function
        if(index == len(array)):
            print output
            if(len(output) == m):
                return True
            return
        subArray = []
        for i in range(index, len(array)):
            subArray.append(array[i])
            if(sum(subArray) <= givenSum):
                output.append(subArray)
                if(self.splitArrayToSubArraysWithLessOrEqualGivenSum(array, m, givenSum, output, i+1)):
                    return True
                output.pop()
                

    def canWeSplitArrayToMSubArrayWithLessOrEqualGivenSum(self, array, m, givenSum):
        # it is worth noting here that the integers are non-negative in the array
        print "The sub arrays that have sum less than or equal to given sum are:"
        canSplitToMSubArrays = bool(self.splitArrayToSubArraysWithLessOrEqualGivenSum(array, m, givenSum, [], 0))
        print "Can we split ", array, " to",m, "sub arrays ?", canSplitToMSubArrays
        self.givenSums.append(givenSum)
        self.possibleToSplitArray.append(canSplitToMSubArrays)
        

    def findSumOfSubArrays(self, subArrays):
        print "The sub arrays are ",subArrays
        for subArray in subArrays:
            print "Sum of sub array", subArray,"is",sum(subArray)
        print "-"*50

    # funciton that finds all possible sub arrays of size m
    def findAllSubArraysOfSizeM(self, nums, m, index, output):
        if(index == len(nums)):
            if(len(output) == m):
                self.findSumOfSubArrays(output)
            return
        subArray = []
        for i in range(index, len(nums)):
            subArray.append(nums[i])
            output.append(subArray)
            self.findAllSubArraysOfSizeM(nums, m, i+1, output)
            output.pop()
            
    def splitArray(self, nums, m):
        print "Here we need to split the array into m sub arrays such that"
        print "the indivudial largest sum amongst these sub arrays is the smallest you can get."
        print "\nSplitting the given array into all possible sub arrays we get:\n"
        self.findAllSubArraysOfSizeM(nums, m, 0, [])
        print "Can we do this in a better way ?"
        print "Think..., the largest subArray sum at any given point"
        print "has to be AT LEAST equal to the largest element in the array"
        print "Also, the largest sum cannot increast more than sum of all elements of array."
        print "This tells us that the smallest max subArray sum lies between"
        print "largest element of the array and sum of all elements of the array."
        print "The problme now breaks down into: "
        print "given 'a sum' can we split the array into m sub arrays such that at least 1 sub array has this 'sum'"
        print "and the rest of the arrays have sum less than or equal to this 'sum'."
        print "Since the range of the sum is between largest element of array and sum of all elements of array"
        print "and we need to find the smallest of the largest sum\n"
        for givenSum in range(sum(nums), max(nums)-1, -1):
            print "The given sum is ", givenSum
            self.canWeSplitArrayToMSubArrayWithLessOrEqualGivenSum(nums, m, givenSum)
        print "\nSo now let's look at the cumulative of all these sums and if we can split it into",m,"sub arrays"
        for i in range(len(self.givenSums)):
            print "When the given sum was",self.givenSums[i],"could we split to",m,"subArrays?",self.possibleToSplitArray[i]
        print "\nDo you see a trend?"
        print "Can we use BINARY SEARCH here?"
        print "Again, what was the problem statement ? We need to minimize the largest sum of these sub Arrays"
        self.binarySearchToGetMinSumOfLargestSumOfSubArrays(array, m, max(nums), sum(nums))
        print "Thus the lowest recorded sum we have seen is",self.recordLowestSum
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

#Main
array = [7,2,5,10,8]
obj = Solution()
obj.splitArray(array, 2)
