#Bubble sort
#The main aim is to get the largest element and bring it to its original sorted position
#So the largest element will move to the bottom of the array

def bubble_sort(array):
    for passes in range (1, len(array)):
        #Note: we are subctracting passes from array lenght so thats why we start passes from 1 and not 0
        #We can think about starting passes from 0 to len(array) but again the substraction wont work
        for i in range(0, len(array)-passes):
            if(array[i] > array[i+1]):
                print "swapping "+str(array[i])+" with "+str(array[i+1])
                print "The array is "+str(array)
                array[i], array[i+1] = array[i+1], array[i]
                print "***********"
    print "The sorted array is "+str(array)


#Main program
bubble_sort([8,5,6,7,9,1,0])
