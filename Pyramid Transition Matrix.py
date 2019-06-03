#Pyramid Transition Matrix
#https://leetcode.com/problems/pyramid-transition-matrix/
class TrieNode(object):
    def __init__(self, letter):
        self.letter = letter
        self.next = [None for i in range(26)]
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def createNode(self, letter):
        node = TrieNode(letter)
        return node

    def findLetterIndex(self, letter):
        return ord(letter.lower()) - ord('a')

    def addWord(self, word):
        ptr = self.root
        for char in word:
            index = self.findLetterIndex(char)
            if(ptr.next[index] == None):
                node = self.createNode(char)
                ptr.next[index] = node
            ptr = ptr.next[index]
        ptr.endOfWord = True

    def findThirdBlock(self, b1, b2):
        b1Index = self.findLetterIndex(b1)
        b2Index = self.findLetterIndex(b2)
        b1Node = self.root.next[b1Index] 
        if(b1Node != None):
            b2Node = b1Node.next[b2Index]
            if(b2Node != None):
                return True, [block.letter for block in b2Node.next if(block != None)]                
        return False, -1

    def dfs(self, node, output):
        if node.endOfWord == True:
            print output
        for nextNode in node.next:
            if(nextNode != None):
                self.dfs(nextNode, output+nextNode.letter) 

    def display(self):
        self.dfs(self.root, "")
        
class Solution(object):
    def __init__(self):
        self.trie = Trie()
        
    def putWordsInTrie(self, allowed):
        for word in allowed:
            self.trie.addWord(word)
        #self.trie.display()
        
    def constructTopLayer(self, bottom, index, output, topLayer):
        if(index == len(bottom)):
            output.append(topLayer)
            return 
        flag, nextLetters = self.trie.findThirdBlock(bottom[index-1], bottom[index])
        if(flag):
            for nextLetter in nextLetters:                
                self.constructTopLayer(bottom, index+1, output, topLayer+nextLetter)

    def logic(self, bottom):
        if(len(bottom) == 1):
            return True
        #passing topLayers by reference
        topLayers = []
        self.constructTopLayer(bottom, 1, topLayers, "")
        for topLayer in topLayers:
            if(self.logic(topLayer) == True):
                return True
            
        
    def pyramidTransition(self, bottom, allowed):
        self.putWordsInTrie(allowed)
        if (self.logic(bottom)):
            return True
        return False
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """

#Main
obj = Solution()
print obj.pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF", "BCF"])

obj2 = Solution()
print obj2.pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"])

