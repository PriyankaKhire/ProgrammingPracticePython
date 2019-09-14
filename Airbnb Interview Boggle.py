# -*- coding: cp1252 -*-
# Boggle
'''
Given dictionary of words, and a board.
You need to find largest set of words on the board that are present in dictionary such that:

1)
Words should be created by using adjoining letters,
The letters may join in any direction – horizontally, vertically, or diagonally.
Words can be spelled in any direction, including backwards.

2)
You may not use a letter cube multiple times in a single word.

3)
Once you find a word, you may not use the same cubes of the letters in the word to find other words.

Example:
Input:
board = [
['o', 'a', 'a', 'n'],
['e', 't', 'a', 'e'],
['i', 'h', 'k', 'r'],
['i', 'f', 'l', 'v']
    ]
wordList = ["eat", "oath", "aak", "ner", "oei", "thfl"]

Output:
["aak", "ner", "oei", "thfl"]

Explanation:
Actually all these words can be formed in the matrix, but we have to ensure the biggest list of words.
'''
#Approch:
# Please go through Word Search II to find out most of the logic.
class TrieNode(object):
    def __init__(self, letter):
        self.letter = letter
        self.next = {}
        # this helps in determining end of word
        self.word = ""

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def createNode(self, letter):
        return TrieNode(letter)

    def addWord(self, word):
        ptr = self.root
        for char in word:
            if not(char in ptr.next):
                ptr.next[char] = self.createNode(char)
            ptr = ptr.next[char]
        ptr.word = word

    def dfs(self, node):
        if(node.word != ""):
            print node.word
        for n in node.next:
            self.dfs(node.next[n])

    def display(self):
        self.dfs(self.root)

class BoggleTrieDfs(object):
    def __init__(self):
        # key is word value is [board coordinates]
        self.hash = {}
        self.trie = Trie()
        self.maxWordList = []

    def isValid(self, row, col, board):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                return True

    def findWordsOnBoard(self, board, row, col, trieNode, visited, coordinates):
        # if we find a word add the coordinates of that to hash table
        if(trieNode.word != ""):
            self.hash[trieNode.word].append(coordinates)
        # continue the search
        # we are moving, up, down, left, right, and diagonally up left, diagonally up right, diagonally down left, diagonally down right
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        for move in moves:
            new_r = move[0]+row
            new_c = move[1]+col
            # if new row is valid and not visited
            if(self.isValid(new_r, new_c, board) and visited[new_r][new_c] == False):
                # if the valid board cell letter is present in trie node next
                if not(board[new_r][new_c] in trieNode.next):
                    continue
                visited[new_r][new_c] = True
                # please pay special attention to trieNode.next[board[new_r][new_c]]
                # here we are sending the trie node who's letter matches with that of board[new_r][new_c]
                self.findWordsOnBoard(board, new_r, new_c, trieNode.next[board[new_r][new_c]], visited, coordinates+[[new_r, new_c]])
                # backtrack
                visited[new_r][new_c] = False

    def findWords(self, board):
        # here is where we do things a little differently from word search II
        # when we find a word on the board, we also find it's coordinates and we store thos coordinates in hash table
        # so now let's start finding the words on the board from each point
        for row in range(len(board)):
            for col in range(len(board[0])):
                # if current letter of the board is in trie
                if not(board[row][col] in self.trie.root.next):
                    continue
                visited = [[False for c in range(len(board[0]))] for r in range(len(board))]
                visited[row][col] = True
                # please pay special attention to self.trie.root.next[board[row][col]]
                # here we are sending the node who's letter matches with that of board[row][col]
                self.findWordsOnBoard(board, row, col, self.trie.root.next[board[row][col]], visited, [[row, col]])

    def coordinatesPresent(self, coordinates, outputCoordinates):
        for coordinate in coordinates:
            if(coordinate in outputCoordinates):
                return True
        return False

    def findMaxListOfWords(self, wordList, index, wordOutput, outputCoordinates):
        if(index == len(wordList)):
            if(len(wordOutput) > len(self.maxWordList)):
                self.maxWordList = wordOutput[:]
            return
        for i in range(index, len(wordList)):
            for coordinates in self.hash[wordList[i]]:
                # if coordinates not present in output coordinates
                if not(self.coordinatesPresent(coordinates, outputCoordinates)):
                    self.findMaxListOfWords(wordList, i+1, wordOutput+[wordList[i]], outputCoordinates+coordinates)

    def getMaxWordOnBoard(self, board, wordList):
        # add all words in word list to trie
        for word in wordList:
            self.trie.addWord(word)
        # initialize the hash table
        self.hash = {word:[] for word in wordList}
        #self.trie.display()
        self.findWords(board)
        #print self.hash
        self.findMaxListOfWords(wordList, 0, [], [])
        print self.maxWordList
        

# Main

board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
    ]
wordList = ["eat", "oath", "aak", "ner", "oei", "thfl"]
b = BoggleTrieDfs()
b.getMaxWordOnBoard(board, wordList)

board = [
    ["a", "x", "e"],
    ["s", "e", "l"],
    ["s", "h", "o"]
    ]
wordList = ["asshole", "ass", "she", "ex", "hole"]
b = BoggleTrieDfs()
b.getMaxWordOnBoard(board, wordList)


board=[
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
    ]
wordList=["oath","pea","eak","rain","ifl"]
b = BoggleTrieDfs()
b.getMaxWordOnBoard(board, wordList)


board=[
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"]
    ]
wordList=["abc", "cfi", "beh", "defi", "gh"]
b = BoggleTrieDfs()
b.getMaxWordOnBoard(board, wordList)


board=[
    ["a","b"],
    ["c","d"],
    ["a","b"],
    ["c","d"]
    ]
wordList=["ab","ac","acd","c","d"]
b = BoggleTrieDfs()
b.getMaxWordOnBoard(board, wordList)


board=[
    ["a","a","b","a"],
    ["a","b","a","a"],
    ["a","a","a","b"],
    ["b","a","a","a"]
    ]
wordList=["aba","ba","baba","abab", "ab", "b"]
b = BoggleTrieDfs()
b.getMaxWordOnBoard(board, wordList)

# this takes too much time.
board=[
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"],
    ["a","a","a","a"]
    ]
wordList=["aaa","aa","aaaa","aaaa", "aa", "a"]
b = BoggleTrieDfs()
b.getMaxWordOnBoard(board, wordList)
