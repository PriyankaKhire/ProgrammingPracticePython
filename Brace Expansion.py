# Brace Expansion
# https://leetcode.com/problems/brace-expansion/
class Solution(object):
    def logic(self, array, index, output, stringList):
        if(index == len(array)):
            stringList.append(output)
            return
        for char in array[index].split(','):
            self.logic(array, index+1, output+char, stringList)
            
    def expand(self, S):
        array = []
        for splitLetters in S.split("{"):
            array = array + splitLetters.split("}")
        # remove empty strings from array
        new_array = []
        for char in array:
            if(char != ''):
                if(len(char.split(',')) > 1):
                    sortedChar = [x for x in sorted(char) if x!=',']
                    char = ','.join(sortedChar)
                new_array.append(char)
        stringList = []
        self.logic(new_array, 0, "", stringList)
        print stringList
        """
        :type S: str
        :rtype: List[str]
        """

# Main
obj  = Solution()
obj.expand("{a,b}c{d,e}f")

obj  = Solution()
obj.expand("abcd")

obj  = Solution()
obj.expand("{a,b}{z,x,y}")
