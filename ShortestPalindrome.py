#Shortest Palindrome
#Difficulty:Hard
#
#Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
#
#Example 1:
#
#Input: "aacecaaa"
#Output: "aaacecaaa"
#Example 2:
#
#Input: "abcd"
#Output: "dcbabcd"

class ShortestPalindrome(object):
    def __init__(self, string):
        self.string = string
        self.string = self.makeStringLenOdd(string)

    def isPalindrome(self, string):
        for i in range(len(string)/2):
            if(string[i] != string[len(string)-1-i]):
                return False
        return True

    def makeStringLenOdd(self, string):
        s = "$"
        for char in string:
            s = s+char+"$"
        return s

    def removeSpecialCharacter(self, string):
        s = ""
        for char in string:
            if char != "$":
                s = s+char
        return s

    def solution(self):
        if self.isPalindrome(self.string):
            self.string = self.removeSpecialCharacter(self.string)
            return self.string
        currentIndex = len(self.string)-1
        tempIndex = 0
        while (currentIndex-tempIndex != 0 or currentIndex+tempIndex != len(self.string)-1):
            tempIndex = tempIndex+1
            #if we run out of length on left
            if(currentIndex+tempIndex >= len(self.string)):
                currentIndex = currentIndex-1
                tempIndex = 0
            elif(currentIndex-tempIndex < 0):
                #We add characters
                print "Adding "+self.string[currentIndex+tempIndex]+" to the front of the string"
                self.string = self.string[currentIndex+tempIndex]+self.string
                #shift current index by one since we added a character to the front of the string
                currentIndex = currentIndex + 1
            elif(self.string[currentIndex+tempIndex] != self.string[currentIndex-tempIndex]):
                #Move to left again
                currentIndex = currentIndex-1
                tempIndex = 0
        self.string = self.removeSpecialCharacter(self.string)
        return self.string
              

    

#Main Program
o = ShortestPalindrome("aabbaad")
print o.solution()
