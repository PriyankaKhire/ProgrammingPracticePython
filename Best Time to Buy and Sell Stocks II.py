#Best Time to Buy and Sell Stock
#Say you have an array for which the ith element is the price of a given stock on day i.
#Design an algorithm to find all the profitable transactions

class FindPeaks(object):
    def __init__(self, array):
        self.array = array

    def findPeak(self):
        low = 0
        high = 0
        peaks = []
        for i in range(1, len(self.array)):
            if(self.array[i-1] > self.array[i]):
                #descending from peak
                low = i
            elif(self.array[i-1] < self.array[i]):
                #climbing the peak
                high = i
                print "peak value between indices ", low, " and ", high," is ", (self.array[high]-self.array[low])
                if(peaks and peaks[-1][0] == self.array[low]):
                    peaks[-1][1] = self.array[high]
                else:
                    peaks.append([self.array[low], self.array[high]])
        print peaks
                    
            
        
    def logic(self):
        self.findPeak()

#Main
a1 = [4,3,1,3,5,3,7]
a2 = [3,3,5,0,0,3,1,4]
obj = FindPeaks(a2)
obj.logic()
