# Generate all permutations of a string
class Solution(object):
    def __init__(self, inputString):
        self.inputStr = inputString

    def removeCharAtGivenIndex(self, string, index):
        return string[:index] + string[index+1:]

    def permutations(self, inputStr, result):
        if not inputStr:
            print result
            return
        for i in range(len(inputStr)):
            # Save this character to add to result later
            char = inputStr[i]
            # remove character from string at index i
            newStr = self.removeCharAtGivenIndex(inputStr, i)
            # add the character in function call so we don't have to write an extra line remove it in backtracking
            self.permutations(newStr, result+char)

    def run(self):
        self.permutations(self.inputStr, "")
        

# Main
obj = Solution("AABC")
obj.run()
