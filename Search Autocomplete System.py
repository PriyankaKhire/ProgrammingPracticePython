#Design Search Autocomplete System
#
#Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:
#
#The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
#The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
#If less than 3 hot sentences exist, then just return as many as you can.
#When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
#Your job is to implement the following functions:
#
#The constructor function:
#
#AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.
#
#Now, the user wants to input a new sentence. The following function will provide the next character the user types:
#
#List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.
#
#
#Example:
#Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2]) 
#The system have already tracked down the following sentences and their corresponding times: 
#"i love you" : 5 times 
#"island" : 3 times 
#"ironman" : 2 times 
#"i love leetcode" : 2 times 
#Now, the user begins another search: 
#
#Operation: input('i') 
#Output: ["i love you", "island","i love leetcode"] 
#Explanation: 
#There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored. 
#
#Operation: input(' ') 
#Output: ["i love you","i love leetcode"] 
#Explanation: 
#There are only two sentences that have prefix "i ". 
#
#Operation: input('a') 
#Output: [] 
#Explanation: 
#There are no sentences that have prefix "i a". 
#
#Operation: input('#') 
#Output: [] 
#Explanation: 
#The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search. 
#
#Note:
#The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
#The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
#Please use double-quote instead of single-quote when you write test cases even for a character input.
#Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
from operator import itemgetter
#This is a tri node
class Node(object):
    def __init__(self, data):
        self.data = data
        self.childern = [None for i in range(255)]
        #sentence and score value
        self.hotSentences = []
        # A node only has hot score if its #
        self.hotScore = 0

class Trie(object):
    def __init__(self):
        self.root = self.createNode("")

    def createNode(self, data):
        node = Node(data)
        return node
    
    def findChronologicalOrder(self, s1, s2):
        if s1 == s2:
            return s1
        length = len(s1)
        if len(s2) < len(s1):
            length = len(s2)
        for i in range(length):
            #find first different letter
            if(s1[i] != s2[i]):
                if(ord(s1[i]) < ord(s2[i])):
                    return s1
                return s2
        #if sentence such as abc and abcd then return abc
        if len(s1) < len(s2):
            return s1
        return s2

            
    #updates the hot score
    def updateHotSentences(self, node, hotScore, sentence):
        #print "current hot sentence is "+sentence+" with score "+str(hotScore)
        #print "presently the node "+node.data+" has these hot sentences"+str(node.hotSentences)
        #if sentence is same but score has changed
        for s in node.hotSentences:
            if(s[0] == sentence):
                #print "since "+s[0]+" is same as current hot sentence ",
                s[1] = hotScore
                #print "after updating its hot score "+str(sentence),
                #print "the node now is "+str(node.hotSentences)
                return
        #less than 3 sentences present
        if (len(node.hotSentences) < 3):
            node.hotSentences.append([sentence, hotScore])
            #print "Since node has less than 3 hot sentences we append now node has"+str(node.hotSentences)
            return
        #if 2 nodes have same hot score
        for s in node.hotSentences:       
            if (s[1] == hotScore):
                sentence = self.findChronologicalOrder(s[0], sentence)
                s[0] = sentence
                return
        #print "sorting and removing excess sentences from node "+str(node.hotSentences)
        #if adding new sentence
        node.hotSentences.append([sentence, hotScore])
        #print "after appending the node is "+str(node.hotSentences)
        #just sort these 4 by the order of their hot score and put it back in node.hotSentences
        sorted(node.hotSentences, key=itemgetter(1))
        #print "after sorting the node is "+str(node.hotSentences)
        #pop the hotScore and sentence at index 3 from node.hotSentences
        node.hotSentences.pop()
        #print "after popping the node is "+str(node.hotSentences)
        
        

    def insertChild(self, parentNode, childData):
        #Find place to insert by calculating child's ASCII value
        asciiValue = ord(childData)
        childNode = None
        #if no child at that location is present only then insert
        #if there is a child already there, that means we dont need to insert anything
        if (parentNode.childern[asciiValue]  == None):
            childNode = self.createNode(childData)
            parentNode.childern[asciiValue] = childNode
        else:
            childNode = parentNode.childern[asciiValue]
        return childNode

    def insertSentence(self, sentence):
        #first search for the sentence, if its present then just increase its hot degree count.
        hotScore = 1
        flag, lastNode = self.searchSentence(sentence)
        if flag:
            hotScore = lastNode.hotScore+1
        parent = self.root
        for i in range(len(sentence)):
            parent = self.insertChild(parent, sentence[i])
            self.updateHotSentences(parent, hotScore, sentence[i:])
            if sentence[i] == "#":
                parent.hotScore = hotScore
                
    #returns true if sentence found along with final node of the sentence.
    def searchSentence(self, sentence):
        parent = self.root
        for char in sentence:
            ascii = ord(char)
            if(parent.childern[ascii] == None):
                return False, None
            parent = parent.childern[ascii]
            #print parent.data, parent.hotScore, parent.hotSentences
        return True, parent

class AutoComplete(object):
    def __init__(self, sentences, times):
        self.trie = Trie()
        #add sentence in trie those many times
        for i in range(len(sentences)):
            for insert in range(times[i]):
                self.trie.insertSentence(sentences[i])

    def constructSentence(self):
        choice = "y"
        while choice == "y":
            char = ""
            sentence = ""
            while char != "#":
                char = raw_input("\nEnter next part of sentence ")
                sentence = sentence+char
                f, n = self.trie.searchSentence(sentence)
                if f:
                    for hotSentence in n.hotSentences:
                        print sentence+hotSentence[0][1:],
            print "the sentence is complete "+sentence
            self.trie.insertSentence(sentence)
            choice = raw_input("\n Would you like to insert more sentences ? y/n ")
            
        

#Main Program
o = Trie()
print "inserting i love you#"
o.insertSentence("i love you#")
print "inserting i love priyanka#"
o.insertSentence("i love priyanka#")
print "inserting i love priyanka#"
o.insertSentence("i love priyanka#")
print "inserting i love priyanka#"
o.insertSentence("i love priyanka#")
print "inserting i love you#"
o.insertSentence("i love you#")
print "inserting i love laddoo#"
o.insertSentence("i love laddoo#")
print "inserting i love easter#"
o.insertSentence("i love easter#")
print "inserting i abcd#"
o.insertSentence("i abcd#")
flag, node =  o.searchSentence("i")
print flag, node.hotSentences
flag, node =  o.searchSentence("i l")
print flag, node.hotSentences
a = AutoComplete(["i love you#", "i love priyanka#", "inserting i love laddoo#", "i love easter#"],[2, 3, 1, 1])
a.constructSentence()
