#Word Ladder II
#https://leetcode.com/problems/word-ladder-ii/
class GraphNode(object):
    def __init__(self, word):
        self.word = word
        self.next = []

class Graph(object):
    def __init__(self):
        self.root = None

    def createNode(self, word):
        return GraphNode(word)

    def addToNode(self, node, word):
        newNode = self.createNode(word)
        node.next.append(newNode)

    def dfs(self, node, output, finalDisplay, endWord):
        if not node.next:
            if(endWord == node.word):
                finalDisplay.append(output)
            return
        for n in node.next:
            self.dfs(n, output+[n.word], finalDisplay, endWord)

    def display(self, endWord):
        finalDisplay = []
        self.dfs(self.root, [self.root.word], finalDisplay, endWord)
        return finalDisplay
    
class Solution(object):
    def __init__(self):
        self.g = Graph()
    
    def differentByOne(self, word1, word2):
        if(word1 == word2):
            return False
        flag = False
        for i in range(len(word1)):
            if(word1[i] != word2[i]):
                if(flag == False):
                    flag = True
                else:
                    return False
        return True
    
    def bfs(self, endWord, wordList, visited, queue):
        #If the queue is empty then return
        if(not queue):
            return
        #pop the top node from queue
        topNode = queue.pop(0)
        top = topNode.word
        #if top is end word, then we return we do this because we want end word in final graph
        if(top == endWord):
            return
        for i in range(len(wordList)):
            #if the word is not visited and is different by one
            if(visited[i] == False and self.differentByOne(top, wordList[i])):
                #add it to queue
                gNode = self.g.createNode(wordList[i])
                queue.append(gNode)
                #Add this node to top node in graph
                topNode.next.append(gNode)
                #if the current word is end word, just add it to queue but dont mark is visited, we do this so that we can add end word to more than 1 output.
                if(wordList[i] == endWord):
                    continue
                #Mark the word visited
                visited[i] = True                               
        #recurrse
        self.bfs(endWord, wordList, visited, queue)      
        
    def findLadders(self, beginWord, endWord, wordList):
        gNode = self.g.createNode(beginWord)
        self.g.root = gNode
        queue = [gNode]
        visited = [False for i in range(len(wordList))]
        self.bfs(endWord, wordList, visited, queue)
        print self.g.display(endWord)
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
#Main
obj = Solution()
obj.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"])

obj.findLadders('hit', 'cog', ["hot","dot","dog","lot","log"])
