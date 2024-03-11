# Add Bold Tag in String
# https://leetcode.com/problems/add-bold-tag-in-string/description/

class Solution(object):
    def findWord(self, word, subString, index):
        for i in range(len(word)):
            if (index+i >= len(subString)):
                return False
            if (word[i] != subString[index+i]):
                return False
        return True
    
    def markBold(self, word, bold, index):
        for i in range(index, index+len(word)):
            bold[i] = True
        

    def addBoldTag(self, s, words):
        bold = [False for i in range(len(s))]
        
        # for all the words mark them true in bold array
        for word in words:
            for i in range(len(s)):
                # if current letter is first letter of word
                if (s[i] == word[0]):
                    # find if the word exists in sub string
                    if (self.findWord(word, s, i)):
                        # mark bold
                        self.markBold(word, bold, i)
        # collect all bolds and put the bold tag around them
        i = 0
        output = ""
        while(i<len(bold)):
            if not(bold[i]):
                output += s[i]
                i += 1
                continue
            # start of bold
            output += "<b>"
            while(i<len(bold) and bold[i]):
                output += s[i]
                i += 1
            output += "</b>"
        return output

                    
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
