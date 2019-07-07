#Generate Parentheses
#https://leetcode.com/problems/generate-parentheses/

#Generate anagram
class GenerateAnagram(object):
    def logic(self, string, visited, output, anagrams):
        if(len(output) == len(string)):
            anagrams.append(output)
            return
        for i in range(len(visited)):
            if(visited[i] == 0):
                visited[i] = 1
                self.logic(string, visited, output+string[i], anagrams)
                #Backtrack
                visited[i] = 0
        
    def generateAnagrams(self, string):
        anagrams = []
        self.logic(string, [0 for i in range(len(string))], '', anagrams)
        return anagrams

#Find if valid pair of parenthesis
class ValidParenthesis(object):
    def findValid(self, parenthesis):
        stack = []
        for i in range(len(parenthesis)):
            if(parenthesis[i] == '('):
                stack.append('(')
            else:
                if(stack):
                    stack.pop()
                else:
                    return False
        if(stack):
            return False
        return True
                

class Solution(object):
    def generateParenthesis(self, n):
        anagram = GenerateAnagram()
        parenthesis = ''
        for i in range(n):
            parenthesis = parenthesis + '()'
        parenthesisList = anagram.generateAnagrams(parenthesis)
        isValid = ValidParenthesis()
        output = []
        for parenthesisCombination in parenthesisList:
            if(isValid.findValid(parenthesisCombination)):
                if not(parenthesisCombination in output):
                    output.append(parenthesisCombination)
        print output
        """
        :type n: int
        :rtype: List[str]
        """
#Main
obj = Solution()
obj.generateParenthesis(3)


