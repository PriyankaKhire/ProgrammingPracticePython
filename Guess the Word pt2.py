# Guess the Word
# https://leetcode.com/problems/guess-the-word/
import random, string
class Master(object):
    def __init__(self, numberOfWords, wordLength, numberOfAlphabets):
        #self.wordList = [self.generateWord(wordLength, numberOfAlphabets) for i in range(numberOfWords)]
        self.wordList = ["mjpsce","giwiyk","slbnia","pullbr","ezvczd","dwkrmt","qgzebh","wvhhlm","kqbmny","zpvrkz","pdwxvy","gilywa","gmrrdc","vvqvla","rmjirt","qmvykq","mhbmuq","unplzn","qkcied","eignxg","fbfgng","xpizga","twubzr","nnfaxr","skknhe","twautl","nglrst","mibyks","qrbmpx","ukgjkq","mhxxfb","deggal","bwpvsp","uirtak","tqkzfk","hfzawa","jahjgn","mteyut","jzbqbv","ttddtf","auuwgn","untihn","gbhnog","zowaol","feitjl","omtiur","kwdsgx","tggcqq","qachdn","dixtat","hcsvbw","chduyy","gpdtft","bjxzky","uvvvko","jzcpiv","gtyjau","unsmok","vfcmhc","hvxnut","orlwku","ejllrv","jbrskt","xnxxdi","rfreiv","njbvwj","pkydxy","jksiwj","iaembk","pyqdip","exkykx","uxgecc","khzqgy","dehkbu","ahplng","jomiik","nmcsfe","bclcbp","xfiefi","soiwde","tcjkjp","wervlz","dcthgv","hwwghe","hdlkll","dpzoxb","mpiviy","cprcwo","molttv","dwjtdp","qiilsr","dbnaxs","dbozaw","webcyp","vftnkr","iurlzf","giqcfc","pcghoi","zupyzn","xckegy"]
        self.secret = random.choice(self.wordList)
        
    def generateWord(self, wordLength, numberOfAlphabets):
        letters = string.ascii_lowercase[:numberOfAlphabets]
        return ''.join(random.choice(letters) for i in range(wordLength))

    def awayFrom(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if(w1[i] == w2[i]):
                count = count+1
        return count
        
    def guess(self, word):
        return self.awayFrom(self.secret, word)
        """
        :type word: str
        :rtype int
        """

class Solution(object):
    def __init__(self):
        # the key is the word from word list and value is the listOfMatches hash table for that word.
        self.wordList = {}
        # key is the word, value is the master.guess return value
        self.guesses = {}

    def awayFrom(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if(w1[i] == w2[i]):
                count = count+1
        return count

    def findMatches(self, word, wordList):
        # the key is the number of matches and the value is the list of words having those many matches
        listOfMatches = {}
        for w in wordList:
            if(w == word):
                matchCount = len(word)
            else:
                matchCount = self.awayFrom(word, w)
            if not(matchCount in listOfMatches):
                listOfMatches[matchCount] = [w]
            else:
                listOfMatches[matchCount].append(w)
        return listOfMatches

    def findListOfMatches(self, wordlist):
        for word in wordlist:
            self.wordList[word] = self.findMatches(word, wordlist)
        print self.wordList

    def bfs(self, queue, guessCount, master):
        while(queue and guessCount<10):
            top = queue.pop(0)
            print "top word is", top
            if(top in self.guesses):
                continue
            distance = master.guess(top)
            print "distance from secret is", distance
            if(distance == len(top)):
                print "Found secret in", guessCount,"guesses"
                print "The secret is", top
                return True
            self.guesses[top] = distance
            print "guesses so far", self.guesses
            guessCount = guessCount + 1
            # union of 2 lists
            queue = list(set(queue) | set(self.wordList[top][distance]))
        print "Couldn't find the secret in 10 guesses, the queue was",queue
        return False
            
    def findSecretWord(self, wordlist, master):
        self.findListOfMatches(wordlist)
        guessCount = 0
        for word in wordlist:
            if(word in self.guesses):
                continue
            print "word is ",word
            distance = master.guess(word)
            self.guesses[word] = distance
            if(distance == len(word)):
                print "Found secret in", guessCount,"guesses"
                print "The secret is", word
                return True
            guessCount = guessCount + 1
            print "guesses so far", self.guesses
            if(self.bfs(self.wordList[word][distance], guessCount, master)):
                return True
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """

# Main
m = Master(10, 6, 4)
print "Secret is", m.secret
obj = Solution()
obj.findSecretWord(m.wordList, m)

