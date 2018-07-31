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
