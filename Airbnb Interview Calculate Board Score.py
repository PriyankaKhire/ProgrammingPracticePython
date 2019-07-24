'''
Given a board that is a kingdom. The board is represented as an array of strings. Each string contains a number of tiles separated by a space. Each tile consists of a letter, and there can be 0-9 crowns. Your task is to calculate the total score. The score calculation is done by using the following formula:
number of same tiles in an area * number of crowns in that area.

A board can be of any size no greater than 5x5.

Input:
["L0 W1 W1 W0 F2",
"W0 W0 T0 T0 T0",
"W0 W1 T0 R2 R1" ,
"L0 K0 L1 L0 L0",
"R0 C2 C0 L1 T0"]

Output: 41

Explanation: The total score of this board is 41.
(1 * 0) + (7 * 3) + (1 * 2) + (4 * 0) + (2 * 3) + (1 * 0) + (4 * 2) + (1 * 0) + (2 * 2) + (1 * 0) = 0 + 21 + 2 + 0 + 6 + 0 + 8 + 0 + 4 + 0 = 41.
'''
def isValid(graph, row, col):
    if(row >= 0 and row < len(graph)):
        if(col >= 0 and col < len(graph[0])):
            return True
    return False

def findIsland(graph, row, col, letter, count):
    graph[row][col] = 'x'
    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for neighbor in neighbors:
        nr = neighbor[0]+row
        nc = neighbor[1]+col
        if(isValid(graph, nr, nc) and graph[nr][nc][0] == letter):
            #islands
            count[0] = count[0] + 1
            #crowns
            count[1] = count[1] + int(graph[nr][nc][1])
            findIsland(graph, nr, nc, letter, count)
            

def islands(graph):
    total = 0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if(graph[row][col] != 'x'):
                count = [1, int(graph[row][col][1])]
                letter = graph[row][col][0]
                findIsland(graph, row, col, letter, count)
                total = total +(count[0]*count[1])
    print total


def convertGraph(graph):
    new_graph = []
    for line in graph:
        new_graph.append(line.split(" "))
    islands(new_graph)

#Main
graph = ["L0 W1 W1 W0 F2",
         "W0 W0 T0 T0 T0",
         "W0 W1 T0 R2 R1" ,
         "L0 K0 L1 L0 L0",
         "R0 C2 C0 L1 T0"]
convertGraph(graph)
