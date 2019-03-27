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
        #we are only supporting lower case alphabets
        self.next = [None for i in range(26)]

class Trie(object):
    def __init__(self):
        self.root = self.createNode("")

    def createNode(self, char):
        return trieNode(char)

    def getCharIndex(self, char):
        return ord('a') - ord(char.lower())

    def addWord(self, word):
        ptr = self.root
        for letter in word:
            #get letter index
            index = self.getCharIndex(letter)
            if(ptr.next[index] == None):
                #create a node for that letter
                node = self.createNode(letter)
                #add that node to next
                ptr.next[index] = node
            #increment ptr
            ptr = ptr.next[index]
        ptr.endOfWord = True

    def dfs(self, node, output, wordList):
        if(node.endOfWord == True):
            print output
            wordList.append(output)
        for nextNode in node.next:
            if(nextNode != None):
                self.dfs(nextNode, output+nextNode.char, wordList)
        return wordList

    def display(self):
        print self.dfs(self.root, "",[])
    

class Solution2(object):
    def __init__(self):
        self.trie = Trie()

    def isPalindrome(self, word):
        if word == "":
            return False
        for i in range(len(word)/2):
            if(word[i] != word[len(word)-1-i]):
                return False
        return True

    def explanation(self):
        print "Now in this class we first understand how we check for palindrome"
        print "We first start with last and first letter and check if ther are same"
        print "If they are then we proceed to move the 2 pointers towards eachother,"
        print "checking every letter on the way if they are same or not, if not we stop and return false \n"
        print "We leverage this in the current solution, we first create a trie and put all words in the trie in reverse manner"
        print "Go through words and for each and every letter of the word see if you find a matching word in tire"

    def addWordsToTrieInReverseOrder(self, words):
        for word in words:
            self.trie.addWord(word[::-1])
        self.trie.display()

    def logic(self, words):
        output = []
        for i in range(len(words)):
            print "currently on word ", words[i]
            ptr = self.trie.root
            matchWord = ""
            j = 0
            breakFlag = False
            while(j < len(words[i])):
                letter = words[i][j]
                print letter
                letterIndex = self.trie.getCharIndex(letter)
                if (ptr.next[letterIndex] == None):
                    breakFlag = True
                    break
                ptr = ptr.next[letterIndex]
                matchWord = matchWord + ptr.char
                j = j+1
            if(ptr.endOfWord== True and j == len(words[i])):
                print "Found a match between ", words[i],matchWord[::-1]
            else:
                #break flag is just to prevent words that have no match like sssll cannot be matched with s or sll from trie
                if(breakFlag == False):
                    print "Rest of the word is ", matchWord, 
                    restOfWords = self.trie.dfs(ptr, "", [])
                    #if rest of the word is a palindrome then we found a match
                    for word in restOfWords:
                        if(self.isPalindrome(word)):
                            print "it is a Match"

    def palindromePairs(self, words):
        self.addWordsToTrieInReverseOrder(words)
        self.logic(words)
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
#Main

a1 = ["abcd","dcba","lls","s","sssll"]
'''
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
obj4.palindromePairs(a1)
