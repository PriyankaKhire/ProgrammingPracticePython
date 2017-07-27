#String Compression

def foo(string):
    result = ""
    count = 1
    for currChar in range(1, len(string)):
        if(string[currChar] == string[currChar-1]):
            count +=1
        else:
            result += string[currChar-1]+str(count)
            count = 1
    #Add the last character
    result += string[len(string)-1]+str(count)
    print result

#Main Program
foo("eaabbbcccaaatzaaa")
