#Split given array into m sub arrays using back tracking
#the solution is inspired from my split array largest sum
class splitArray(object):
    def __init__(self, array, m):
        self.array = array
        self.m = m

    def recurrse(self, output, index):
        if(len(output) == self.m):
            if(index < len(self.array)):
                print "Not all numbers have been added to output array", output
            else:
                print output
            return
        subArray = []
        for i in range(index, len(self.array)):
            subArray.append(self.array[i])
            output.append(subArray)
            self.recurrse(output, i+1)
            #Backtrack
            output.pop()
            
    def logic(self):
        self.recurrse([], 0)
        
#Main
obj = splitArray([1,2,3,4,5], 3)
obj.logic()
           
