# Welsh alphabetical order
# Given a welsh dictionary, sorted in welsh alphabetical order,
# and a list of words written in the welsh language, sort the list of words
# in welsh alphabetical order

# Please refer to https://developers.google.com/edu/python/sorting

class Solution(object):
    def __init__(self):
        self.alphabets = ['a','b','c','ch','dd','d','e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
        self.newAlphabets = []
        # key = newWord val = old word
        self.newWordOldWordDict = {}

    # convert letters inot ascii ordered letters so a becomes A
    # b -> B, c->C, cd->D etc.
    def convertAlphabets(self):
        for i in range(len(self.alphabets)):
            # chr converts ascii value to alphabet
            # we can even start with 0 but 65 is letter A
            # with 0 it takes longer for compiler to compile.
            newChar = chr(i+65)
            self.newAlphabets.append(newChar)

    def convertWord(self, word):
        i = 0
        newWord = ''
        while i < len(word):
            if (i+1 < len(word) and word[i]+word[i+1] in self.alphabets):
                newWord += self.newAlphabets[self.alphabets.index(word[i]+word[i+1])]
                i = i+2
            else:
                newWord += self.newAlphabets[self.alphabets.index(word[i])]
                i = i+1
        # add to dict
        self.newWordOldWordDict[newWord] = word
        return newWord
    
    # convert the words into ascii ordered words based on new alphabets   
    def logic(self, words):
        print "old words", words
        self.convertAlphabets()
        newWords = []
        for word in words:
            newWords.append(self.convertWord(word))
        print "new words", newWords
        # sort new words
        newWords.sort()
        print "sorted new words", newWords
        # replace new words with old words
        sortedOldWords = []
        for w in newWords:
            sortedOldWords.append(self.newWordOldWordDict[w])
        print sortedOldWords
# Main
obj = Solution()
obj.logic(["ddr","nah","dea","dd","ngah"])

