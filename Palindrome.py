#Palendrome

#iterative
def foo(string):
    for i in range(0, len(string)):
        if(string[i] != string[len(string)-1-i]):
            return False
        return True

#recurrssive
def bar(string, i):
    #return condition
    if(i == len(string)):
        #This true returns back to the calling function
        return True
    if(string[i] != string[len(string)-1-i]):
        return False
    bar(string, i+1)
    return True
    

#Main program
print foo("aaa")
print foo("aba")
print foo("aabc")

print bar("aaa",0)
print bar("aba",0)
print bar("aabc",0)

