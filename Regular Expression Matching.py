#Regular Expression Matching
#https://leetcode.com/problems/regular-expression-matching/description/

#using backtracking
class Approch1(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    def combineAll(self, string, pattern):
        #print string,pattern
        if pattern == string:
            return True
        if not pattern:
            return False
        if not string:
            return False
        if(len(pattern) > 1 and pattern[1] == "*"):
            #a star can match 0 to multiple instance's  of preeceeding character in string
            #here is a python do while
            while True:
                if(self.combineAll(string, pattern[2:])):
                    return True
                if not string or (string[0] != pattern[0] and pattern[0] != "."):
                    return False
                string = string[1:]
        else:
            if string and (pattern[0] == "." or pattern[0] ==string[0]):
                if(self.combineAll(string[1:], pattern[1:])):
                    return True
            else:
                return False

    def withDot(self, string, pattern):
        print string,pattern
        if pattern == string:
            return True
        if not pattern:
            return False
        if(len(pattern) > 1 and pattern[1] == "*"):
            #a star can match 0 to multiple instance's  of preeceeding character in string
            #here is a python do while
            while True:
                if(self.withDot(string, pattern[2:])):
                    return True
                if(string[0] != pattern[0] and pattern[0] != "."):
                    return False
                string = string[1:]


    def withoutDot(self, string, pattern):
        print string,pattern
        if pattern == string:
            return True
        if not pattern:
            return False
        if(len(pattern) > 1 and pattern[1] == "*"):
            #a star can match 0 to multiple instance's  of preeceeding character in string
            #here is a python do while
            while True:
                if(self.withoutDot(string, pattern[2:])):
                    return True
                if(string[0] != pattern[0]):
                    return False
                string = string[1:]
            
                
    def withoutStar(self, string, pattern):
        print string, pattern
        if pattern == string:
            return True
        if not pattern:
            return False
        #let's simplify the problem
        #what if there are no *
        if(len(pattern) > 1 and pattern[1] != "*"):
            if(pattern[0] == "." or pattern[0] ==string[0]):
                if(self.withoutStar(string[1:], pattern[1:])):
                    return True
            else:
                return False
        

    def solution(self):
        print self.withoutStar("aab", "a.b")
        print self.withoutDot("aab", "c*a*b")
        print self.withDot("bbbc", ".*")
        print self.combineAll("bbc", ".*c")
        print self.combineAll("aa", "a")
        print self.combineAll("ab", ".*c")
        print self.combineAll("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c")
                
        

#Main
o = Approch1("bbbc", ".*")
o.solution()

