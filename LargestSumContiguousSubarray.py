#Largest sum contiguous sub array

def foo(a):
    max_sum = 0
    current_sum = 0
    start_pos = 0
    end_pos = 0
    #Find end pos
    for i in range(0, len(a)):
        current_sum += a[i]
        if(current_sum < 0):
            current_sum = 0
        if(max_sum < current_sum):
            max_sum = current_sum
            end_pos = i
        print "i = "+str(i)
        print "a[i] = "+str(a[i])
        print "Current sum = "+str(current_sum)
        print "Max sum so far = "+str(max_sum)
        print "End pos = "+str(end_pos)
    #Find start pos
    max_sum = 0
    current_sum = 0
    for i in range(end_pos, 0, -1):
        current_sum += a[i]
        if(current_sum < 0):
            current_sum = 0
        if(max_sum < current_sum):
            max_sum = current_sum
            start_pos = i
        print "i = "+str(i)
        print "a[i] = "+str(a[i])
        print "Current sum = "+str(current_sum)
        print "Max sum so far = "+str(max_sum)
        print "Start pos = "+str(start_pos)
        


#Main program
foo([-2, -3, 4, -1, -2, 1, 5, -3])
