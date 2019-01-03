#Burst Balloons
#https://leetcode.com/problems/burst-balloons/

class Approch1(object):
    def __init__(self, array):
        self.array = array

    def findLeft(self, intermediateArray, index):
        for i in range(index-1, -1, -1):
            if(intermediateArray[i] != 'x'):
                return intermediateArray[i]
        return 1

    def findRight(self, intermediateArray, index):
        for i in range(index+1, len(intermediateArray)):
            if(intermediateArray[i] != 'x'):
                return intermediateArray[i]
        return 1

    def addResult(self, indexArray):
        total = 0
        intermediateArray = self.array[:]
        for i in range(len(indexArray)):
            currBallon = intermediateArray[indexArray[i]]
            prevBallon = self.findLeft(intermediateArray, indexArray[i])
            nextBallon = self.findRight(intermediateArray, indexArray[i])
            total = total + (prevBallon* currBallon*nextBallon)
            intermediateArray[indexArray[i]] = 'x'
        return total

    def permutation(self, indexArray, result, resultIndex, count):
        if(count == len(indexArray)):
            print result, resultIndex, self.addResult(resultIndex)
            return
        for i in range(len(indexArray)):
            if(indexArray[i] > 0):
                result.append(self.array[i])
                resultIndex.append(i)
                indexArray[i] = indexArray[i]-1
                self.permutation(indexArray, result, resultIndex, count+1)
                #Backtrack
                result.pop()
                resultIndex.pop()
                indexArray[i] = indexArray[i]+1
                
    def logic(self):
        #permutation method is taken from tushar roy's video.
        indexArray = [1 for i in range(len(self.array))]
        self.permutation(indexArray, [], [], 0)


#Main
obj = Approch1([3,1,5,8])
obj.logic()
