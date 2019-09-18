# Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/
class Node(object):
    def __init__(self, letter):
        self.letter = letter
        self.next = {}
        self.eow = False
        self.index = None
        # we collect the indices of the words that are palindromes after our current letter.
        self.palindromesBelow = []
        
class Trie(object):
    def __init__(self):
        self.root = Node("")

    def createNode(self, letter):
        return Node(letter)

    def isPalindrome(self, word):
        for i in range(len(word)/2):
            if(word[i] != word[len(word)-1-i]):
                return False
        return True

    def addWord(self, word, index):
        print "Adding word",word,"present at index",index,"in word list"
        ptr = self.root
        for i in range(len(word)):
            print "Adding char",word[i],"to trie"
            char = word[i]
            if not(char in ptr.next):
                ptr.next[char] = self.createNode(char)
            #this block is the only extra addition to this normal add word function
            if(self.isPalindrome(word[i:])):
                print "the word",word,"is palidrome from",word[i:]
                # note you are not appending the word but index
                ptr.palindromesBelow.append(index)
                print "We add the INDEX",index,"of this word in palindromesBelow array"
            ptr = ptr.next[char]
        ptr.eow = True
        ptr.index = index

    def searchWord(self, word, index):
        output = []
        ptr = self.root
        while word:
            print "word ->",word, "trie node letter ->",ptr.letter
            if not(word[0] in ptr.next):
                print "The rest of the word does not match trie node"
                return output
            ptr = ptr.next[word[0]]
            print "The ptr advanced to",ptr.letter
            #1) if a node has ended
            if(ptr.eow == True):
                print "Reached end of node"
                # check if the rest of the word is a palindrome ?
                if(self.isPalindrome(word[1:])):
                    print "rest of the word",word[1:],"is a palindrome"
                    output.append(ptr.index)
            # else continue
            word = word[1:]
            print "Chopping first letter of the word"
        # 2) if word has ended and even the node has reached eow
        if(ptr.eow == True):
            print "Both word has ended and trie node has also ended"
            output.append(ptr.index)
        # 3) if word has ended and trie nodes have not, since we recoded of the index of the words that are palindromes
        if(ptr.palindromesBelow):
            print "The word has ended but node has not so we just add the palidromes collected below"
        output.extend(ptr.palindromesBelow)
        return output

    def display(self, node, output):
        if(node.eow == True):
            print output
        for n in node.next:
            self.display(node.next[n], output+n)
    
class Solution(object):
    def __init__(self):
        self.trie = Trie()
        
    def palindromePairs(self, words):
        for i in range(len(words)):
            word = words[i]
            # add the reverse of the word
            self.trie.addWord(word[::-1], i)
        #self.trie.display(self.trie.root, "")
        print "-"*50
        for i in range(len(words)):
            print words[i], i
            if(words[i][0] in self.trie.root.next):
                print self.trie.searchWord(words[i], i)
            print "*"*50
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

# Main
obj = Solution()
obj.palindromePairs(["abcd","dcba","lls","s","sssll"])
