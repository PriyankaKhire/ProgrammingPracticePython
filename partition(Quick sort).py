#Quick sort

def partition(pivot, a):
    i = 0
    j = len(a)-2
    while(i<j):
        while(a[i] < pivot and i<j):
            i = i+1
        while(a[j] > pivot and i<j):
            j = j-1
        print "Swapping "+str(a[i])+" and "+str(a[j])
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i = i+1
        j = j-1
    #Swap a[i] with pivot
    temp = a[i]
    a[i] = a[len(a)-1]
    a[len(a)-1] = temp
    print a
    
        

#Main program
partition(9, [1,8,3,7,4,5,9])
