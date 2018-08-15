#Regular Expression Matching
#https://leetcode.com/problems/regular-expression-matching/description/

#using backtracking
class Approch1(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    def solution(self, string, pattern):
        print "String is "+string+" pattern is "+pattern
        if not pattern:
            print "Pattern empty, returning False"
            return False
        if(string == pattern):
            print "Pattern = string returning True"
            return True
        if(len(pattern) > 1 and pattern[1] == "*"):
            print "preeceding character is *"
            #it will match 0 or  any lengths of preceeding characters
            while(pattern[0] == "." or string[0] == pattern[0]):
                print pattern[0], string[0]
                self.solution(string, pattern[2:])
                string.pop(0)
                print "string and pattern in while loop ",
                print string, pattern
            print "string and pattern out of while loop ",string, pattern
            #pop the preeciding character
            #pattern.pop(0)
            #pop the *
            #pattern.pop(0)
        else:
            print "string in else Part "+string
            print "pattern in else part "+pattern
            if(string[0] == pattern[0] or pattern[0] == "."):
                string.pop(0)
                pattern.pop(0)
                print "string and pattern after popping ",string, pattern
                self.solution(string, pattern)
                print "in backtracking portion ", string, pattern
        
                
        

#Main
o = Approch1("aab", "c*a*b")
o.solution("aaa", ".*a*")

