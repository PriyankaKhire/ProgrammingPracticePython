#Word Search II
# https://leetcode.com/problems/word-search-ii/
class Backtracking(object):

    def isValid(self, row, col, board):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                return True

    def dfs(self, word, index, row, col, board, visited):
        if(word[index] != board[row][col]):
            return
        if(index == len(word)-1):
            return True
        moves = [[0, 1],[0, -1], [1, 0], [-1, 0]]
        for move in moves:
            new_r = move[0]+row
            new_c = move[1]+col
            if(self.isValid(new_r, new_c, board) and visited[new_r][new_c] == False):
                visited[new_r][new_c] = True
                if(self.dfs(word, index+1, new_r, new_c, board, visited)):
                    return True
                visited[new_r][new_c] = False
        
    
    def findWord(self, word, board):
        # The same letter cell may not be used more than once in a word.
        visited = [[False for col in range(len(board[0]))] for row in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited[row][col] = True
                if(self.dfs(word, 0, row, col, board, visited)):
                    return True
                visited[row][col] = False
        
    def findWords(self, board, words):
        print words
        result = []
        for word in words:
            if(self.findWord(word, board)):
                result.append(word)
        print result
        print "*"*50
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
######################################################
######################################################
######################################################
# took help from https://leetcode.com/problems/word-search-ii/discuss/59814/A-detailed-explanation-C%2B%2B-solution-(Trie-%2B-backtracking)
# https://www.youtube.com/watch?v=x02b8zfvGFU&t=614s
class TrieNode(object):
    def __init__(self, letter):
        self.letter = letter
        # key is letter, value is object
        self.next = {}
        self.eow = False
        # this is for dfs
        self.wordAddedToResult = False
        self.word = ""

class TrieOperations(object):
    def __init__(self):
        self.root = TrieNode("Root")

    def addWord(self, word):
        ptr = self.root
        for char in word:
            if not(char in ptr.next):
                ptr.next[char] = TrieNode(char)
            ptr = ptr.next[char]
        ptr.eow = True
        ptr.word = word

    def dfs(self, node, output):
        if(node.eow):
            print output
        for n in node.next:
            self.dfs(node.next[n], output+node.next[n].letter)

    def display(self):
        self.dfs(self.root, "")

class TrieDFS(object):
    def __init__(self):
        self.trie = TrieOperations()

    def isValid(self, row, col, board):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                return True

    def dfs(self, board, row, col, result, trieNode, visited):
        print "Current trie node is",trieNode.letter
        print "The visited matrix"
        for r in range(len(visited)):
            print visited[r]
        # if the current trie node forms a complete word and if this has not already been added to result, then we add it to result
        if(trieNode.eow == True and trieNode.wordAddedToResult == False):
            print "Added word",trieNode.word,"to result"
            result.append(trieNode.word)
            trieNode.wordAddedToResult = True
        # continue searching coz there can be more words that have same prefix ex: aaa, aaab, aaaa
        # so if we find word aaa, we still need to keep going coz words aaaa, aaab are still ahead
        # the below part is taken from backtracking class dfs method, with additional trie support.
        moves = [[1,0], [-1,0], [0, 1], [0, -1]]
        for move in moves:
            new_r = move[0]+row
            new_c = move[1]+col
            print "Considering new row",new_r,"new col", new_c
            # for every valid, and unvisited cell in board
            if(self.isValid(new_r, new_c, board) and visited[new_r][new_c] == False):
                # check if that cell letter is present in trie or not
                if not(board[new_r][new_c] in trieNode.next):
                    print "Current board letter",board[new_r][new_c],"is not present in trie node next"
                    continue
                print "Current board letter",board[new_r][new_c],"is present in trie node next"
                visited[new_r][new_c] = True
                self.dfs(board, new_r, new_c, result, trieNode.next[board[new_r][new_c]], visited)
                visited[new_r][new_c] = False

    def logic(self, board):
        # how many words can we add from each point of board ?
        finalResult = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                print "Currently on row =",r,"and col =",c,"on board"
                print "Current board letter is",board[r][c]
                # if there is no letter in trie root that matches the current letter then move on to next cell on board.
                if not(board[r][c] in self.trie.root.next):
                    continue
                result = []
                visited = [[False for col in range(len(board[0]))] for row in range(len(board))]
                visited[r][c] = True
                self.dfs(board, r, c, result, self.trie.root.next[board[r][c]], visited)           
                print "The result we got from current row and col is:",result
                finalResult.extend(result)
        print finalResult
                
        
    def findWords(self, board, words):
        print "The board is"
        for r in range(len(board)):
            print board[r]
        #Add all words to trie
        for word in words:
            self.trie.addWord(word)
        # start searching the trie.
        self.logic(board)
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

######################################################
######################################################
######################################################
# without explanantion method, leetcode accepted
class Node(object):
    def __init__(self, letter):
        self.letter = letter
        self.next = {}
        # used to mark end of word.
        self.word = ""

class Trie(object):
    def __init__(self):
        self.root = Node("")
    
    def addWord(self, word):
        ptr = self.root
        for char in word:
            if not(char in ptr.next):
                ptr.next[char] = Node(char)
            ptr = ptr.next[char]
        # we mark end of word by assigning word.
        ptr.word = word
            
class Solution(object):
    def __init__(self):
        self.trie = Trie()
    
    def isValid(self, row, col, board):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                return True
    
    def dfs(self, board, row, col, trieNode, visited, res):
        if(trieNode.word != ""):
            res.append(trieNode.word)
            trieNode.word = ""
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for move in moves:
            new_r = move[0]+row
            new_c = move[1]+col
            if(self.isValid(new_r, new_c, board) and visited[new_r][new_c] == False):
                if not(board[new_r][new_c] in trieNode.next):
                    continue
                visited[new_r][new_c] = True
                self.dfs(board, new_r, new_c, trieNode.next[board[new_r][new_c]], visited, res)
                visited[new_r][new_c] = False
    
    def logic(self, board):
        finalRes = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if not(board[r][c] in self.trie.root.next):
                    continue
                res = []
                visited = [[False for col in range(len(board[0]))] for row in range(len(board))]
                visited[r][c] = True
                self.dfs(board, r, c, self.trie.root.next[board[r][c]], visited, res)
                finalRes.extend(res)
        return finalRes
        
    def findWords(self, board, words):
        # add all words to trie
        for word in words:
            self.trie.addWord(word)
        return self.logic(board)
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
# Main
print "Backtracking"
obj = Backtracking()
obj.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])

obj = Backtracking()
obj.findWords([["a","b"],["a","a"]], ["aba","baa","bab","aaab","aaa","aaaa","aaba"])

obj = Backtracking()
obj.findWords([["a","a"]], ["a"])

obj = Backtracking()
obj.findWords([["a"]], ["ab"])
print "=-"*30

print "Trie Solution explanation"
obj = TrieDFS()
obj.findWords([["a","b"],["a","a"]], ["aba","baa","bab","aaab","aaa","aaaa","aaba"])
print "=-"*30
print "Without explanantion, leetcode accepted"
obj = Solution()
print obj.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
print "=-"*30
