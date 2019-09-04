class Solution1(object):
    def __init__(self):
        # key is word value is [[matrix coordinates of the word]]
        self.hashTable = {}
    
    def isValid(self, row, col, matrix):
        if(row >= 0 and row < len(matrix)):
            if(col >= 0 and col < len(matrix)):
                if(matrix[row][col] != '0'):
                    return True
        return False
    
    def findWord(self, matrix, word, row, col, index, coordinates):
        if(index == len(word)):
            return True
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for move in moves:
            new_r = row+move[0]
            new_c = col+move[1]
            if(self.isValid(new_r, new_c, matrix) and matrix[new_r][new_c] == word[index]):
                coordinates.append([new_r, new_c])
                if(self.findWord(matrix, word, new_r, new_c, index+1, coordinates)):
                    return True
                coordinates.pop()
                
    def putInHash(self, wordList, matrix):
        print "Hash Table"
        for word in wordList:
            print word
            self.hashTable[word] = []
            # Put the coordinates of matrix where the word is present.
            for r in range(len(matrix)):
                for c in range(len(matrix)):
                    if(matrix[r][c] == word[0]):
                        coordinates = [[r, c]]
                        # The complete word may or may not be found starting at r, c
                        # if a word is found then findWord returns true.
                        if(self.findWord(matrix, word, r, c, 1, coordinates)):
                            self.hashTable[word].append(coordinates)           
            print self.hashTable[word]
        print "*"*30

    def checkMatrixIfCoordinatesAreTaken(self, coordinates, matrix):
        for coordinate in coordinates:
            if(matrix[coordinate[0]][coordinate[1]] == '0'):
                # The matrix coordiantes are taken by another word.
                return True
        return False

    # replaces matrix coordinates with '0'
    def OverTakeCoordinates(self, coordinates, matrix):
        for coordinate in coordinates:
            matrix[coordinate[0]][coordinate[1]] = '0'

    # replaces back matrix coordinates with word, this is used for backtracking.
    def GiveAwayCoordinates(self, coordinates, matrix, word):
        i = 0
        for coordinate in coordinates:
            matrix[coordinate[0]][coordinate[1]] = word[i]
            i = i+1

    def dfs(self, wordList, index, output, matrix, allLists):
        # Gather all the possible lists that are formed
        # [:] is used to copy list, else the list will be stored as a reference and we dont want that.
        allLists.append(output[:])
        if(index == len(wordList)):
            return
        for i in range(index, len(wordList)):            
            for coordinate in self.hashTable[wordList[i]]:
                # if matrix coordinates are not taken 
                if not(self.checkMatrixIfCoordinatesAreTaken(coordinate, matrix)):
                    # then take the matrix coordinates
                    self.OverTakeCoordinates(coordinate, matrix)
                    self.dfs(wordList, i+1, output+[wordList[i]], matrix, allLists)
                    # backtrack
                    self.GiveAwayCoordinates(coordinate, matrix, wordList[i])
        
    def getMaxWords(self, wordList, matrix):
        # 1) Build a hash table where the value is word and key is places in matrix where the word is present
        self.putInHash(wordList, matrix)
        # 2) Do a simple DFS on words present in word list.
        # each time we either add the current word with current coordinates or we add different word.
        allLists = []
        self.dfs(wordList, 0, [], matrix, allLists)
        # Find the longest list
        longestList = []
        for l in allLists:
            if(len(l) > len(longestList)):
                longestList = l
        print longestList

# Main
wordList = ["eat", "oath", "aak", "ner", "oei", "thfl"]
matrix = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
    ]
obj = Solution1()
obj.getMaxWords(wordList, matrix)
