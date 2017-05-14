#Search an element in a sorted and rotated array

def foo(a, s, e):
    #If length of array is 2 then return smaller of two
    if (len(a) == 2):
        if(a[s] < a[e]):
            return s
        else:
            return e
    #if lenght of aray is 1
    if(s == e):
        return s
    #for all other cases
    if (s < e):
        m = (s+e)/2
        #Sorted
        if(a[s] < a[m] and a[m] < a[e]):
            if(a[m] < a[m+1]):
                print "Array is sorted "+str(a)
                return 0
        #Pivot is mid
        if(a[s] > a[m] and a[m] < a[e]):
            if(a[m-1] > a[m] and a[m] < a[m+1]):
                print "pivot is mid at pos "+str(m)
                return 
        #Pivot in left
        if(a[s] > a[m] and a[m] < a[e]):
            if(a[m] < a[m+1]):
                print "Going left"
                foo(a, s, m-1)
        #Pivot is next to mid on the right side
        if(a[s] < a[m] and a[m] > a[e]):
            if(a[m-1] < a[m] and a[m] > a[m+1]):
                print "pivot is next to mid at pos "+str(m+1)
                return
        #pivot in right
        if(a[s] < a[m] and a[m] > a[e]):
            if(a[m-1] < a[m]):
                print "Going right"
                foo(a, m+1, e)

#Main program
foo([1,2,3,4,5,6,7], 0, 6)
print "****"
foo([7,1,2,3,4,5,6], 0, 6)
print "****"
foo([6,7,1,2,3,4,5], 0, 6)
print "****"
foo([5,6,7,1,2,3,4], 0, 6)
print "****"
foo([4,5,6,7,1,2,3], 0, 6)
print "****"
foo([3,4,5,6,7,1,2], 0, 6)
print "****"
foo([2,3,4,5,6,7,1], 0, 6)
print "\n %%% \n"
foo([1,2,3],0,2)
print "****"
foo([3,1,2],0,2)
print "****"
foo([2,3,1],0,2)

print "What did we learn from this ?"
print "Order of the things matter"
print "When my mid block was positioned in middle the program took loger to run"

