#Generate all subsuts of a set Tushar Roy methode

def foo(mainSet, result, index):
    print result
    for i in range(index, len(mainSet)):
        result.append(mainSet[i])
        foo(mainSet, result, i+1)
        #Backtrack
        result.pop()


#Main Program
foo(['a', 'a', 'b','c'], [], 0)
print "With repeated characters such as this, we get set a,b,c printed twice"
print "To avoid that just do what you did in stirng permutation method"
    
