class Solution(object):
    def isVowel(self, letter):
        if (letter.lower() in ('a', 'e', 'i', 'o', 'u')):
            return True
        return False

    def countVowelsInWord(self, word):
        # print "Substring is", word
        count = 0
        for letter in word:
            if (self.isVowel(letter)):
                count += 1
        return count

    def generateSubstrings(self, word):
        count = 0
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                substring = word[i:j]
                count += self.countVowelsInWord(substring)
        return count

    def countVowels(self, word):
        return self.generateSubstrings(word)
        """
        :type word: str
        :rtype: int
        """
