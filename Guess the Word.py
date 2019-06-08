#Guess the Word
#https://leetcode.com/problems/guess-the-word/
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
import random
class Master(object):
    def __init__(self, wordList):
        randomIndex = random.randint(0, len(wordList)-1)
        self.secret = wordList[randomIndex]
        self.wordList = wordList

    def correctPos(self, word):
        count = 0
        i = 0
        j = 0
        while(i<len(word) and j<(len(self.secret))):
            if(word[i] == self.secret[j]):
                count = count + 1
            i = i+1
            j = j+1
        return count
        
    def guess(self, word):
        if not(word in self.wordList):
            return -1
        return self.correctPos(word)

class Solution(object):
    def __init__(self):
        self.hashTable = {}
    
    def correctPos(self, word, currentWord):
        count = 0
        i = 0
        j = 0
        while(i<len(word) and j<(len(currentWord))):
            if(word[i] == currentWord[j]):
                count = count + 1
            i = i+1
            j = j+1
        return count

    def putInHash(self, wordList):
        for i in range(len(wordList)):
            if not(wordList[i] in self.hashTable):
                self.hashTable[wordList[i]] = []
                #find correct postion of letters of each word against our current word
                for w in wordList:
                    if(w!=wordList[i] and w in self.hashTable):
                        self.hashTable[wordList[i]].append(self.hashTable[w][i])
                    else:
                        self.hashTable[wordList[i]].append(self.correctPos(w, wordList[i]))
        print self.hashTable

    def selectWords(self, guessData, canBeSecret, index):
        if(len(canBeSecret) == 1 or index >= len(guessData)):
            return canBeSecret
        newCanBeSecret = []
        for word in canBeSecret:
            if(self.hashTable[word][index] == guessData[index]):
                newCanBeSecret.append(word)
        return self.selectWords(guessData, newCanBeSecret, index+1)
        
    
    
    def findSecretWord(self, wordlist, master):
        self.putInHash(wordlist)
        guessData = []
        for i in range(9):
            guessData.append(master.guess(wordlist[i]))
        #Guess data gives partial array of correct position of letters against secret.
        print self.selectWords(guessData, wordlist, 0)
        print master.secret
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
#Main
wordList = ["census","series","access","chorus","canvas","stress","thanks","excess"]
wordList = ["witness","clothes","species","digress","dismiss","process","glasses","impress","grounds","address","undress","discuss","serious"]
wordList = ["mjpsce","giwiyk","slbnia","pullbr","ezvczd","dwkrmt","qgzebh","wvhhlm","kqbmny","zpvrkz","pdwxvy","gilywa","gmrrdc","vvqvla","rmjirt","qmvykq","mhbmuq","unplzn","qkcied","eignxg","fbfgng","xpizga","twubzr","nnfaxr","skknhe","twautl","nglrst","mibyks","qrbmpx","ukgjkq","mhxxfb","deggal","bwpvsp","uirtak","tqkzfk","hfzawa","jahjgn","mteyut","jzbqbv","ttddtf","auuwgn","untihn","gbhnog","zowaol","feitjl","omtiur","kwdsgx","tggcqq","qachdn","dixtat","hcsvbw","chduyy","gpdtft","bjxzky","uvvvko","jzcpiv","gtyjau","unsmok","vfcmhc","hvxnut","orlwku","ejllrv","jbrskt","xnxxdi","rfreiv","njbvwj","pkydxy","jksiwj","iaembk","pyqdip","exkykx","uxgecc","khzqgy","dehkbu","ahplng","jomiik","nmcsfe","bclcbp","xfiefi","soiwde","tcjkjp","wervlz","dcthgv","hwwghe","hdlkll","dpzoxb","mpiviy","cprcwo","molttv","dwjtdp","qiilsr","dbnaxs","dbozaw","webcyp","vftnkr","iurlzf","giqcfc","pcghoi","zupyzn","xckegy"]
m = Master(wordList)

obj = Solution()
obj.findSecretWord(wordList, m)

#This algo needs 11 guesses to guess the secret correctly.
