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
# [3, 17, 5, 12, 6, 2, 1] => 1 we can remove 5 to make it 3, 17, 12, 6, 2, 1
# [3, 7, 4, 8, 6, 2, 1, 5] => 2 we can remove 7 and 5 to make it 3, 4, 8, 6, 2, 1
# [9, 6, 4, 3, 10 => 0 the sequence is already in bitonic order
class BeautifulRow(object):
    def __init__(self, array):
        self.inputArray = array

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

    def removeElementsOnLeftSide(self, lowIndex, highIndex, currOutput):
        #remove the elements on left side

    def removeElementsOnRightSide(self, lowIndex, highIndex, currOutput):
        #remvoe the elements on right side.
        
    def logic(self):
        if(self.isBitonic(self.array)):
            return True
        #Taking each indivudial number as the peak
        for i in range(len(self.array)):
            


#Main
obj = BeautifulRow([1,2,3,4,5,6,7,8,9,6,3,1])
print obj.isBitonic([5,6,7,8,1])
