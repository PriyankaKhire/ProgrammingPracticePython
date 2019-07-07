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
                

class BruteForce(object):
    
    def generateNPairsOfParenthesis(self, n):
        parenthesis = ''
        for i in range(n):
            parenthesis = parenthesis + '()'
        return parenthesis
        
    def generateParenthesis(self, n):
        #Declare Variables
        anagram = GenerateAnagram()
        isValid = ValidParenthesis()
        output = []
        #get the n pairs of parenthesis
        parenthesis = self.generateNPairsOfParenthesis(n)
        #get the anagram list of the parenthesis
        parenthesisList = anagram.generateAnagrams(parenthesis)
        #validate the parenthesis.
        for parenthesisCombination in parenthesisList:
            if(isValid.findValid(parenthesisCombination)):
                if not(parenthesisCombination in output):
                    output.append(parenthesisCombination)
        print output
        """
        :type n: int
        :rtype: List[str]
        """

#Saw this approch on leetcode, didn't see the code though
class Solution2(object):
    def generateNPairsOfParenthesis(self, n):
        parenthesis = ''
        for i in range(n):
            parenthesis = parenthesis + '()'
        return parenthesis
    
    #let's combine generate anagram and ValidParenthesis
    #to write this function, I first copied the logic function of generate anagrams class and added to it.
    def logic(self, string, visited, output, anagrams, stack):
        if(len(output) == len(string) and not(output in anagrams)):
            anagrams.append(output)
            return
        for i in range(len(visited)):
            if(visited[i] == 0):
                visited[i] = 1
                if(string[i] == '('):
                    self.logic(string, visited, output+string[i], anagrams, stack+['('])
                else:
                    if(stack):
                        self.logic(string, visited, output+string[i], anagrams, stack[:-1])
                #Backtrack
                visited[i] = 0
                
    def generateParenthesis(self, n):
        #get the n pairs of parenthesis
        parenthesis = self.generateNPairsOfParenthesis(n)
        anagrams = []
        self.logic(parenthesis, [0 for i in range(len(parenthesis))], '', anagrams, [])
        print anagrams
        """
        :type n: int
        :rtype: List[str]
        """
#Main
obj = Solution2()
obj.generateParenthesis(3)


