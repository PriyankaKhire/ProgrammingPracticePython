#Random Programs
class PrintTriangle(object):
    def __init__(self, range_numbers):
        self.range = range_numbers

    def logic(self):
        space = 0
        for i in range(self.range/2):
            print ((self.range/2)-i)*" ", i+1, space*" ", self.range-i
            space = space+2

class PrintDiamond(object):
    def __init__(self, range_numbers):
        self.range = range_numbers

    def logic(self):
        space = 0
        for i in range((self.range/4)+1):
            print ((self.range/2)-i)*" ", i+1, space*" ", self.range-i
            space = space+2
        space = space-4
        for i in range(self.range/4 + 1, self.range/2):
            print (i+1)*" ", i+1, space*" ", self.range-i
            space = space-2

#Main
pt = PrintTriangle(10)
#pt.logic()

pd = PrintDiamond(100)
pd.logic()
