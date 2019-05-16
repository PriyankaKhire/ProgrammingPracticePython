#Median of Medians
class FindMedian(object):

    def recurrse(self, array, medians, index):
        if(index >= len(array)):
            return medians
        #Step 1) divide array in chunks of 5
        if(index+5 < len(array)):
            chunk = array[index: index+5]
        else:
            chunk = array[index:len(array)]
        #Step 2) sort these chunks (sort preferably by selection sort)
        chunk.sort()
        #Step 3) get the median
        medians.append(chunk[(len(chunk)-1)/2])
        return self.recurrse(array, medians, index+5)

    def mediansOfMedians(self, array):
        medians = array
        while (len(medians) != 1):
            #Step 4) repeat until you find a pivot.
            medians = self.recurrse(medians, [], 0)
        return medians[0]

    def partition(self, array, pivot, low, high):
        if (low == high):
            return array, high
        #Step 5) Partition around pivot element.
        while(low < high):
            while(low < high and array[low] <= pivot):
                low = low + 1
            while(low < high and array[high] > pivot):
                high = high - 1
            #Swap
            array[low], array[high] = array[high], array[low]
        #Finally place pivot at its right position
        low = 0
        pivotIndex = high - 1
        while(low < pivotIndex):
            while(low < pivotIndex and array[low] != pivot):
                low = low + 1
            while(low < pivotIndex and array[pivotIndex] == pivot):
                pivotIndex = pivotIndex - 1
            #Swap
            array[low], array[pivotIndex] = array[pivotIndex], array[low]
        return array, pivotIndex
        
        
    def logic(self, array):
        pivotIndex = 0
        medianIndex = (len(array)-1)/2
        print "The index of median in the array is ", medianIndex
        low = 0
        high = (len(array)-1)
        while(pivotIndex != medianIndex):
            #Slicing an array: if a = [0,1,2,3,4,5] then a[0:3] = [0,1,2] and != [0,1,2,3] thats why we add extra one to high
            pivot = self.mediansOfMedians(array[low:high+1])
            array, pivotIndex = self.partition(array, pivot, low, high)
            #Step 6) if median index is less than pivot index then go search in left side else search in right side
            if(pivotIndex > medianIndex):
                high = pivotIndex - 1
            else:
                low = pivotIndex + 1
        print "The median of unsroted array is ",pivot

#Main
obj = FindMedian()
obj.logic([25,21,98,100,76,22,43,60,89,87,1,5,6,7,9,5,4,33,66,54,79,64,85,19])
