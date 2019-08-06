#Chocolate Sweetness
#https://leetcode.com/discuss/interview-question/350800/Google-or-Onsite-or-Chocolate-Sweetness
class Backtracking(object):
    # Because you need to be able to ATLEAST code the worst case solution if you cannot think of the best answer
    def calculateSweetness(self, output):
        minSweetness = 9999
        for arraySet in output:
            minSweetness = min(minSweetness, sum(arraySet))
        return minSweetness
        
    def logic(self, array, k, output, index, sweetness):
        if(index == len(array)):
            if(len(output) == k):
                barSweetness = self.calculateSweetness(output)
                print "The min sweetness is ",output, "=>", barSweetness
                sweetness.append(barSweetness)
            return
        subArray = []
        for i in range(index, len(array)):
            subArray.append(array[i])
            output.append(subArray)
            self.logic(array, k, output, i+1, sweetness)
            output.pop()
        
    def splitArray(self, array, k):
        sweetness = []
        self.logic(array, k, [], 0, sweetness)
        print max(sweetness)
        

# Main
array = [6, 3, 2, 8, 7, 5]
obj = Backtracking()
obj.splitArray(array, 3)
