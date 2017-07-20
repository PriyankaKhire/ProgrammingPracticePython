#Longest Bitonic Subsequence
#This solution only works if the array elements are unique
#http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/

def getSubsequence(a, i, d):    
    print "The lenght of longest biotonic subsequence is "+str(i[len(a)-1]+d[len(a)-1]-1)


def foo(a):
    increasing = [1 for col in range(len(a))]
    decreasing = [1 for col in range(len(a))]
    for current in range(len(a)):
        previous = current -1
        while(previous >= 0):
            if(a[previous] > a[current]):
                #then the current sequence is decreasing
                decreasing[current] = max(decreasing[current], decreasing[previous]+1)
            else:
                #Then this is increasing sub sequence
                increasing[current] = max(increasing[current], increasing[previous]+1)
            previous -=1
    print a
    print increasing
    print decreasing
    getSubsequence(a, increasing, decreasing)
    print "*****"

#Main Program
foo([1, 11, 2, 10, 4, 5, 2, 1])
foo([12, 11, 40, 5, 3, 1])
foo([80, 60, 30, 40, 20, 10])
#Does not work for this case
foo([3,4,5,6,2,1])
