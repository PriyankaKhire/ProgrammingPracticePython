#Palindrome Pairs
#https://leetcode.com/problems/palindrome-pairs/description/
#Bad burte force solution
class Solution1(object):
    def __init__(self):
        self.ht = {}
        self.letters = {}

    def explanation(self):
        print "***************************************************************************************************************************"
        print "So this solution first takes all the words puts them in the hast table with key as starting letter"
        print "and value as list of words that start from that letter"
        print "I handel the following cases"
        print "1) null word:- if the current word is null we concatinate it with words in input array list that are palindromes"
        print "2) if reverse exists:- if the reverse of the current word exist in hash table then we concatinate them"
        print "3) take a word find all words in hash that start and end with our current word concatinate them and see if result is palindrome or not"
        print "***************************************************************************************************************************"

    def isPalindrome(self, word):
        if word == "":
            return False
        for i in range(len(word)/2):
            if(word[i] != word[len(word)-1-i]):
                return False
        return True

    def reverseString(self, string):
        return string[::-1]
    
    def putInHashTable(self, words):
        for i in range(len(words)):
            #handel null word
            if(words[i] == ""):
                continue
            if not(words[i] in self.ht):
                self.ht[words[i]] = i
            if not(words[i][0] in self.letters):
                self.letters[words[i][0]] = [words[i]]
            else:
                self.letters[words[i][0]].append(words[i])
        print self.ht, self.letters

    def concatIfPalindrome(self, word, index):
        if (word == ""):
            return []
        output = []
        w = []
        if(word[0] in self.letters):
            w = w+self.letters[word[0]]
        if(word[-1] in self.letters):
            w = w+self.letters[word[-1]]
        for wrd in w:
            if(self.isPalindrome(word+wrd) and index != self.ht[wrd]):
                output.append([index, self.ht[wrd]])
            if(self.isPalindrome(wrd+word) and index != self.ht[wrd]):
                output.append([self.ht[wrd], index])
        return output

    def nullWord(self, index, words):
        #can be concatinated with other palindromes or null words
        output = []
        for i in range(len(words)):
            if(i != index):
                if(self.isPalindrome(words[i])):
                    output.append([index, i])
                    output.append([i, index])
        return output
        
    def logic(self, words):
        output = []
        for i in range(len(words)):
            #handel the null word case
            if (words[i] == ""):
                output = output + self.nullWord(i, words)
            #find if reverse of the said word exists in hast table
            if(self.reverseString(words[i]) in self.ht and (i != self.ht[self.reverseString(words[i])])):
                output.append([i, self.ht[self.reverseString(words[i])]])
            #find words starting and ending from current words starting and ending
            output = output + self.concatIfPalindrome(words[i], i)
        #remove duplicates from list and give answer
        print [list(t) for t in set(tuple(element) for element in output)]
                
    def palindromePairs(self, words):
        self.explanation(self)
        self.putInHashTable(words)
        self.logic(words)
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
#********************************************************************************************
class trieNode(object):
    def __init__(self, char):
        self.char = char
        self.endOfWord = False
        self.next = [0 for i in range(26)]

class Trie(object):
    def __init__(self):
        self.root = self.createNode("")

    def createNode(self, char):
        return trieNode(char)

    def getCharIndex(self, char):
        print ord(char)

    #def addWord(self, word):
    

class Solution2(object):
    def __init__(self):
        self.trie = Trie() 

    def explanation(self):
        print "Now in this class we first understand how we check for palindrome"
        print "We first start with last and first letter and check if ther are same"
        print "If they are then we proceed to move the 2 pointers towards eachother,"
        print "checking every letter on the way if they are same or not, if not we stop and return false \n"
        print "We leverage this in the current solution, we first create a trie and put all words in the trie in reverse manner"


    def palindromePairs(self, words):
        print self.trie.getCharIndex('a')
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
#Main
'''
a1 = ["abcd","dcba","lls","s","sssll"]
obj1 = Solution1()
obj1.palindromePairs(a1)

a2 = ["bat","tab","cat"]
obj2 = Solution1()
obj2.palindromePairs(a2)

a3 = ["a",""]
obj3 = Solution1()
obj3.palindromePairs(a3)
'''
obj4 = Solution2()
obj4.palindromePairs([])
