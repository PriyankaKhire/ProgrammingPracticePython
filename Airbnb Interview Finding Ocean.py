# Finding Ocean
class Solution(object):

    def isValid(self, row, col, matrix):
        if(row >= 0 and row < len(matrix)):
            if(col >= 0 and col < len(matrix[0])):
                return True
        return False

    def convertOcean(self, matrix, row, col):
        if(matrix[row][col] == 'L'):
            return
        # mark current water as ocean
        matrix[row][col] = 'O'
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for move in moves:
            new_r = move[0]+row
            new_c = move[1]+col
            if(self.isValid(new_r, new_c, matrix) and matrix[new_r][new_c] == 'W'):
                self.convertOcean(matrix, new_r, new_c)
                

    def convertInputMapToMatrix(self, inputMap):
        matrix = [[None for col in range(len(inputMap[0]))] for row in range(len(inputMap))]
        for row in range(len(inputMap)):
            for col in range(len(inputMap[0])):
                matrix[row][col] = inputMap[row][col]
        return matrix

    def findOcean(self, inputMap, row, col):
        matrix = self.convertInputMapToMatrix(inputMap)
        self.convertOcean(matrix, row, col)
        for row in range(len(matrix)):
            print "".join(matrix[row])

# Main
inputMap = ["WWWLLLW","WWLLLWW","WLLLLWW"]
row = 0
col = 1
obj = Solution()
obj.findOcean(inputMap, row, col)
print "\n"
inputMap = ["WWWLLLW","WWLLLWW","WLLLLWW"]
row = 2
col = 6
obj = Solution()
obj.findOcean(inputMap, row, col)
print "\n"
inputMap = ["LLLLLLLLLLLLLLLLLLLL","LLLLLLLLLLLLLLLLLLLL","LLLLLLLLLLLLLLWLLLLL","LLWWLLLLLLLLLLLLLLLL","LLWWLLLLLLLLLLLLLLLL","LLLLLLLLLLLLLLLLLLLL","LLLLLLLWWLLLLLLLLLLL","LLLLLLLLWWLLLLLLLLLL","LLLLLLLLLWWWLLLLLLLL","LLLLLLLLLLWWWWWWLLLL","LLLLLLLLLLWWWWWWLLLL","LLLLLLLLLLWWWWWWLLLL","LLLLWWLLLLWWWWWWLLLL","LLLLWWWLLLWWWWWWWWWW","LLLLLWWWWWWWWWWWLLLL","LLLLLLLLLLLLLLWWWWLL","LLLLLLLLLLLLLLWLLLLL","LLLLWLLLLLLLLLLLLWLL","LLLLLLLLLLLLLLLLLLWL"]
row = 9
col = 12
obj = Solution()
obj.findOcean(inputMap, row, col)
