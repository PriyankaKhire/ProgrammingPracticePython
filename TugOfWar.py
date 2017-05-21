#Tug of War

#Given a set of n integers, divide the set in two subsets of n/2 sizes each such that
#the difference of the sum of two subsets is as minimum as possible.
#If n is even, then sizes of two subsets must be strictly n/2 and if n is odd,
#then size of one subset must be (n-1)/2 and size of other subset must be (n+1)/2.

'''
The proposed solution for this problem is to generate all possible subsets of size n/2 and then see the
difference between them.
Print subset with least difference
'''
def getSum(arr):
    arrSum = 0
    for element in arr:
        arrSum += element
    return arrSum

def getDif(setOne, setTwo):
    sumOne = getSum(setOne)
    sumTwo = getSum(setTwo)
    return abs(sumOne - sumTwo)

def getRest(mainSet, result):
    otherSet = []
    for element in mainSet:
        if element not in result:
            otherSet.append(element)
    return otherSet
    
def subSet(mainSet, result, index, n):
    global difference
    if(len(result) == n):
        otherSet = getRest(mainSet, result)
        dif = getDif(otherSet, result)
        if(dif < difference):
            difference = dif
            leftSet = otherSet
            print leftSet
            print result
            print dif
    for i in range(index, len(mainSet)):
        result.append(mainSet[i])
        subSet(mainSet, result, i+1, n)
        element = result.pop()

def foo(mainSet):
    n = 0
    if(len(mainSet)%2 == 0):
        n = len(mainSet)/2
    else:
        n = (len(mainSet)/2) + 1
    subSet(mainSet, [], 0, n)

    

#Main Program
difference = 9999999
foo([3, 4, 5, -3, 100, 1, 89, 54, 23, 20])
print "*****"
difference = 999999
foo([23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4])

