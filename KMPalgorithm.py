#Knuth-Morris-Pratt algorithm for string matching

class KMP(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    #generate longest suffix which is same as suffix table for a Pattern
    def lps(self):
        table = [0 for i in range(len(self.pattern))]
        prefix = 0
        suffix = prefix +1
        while (suffix < len(self.pattern)):
            if (self.pattern[prefix] == self.pattern[suffix]):
                #if pattern[suffix] == pattern[prefix] then
                table[suffix] = prefix + 1
                suffix = suffix+1
                prefix = prefix+1
            else:
                #if pattern[suffix] != pattern[prefix]
                while(prefix > 0 and self.pattern[prefix] != self.pattern[suffix]):
                    prefix = table[prefix-1]
                if(self.pattern[prefix] == self.pattern[suffix]):
                    table[suffix] = prefix + 1
                prefix = 0
                suffix = suffix + 1
        print table


#Main Program
o = KMP("", "aaaabaacd")
o.lps()
        
