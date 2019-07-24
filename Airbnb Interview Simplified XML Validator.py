'''
Your input will be an ASCII string, and you will output a boolean, which indicates whether the string is valid xml.

We simplify the xml format to only have content or tags.

Content
Text which can contain any ascii characters EXCEPT < and >

Tags
Tags come in two flavors. < and > must only appear as the start and end of a tag, and the tags cannot be empty. I.e <> and </> are invalid.

The start-tag and end-tag elements must be correctly nested, with none missing and none overlapping. For example, text <a> text</a>, <a>text<b>other text</b></a> are valid, <a>text<b>other text</a></b> is not.

The goal of this question is to simulate an xml validator. We will give you sample xml text and you should output wheter the text is valid xml or not.

###Example input/output

Input
	text
Output
	true
Input
	text<a>more text</a>
Output
	true
Input
	text</a>
Output
	false
Input
	<invalid<>text</invalid>
Output
	false
'''
#Tells if <tag> is valid or not, if it is then returns the tag inside <>
def validParenthesis(text):
    if(text[0] != "<"):
        return False, -1
    tag = ""
    for i in range(1, len(text)):
        if(text[i] == "<"):
            #text = <<abc>
            return False, -1
        if(text[i] == ">"):
            #Completes the tag <abc>
            return True, tag
        #text inside the tag
        tag = tag+text[i]
        
def valid(text):
    i = 0
    stack = []
    while(i< len(text)):       
        if(text[i] == "<"):
            flag, tag = validParenthesis(text[i:])
            if not flag:
                return False
            #tags cannot be empty
            if(tag == "" or tag == "/"):
                return False
            #If we find a closing tag </abc>
            if(tag[0] == "/"):
                #if stack is empty, that means there was no opening tag, return false
                if not stack:
                    return False
                #if stack top is 'abc' but our closing tag is 'xyz', return False
                if (stack[-1] != tag[1:]):
                    return False
                #if there is a match to our closing tag then pop it from stack
                stack.pop()
            else:
                #if this is the opening tag then add it to stack
                stack.append(tag)
            #we increment i to tag length plus 2 to add <> to the legth of i
            i = i + len(tag)+2
        elif(text[i] == ">"):
            #if there is a random > in text then return false
            return False
        else:
            i = i+1
    if(stack):
        #if we never found a closing tag to one of our opening tags
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
print valid("<> </>") #False
