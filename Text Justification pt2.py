# Text Justification
# https://leetcode.com/problems/text-justification/
class Solution(object):
    def leftJustify(self, line, maxWidth):
        print line
        string = ""
        while(line):
            string = string + line.pop(0)
            if(line):
                string = string + ' '
        while(len(string) < maxWidth):
            string = string + ' '
        return string
        
    def createFinalAnswer(self, lines, spaces, maxWidth):
        answer = []
        for i in range(len(spaces)):
            string = ""
            if not spaces[i]:
                string = self.leftJustify(lines[i], maxWidth)
                answer.append(string)
                continue
            while(spaces[i]):
                # Add word
                string = string + lines[i].pop(0)
                # add space
                amountSpace = spaces[i].pop(0)
                for s in range(amountSpace):
                    string = string + ' '
            # add remaining word
            string = string + lines[i].pop(0)
            answer.append(string)
        # construct final line
        string = self.leftJustify(lines[-1], maxWidth)
        answer.append(string)
        return answer
        
        
    def addSpaces(self, lines, maxWidth):
        spaces = []
        for i in range(len(lines)-1):
            line = lines[i]
            #print line
            space = [0 for i in range(len(line)-1)]
            #print space
            if not space:
                spaces.append(space)
                continue
            lineLength = sum([len(word) for word in line])
            #print lineLength
            index = 0
            #print space
            while(lineLength < maxWidth):
                space[index] = space[index]+1
                lineLength = lineLength + 1
                index = (index + 1)%(len(line)-1)
            #print space
            spaces.append(space)
            #print "*"*20
        return spaces
    
    def createLines(self, words, maxWidth):
        lines = []
        line = []
        lineLength = 0
        for word in words:
            # if adding current words exceeds max width then add line to lines
            if(len(word)+lineLength > maxWidth):
                lines.append(line)
                line = []
                lineLength = 0
            line.append(word)
            # add 1 for space
            lineLength = lineLength + len(word) + 1
        # add last line to lines
        lines.append(line)
        return lines
    
    def fullJustify(self, words, maxWidth):
        lines = self.createLines(words, maxWidth)
        spaces = self.addSpaces(lines, maxWidth)
        return self.createFinalAnswer(lines, spaces, maxWidth)
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
