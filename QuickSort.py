#Quick sort
def partition(a, start,end):
    pivot = a[end]
    i = start
    j = end-1
    while(i<j):
        while(a[i] < pivot and i<j):
            i = i+1
        while(a[j] > pivot and i<j):
            j = j-1
        #Swap a[j] and a[i]
        print "Swapping "+str(a[i])+" and "+str(a[j])
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i = i+1
        j = j-1
    #Swap pivot and a[i]
    if(a[i] > a[end]):
        print "Swapping "+str(a[end])+" and "+str(a[i])
        temp = a[i]
        a[i] = a[end]
        a[end] = temp
    print a
    return a, i

def quick_sort(a, start, end):
    if(start > end or start == end):
        print a
        return
    else:
        print a
        print "Start = "+str(start)+" end = "+str(end)
        a, pivot_pos = partition(a, start,end)
        quick_sort(a, start, pivot_pos-1)
        quick_sort(a, pivot_pos+1, end)
    

#Main program
quick_sort([1,8,3,9,4,6,7], 0, 6)

