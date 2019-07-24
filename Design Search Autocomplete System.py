#Design Search Autocomplete System
#https://leetcode.com/problems/design-search-autocomplete-system/
from operator import itemgetter
class TrieNode(object):
    def __init__(self, letter):
        self.letter = letter
        #The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#').
        self.next = [None for i in range(28)]
        self.eow = False
        self.hotDegree  = 0
        
class Trie(object):
    def __init__(self):
        self.root = self.createNode("")

    def createNode(self, letter):
        return TrieNode(letter)

    def getIndex(self, char):
        if(char == '#'):
            return 26
        if(char == " "):
            return 27
        return ord(char) - ord('a')

    def addWord(self, word, hotDegree=1):
        ptr = self.root
        for char in word:
            index = self.getIndex(char)
            if(ptr.next[index] == None):
                node = self.createNode(char)
                ptr.next[index] = node
            ptr = ptr.next[index]
        #add end of word
        ptr.eow = True
        #Increment its hot degree
        ptr.hotDegree = ptr.hotDegree + hotDegree

    def dfs(self, node, output, outputList):
        if(node.eow == True):
            outputList.append([output, node.hotDegree])
        for nextNode in node.next:
            if(nextNode != None):
                self.dfs(nextNode, output+nextNode.letter, outputList)
                
    def display(self):
        outputList = []
        self.dfs(self.root, "", outputList)
        print outputList

    def get3HotSentences(self, letter, node):
        index = self.getIndex(letter)
        if(node.next[index] == None):
            return [], node
        hotSentences = []
        self.dfs(node.next[index], "", hotSentences)
        #Sort it in descending order to pick the top 3 sentences
        hotSentences = sorted(hotSentences, key=itemgetter(1), reverse=True)
        #pick hot 3 sentences
        return hotSentences[:3], node.next[index]
                
    
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.addWord(sentences[i], times[i])
        self.historicalSentence = ""
        self.lastTraversedNode = self.trie.root
        """
        :type sentences: List[str]
        :type times: List[int]
        """

    def saveHistoricalSentence(self):
        self.trie.addWord(self.historicalSentence)
        self.historicalSentence = ""
        self.lastTraversedNode = self.trie.root
        self.trie.display()
        
    def input(self, c):
        self.historicalSentence = self.historicalSentence + c
        if(c == "#"):
            #save the historical sentence and reset it to ""
            self.saveHistoricalSentence()
            return
        sentences, self.lastTraversedNode = self.trie.get3HotSentences(c, self.lastTraversedNode)
        output = []
        for sentence in sentences:
            output.append(self.historicalSentence+sentence[0])
        print output
        """
        :type c: str
        :rtype: List[str]
        """

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

#Main
obj = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
obj.input('i')
obj.input(" ")
obj.input("a")
obj.input("#")
