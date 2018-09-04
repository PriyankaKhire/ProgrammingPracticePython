#Word Break
# This time using bfs
class Node(object):
    def __init__(self, word):
        self.word = word
        #index of the last letter of the word
        self.lastIndex = None
        self.link = []
        
class Solution(object):
    def __init__(self):
        self.root = None
        self.q = []
        self.output = []
        
    def createNode(self, word, lastIndex):
        node = Node(word)
        node.lastIndex = lastIndex
        return node
    
    def addLink(self, node, child):
        node.link.append(child)

    def createTree(self, s, wordDict):
        #create root
        self.root = self.createNode(s[0], -1)
        self.q.append(self.root)
        while self.q:
            top = self.q.pop(0)
            #add all words starting from last index till end of s
            word = ""
            for i in range(top.lastIndex+1, len(s)):
                word = word + s[i]
                if(word in wordDict):
                    node = self.createNode(word, i)
                    self.addLink(top, node)
                    self.q.append(node)
                    
    def displayTree(self, root, output, s):
        if not root.link:
            if(root.lastIndex == len(s)-1):
                self.output.append(output.strip())
            return
        for child in root.link:
            self.displayTree(child, output+" "+child.word, s)
    
    def wordBreak(self, s, wordDict):
        self.createTree(s, wordDict)
        self.displayTree(self.root, "", s)
        print self.output

#Main
wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "catsandog"
o = Solution()
o.wordBreak(s, wordDict)
