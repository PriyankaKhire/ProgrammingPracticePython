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
        parentNode = self.trieRoot
        for letter in word:
            childFlag, childNode = self.findChild(parentNode, letter)
            if childFlag:
                parentNode = childNode
            else:
                #Create child node
                cnode = self.createNode(letter)
                self.addChildToTrieNode(cnode, parentNode)
                parentNode = cnode
                
        



#Main program
words = ["baa", "abcd", "abca", "cab", "cad"]
o = CreateTrie()
o.addWordToTrie("abcd")
