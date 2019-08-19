# Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/
# soluiton inspired by this post
# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step

class BruteForce(object):
    
    def allSubArrays(self, A):
        sumOfMins = 0
        print "All sub arrays of A and their mins"
        for start in range(len(A)):
            for end in range(start, len(A)):
                subArray = A[start:end+1]
                print "Sub array is",subArray,"min is", min(subArray)
                sumOfMins = sumOfMins + min(subArray)
        print "Total sum of mins is", sumOfMins
            
    def sumSubarrayMins(self, A):
        print "The given array is", A
        self.allSubArrays(A)
        print "Time complexity O(n^2)"
        """
        :type A: List[int]
        :rtype: int
        """

class MonotonousStackApproch(object):

    def findPreviousSmallElements(self, A):
        stack = []
        answer = [None for i in range(len(A))]
        for i in range(len(A)):
            while(stack and A[stack[-1]] > A[i]):
                stack.pop()
            if not stack:
                answer[i] = None
            else:
                answer[i] = stack[-1]
            stack.append(i)
        print "The indices of elements on the LEFT that are smaller than the current element are", answer
        return answer

    def findNextSmallElements(self, A):
        stack = []
        answer = [None for i in range(len(A))]
        # we do the same processing like how we did in findPreviousSmallElements but just in reverse order
        for i in range(len(A)-1, -1, -1):           
            while(stack and A[stack[-1]] > A[i]):
                stack.pop()
            if not stack:
                answer[i] = None
            else:
                answer[i] = stack[-1]
            stack.append(i)
        print "The indices of elements on the RIGHT that are smaller than the current element are", answer
        return answer
    
    def isCurrElementMinInSubArraysOfA(self, currElement, A):
        total = 0
        presentButNotMin = []
        for start in range(len(A)):
            for end in range(start, len(A)):
                if(min(A[start:end+1]) == A[currElement]):
                    print A[start:end+1]
                    total = total + 1
                else:
                    # find those sub arrays where our current element is present but is not min
                    if(A[currElement] in A[start:end+1]):
                        presentButNotMin.append(A[start:end+1])
        print "Total =",total
        print "These are the sub arrays where",A[currElement],"is present but not min"
        print presentButNotMin

    def restOfExplanation(self, A, currElementIndex, previousSmall, nextSmall):
        print "Now for our current element",A[currElementIndex]
        print "Why we find previousSmall ?"
        if(previousSmall[currElementIndex] == None):
            print "There are no elements on LEFT that are smaller than our current element"
            print "Which means, what ever sub array between the indices 0 to",currElementIndex,"that have",A[currElementIndex],"towards the END"
            print "There are",(currElementIndex-0),"sub arrays that end with",A[currElementIndex]
        else:
            print "The index of the element on LEFT that is smaller that our current element is",previousSmall[currElementIndex]
            print "Which means, what ever sub array between the indices",previousSmall[currElementIndex]+1,"to",currElementIndex,"that have",A[currElementIndex],"towards the END"
            print "There are",(currElementIndex-previousSmall[currElementIndex]),"sub arrays that end with",A[currElementIndex]
        print "They all have",A[currElementIndex],"as their min element"
        print "Why we find nextSmall ?"
        if(nextSmall[currElementIndex] == None):
            print "There are no elements on RIGHT that are smaller than our current element"
            print "Which means, what ever sub array between the indices",currElementIndex,"to",len(A)-1,"that have",A[currElementIndex],"towards the START"
            print "There are",len(A)-currElementIndex,"sub arrays that start with",A[currElementIndex]
        else:
            print "The index of the element on RIGHT that is smaller that our current element is",nextSmall[currElementIndex]
            print "Which means, what ever sub array between the indices",currElementIndex,"to",nextSmall[currElementIndex]-1,"that have",A[currElementIndex],"towards the START"
            print "There are",nextSmall[currElementIndex]-currElementIndex,"sub arrays that start with",A[currElementIndex]
        print "They all have",A[currElementIndex],"as their min element"
        print "You can see the sub arrays above if the indices are not clear"
        print "Ya i know the calculation for sub arrays is a bit weird, just look at the post if you are confused"
        print "So the total sub arrays with",A[currElementIndex],"is, sub arrays to left * sub arrays to right"
        left = 0
        if(previousSmall[currElementIndex] == None):
            left = currElementIndex
        else:
            left = currElementIndex-previousSmall[currElementIndex]
        if(left == 0):
            # coz we cant multiply by 0
            left = 1
        right = 0
        if(nextSmall[currElementIndex] == None):
            right = len(A)-currElementIndex
        else:
            right = nextSmall[currElementIndex]-currElementIndex
        if(right == 0):
            # coz we cant multiply by 0
            right = 1
        print "Which is",left*right,"Compare this value to total number of sub arrays and you'll know what I mean"
        print "And since the original point of the quesiton was to add all these min elements we just multiply the value of current element to this number"
        print "that is",left*right*A[currElementIndex]
        return left*right*A[currElementIndex]
           
        
            
    def sumSubarrayMins(self, A):
        print "The given array is", A
        print "Let's find their previous small element"
        previousSmall = self.findPreviousSmallElements(A)
        print "Now let's find their next small element"
        nextSmall = self.findNextSmallElements(A)
        print "Now let's take each element of array individually"
        answer = 0
        for i in range(len(A)):
            print "In how many sub arrays is",A[i],"the min element"
            self.isCurrElementMinInSubArraysOfA(i, A)
            answer = answer + self.restOfExplanation(A, i, previousSmall, nextSmall)
            print "-"*40
        print "So the final answer is",answer
# Main
obj = BruteForce()
obj.sumSubarrayMins([3,1,2,4])
print "=-"*30,"\n"
obj = MonotonousStackApproch()
obj.sumSubarrayMins([3,1,2,4])
