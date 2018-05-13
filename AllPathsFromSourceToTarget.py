#All Paths From Source to Target
#https://leetcode.com/problems/all-paths-from-source-to-target/description/

class dfs(object):
    def __init__(self, input_matrix):
        self.input_matrix = input_matrix

    def solution(self, source, destination, path):
        if source == destination:
            print path
            return
        for next_node in self.input_matrix[source]:
            path.append(next_node)
            self.solution(next_node, destination, path)
            #Back track
            path.pop()
'''
Cannot really thik of a way to do it in bfs
class bfs(object):
    def __init__(self, input_matrix):
        self.input_matrix = input_matrix

    def solution(self, source, destination, path):
        q = []
        q.append(source)
        path = []
        while q:
            top - = q.pop(0)
            if(top == destination):
                print path
                continue
'''            

#Main Program
matrix = [[1,2], [3], [3], []]
obj = dfs(matrix)
obj.solution(0, 3, [0])
