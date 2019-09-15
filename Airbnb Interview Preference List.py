# Preference List
'''
Given a list of lists that contains every one's preferred cityes
ouput city list that follows every one's prefernce.

Input:
[[3, 5, 7, 9], [2, 3, 8], [5, 8]]

Output:
One of possible output is
[2, 3, 5, 8, 7, 9].
'''
class Solution(object):
    def __init__(self):
        self.pointers = None
        self.numListThatReachedEnd = 0
    
    def findPreferences(self, cityList):
        self.pointers = [0 for i in range(len(cityList))]
        output = []
        while(self.numListThatReachedEnd < len(cityList)):
            for currList in range(len(cityList)):
                if(self.pointers[currList] < len(cityList[currList])):
                    if not(cityList[currList][self.pointers[currList]] in output):
                        output.append(cityList[currList][self.pointers[currList]])
                    # advance the pointer
                    self.pointers[currList] = self.pointers[currList] + 1
                    # if pointer has reached the end of list then increment numListThatReachedEnd
                    if(self.pointers[currList] == len(cityList[currList])):
                        self.numListThatReachedEnd = self.numListThatReachedEnd + 1
        print output
        
# Main
obj = Solution()
obj.findPreferences([[3, 5, 7, 9], [2, 3, 8], [5, 8]])
