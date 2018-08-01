<<<<<<< Updated upstream
#Given an absolute path for a file (Unix-style), simplify it.
#
#For example,
#path = "/home/", => "/home"
#path = "/a/./b/../../c/", => "/c"
#
#Corner Cases:
#
#Did you consider the case where path = "/../"?
#In this case, you should return "/".
#Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
#In this case, you should ignore redundant slashes and return "/home/foo".
#/path/../ = /
#/path/./ = /path
#/path/ =  /path
#path = /path
class Approch1(object):
    def __init__(self, path):
        self.path = path
        self.stack = []

    #Split path on basis of /
    def splitPath(self):
        string = ""
        for letter in self.path:
            if letter=="/":
                if string!="":
                    self.stack.append(string)
                    string=""
            else:
                string = string+letter
        if string !="":
            self.stack.append(string)

    def logic(self):
        negative = 0
        for i in range((len(self.stack)-1), -1, -1):
            if(self.stack[i] == ".."):
                negative = negative+1
                self.stack[i] = ""
            elif(self.stack[i] == "."):
                self.stack[i] = ""
            else:
                if(negative > 0):
                    negative = negative-1
                    self.stack[i] = ""
        path = ""
        for letter in self.stack:
            if letter != "":
                path = path+"/"+letter
        if path == "":
            path = "/"
        return path
    
    def solution(self):
        self.splitPath()
        p = self.logic()
        return p

#Main
o = Approch1("/...")
print o.solution()

'''
=======
#Simplify Path
#
#Given an absolute path for a file (Unix-style), simplify it.
#
#For example,
#path = "/home/", => "/home"
#path = "/a/./b/../../c/", => "/c"
#
#Corner Cases:
#
#Did you consider the case where path = "/../"?
#In this case, you should return "/".
#Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
#In this case, you should ignore redundant slashes and return "/home/foo".
class Approach1(object):
    def __init__(self, string):
        self.string = string
        self.stack = []

    #insert input string in stack in reverse order such that top of stack is beginning of string
    def insertInStack(self):
        for i in range(len(self.string)-1, -1, -1):
            self.stack.append(self.string[i])

    def applyRulesToOutput(self, currString, previousString):
        if (currString == "/"):
            return previousString, currString
        #/path/ = /path
        if(currString[-1] == "/"):
            currString = currString[:-1]
        # /path/../ = /
        if(currString == ".."):
            return "", ""
        # /path/./ = /path
        if(currString == "."):
            return previousString, "/"
        return previousString, currString
            

    def processSolution(self):
        self.insertInStack()
        output =  self.stack.pop()
        previous = ""
        while self.stack:
            #pop from stack till next / is found
            current = ""
            while (self.stack and self.stack[-1] != "/"):
                current = current+self.stack.pop()
            #Add the next / to current
            current = current +self.stack.pop()
            previous, current = self.applyRulesToOutput(current, previous)
            output = output + previous
            previous = current
        output = output+previous
        print output

            




#Main
        #put print statements and verify why is this wrong
o = Approach1("/a/./b/../../c/")
o.processSolution()
>>>>>>> Stashed changes
'''
