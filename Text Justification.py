#Text Justification
#https://leetcode.com/problems/text-justification/
class Solution(object):
    def __init__(self):
        self.output = []

    def formLine(self, line):
        l = ""
        for char in line:
            if(self.isinteger(char)):
                l = l + (char*" ")
            else:
                l = l + char
        self.output.append(l)
        
    def isinteger(self, a):
        try:
            int(a)
            return True
        except ValueError:
            return False
    
    def addSpace(self, line, width, maxWidth):
        remainingSpace = maxWidth - width
        while(remainingSpace > 0 and len(line) > 1):
            for i in range(len(line)):
                if(self.isinteger(line[i]) and remainingSpace>0):
                    line[i] = line[i]+1
                    remainingSpace = remainingSpace - 1
        if(len(line) == 1):
            line.append(maxWidth - width)
        self.formLine(line)
                
    def logic(self, words, maxWidth):
        line = []
        width = 0
        for word in words:
            if not line:
                line.append(word)
                width = len(word)
            else:
                if(width+1+len(word) > maxWidth):
                    self.addSpace(line, width, maxWidth)
                    #we dont append current word                    
                    line = [word]
                    width = len(word)
                else:
                    line.append(1)
                    line.append(word)
                    width = width+1+len(word)
        #format last line
        line.append(maxWidth - width)
        self.formLine(line)
            
    def fullJustify(self, words, maxWidth):
        self.logic(words, maxWidth)
        print self.output
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

#Main
words = ["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"]
obj = Solution()
obj.fullJustify(words, 20)

words = ["What","must","be","acknowledgment","shall","be"]
obj = Solution()
obj.fullJustify(words, 16)
