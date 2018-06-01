#Given a sorted dictionary of an alien language, find order of characters

class trieNode(object):
    def __init__(self, letter):
        self.letter = letter
        self.childern = []
        self.childCount = 0

class CreateTrie():
    def __init__(self):
        self.trieRoot = trieNode("")

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
        
    def addWordToTrie(self, word):
        childFlag, child = self.findChild(self.trieRoot, word[0])
        parentNode = self.trieRoot
        #if child not found
        if not childFlag:
            #Add the word as is            
            for letter in word:
                #Create node for it
                node = self.createNode(letter)
                #Add node as child to parent node
                self.addChildToTrieNode(node, parentNode)
                #make current node as parent node
                parentNode = node
        else:
            #if child is found then add to existing node
            wordIndex = 0
            while wordIndex < len(word):
                
        



#Main program
words = ["baa", "abcd", "abca", "cab", "cad"]
o = CreateTrie()
o.addWordToTrie("abcd")
