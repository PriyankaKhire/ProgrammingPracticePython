# Friend Circles
# https://leetcode.com/problems/friend-circles/submissions/
class Solution(object):
    
    def bfs(self, M, visited, queue):
        while(queue):
            top = queue.pop(0)
            visited[top] = True
            # add all unvisited neighbors of top
            for neighbor in range(len(M)):
                if(M[top][neighbor] == 1 and visited[neighbor] == False):
                    queue.append(neighbor)
        
    def findCircleNum(self, M):
        visited = [False for i in range(len(M))]
        circle = 0
        for friend in range(len(M)):
            if(visited[friend] == False):
                self.bfs(M, visited, [friend])
                circle = circle + 1
        return circle
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
