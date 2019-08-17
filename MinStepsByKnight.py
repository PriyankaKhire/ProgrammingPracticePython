# Minimum number of moves taken by a knight on a chess board to reach cell m,n
# https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/
class Solution(object):

    def isValid(self, chessBoardSize, row, col):
        if(row >= 0 and row < chessBoardSize):
            if(col >= 0 and col < chessBoardSize):
                return True
        return False

    def dfs(self, row, col, chessBoardSize, m, n, moveNumber, visited):
        if(row == m and col == n):
            print moveNumber
            return
        #                               down                up                right                left
        possibleMoves = [[2, -1],[2, 1], [-2, -1],[-2, 1], [-1, 2],[1, 2], [-1,-2],[1, -2]]
        for move in possibleMoves:
            new_row = row + move[0]
            new_col = col + move[1]
            if(self.isValid(chessBoardSize, new_row, new_col) and visited[new_row][new_col] == False):
                visited[new_row][new_col] = True
                self.dfs(new_row, new_col, chessBoardSize, m, n, moveNumber+1, visited)
                visited[new_row][new_col] = False

    def bfs(self, chessBoardSize, m, n, visited, queue):
        if not queue:
            return
        top = queue.pop(0)
        rowCol = top[0]
        moveNumber = top[1]
        if(rowCol[0] == m and rowCol[1] == n):
            print moveNumber
            return
        visited[rowCol[0]][rowCol[1]] = True
        #                               down                up                right                left
        possibleMoves = [[2, -1],[2, 1], [-2, -1],[-2, 1], [-1, 2],[1, 2], [-1,-2],[1, -2]]
        for move in possibleMoves:
            new_row = rowCol[0] + move[0]
            new_col = rowCol[1] + move[1]
            if(self.isValid(chessBoardSize, new_row, new_col) and visited[new_row][new_col] == False):
                queue.append([[new_row, new_col], moveNumber+1])
        self.bfs(chessBoardSize, m, n, visited, queue)
                
                
    def numberOfMoves(self, chessBoardSize, m,n):
        # the chessboard is square so the size is chessBoardSize X chessBoardSize
        # the knight always starts at 0, 0
        visited = [[False for col in range(chessBoardSize)] for row in range(chessBoardSize)]
        # You can see dfs is not a good algo for this, bfs is.
        self.dfs(0, 0, chessBoardSize, m, n, 0, visited)
        self.bfs(chessBoardSize, m,n, visited, [[[0, 0], 0]])

# Main
obj = Solution()
obj.numberOfMoves(6, 5, 0)
