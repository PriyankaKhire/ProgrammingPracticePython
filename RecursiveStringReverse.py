#Recursively reverse a string
def foo(string, i):
    if(i == len(string)):
        return
    foo(string, i+1)
    print string[i]


#Main Program
foo("abc", 0)
