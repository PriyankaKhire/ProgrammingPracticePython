#Rotate an array

def reverse(a, start, end, size):
    #start and end tell the pos of first and last element in array
    #size tells the length of the array
    for i in range(0, size/2):
        #Swap a[start+i] and a[end-i]
        temp = a[start+i]
        a[start+i] = a[end-i]
        a[end-i] = temp

def foo(d, arr):
    #Need to rotate the array by d elements
    #Why do we ask size in the reverse function ?
    #at first i calculated size as end element - first element to calculate size
    #but when start element is at pos 0 it takes it as 0 elements and not 0th element
    #so element at index 0 is not counted
    reverse(arr, 0, d-1, d)
    reverse(arr, d, len(arr)-1, len(arr)-d)
    reverse(arr, 0, len(arr)-1, len(arr))
    print arr

#Main program
foo(2,[1,2,3,4,5,6])
