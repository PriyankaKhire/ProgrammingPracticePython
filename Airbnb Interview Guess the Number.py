# Guess Number
'''
Problem similar to https://leetcode.com/problems/guess-the-word/
but instead of  6 letter long word, we have 4 digit long number
each digit in the number is in range 1-6

In order to play the game, you must give master a number that is 4 digit long
and has digits between 1-6
'''
import random
class Master(object):
    def __init__(self):
        self.secret = [str(random.randint(1,6)) for i in range(4)]

    def guess(self, number):
        num = list(str(number))
        matchCount = 0
        for i in range(len(num)):
            if(num[i] == self.secret[i]):
                matchCount = matchCount + 1
        return matchCount

class Solution1(object):

    def permutations(self, digits, output, master, correctNumber):
        if(len(output) == 4):
            if(master.guess(int("".join(output))) == 4):
                correctNumber[0] = int("".join(output))
                return True
            return
        for i in digits:
            if(self.permutations(digits, output+[str(i)], master, correctNumber)):
                return True
    
    def findDigits(self, master):
        digits = []
        for i in range(1, 7):
            guessNum = i*1000+i*100+i*10+i
            if(master.guess(guessNum) > 0):
                digits.append(i)
        return digits
            
    def guessNumber(self, master):
        digits = self.findDigits(master)
        correctNumber = [0]
        self.permutations(digits, [], master, correctNumber)
        return correctNumber[0]

class Digit(object):
    def __init__(self, d, m):
        self.digit = d
        self.matches = m
        
class Solution2(object):

    # logic very similar to dfs
    def permutations(self, digits, visited, output, master):
        if(len(output) == len(digits)):
            if(master.guess(int("".join(output))) == 4):
                print int("".join(output))
                return True
            return
        for i in range(len(digits)):
            # if the digit has not been visited, visit it
            if(visited[i] == False):
                visited[i] = True 
                if(self.permutations(digits, visited, output+[str(digits[i])], master)):
                    return True
                visited[i] = False
            

    def findNum(self, digits, master):
        permutationsDigit = []
        for digit in digits:
            permutationsDigit = permutationsDigit + [digit.digit for i in range(digit.matches)]
        # one of the permutations of these digits is the secret
        # just for your understanding uncomment the below line and see
        # print permutationsDigit, master.secret
        self.permutations(permutationsDigit, [False for i in range(len(permutationsDigit))], [], master)
            
    def findDigitsAndMatches(self, master):
        digits = []
        for i in range(1, 7):
            guessNum = i*1000+i*100+i*10+i
            matches = master.guess(guessNum)
            if(matches > 0):
                digits.append(Digit(i, matches))
        return digits
    
    def guessNumber(self, master):
        digits = self.findDigitsAndMatches(master)
        self.findNum(digits, master)

# Main
m = Master()
obj = Solution1()
print obj.guessNumber(m)

obj = Solution2()
obj.guessNumber(m)
