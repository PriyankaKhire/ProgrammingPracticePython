#Find Maximum number possible by doing at-most K swaps
#Given a positive integer, find maximum integer possible by doing at-most K swap operations on its digits.
#http://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/
sol = 0

def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def isSafe(d, i, curindex):
    global sol
    #swap
    d = swap(d, i, curindex)
    #if this new number is greater than previously found number
    if(int(d) > sol):
        return d
    return False

def foo(d, k, curindex):
    global sol
    #Return condition
    if k == 0:
        if ( int(d) > sol):
            sol = d
        return True
    print "Current index:"+str(curindex)+" k = "+str(k)+" d = "+str(d)
    for i in range(curindex+1, len(d)):
        new_d = isSafe(d, i, curindex)
        print "the new digit is "+str(new_d)
        if(new_d != False):
            sol = int(new_d)
    print "After "+str(k-1)+" swaps remaining the number is "+str(sol)
    #Once all the swaps are done then move on to next swap
    foo(str(sol), k-1, curindex+1)
    

#Main Program
digit = "7599"
foo(digit, 2, 0)
