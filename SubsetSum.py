# Subset sum problem is to find subset of elements that are selected from a given set
# whose sum adds up to a given number K. We are considering the set contains non-negative values.
# It is assumed that the input set is unique (no duplicates are presented).

def isSafe(element, current_sum, k):
    if((element+current_sum) > k):
        return False
    else:
        return True

def foo(a,k,current_sum,s_set):
    if current_sum == k:
        print "Set is "+str(s_set)
        return True
    i = 0
    for element in a:
        i +=1
        print "a = "+str(a)
        print "Element = "+str(element)
        print "isSafe "+str(isSafe(element, current_sum, k))
        if(isSafe(element, current_sum, k)):
            #Add element to set
            s_set.append(element)
            #Remove that element from list
            # i acts as those many elements to be removed from the list
            #run the program to understand with k = 13 and a = [1,2,3,4,5,6]
            #I can even make that element 0 with its index, instead of doing this fancy thing
            print "After appending the new element "+str(s_set)
            if(foo(a[i:], k, current_sum+element, s_set)):
                return True
            else:
                p = s_set.pop()
                print "Popped element "+str(p)
                print "After popping the set "+str(s_set)

#Main Program
#a = [1,2,3,4,5,6]
#k = 13
a = [15, 22, 14, 26, 32, 9, 16, 8]
k = 53
foo(a,k,0, [])
