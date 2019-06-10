#Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/
class TrieNode(object):
    def __init__(self, letter):
        self.letter = letter
        self.next = [None for i in range(26)]
        self.endOfWord = False
        self.numberOfNextEntries = 0
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def getIndex(self, letter):
        return ord(letter.lower()) - ord('a')

    def addWord(self, word):
        ptr = self.root
        for char in word:
            index = self.getIndex(char)
            if(ptr.next[index] == None):
                node = TrieNode(char)
                ptr.next[index] = node
                ptr.numberOfNextEntries = ptr.numberOfNextEntries + 1
            ptr = ptr.next[index]
        ptr.endOfWord = True
            
    def dfs(self, node, word):
        if (node.endOfWord == True):
            print word
        for n in node.next:
            if(n != None):
                self.dfs(n, word+n.letter)
            
    def display(self):
        self.dfs(self.root, '')

    def commonPrefix(self, node, prefix):
        if(node.numberOfNextEntries > 1 or node.endOfWord == True):
            return prefix
        for n in node.next:
            if(n != None):
                return self.commonPrefix(n, prefix+n.letter)

    def findCommonPrefix(self):
        return self.commonPrefix(self.root, "")
            
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        trie = Trie()
        for word in strs:
            trie.addWord(word)
            if(trie.root.numberOfNextEntries > 1):
                return ""
        prefix = trie.findCommonPrefix()
        if not prefix:
            print  "None return"
        else:
            print prefix
        """
        :type strs: List[str]
        :rtype: str
        """
#Main
obj = Solution()
obj.longestCommonPrefix(["flower","flow","flight"])

obj = Solution()
obj.longestCommonPrefix(["a"])
