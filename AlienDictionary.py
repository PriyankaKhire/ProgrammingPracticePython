#Given a sorted dictionary of an alien language, find order of characters
class graphNode(object):
    def __init__(self, data):
        self.data = data
        self.link = []

class CreateGraph():
    def __init__(self):
        #key is node data and value is node object
        self.nodesDictionary = {}
        self.root = None

    def createNode(self, data):
        node = graphNode(data)
        return node

    def addChildNode(self, parentNode, childNode):
        parentNode.link.append(childNode)
        return parentNode

    #Creates uni directed graph from given array
    #So if array is b,a,d then graph will be
    #b->a->d
    def createGraph(self, array):
        #Create graph nodes and fill dictionary
        for letter in array:
            if not letter in self.nodesDictionary:
                node = self.createNode(letter)
                self.nodesDictionary[letter] = node
                if self.root == None:
                    self.root = node
        #Add edges
        for i in range(len(array)-1):
            pnode = self.nodesDictionary[array[i]]
            cnode = self.nodesDictionary[array[i+1]]
            pnode = self.addChildNode(pnode, cnode)

    def dfs(self, node, output):
        if not node.link:
            print output
            return
        for child in node.link:
            output.append(child.data)
            self.dfs(child, output)
            output.pop()

    def dfsTraversal(self):
        self.dfs(self.root, [self.root.data])
        
        
                
                
        
        
class trieNode(object):
    def __init__(self, letter):
        self.letter = letter
        self.childern = []
        self.childCount = 0

class CreateTrie():
    def __init__(self):
        self.trieRoot = trieNode("")
        #keeps track of all letters of all words in trie
        self.letterDictionary = []
        self.childCollector = []

    def traverse_collectChildern(self, parentNode):
        if not parentNode.childern:
            return       
        for child in parentNode.childern:
            if child.childCount > 1:
                childNodeData = self.returnChildNodeData(child)
                self.childCollector.append(childNodeData)
            self.traverse_collectChildern(child)
    #Traverses the trie and returns all the intermediate node childern    
    def collectChildern(self):
        rootChildern = self.returnChildNodeData(self.trieRoot)
        self.childCollector.append(rootChildern)
        self.traverse_collectChildern(self.trieRoot)
        return self.childCollector

    def findWord(self, word):
        parentNode = self.trieRoot
        for letter in word:
            childFlag, childNode = self.findChild(parentNode, letter)
            if childFlag:
                parentNode = childNode
            else:
                return False
        return True

    def returnChildNodeData(self, node):
        if not node.childern:
            return False
        output = []
        for child in node.childern:
            output.append(child.letter)
        return output

    def createNode(self, letter):
        node = trieNode(letter)
        return node

    def addChildToTrieNode(self, child, node):
        node.childern.append(child)
        node.childCount = node.childCount + 1

    def findChild(self, node, childData):
        #if Node does not have childern
        if not node.childern:
            return False, -1
        for child in node.childern:
            if(child.letter == childData):
                return True, child
        return False, -1
        
    def addWordToTrie(self, word):
        parentNode = self.trieRoot
        for letter in word:
            #Add letter to letter dictionary
            if not letter in self.letterDictionary:
                self.letterDictionary.append(letter)
            childFlag, childNode = self.findChild(parentNode, letter)
            if childFlag:
                parentNode = childNode
            else:
                #Create child node
                cnode = self.createNode(letter)
                self.addChildToTrieNode(cnode, parentNode)
                parentNode = cnode

class AlienDictionary(object):
    def __init__(self, words):
        self.graph = CreateGraph()
        self.trie = CreateTrie()
        #Create a trie
        for word in words:
            self.trie.addWordToTrie(word)

    def print_order(self):
        allChildern = self.trie.collectChildern()
        for child in allChildern:
            self.graph.createGraph(child)
        self.graph.dfsTraversal()



#Leetcode solution
class LeetCodeGraphNode(object):
    def __init__(self, letter):
        self.letter = letter
        self.next = None
        
class Solution(object):
    def __init__(self):
        self.hashTable = {}
        self.root = None
        
    def createNode(self, letter):
        node = LeetCodeGraphNode(letter)
        return node
    
    def addNextToNode(self, node, nextLink):
        node.next = nextLink

    def addToHashTable(self,letter):
        if not(letter in self.hashTable):
            self.hashTable[letter] = self.createNode(letter)
        if(self.root == None):
            self.root = self.hashTable[letter]

    def logic(self, words):
        for i in range(1, len(words)):
            letterIndex = 0
            while(letterIndex < len(words[i-1]) and letterIndex < len(words[i]) and words[i-1][letterIndex] == words[i][letterIndex]):
                self.addToHashTable(words[i][letterIndex])
                letterIndex = letterIndex+1
            
                
            
        
    def alienOrder(self, words):
        self.logic(words)
        """
        :type words: List[str]
        :rtype: str
        """






#Main program
#words = ["baa", "abcd", "abca", "cab", "cad"]
#words = ["caa", "aaa", "aab"]
words = ["wrt", "wrf", "er", "ett", "rftt"]
#o = AlienDictionary(words)
#o.print_order()

obj1 = Solution()
obj1.alienOrder(words)
