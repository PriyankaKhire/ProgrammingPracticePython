# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node(object):
    def __init__(self, letter):
        # key is letter value is trie node
        self.links = {}
        self.letter = letter
        self.isEnd = False
    
    def putLink(self, letter):
        if (letter in self.links):
            return
        node = Node(letter)
        self.links[letter] = node
    
    def linkExists(self, letter):
        if (letter in self.links):
            return True
        return False
    
    def getLink(self, letter):
        if (self.linkExists(letter)):
            return self.links[letter]

class Trie(object):

    def __init__(self):
        # set head node
        self.trie = Node("Head")
    
    def display(self, node, word):
        if node.isEnd:
            print word
        for n in node.links:
            self.display(node.links[n], word+n)
        
        
    def insert(self, word):
        currNode = self.trie
        for letter in word:
            # insert current letter on to current Node
            currNode.putLink(letter)
            currNode = currNode.getLink(letter)
        # Mark last node as end
        currNode.isEnd = True
        """
        :type word: str
        :rtype: None
        """

    def searchPrefix(self, prefix): 
        currNode = self.trie
        for letter in prefix:
            if not(currNode.linkExists(letter)):
                return False, None
            currNode = currNode.getLink(letter)
        return True, currNode

    def search(self, word):
        flag, currNode = self.searchPrefix(word)
        if not flag:
            return False
        if (currNode.isEnd):
            return True
        return False
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        flag, currNode = self.searchPrefix(prefix)
        if (flag):
            return True
        return False
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
