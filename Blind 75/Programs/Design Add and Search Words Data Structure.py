# Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node(object):
    def __init__(self):
        self.value = None
        # key: letter value: node
        self.next = {}
        self.eow = False
        
class Trie(object):
    def __init__(self):
        self.head = Node()
    
    def createNode(self, value):
        node = Node()
        node.value = value
        return node
    
    def add(self, word, index, node):
        if (index == len(word)):
            node.eow = True
            return
        # if letter not in node next
        if (word[index] not in node.next):
            newNode = self.createNode(word[index])
            node.next[word[index]] = newNode
        # move on to next letter
        self.add(word, index+1, node.next[word[index]])
    
    def addWord(self, word):
        self.add(word, 0, self.head)
        self.display(self.head, [])
    
    def display(self, node, words):
        if node.eow:
            print "".join(words)
        for key in node.next:
            self.display(node.next[key], words+[key])
    
    def searchWord(self, word):
        return self.search(self.head, word, 0)
        
    def search(self, node, word, index):
        if (index == len(word)):
            if (node.eow):
                return True
            return False
        #print "checking", word[index]
        if (word[index] != "." and (word[index] not in node.next)):
            return False
        # dot can match any character
        if (word[index] == "."):
            for key in node.next:
                if(self.search(node.next[key], word, index+1)):
                    return True
        else:
            return self.search(node.next[word[index]], word, index+1)
        
        
class WordDictionary(object):

    def __init__(self):
        self.trie = Trie()
        """
        Initialize your data structure here.
        """
        

    def addWord(self, word):
        self.trie.addWord(word)
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        return self.trie.searchWord(word)
        """
        :type word: str
        :rtype: bool
        """
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
