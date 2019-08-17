# Cracking the Safe
# https://leetcode.com/problems/cracking-the-safe/
# goal: to find the shortest length input password such that each possible n-length
# combination of digits [0..k-1] occurs exactly once as a substring.
class Solution(object):
    
    def findAllCombinations(self, n, numbers, combination, allCombinations):
        if(n == 0):
            allCombinations.append(combination)
            return 
        for num in numbers:
            self.findAllCombinations(n-1, numbers, combination+str(num), allCombinations)

    # returns true if last n-1 characters of the string match the first n-1 characters of node
    # this specific check prevents from creating longer length combinations.
    # how did i get this idea to incorporate this check ?
    # lets say n = 2 and k = 2
    # thus the k numbers are [0, 1]
    # n length combinations of k numbers are [00, 01, 10, 11]
    # one of the accepted password is 00110
    # now if we break down the password we get
    # "00" 110 -> 00
    # 0 "01" 10 -> 01
    # 00 "11" 0 -> 11
    # 001"10" -> 10
    # thus covering all the n length combinations of k numbers.
    # now if you look closely, where one combination ends, another one starts.
    def startsWith(self, n, string, node):
        if(n == 1):
            # because n-1 is 0 so we are comparing null string to null string
            return True
        return bool(string[-(n-1):] == node[:(n-1)])

    def dfs(self, nodes, visited, nodesVisited, output, n):
        print "Password string constructed so far is", output,"and visited nodes so far are",[nodes[i] for i in range(len(visited)) if visited[i] == True]
        print "Possible good fits to construct this password further begin with",output[-(n-1):]
        if(nodesVisited == len(nodes)):
            print output
            return
        for i in range(len(nodes)):
            if(self.startsWith(n, output, nodes[i]) and visited[i] == False):
                visited[i] = True
                self.dfs(nodes, visited, nodesVisited+1, output+nodes[i][-1], n)
                visited[i] = False
            
    def crackSafe(self, n, k):
        numbers = [i for i in range(k)]
        print "The k numbers are",numbers
        nLengthCombinationOfKnumbers = []
        self.findAllCombinations(n, numbers, "", nLengthCombinationOfKnumbers)
        print "The n length combinations of K digits are",nLengthCombinationOfKnumbers
        print "now from here this problem boils down to graph problem\n"
        print "The function startsWith returns true if last n-1 characters of the string match the first n-1 characters of node"
        print "this specific check prevents from creating longer length combinations."
        print "how did i get this idea to incorporate this check ?"
        print "lets say n = 2 and k = 2"
        print "thus the k numbers are [0, 1]"
        print "n length combinations of k numbers are [00, 01, 10, 11]"
        print "one of the accepted password is 00110"
        print "now if we break down the password we get"
        print "'00' 110 -> 00"
        print "0 '01' 10 -> 01"
        print "00 '11' 0 -> 11"
        print "001 '10' -> 10"
        print "thus covering all the n length combinations of k numbers."
        print "now if you look closely, where one combination ends, another one starts.\n"
        visited = [False for i in range(len(nLengthCombinationOfKnumbers))]
        for i in range(len(nLengthCombinationOfKnumbers)):
            visited[i] = True
            self.dfs(nLengthCombinationOfKnumbers, visited, 1, str(nLengthCombinationOfKnumbers[i]), n)
            visited[i] = False
        """
        :type n: int
        :type k: int
        :rtype: str
        """
# Main
obj = Solution()
obj.crackSafe(2, 2)
