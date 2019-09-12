# Find Case Combinations of a String
'''
Find all the combinations of a string in lowercase and uppercase.
For example, string "ab" >>> "ab", "Ab", "aB", "AB".
So, you will have 2^n (n = number of chars in the string) output strings.
The goal is for you to test each of these strings and see if it matchs a hidden string.
'''
class Solution(object):
    def logic(self, strLst, index, output):
        if(index == len(strLst)):
            print output
            return
        # add capital to output
        self.logic(strLst, index+1, output+strLst[index].upper())
        # add lower to output
        self.logic(strLst, index+1, output+strLst[index].lower())
        
    def findCombinaitons(self, string):
        self.logic(list(string), 0, "")


# Main
obj = Solution()
obj.findCombinaitons('AirBnB')
