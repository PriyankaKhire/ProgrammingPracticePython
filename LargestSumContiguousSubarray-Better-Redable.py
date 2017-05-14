#Longest sum contigious sub array

def isSafe(element, currSum):
    #Check if the sum is not less than 0
    if ((element+currSum) <= 0):
        return False
    else:
        return True

def foo(a,currSum, maxSum, currArray, maxArray):
    for element in a:
        if(isSafe(element, currSum)):
            #if adding the element is safe then
            currArray.append(element)
            currSum += element
            # we check current with max
            if(currSum > maxSum):
                maxSum = currSum
                maxArray = currArray
        else:            
            #if the element is not safe then we make current list empty again
            #The current list contains only contiguous elements
            currArray = []
            currSum = 0
    #Once we finish search in the current array then we print the max array
    print maxArray
    print maxSum

#Main Program
foo([-2, -3, 4, -1, -2, 1, 5, -3],0,0,[],[])
