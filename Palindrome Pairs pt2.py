#Palindrome Pairs
#https://leetcode.com/problems/palindrome-pairs/
class Solution(object):
    def __init__(self):
        self.hashTable = {}

    def isPalindrome(self, word):
        for i in range(len(word)/2):
            if(word[i] != word[len(word)-1-i]):
                return False
        return True

    def putInHash(self, words):
        self.hashTable["FreeWord"] = []
        for i in range(len(words)):
            if(words[i] == ""):
                self.hashTable["FreeWord"].append(i)
                continue
            lastLetter = words[i][-1]
            if not(lastLetter in self.hashTable):
                self.hashTable[lastLetter] = [i]
            else:
                self.hashTable[lastLetter].append(i)
        print self.hashTable

    def findAllPalindromeWords(self, words):
        palindromeWords = []
        for i in range(len(words)):
            if(self.isPalindrome(words[i])):
                palindromeWords.append(i)
        return palindromeWords

    def logic(self, words):
        output = []
        self.putInHash(words)
        for wordIndex in range(len(words)):
            word = words[wordIndex]
            if(word == ""):
                #find all palindromes in words and return that
                palindromeWords = self.findAllPalindromeWords(words)
                output = output + [[wordIndex, i] for i in palindromeWords if i != wordIndex]
                continue
            print "Word ", word
            firstLetter = word[0]
            #find other words in hash that end with first letter
            if not(firstLetter in self.hashTable):
                continue
            otherWordIndices = self.hashTable[firstLetter]+self.hashTable["FreeWord"]
            for otherWordIndex in otherWordIndices:
                if(otherWordIndex == wordIndex):
                    continue
                otherWord = words[otherWordIndex]
                print "Other word ", otherWord
                i = 0
                j = len(otherWord)-1
                while((i < len(word) and j >= 0) and (word[i] == otherWord[j])):
                    i = i+1
                    j = j-1
                if(i == len(word) and j == -1):
                    print "Found pair between ", word, otherWord
                    output.append([wordIndex, otherWordIndex])
                    continue
                if(i < len(word) and j >= 0):
                    print "The words are not a palindrome"
                    continue
                #there are 2 cases
                #1) part of other word is reamining to scan
                remaining = ""
                if(j >= 0 and i == len(word)):
                    remaining = otherWord[:j+1]
                #2)part of word is remaining to scan
                elif(j == -1 and i < len(word)):
                    remaining = word[i:]
                if(self.isPalindrome(remaining)):
                    print "Found pair between ", word, otherWord
                    output.append([wordIndex, otherWordIndex])
        return output
        
    def palindromePairs(self, words):
        print self.logic(words)
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
#Main
obj = Solution()
obj.palindromePairs(["abcd","dcba","lls","s","sssll"])

obj.palindromePairs(["bat","tab","cat"])

obj.palindromePairs(["a",""])
