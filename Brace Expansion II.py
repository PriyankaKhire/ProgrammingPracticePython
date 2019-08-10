# Brace Expansion II
# https://leetcode.com/problems/brace-expansion-ii/
class Solution(object):

    def isList(self, expression):
        try:
            if(expression.isalpha()):
                return False
        except:
            return True

    def makeItIntoList(self, expression):
        if not (self.isList(expression)):
            return [expression]
        return expression

    def union(self, list1, list2):
        return list(set(list1) | set(list2))

    def concatinateSet(self, list1, list2):
        # we swap lists coz it's a stack and we are popping in reverse order
        output = []
        for c1 in list2:
            for c2 in list1:
                output.append(str(c1)+str(c2))
        return output
        
    def convertToList(self, expression):
        stack = []
        output = []
        for char in expression:
            if(char == '}'):
                string = []
                first = None
                second = None
                while(stack[-1] != '{'):
                    print stack, first, second
                    if(first == None):
                        first = self.makeItIntoList(stack.pop())
                        print first
                    elif(second == None):
                        second = stack.pop()
                        if(second == ','):
                            second = self.makeItIntoList(stack.pop())
                            first = self.union(first, second)
                        else:
                            second = self.makeItIntoList(second)
                            first = self.concatinateSet(first, second)
                        second = None
                stack.pop()
                stack.append(sorted(first))
            else:
                if(char != ',' and char != "{"):
                    # look at previous char
                    while(stack[-1] != ',' and stack[-1] != '{'):
                        # if stack top and char are not lists
                        if(not self.isList(stack[-1]) and not self.isList(char)):
                            char = stack.pop() + char
                        else:
                            # if either one of them is a list then
                            charList = self.makeItIntoList(char)
                            top = self.makeItIntoList(stack.pop())
                            char = self.concatinateSet(charList, top)
                        print 'char now is', char
                stack.append(char)
        print stack
                
    def braceExpansionII(self, expression):
        array = self.convertToList('{'+expression+'}')
        #self.normalizeExpression(array)
        """
        :type expression: str
        :rtype: List[str]
        """

# Main
obj = Solution()
#obj.braceExpansionII("a{b,c}d")

obj = Solution()
#obj.braceExpansionII("{a,b}{c,{d,e}}")

obj = Solution()
obj.braceExpansionII("{{a,z},a{b,c},{ab,z}}")
