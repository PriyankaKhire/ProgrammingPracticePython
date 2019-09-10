#Maximum Number of Nights You Can Accommodate
'''
Given a set of numbers in an array which represent number of consecutive nights of AirBnB
reservation requested, as a host, pick the sequence which maximizes the number of days of
occupancy, at the same time, leaving at least 1 day gap in between bookings for cleaning.
Problem reduces to finding max-sum of non-consecutive array elements.
Note: all array elements will be positive.
'''
class Backtracking(object):
    def __init__(self):
        self.largestSum = 0
        
    def logic(self, array, index, output):
        # len(array)-2 because, we cannot pick last element if n-2th element is picked
        if(index >= len(array)-2):
            self.largestSum = max(sum(output), self.largestSum)
            return
        for i in range(index+2, len(array)):
            self.logic(array, i, output+[array[i]])
            
    def maxSum(self, array):
        for i in range(len(array)):
            self.logic(array, i, [array[i]])
        print self.largestSum

# https://www.youtube.com/watch?v=UtGtF6nc35g
class TusharRoyVideo(object):
    
    def logic(self, array):
        # tells me the max sum I can get till this point including this number
        incl = 0
        # tells me the max sum I can get till this point excluding this number.
        excl = 0
        for i in range(len(array)):
            #print "i=",i, "incl=",incl, "excl=",excl
            old_incl = incl
            incl = max(incl, array[i]+excl)
            excl = old_incl
        #print "incl=",incl, "excl=",excl
        return max(incl, excl)
                
    def maxSum(self, array):
        print self.logic(array)

# took some time to come up with this method, is also based on video
class MyDP(object):
    def logic(self, array):
        # including the current element, whats the max sum?
        incl = []
        # excluding the current element, whats the max sum?
        excl = []
        # for i = 0 incl will always be array[0] because including 0th index element the max sum can only be array[0]
        # and excl will always be 0 because nothing before 0th index element.
        incl.append(array[0])
        excl.append(0)
        # now the rule is that elements cannot be adjacent
        # so to include the current element we'd need to go back 2 steps and get the max sum there was
        # and if we exclude the current element, we'd need to go back just 1 step and get the max sum
        # for i=1, going back 2 steps is 0, and -1, and since -1 aint in index, we can just say that
        # including current element, the max sum was the current element it self, just like for i=0 case
        # but excluding the current element the current sum was max(incl[0], excl[0])
        incl.append(array[1])
        excl.append(max(incl[0], excl[0]))
        for i in range(2, len(array)):
            incl.append(array[i] + max(incl[i-2], excl[i-2]))
            excl.append(max(incl[i-1], excl[i-1]))
        return max(incl[-1], excl[-1])        
        
    def maxSum(self, array):
        if(len(array) == 1):
            return array[0]
        if(len(array) == 2):
            return max(array)
        # for this method to work we need array size of at least 3 or more.
        print self.logic(array)
        # time complexity, O(n)

# Main
print "Backtracking, came up with it by my self, took 15 mins to code fully working"
obj = Backtracking()
obj.maxSum([5, 5, 10, 100, 10, 5])

obj = Backtracking()
obj.maxSum([1, 2, 3])

obj = Backtracking()
obj.maxSum([1, 20, 3])

obj = Backtracking()
obj.maxSum([4,1,1,4,2,1])

obj = Backtracking()
obj.maxSum([2,5,3,1,7])

print "Tushar roy video logic, do not understand"
obj = TusharRoyVideo()
obj.maxSum([4,1,1,4,2,1])

obj = TusharRoyVideo()
obj.maxSum([5, 5, 10, 100, 10, 5])

print "My dp method, similar to video but I came up with it"
obj = MyDP()
obj.maxSum([5, 5, 10, 100, 10, 5])

obj = MyDP()
obj.maxSum([1, 2, 3])

obj = MyDP()
obj.maxSum([1, 20, 3])

obj = MyDP()
obj.maxSum([4,1,1,4,2,1])

obj = MyDP()
obj.maxSum([2,5,3,1,7])
