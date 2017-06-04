#Partition of a set into K subsets with equal sum

#Given an integer array of N elements, the task is to divide this array into
#K non-empty subsets such that the sum of elements in every subset is same.
#All elements of this array should be part of exactly one partition.

#Global
res = []

#Condition input array cannot contain duplicates
def getRestElements(curSet, array):
    return [x for x in array if x not in curSet]
    
def getSumOfSet(curSet):
    s = 0
    for element in curSet:
        s+= element
    return s

def getSets(array, subSets, s, result, index):
    print "the array is "+str(array)
    print "subSet is "+str(subSets)
    print "result so far "+str(result)
    print "sum of subset "+str(getSumOfSet(subSets))
    global res
    #Find elements in array that add up to given sum
    if not array:
        print "\nCongratulations we found the result"
        res = result
        return True
    #if cur Set sum == s then add it to result 
    if(getSumOfSet(subSets) == s):
        print "sum is equal in subset"
        result.append(subSets)
        array = getRestElements(subSets, array)
        print "the result now is "+str(result)
        print "the array now is "+str(array)
        if(getSets(array, [], s, result, 0)):
            return True
        else:
            #BackTrack
            print "backtracking"
            array += result.pop()
            print array
            print result
            print "*****"
    if(getSumOfSet(subSets) > s):
        return False
    for i in range(index, (len(array))):
        print "adding element "+str(array[i])+" to subset"+str(subSets)
        subSets.append(array[i])
        print "the subset now is "+str(subSets)
        if(getSets(array, subSets, s, result, i+1)):
            return True
        else:
            #Backtrack
            print "backtracking and removing the element "
            subSets.pop()
        

def getKminusOneSets(curSet, array, k):
    curSetSum = getSumOfSet(curSet)
    restElements = getRestElements(curSet, array)
    #if there are no rest of the elements and k != 1
    if not restElements and k!=1:
        return
    #Here the problem boils down to here is the sum and find sets with this sum
    getSets(restElements, [], curSetSum, [], 0)
    if not res:
        print "there exists no solution"
        return
    if len(res) == (k-1):
        print "we found solution"
        print curSet
        print res
        return
    print "We found solution but not k sets"
    print curSet
    print res

def generateSubsets(array, result, index, k):
    print "$$$$$"
    print "for set "+str(result)
    if result:
        getKminusOneSets(result, array, k)
    if index == len(array):
        return
    for i in range(index, len(array)):
        result.append(array[i])
        generateSubsets(array, result, i+1, k)
        result.pop()
    

#Main  program
generateSubsets([2,3,1,4], [], 0, 2)
print "\n\n\n\n"
generateSubsets([2, 1, 4, 5, 6], [], 0, 3)
#Now that this program works accordingly to how i want, I only need to
#Modify it in such a way that it doesnt unnecessarily calculate the sets
#https://stackoverflow.com/questions/3866528/equal-k-subsets-algorithm
#http://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/
