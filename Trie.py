#Trie
class Node(object):
    def __init__(self, data):
        self.data = data
        self.childern = []
        self.endWord = False

class trie(object):
    def __init__(self):
        self.root = self.createNode("")

    def createNode(self, data):
        node = Node(data)
        return node

    #This function can be modified to add in alphabetical order
    #So instead of just append we would calculate its position and add child word on that position
    #But for simplicity sake we are doing just normal append
    def addChild(self, node, child):
        node.childern.append(child)

    def findChild(self, parent, childData):
        if not parent.childern:
            return False, -1
        for child in parent.childern:
            if(child.data == childData):
                return True, child
        return False, -1

    def addWord(self, word):
        parent = self.root
        endNode = None
        for letter in word:
            childFlag, child = self.findChild(parent, letter)
            if childFlag:
                parent = child
                endNode = child
            else:
                #create child node
                child = self.createNode(letter)
                #Add child to parent
                self.addChild(parent, child)
                parent = child
                endNode = child
        endNode.endWord = True

    def dfs(self, node, word):
        if node.endWord:
            print word
        if not node.childern:
            return
        for child in node.childern:
            word = word + child.data
            self.dfs(child, word)
            word = word[:-1]

    def traverse(self):
        self.dfs(self.root, "")

    def findWord(self, word):
        parent = self.root
        for letter in word:
            flag, child = self.findChild(parent, letter)
            if not flag:
                return False
            parent = child
        return True
            
            
            
        
#Main Program
o = trie()
o.addWord("abc")
o.addWord("abcd")
o.addWord("abcde")
o.addWord("kfs")
o.traverse()
print o.findWord("kfs")
