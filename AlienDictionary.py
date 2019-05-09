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
        #To detect cycle
        self.seen = False
        
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
            print "root is ", letter
            self.root = self.hashTable[letter]

    #creates nodes from letters and adds edge between node1 -> node2
    def connect2Letters(self, letter1, letter2):
        #if the nodes are not in hash table then add them
        self.addToHashTable(letter1)
        self.addToHashTable(letter2)
        #add edge from node1 -> node2
        self.addNextToNode(self.hashTable[letter1], self.hashTable[letter2])
        print "Added edge between ", letter1, " and ", letter2

    #need to imporve this function, right now its only doing simple traversal, we need topo sort or dfs
    def traverseLinkedList(self):
        ptr = self.root
        output = ""
        while(ptr != None):
            if(ptr.seen == True):
                return ""
            output = output +  ptr.letter
            ptr.seen = True
            ptr = ptr.next
        #Go through hash table, if there is no edgebetween rest of them then add it to output by alphabetical order
            
        return output

    def logic(self, words):
        for i in range(1, len(words)):
            if(words[i-1] == words[i]):
                return ""
            self.root = self.hashTable[letter]

    def logic(self, words):
        for i in range(1, len(words)):
            letterIndex = 0
            while(letterIndex < len(words[i-1]) and letterIndex < len(words[i]) and words[i-1][letterIndex] == words[i][letterIndex]):
                self.addToHashTable(words[i][letterIndex])
                letterIndex = letterIndex+1
            if(letterIndex < len(words[i-1]) and letterIndex < len(words[i]) ):
                self.connect2Letters(words[i-1][letterIndex], words[i][letterIndex])
        #Traverse the created linked list
        return self.traverseLinkedList()
                
    def alienOrder(self, words):
        print self.logic(words)
        self.logic(words)
        """
        :type words: List[str]
        :rtype: str
        """






#Main program
words1 = ["baa", "abcd", "abca", "cab", "cad"]
words2 = ["caa", "aaa", "aab"]
words3 = ["wrt", "wrf", "er", "ett", "rftt"]
words4 = [ "z","x","z"]
words5 = ["z", "z"]
words6 = ["wrt","wrtkj"]
#words = ["baa", "abcd", "abca", "cab", "cad"]
#words = ["caa", "aaa", "aab"]
words = ["wrt", "wrf", "er", "ett", "rftt"]
#o = AlienDictionary(words)
#o.print_order()

obj1 = Solution()
obj1.alienOrder(words1)

obj2 = Solution()
obj2.alienOrder(words2)

obj3 = Solution()
obj3.alienOrder(words3)

obj4 = Solution()
obj4.alienOrder(words4)

obj5 = Solution()
obj5.alienOrder(words5)

obj6 = Solution()
obj6.alienOrder(words6)

