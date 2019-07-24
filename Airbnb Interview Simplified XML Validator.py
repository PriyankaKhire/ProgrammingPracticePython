#Tells if <tag> is valid or not, if it is then returns the tag inside <>
def validParenthesis(text):
    if(text[0] != "<"):
        return False, -1
    tag = ""
    for i in range(1, len(text)):
        if(text[i] == "<"):
            return False, -1
        if(text[i] == ">"):
            return True, tag
        tag = tag+text[i]
        
def valid(text):
    i = 0
    stack = []
    while(i< len(text)):       
        if(text[i] == "<"):
            flag, tag = validParenthesis(text[i:])            
            if not flag:
                return False
            if(tag[0] == "/"):
                if not stack:
                    return False
                if (stack[-1] != tag[1:]):
                    return False
                stack.pop()
            else:
                stack.append(tag)
            i = i + len(tag)+2
        elif(text[i] == ">"):
            return False
        else:
            i = i+1
    if(stack):
        return False
    return True
    
#Main
print valid("text") #True
print valid("text<a>more text</a>") #True
print valid("text</a>") #False
print valid("<invalid<>text</invalid>") #False
print valid("<abc>") #False
print valid("<a>text<b>other text</b></a>") #True
print valid("<a>text<b>other text</a></b>") #False
