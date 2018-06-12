#Trapping Rain Water
# https://www.geeksforgeeks.org/trapping-rain-water/

class TrappingRainWater(object):
    def __init__(self, inputArray):
        self.inputArr = inputArray

    def findRainWater(self, wall1, wall2):
        #if 2 walls are right next to each other then there can be no water trpped
        if wall2 == wall1+1:
            print "since wall2 is at index "+str(wall2)+" and wall1 is at index "+str(wall1)+" we return 0"
            return 0
        #if we find wall that is immediately next to wall 2 and is of equal or more height then return 0
        if self.inputArr[wall2-1] >= self.inputArr[wall2]:
            print "since the wall next to wall2 is "+str(self.inputArr[wall2-1])+" and wall2 is "+str(self.inputArr[wall2])+" we return 0"
            return 0
        rainWater = 0
        i = wall2-1
        print "Inside function now, i is "+str(i)
        print "wall1 is "+str(self.inputArr[wall1])+" and wall2 is "+str(self.inputArr[wall2]),
        # if wall 1 < wall 2
        if self.inputArr[wall2] > self.inputArr[wall1]:
            print " since wall1 < wall2"
            print "arr[i]  is "+str(self.inputArr[i])+" arr[wall1] is "+str(self.inputArr[wall1])
            while self.inputArr[i] < self.inputArr[wall1]:
                print "since arr[i] < arr[wall1]"
                rainWater = rainWater + (self.inputArr[wall1] - self.inputArr[i])
                i = i-1
                print "arr[i]  is "+str(self.inputArr[i])+" arr[wall1] is "+str(self.inputArr[wall1])
                print "i is "+str(i)
        else:
            #if wall1 >= wall2
            print " since wall1 >= wall2"
            print "arr[i]  is "+str(self.inputArr[i])+" arr[wall2] is "+str(self.inputArr[wall2])
            while self.inputArr[i] < self.inputArr[wall2]:
                print "since arr[i] < arr[wall2]"
                rainWater = rainWater + (self.inputArr[wall2] - self.inputArr[i])
                i = i-1
                print "arr[i]  is "+str(self.inputArr[i])+" arr[wall2] is "+str(self.inputArr[wall2])
                print "i is "+str(i)
        print "total rain water returned from function is "+str(rainWater)+" between wall 1 = "+str(self.inputArr[wall1])+" and wall 2 = "+str(self.inputArr[wall2])
        return rainWater
            
            

    def trapWater(self):
        indexHighestWallSoFar = None
        rainWater = 0
        for i in range(len(self.inputArr)):
            if self.inputArr[i] > 0:
                if indexHighestWallSoFar == None:
                    indexHighestWallSoFar = i
                    print "highest wall so far is "+str(self.inputArr[indexHighestWallSoFar])+" and is at index "+str(indexHighestWallSoFar)
                    continue
                rainWater = rainWater + self.findRainWater(indexHighestWallSoFar, i)
                print "Rain water collected so far between wall 1 = "+str(self.inputArr[indexHighestWallSoFar])+" at index "+str(indexHighestWallSoFar)+" and wall 2 = "+str(self.inputArr[i])+" at index "+str(i)+" is "+str(rainWater)
                if self.inputArr[indexHighestWallSoFar] < self.inputArr[i]:
                    indexHighestWallSoFar = i
                    print "highest wall so far is "+str(self.inputArr[indexHighestWallSoFar])+" and is at index "+str(indexHighestWallSoFar)
        print rainWater
                
#Main Program
o = TrappingRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
o.trapWater()
