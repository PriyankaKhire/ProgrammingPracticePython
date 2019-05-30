#Word Search II
#https://leetcode.com/problems/word-search-ii/
class TrieNode(object):
    def __init__(self):
        self.alphabets = [None for i in range(26)]
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def createNode(self):
        node = TrieNode()
        return node

    def addWord(self, word):
        index = 0
        ptr = self.root
        while(index < len(word)):
            letter = word[index]
            index = index + 1
            letterIndex = ord(letter.lower()) - ord('a')
            #if nothing present there
            if(ptr.alphabets[letterIndex] == None):
                node = self.createNode()
                ptr.alphabets[letterIndex] = node
            ptr = ptr.alphabets[letterIndex]
        ptr.endOfWord = True

    def dfs(self, node, word):
        if(node.endOfWord == True):
            print word
        for i in range(26):
            if(node.alphabets[i] != None):
                self.dfs(node.alphabets[i], word+chr(ord('a')+i))

    def display(self):
        self.dfs(self.root, "")
            
class Solution(object):
    def __init__(self):
        self.trie = Trie()
        self.output = []

    def displayMatrix(self, visited):
        for row in range(len(visited)):
            for col in range(len(visited[0])):
                print visited[row][col], " ",
            print "\n"
        
    def addWordsToTrie(self, words):
        for word in words:
            self.trie.addWord(word)
        #self.trie.display()

    def isValid(self, row, col, board, visited):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                if(visited[row][col] == 0):
                    return True
        return False

    def getValidRowCol(self, row, col, board, visited):
        output = []
        #up
        if(self.isValid(row-1, col, board, visited)):
            output.append([row-1, col])
        #down
        if(self.isValid(row+1, col, board, visited)):
            output.append([row+1, col])
        #left
        if(self.isValid(row, col-1, board, visited)):
            output.append([row, col-1])
        #right
        if(self.isValid(row, col+1, board, visited)):
            output.append([row, col+1])
        return output

    def findWordDFS(self, board, row, col, trieNode, word, visited):
        if(trieNode.endOfWord == True):
            print "\n*******************",word, "*******************\n"
            self.output.append(word)
        print "Visited \n---------"
        self.displayMatrix(visited)
        for i in range(26):
            if(trieNode.alphabets[i] != None):
                trieLetter = chr(ord('a')+i)
                boardLetters = self.getValidRowCol(row, col, board, visited)
                print "Next Trie letter ->", trieLetter
                print "Current board row -> ", row, " col -> ", col 
                if(boardLetters):
                    for rowCol in boardLetters:
                        print "board row -> ", rowCol[0], " board col -> ", rowCol[1],
                        print " board letter -> ", board[rowCol[0]][rowCol[1]]
                        if(board[rowCol[0]][rowCol[1]] == trieLetter):
                            #Mark next visited
                            visited[rowCol[0]][rowCol[1]] = 1
                            self.findWordDFS(board, rowCol[0], rowCol[1], trieNode.alphabets[i], word+trieLetter, visited)
                            #Backtrack
                            visited[rowCol[0]][rowCol[1]] = 0
                    print "\n"
        

    def searchBoard(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                charIndex = ord(board[row][col]) - ord('a')
                if(self.trie.root.alphabets[charIndex] != None):
                    visited = [[0 for c in range(len(board[0]))] for r in range(len(board))]
                    print "Current Trie Letter ->", board[row][col]
                    print "current row -> ", row, " current col -> ", col
                    visited[row][col] = 1
                    self.findWordDFS(board, row, col, self.trie.root.alphabets[charIndex], ""+board[row][col], visited) 
            print "\n"
        
    def findWords(self, board, words):
        self.addWordsToTrie(words)
        self.searchBoard(board)
        print self.output
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

#Main
board = [
  ['o','a','r','s'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain", "oars"]
obj = Solution()
obj.findWords(board, words)
