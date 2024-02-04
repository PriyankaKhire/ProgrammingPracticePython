# Implement Trie II (Prefix Tree)
# https://leetcode.com/problems/implement-trie-ii-prefix-tree/description/

class Node(object):
    def __init__(self, letter):
        self.letter = letter
        self.links = {}
        self.isEnd = False
        self.count = 0
    
    def putLink(self, letter):
        if (letter in self.links):
            self.links[letter].count += 1
            return
        self.links[letter] = Node(letter)
        self.links[letter].count += 1
    
    def getLink(self, letter):
        #print "getting links for letter", letter
        if not(self.isExists(letter)):
            return False, None
        return True, self.links[letter]
    
    def eraseLink(self, letter):
        #print "erasing link letter", letter
        if (self.isExists(letter)):
            self.links[letter].count -= 1
    
    def isExists(self, letter):
        #print "is exists", self.links[letter], self.links[letter].count
        #print letter in self.links
        #print self.links[letter].count > 0
        if ((letter in self.links) and (self.links[letter].count > 0)):
            #print "here"
            return True
        return False

class Trie(object):
    def __init__(self):
        self.trie = Node("head")

    def display(self, node, word):
        if (node.isEnd):
            print word, node.count
        for n in node.links:
            self.display(node.links[n], word+n)

    def insert(self, word):
        #print "inserting", word
        currPtr = self.trie
        for letter in word:
            #print letter
            currPtr.putLink(letter)
            flag, currPtr = currPtr.getLink(letter)
            #print flag, currPtr, currPtr.count
        # mark the end of the word
        currPtr.isEnd = True
        #self.display(self.trie, "")
        """
        :type word: str
        :rtype: None
        """
    
    def findWordCount(self, word, index, node):
        #print "word index letter", word[index], "node letter", node.letter
        if (word[index] == node.letter and index == len(word)-1):
            return node
        # find if next letter exists in the links of current node
        if (word[index+1] not in node.links):
            return None
        # if the letter exists then recurse
        return self.findWordCount(word, index+1, node.links[word[index+1]])

    def countWordsEqualTo(self, word):
        #print "counting word", word
        # if the first letter of the word not found in head node
        if (word[0] not in self.trie.links):
            return 0
        node = self.findWordCount(word, 0, self.trie.links[word[0]])
        if (node and node.isEnd):
            #print "count", node.count
            return node.count
        return 0
        """
        :type word: str
        :rtype: int
        """
        

    def countWordsStartingWith(self, prefix):
        #print "Counting prefix count of ", prefix
        # if the first letter of the word not found in head node
        if (prefix[0] not in self.trie.links):
            return 0
        node = self.findWordCount(prefix, 0, self.trie.links[prefix[0]])
        if (node):
            #print "count", node.count
            return node.count
        return 0
        """
        :type prefix: str
        :rtype: int
        """
        

    def erase(self, word):
        #print "Erasing the word", word
        # we first need to find the word and make sure it's a complete word and not a prefix
        node = self.findWordCount(word, 0, self.trie.links[word[0]])
        # if word doesn't exist
        if not node:
            return
        # if word exists we do exactly opposite of insert
        #print "Start erasing"
        currPtr = self.trie
        for letter in word:
            prevPtr = currPtr
            # advance the current ptr
            flag, currPtr = currPtr.getLink(letter)
            # erase the letter from current ptr
            prevPtr.eraseLink(letter)
        return None
        """
        :type word: str
        :rtype: None
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
