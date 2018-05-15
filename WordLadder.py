#word ladder
# https://leetcode.com/problems/word-ladder/description/
class Solution(object):

    def __init__(self):
        self.sol = None
    
    #Returns true if 2 words differ by 1 letter
    def differentByOne(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if(w1[i] != w2[i]):
                count = count +1
                if(count > 1):
                    return False
        if(count == 1):
            return True
        return False

class dfs(Solution):
    
    def ladder(self, output, endWord, wordList):
        print output
        print "---"
        if(output[-1] == endWord):
            print str(len(output))
            print output
            if( not self.sol):
                self.sol=len(output)
            if((self.sol) > len(output)):
                self.sol = len(output)
            return 
        topWord = output[-1]
        for word in wordList:
            if(word not in output):
                if(self.differentByOne(word, topWord)):
                    output.append(word)
                    self.ladder(output, endWord, wordList)
                    #Backtrack
                    output.pop()
            
    
    def ladderLength(self, beginWord, endWord, wordList):
        if(beginWord not in wordList):
            return 0
        if(endWord not in wordList):
            return 0
        if(self.differentByOne(beginWord, endWord)):
            return 2
        output = []
        output.append(beginWord)
        self.ladder(output, endWord, wordList)
        return self.sol

#In this approach we build a graph and then perform dfs or bfs on it
class graphNode(object):
    def __init__(self, data, parent):
        self.data = data
        self.childern = []
        self.parent = []
        self.parent.append(parent)
        
class bfs(Solution):

    def __init__(self, startWord, endWord, inputArray):
        self.startWord = startWord
        self.endWord = endWord
        self.inputArray = inputArray
        self.root = None

    def logic(self):
        self.createGraph()
        self.graphTraversal_dfs(self.root, [self.root.data])

    def createNode(self, data, parent):
        node = graphNode(data, parent)
        return node

    def addChildToNode(self, node, child):
        node.childern.append(child)
        return node

    def graphTraversal_dfs(self, root, path):
            if(root.data == self.endWord):
                print path
                return
            #for all the childern of the current node
            for child_node in root.childern:
                if not child_node.data in path:
                    path.append(child_node.data)
                    self.graphTraversal_dfs(child_node, path)
                    path.pop()
            

    def createGraph(self):
        hash_table = {}
        q = []
        self.root = self.createNode(self.startWord, None)
        hash_table[self.startWord] = self.root
        q.append(self.root)
        #While q is not empty
        while q:
            #Find all words in input array that differ by top element of q by one
            top = q.pop(0)
            print "Current top word is "+top.data
            for word in self.inputArray:
                if(self.differentByOne(top.data, word)):
                    #if word has not been added to graph
                    if(word not in hash_table):
                        node = self.createNode(word, top)
                        top = self.addChildToNode(top, node)
                        #We create a double edge
                        #meaning, parent can also be child of a node
                        node = self.addChildToNode(node, top)
                        top.parent.append(node)
                        hash_table[word] = node
                        q.append(node)
                        print "Added wordssss "+str(word)+" as a child of "+str(top.data)+" and vice versa"
                    else:
                        node = hash_table[word]
                        if(node not in top.parent):
                            top = self.addChildToNode(top, node)
                            node.parent.append(top)
                            node = self.addChildToNode(node, top)
                            top.parent.append(node)
                            print "Added word "+word+" as a child of "+top.data+" and vice versa"

    

#main program
s = dfs()
#print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
#print s.ladderLength("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])

#b = bfs("hit", "cog", ["hot","dot","dog","lot","log","cog"])
b = bfs("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
b.logic()
