#Longest Increasing Subsequence

#Backtracking solution
def isSafe(res, element):
    #If this is the first element of the array then return true
    if(len(res) == 0):
        return True
    #If element is larger than the last element of the array then it is safe to add it
    if(element > res[len(res)-1]):
        return True  
    return False

#This function gives all possible solutions in backtracking way
def backtrack(a, index, res):
    print res
    if index == len(a):
        return
    for i in range(index, len(a)):
        if(isSafe(res, a[i])):
            res.append(a[i])
            backtrack(a, i+1, res)
            #Backtrack
            res.pop()

#This is the first stage of dp, here we see that how many times a[i] can be included in different LISs            
def dp1(a, index, res, lis):
    print res
    print lis
    if index == len(a):        
        return
    for i in range(index, len(a)):
        if(isSafe(res, a[i])):
            res.append(a[i])
            lis[i] += 1
            dp1(a, i+1, res, lis)
            #Backtrack
            res.pop()

#learning curve, it doesnt work as expected and is wrong
def dp2(a, index, res, lis):
    print res
    print lis
    if index == len(a):        
        return
    for i in range(index, len(a)):
        print "i is at "+str(i)
        print "current result is "+str(res)        
        for j in range(index+1):
            print "j is at "+str(j)
            print "is "+str(a[i])+" safe ? to add to list "+str(res[j])+" "+str(isSafe(res[j], a[i]))
            if(isSafe(res[i], a[i])):
                #We select elements from i to j
                elements = a[i:j+1]
                res[i].extend(elements)
                lis[i] = max(lis[i], lis[j]+1)
        print "now going in recurrssion..."
        dp2(a, i+1, res, lis)
        #Backtrack
        print "backtracking"
        res.pop()

#this is the final dp program        
def dp3(a, res, lis, index):
    if(index == len(a)):
        return
    #By default the max list ending at this index is the element itself
    print "i is at "+str(index)
    res[index].append(a[index])
    print "current result is "+str(res)
    for j in range(index):
        print "j is at "+str(j)
        print "is "+str(a[j])+" < "+str(a[index])+" = "+str(a[j] < a[index])
        if(a[j] < a[index]):
            print "is "+str(lis[j]+1)+" > "+str(lis[index])+" = "+str(lis[j]+1 > lis[index])
            if(lis[j]+1 > lis[index]):
                #Empty the current list
                res[index] = []
                #copy the elements of one list to another, this is required coz python will create pointer
                # when you say res[index] = res[j]
                for element in res[j]:
                    res[index].append(element)
                #Finally append currnt element
                res[index].append(a[index])
                #Basically the above steps show the lis ending at this index
                #increment lis count
                lis[index] = lis[j]+1
                print "result of i "+str(res)
                print "lis[index] "+str(lis)
    dp3(a, res, lis, index+1)

#MainProgram
backtrack([10, 22, 9, 33, 21, 50, 41, 60, 80], 0, [])
#dp1([10, 22, 9, 33, 21, 50, 41, 60, 80], 0, [], [0 for i in range(9)])
#dp2([10, 22, 9, 33, 21, 50, 41, 60, 80], 0, [[] for j in range(9)], [0 for i in range(9)])
dp3([10, 22, 9, 33, 21, 50, 41, 60, 80], [[] for j in range(9)], [1 for i in range(9)], 0)
