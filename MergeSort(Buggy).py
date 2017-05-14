
def merge(a,b):
    i = 0
    j = 0
    c = []
    while(i < len(a) and j < len(b)):
        if(a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j]) 
            j += 1
    if(i < len(a)):
        c = c+a
    if(j < len(b)):
        c = c+b
    return c


def divide(array):
    if len(array) < 2:
        #THIS IS THE MOST IMPORTANT LINE
        #if i just return array the top of the stack contents would be changed automatically
        #but python works differently
        #it also returns none
        #c++ does not return none
        #and thaats why you need the simplest of the return condition
        return array
    else:
        #Only if the length of the array is greater than 1, we can divide it
        mid = len(array)/2
        a = array[:mid]
        b = array[mid:]
        print "before dividing"
        print a
        print b
        print array
        a = divide(a)
        print "after a dividing"
        print a
        print b
        print array
        b= divide(b)
        print "after b dividing"
        print a
        print b
        print array
        array = merge(a,b)
        print "after merge"
        print a
        print b
        print array
        print "****"
        return array


#Main Program
inpt = [108,54,50,15,4,8,42]
divide(inpt)
