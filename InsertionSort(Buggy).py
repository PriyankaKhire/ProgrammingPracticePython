#Insertion sort
def insertion_sort(array):
    #All elements to the left side of the wall are sorted
    sorted_wall = 1
    for i in range(sorted_wall, len(array)):
        #Compare array[i] to all elements on the other side of the wall
        #So since our current element is array[i] there is a hole in place of it
        element = array[i]
        hole = i
        print "Element is "+str(element)
        print "I is "+str(i)        
        for j in range(0, sorted_wall):
            print "Is element "+str(element)+" < "+str(array[j])
            if(element < array[j]):
                #Shift the elements
                while(hole > j):
                    print "Hole is at "+str(hole)
                    print "Shifting "+str(array[hole-1])+" to "+str(array[hole])
                    array[hole] = array[hole-1]
                    hole = hole - 1
                    print "Array after shifting "+str(array)
                
                print "putting element in hole "+str(array[hole])+" element "+str(element)
                array[hole] = element
                print "Array now is "+str(array)
                sorted_wall = sorted_wall + 1
    


#main program
insertion_sort([108,50,54,15,8,4,42])
