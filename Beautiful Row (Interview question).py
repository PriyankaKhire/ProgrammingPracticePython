#Beautiful Row
#A farmer has planted trees in rows.
#He considers a row  of trees beautiful if the heights of the trees are in bitonic sequence.
#A bitonic sequence is a sequence with:
# 1) x0 <= x1 <= ... <= xk >= xk+1 >= ... >= xn  or
# 2) x0 >= x1 >= ... >= xn or
# 3) x0 <= x1 <= ... xn
#given an array with the height of the trees
#find the minimum number of elements to be removed to make that sequence bitonic
# example:
# [3, 17, 5, 12, 4, 6, 2, 1] => 2 we can remove 17 and 4 to make it 3, 5, 12, 6, 2, 1
# [3, 7, 4, 8, 6, 2, 1, 5] => 2 we can remove 7 and 5 to make it 3, 4, 8, 6, 2, 1
# [9, 6, 4, 3, 10 => 0 the sequence is already in bitonic order
class BeautifulRow(object):
    def __init__(self, array):
        self.array = array

    def isAscending(self, array):
        for i in range(1, len(array)):
            if(array[i] < array[i-1]):
                return False
        return True

    def isDescending(self, array):
        for i in range(1, len(array)):
            if(array[i] > array[i-1]):
                return False
        return True

    #checks if the given array is bitonic or not.
    def isBitonic(self, array):
        if not array:
            return True
        if(self.isAscending(array)):
            return True
        if(self.isDescending(array)):
            return True
        if(len(array) == 1 or len(array) == 2):
            return True
        peakFound = False
        for i in range(len(array)-1):
            #if peak not found you expect array to be ascending
            if not peakFound:
                if(array[i] > array[i+1]):
                    peakFound = True
            else:
                if(array[i] < array[i+1]):
                    return False
        return True

    def removeElementsOnLeftSide(self, lowIndex,  highIndex, currOutput, peak):
        #remove the elements on left side
        for i in range(lowIndex, highIndex):
            if(self.array[i] < peak):
                if(currOutput):
                    if(self.array[i] > currOutput[-1]):
                        currOutput.append(self.array[i])
                        self.removeElementsOnLeftSide(i+1, highIndex, currOutput, peak)
                        currOutput.pop()
                else:
                    currOutput.append(self.array[i])
                    self.removeElementsOnLeftSide(i+1, highIndex, currOutput, peak)
                    currOutput.pop()
        print currOutput

    def removeElementsOnRightSide(self, lowIndex,  currOutput, peak):
        #remvoe the elements on right side.
        for i in range(lowIndex, len(self.array)):
            if(self.array[i] < peak):
                if(currOutput):
                    if(self.array[i] < currOutput[-1]):
                        currOutput.append(self.array[i])
                        self.removeElementsOnRightSide(i+1,  currOutput, peak)
                        currOutput.pop()
                else:
                    currOutput.append(self.array[i])
                    self.removeElementsOnRightSide(i+1,  currOutput, peak)
                    currOutput.pop()
        print currOutput
                
                    
        
    def logic(self):
        if(self.isBitonic(self.array)):
            return True
        #Taking each indivudial number as the peak
        for i in range(len(self.array)):
            print "Current Peak -->", self.array[i]
            #Search on left side
            print "***Left side***"
            self.removeElementsOnLeftSide(0, i, [], self.array[i])
            #search on right side
            print "***Right side***"
            self.removeElementsOnRightSide(i+1,  [], self.array[i])
        print "At the end just combine the left and right side and see what array holds max elements"
        print "the array with max elements needs to remove min elements from original"
        print "and that is your answer"
            


#Main
obj = BeautifulRow([3, 17, 5, 12, 4, 6, 2, 1])
obj.logic()
