# Trie using hashmap
'''
Generally you code a trie using array of 26 spaces
where index of each character is the place where we store the next node
in this one we speed things up by using hash table
'''
class Node(object):
    def __init__(self, letter):
        self.letter = letter
        # key is letter value is letter object
        self.next = {}
        self.eow = False

class Trie(object):
    def __init__(self):
        self.root = Node("")

    def createNode(self, letter):
        return Node(letter)

    def addWord(self, word):
        ptr = self.root
        for char in word:
            if not(char in ptr.next):
                ptr.next[char] = Node(char)
            ptr = ptr.next[char]
        ptr.eow = True

    def dfs(self, node, output):
        if node.eow == True:
            print output
        for n in node.next:
            self.dfs(node.next[n], output+n)

    def display(self):
        self.dfs(self.root, "")

# Main
obj = Trie()
obj.addWord("a")
obj.addWord("aa")
obj.addWord("aaa")
obj.addWord("aaab")
obj.display()
