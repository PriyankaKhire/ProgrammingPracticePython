#Remove Invalid Parentheses

#Checks if equation is balanced with parenthesis or not
def isSafe(string):
    stack = []
    while (string !=""):
        #remove the first character from the string
        #print "The string is "+str(string)
        character = string[:1]
        string = string[1:]
        #print "The current character is "+str(character)
        if (character == ")"):
            #print "Start poping the stack"
            #Statr popping till you find (
            top = ""
            while(stack and top != "("):
                top = stack.pop()
                #print "Popped "+str(top)
            #If you search the entire stack and dont find ( then return false
            if(top != "("):
                return False
        else:
            #print "Push into stack"
            stack.append(character)
    #At the end if stack still has any remaining ( then reutrn false
    while(stack):
        if(stack.pop() == "("):
            #print "The stack still had residual ("
            return False
    return True

def foo(string, index, result):
    if(isSafe(result)):
        print result
    for i in range(index, len(string)):
        result += string[i]
        foo(string, i+1, result)
        result = result[:-1]
foo("()())()", 0, "")
foo("(v)())()", 0, "")
