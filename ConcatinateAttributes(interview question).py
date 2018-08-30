#Given lists of lists, each containing attributes, join them all with one another
#example: input = [[a,b,c],[d,e,f,g],[h,i,j]]
#output = [a.d.h, a.d.i, a.d.j ...]

class Solution(object):
    def __init__(self, lists):
        self.lists = lists

    def permutation(self, listIndex, string, visitedLists):
        if(len(visitedLists) == len(self.lists)):
            print string
            return
        for i in range(len(self.lists)):
            if not(i in visitedLists):
                for attr in self.lists[i]:
                    visitedLists.append(i)
                    self.permutation(i, string+"."+attr, visitedLists)
                    #backtrack
                    visitedLists.pop()

    def wrapper(self):
        for i in range(len(self.lists)):
            for attr in self.lists[i]:
                self.permutation(i, attr, [i])

#Main
lists = [['a','b','c'],['d','e','f','g'],['h','i','j']]
o = Solution(lists)
o.wrapper()
