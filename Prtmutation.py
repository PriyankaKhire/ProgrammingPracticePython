#Permutations of a string
def foo(string, l, r):
    if (l==r):
        print string
    for i in xrange(l, r+1):
        #Swap string of l and r
        string[l], string[i] = string[i], string[l]
        foo(string, l+1, r)
        string[l], string[i] = string[i], string[l]
#Main program
foo(list("abc"), 0, 2)
