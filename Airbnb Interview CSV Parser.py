#CSV Parser
'''
For this problem, there are several cases we need to consider:
1. transform comma to |  so , -> |
2. Don't transform comma inside quotes.
3. If there is single pair of quotes remove them eg: "Alex Perrish" -> Alex Perrish
4. If there are double pairs of quotes following each other then remove one
so for "Alexandra ""Alex"""
first remove outter most pair of quotes according to rule 3
Alexandra ""Alex""
Then according to rule 4 if there are double pairs of quotes remove one
Alexandra "Alex"
Another example:
 """Alexandra Alex"""
 First rule 3 so remove the outter most pair
  ""Alexandra Alex""
Then rule 4
 "Alexandra Alex"
 But what about """"Alexandra Alex""""
 we first run rule 3
 """Alexandra Alex"""
 would we have "Alexandra Alex" or ""Alexandra Alex"" ? not handeling this case for now
'''
class Solution(object):

    def rule4Helper(self, string):
        stack = []
        # get pos of all double quotes
        for i in range(len(string)):
            if(i >= 0 and i+1 < len(string) and string[i] == '"' and string[i+1] == '"'):
                stack.append(i)
        if stack:
            string = string[:stack[0]]+string[stack[0]+1:]
            # since we removed 1 character, the index of this character have shifted by -1
            string = string[:stack[-1]-1]+string[stack[-1]+1-1:]
        return string

    def rule4(self, string):
        stringList = string.split("|")
        for i in range(len(stringList)):
            stringList[i] = self.rule4Helper(stringList[i])
        return "|".join(stringList)

    def rule3Helper(self, string):
        if(string[0] == '"' and string[-1] == '"'):
            string = string[:-1]
            string = string[1:]
        return string

    def rule3(self, string):
        stringList = string.split("|")
        for i in range(len(stringList)):
            stringList[i] = self.rule3Helper(stringList[i])
        return "|".join(stringList)
    
    def rule1and2(self, string):
        stack = []
        newString = ""
        for i in range(len(string)):
            if(string[i] == ',' and not stack):
                # python way of changing string at a particular index
                string = list(string)
                string[i] = "|"
                string = "".join(string)
            elif(string[i] == '"'):
                if(stack):
                    stack.pop()
                else:
                    stack.append('"')
        return string
        
    def csvParser(self, string):
        print string
        new_str = self.rule1and2(string)
        new_str = self.rule3(new_str)
        print self.rule4(new_str)

# Main
obj = Solution()
obj.csvParser('John,Smith,john.smith@gmail.com,Los Angeles,1')
obj.csvParser('Jane,Roberts,janer@msn.com,"San Francisco, CA",0')
obj.csvParser('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1')
obj.csvParser('"""Alexandra Alex"""')

# observation: for something like ""ab,c"",email@domain.com,city
# we first apply rule 4/rule 3 to remove double quotes
# then apply rule rule1  and 2 and the thing would still work.
