#Counting Bits
#https://leetcode.com/problems/counting-bits/description/

class Approch1(object):
    def __init__(self, n):
        self.n = n
        self.matrix = [[0 for col in range(n+1)] for row in range(n+1)]
        self.array = [0 for i in range(n+1)]

    def displayMatrix(self):
        for row in range(self.n+1):
            print self.matrix[row]
        print "\n"

    def cpy(self, lowIndex, highIndex, number):
        #copy values from low index to number in matrix
        #[:] at end is to copy the lists and not make it into reference.
        self.matrix[number] = self.matrix[lowIndex][:]
        #add high Index value
        self.matrix[number][highIndex] = 1
        #Modify the array of 1s count
        self.array[number] = self.array[lowIndex]+1

    def approch(self):
        highIndex = 0
        #for n = 1
        self.matrix[1][0] = 1
        self.array[1] = 1
        #n + 1 coz we want n to be included
        for i in range(2, self.n+1):
            if(i-(2**highIndex) < 2**highIndex):
                self.cpy(i-(2**highIndex), highIndex, i)
            else:
                highIndex = highIndex+1
                self.matrix[i][highIndex] = 1
                self.array[i] = 1

    def logic(self):
        self.approch()
        self.displayMatrix()
        print self.array

class Approch2(object):
    def __init__(self, n):
        self.n = n
        self.array = [0 for i in range(n+1)]

    def approch(self):
        if(self.n >= 1):
            self.array[1] = 1
        if(self.n >= 2):
            self.array[2] = 1
        if(self.n >= 3):
            self.array[3] = 2
        if(self.n >3):
            #high is just like highIndex in approch 1
            high = 4
            for i in range(high, self.n+1):
                if(i-high == high):
                    high = i
                self.array[i] = self.array[i-high]+1

    def logic(self):
        self.approch()
        print self.array


#Main
obj1 = Approch1(23)
obj1.logic()

obj2 = Approch2(23)
obj2.logic()
