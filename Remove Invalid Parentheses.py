#Remove Invalid Parentheses

#An expression will be given which can contain open and close parentheses
#and optionally some characters, No other operator will be there in string.
#We need to remove minimum number of parentheses to make the input string valid.
#If more than one valid output are possible removing same number of parentheses then
#print all such output.

#Examples:

#Input  : str = “()())()” -
#Output : ()()() (())()
#There are two possible solutions
#"()()()" and "(())()"

#Input  : str = (v)())()
#Output : (v)()()  (v())()

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
        

def foo(string, result):
    if(string == ""):
        print result
        return True
    print "String "+str(string)
    expression = result
    for i in range(len(string)):
        print "Result "+str(result)
        expression += string[i]
        print "expression "+str(expression)
        if(isSafe(expression)):
            print "Safe to add this character to result"
            if(foo(string[i+1:], expression)):
                return True
            else:
                print "Backtrack?"
                result[:1]
        else:
            print "if it is not safe then add the next character to the result"

def bar(string, result):
    print "is safe ? "+str(isSafe(result))
    if(isSafe(result) and result != ""):
        print result
        return True
    print "The string is: "+string
    print "The result is: "+result
    for i in range(len(string)):
        print "String character is "+string[i]
        #Append it to result
        result += string[i]
        if(bar(string[i+1:], result)):
            print result 
        else:
            #Remove it from the result
            result = result[-1:]
            print "***** Backtracking *****"

#See the out put and repair this program        
bar("()())()", "")
