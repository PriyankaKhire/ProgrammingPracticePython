#Regular Expression Matching
#https://leetcode.com/problems/regular-expression-matching/description/
class withoutDot(object):
    #A star can match 0 or any occourance of the previous character
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    def recurrse(self, string, pattern):
        print string, pattern
        if(string == pattern):
            return True
        if(len(pattern) > 1 and pattern[1] == '*'):
            #if current string character matches then keep matching till a non matching character is found
            while(string[0] == pattern[0]):
                string = string[1:]
            pattern = pattern[2:]
        elif(len(pattern) > 1 and pattern[1] != '*'):
            if(string[0] == pattern[0]):
                string = string [1:]
                pattern = pattern[1:]
        return self.recurrse(string, pattern)
                        
    def logic(self):
        print self.recurrse(self.string, self.pattern)

class withoutStar(object):
    #A dot can match anything
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    def recurrse(self, string, pattern):
        if(string == pattern):
            return True
        if(string[0] == pattern[0] or pattern[0] == '.'):
            string = string[1:]
            pattern = pattern[1:]
        return self.recurrse(string, pattern)

    def logic(self):
        print self.recurrse(self.string, self.pattern)

class combineBoth(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    def recurrse(self, string, pattern):
        print string, pattern
        if(string == pattern):
            return True
        if(len(pattern) > 1 and pattern[1] == '*'):
            #if current string character matches then keep matching till a non matching character is found
            while(string and string[0] == pattern[0]):
                string = string[1:]
            self.recurrse(string, pattern[2:])
            #for cases like .*
            while(pattern[0] == '.' and len(pattern) > 3 and (string[0] != pattern[2])):
                string = string[1:]
            #incomplete, complete some other day.

    def logic(self):
        self.recurrse()

    

#Main
objStar = withoutDot('ddaab', 'c*dda*b')
#objStar.logic()

objDot = withoutStar('acb', 'a.b')
objDot.logic()
