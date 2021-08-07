# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node(object):
    def __init__(self):
        # Key: letter, Value: Next Node
        # by initializing this as a hashTable, we don't have to do the extra work of ASCII values to get index in array to store the next node at.
        self.nextLink = {}
        self.endOfWord = False
        
class Trie(object):

    def __init__(self):
        self.head = Node()
        """
        Initialize your data structure here.
        """
        
    def insertWord(self, index, word, currNode):
        if (index == len(word)):
            currNode.endOfWord = True
            return
        letter = word[index]
        # if letter not in hashTable
        if (letter not in currNode.nextLink):
            # then we create an empty node and insert it in hash table.
            currNode.nextLink[letter] = Node()
        # if the letter is in hash table then we just access the node corresponding to it.
        self.insertWord(index+1, word, currNode.nextLink[letter])
    
    def displayContentsOfTrie(self, node, word):
        if (node.endOfWord):
            print ''.join(word)
        for key in node.nextLink:
            self.displayContentsOfTrie(node.nextLink[key], word+[key])
        
    def insert(self, word):
        self.insertWord(0, word, self.head)
        print "Contents of trie so far"
        self.displayContentsOfTrie(self.head, [])
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
    def searchWord(self, word, index, node):
        if (index == len(word)):
            if (node.endOfWord):
                return True
            # this return statement is for the case where a word starts with our given word
            # for example apple is in trie but if we search for app, we find it, but it's not a word.
            return False
        letter = word[index]
        if (letter in node.nextLink):
            return self.searchWord(word, index+1, node.nextLink[letter])
        return False

    def search(self, word):
        return self.searchWord(word, 0, self.head)
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
    
    def findPrefix(self, word, index, node):
        if (index == len(word)):
            return True
        letter = word[index]
        if (letter in node.nextLink):
            return self.findPrefix(word, index+1, node.nextLink[letter])
        return False
        
    def startsWith(self, prefix):
        return self.findPrefix(prefix, 0, self.head)
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
