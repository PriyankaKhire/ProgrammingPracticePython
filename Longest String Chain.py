# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
class Solution(object):
    def longestStrChain(self, words):
        # put words in hash table
        # key = word, value = string chain (initial value is 1)
        hashTable = {word:1 for word in words}
        print "The hash table contains",hashTable
        # sort words according to length in descending order (longest word has index 0)
        words.sort(key=len, reverse=True)
        # for every word in words, remove one letter at time and see if its in hash table or not
        for word in words:
            print "Current word is",word
            for i in range(len(word)):
                print "Removing letter at index",i
                print "is",word[:i]+word[i+1:],"present in hash table?",(word[:i]+word[i+1:] in hashTable)
                if(word[:i]+word[i+1:] in hashTable):
                    print "Current string chain length of word",word[:i]+word[i+1:],"is",hashTable[word[:i]+word[i+1:]]
                    hashTable[word[:i]+word[i+1:]] = max(hashTable[word[:i]+word[i+1:]], hashTable[word]+1)
                    print "New string chain legth is",hashTable[word[:i]+word[i+1:]]
            print "*"*30
        print "Longest string chain length is",max(hashTable.values())
        """
        :type words: List[str]
        :rtype: int
        """

# Main
obj = Solution()
obj.longestStrChain(["a","b","ba","bca","bda","bdca"])
