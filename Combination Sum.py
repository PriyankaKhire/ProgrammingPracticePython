# Combination Sum
#https://leetcode.com/problems/combination-sum/
#Wrong logic
class Solution1(object):
    def __init__(self):
        self.ht = {}
        
    def putInHash(self, candidates):
        for num in candidates:
            if not(num in self.ht):
                self.ht[num] = True
                
    def logic(self, candidates, target):
        output = []
        for num in candidates:
            if(num == target):
                output.append([num])
                continue
            print "Number ", num
            temp = [num]
            targetTemp = target
            print "Temp array ", temp, " Temporary Target ", targetTemp
            while(targetTemp-num > 0):
                print "TargetTemp - num ", targetTemp-num
                if(targetTemp-num in self.ht):
                    print "Target Temp - num present in hash"
                    temp.append(targetTemp-num)
                    #this step is performed to avoid duplicate inserts.
                    temp.sort()
                    print "Temp array now is ", temp
                    if not(temp in output):
                        output.append(temp[:])
                        print "Appending temp array to output ", output
                    temp.pop()
                    print "Temp Array now is ", temp
                temp.append(num)
                print "Temp array after appending number ", temp
                targetTemp = targetTemp - num
                print "Temp target is ", targetTemp
        print output
                
    def combinationSum(self, candidates, target):
        self.putInHash(candidates)
        self.logic(candidates, target)
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

#Wrong solution
class Solution2(object):
    def __init__(self):
        self.hash = {}

    def addToHash(self, key, value):
        if not key in self.hash:
            self.hash[key] = [value]
        else:
            self.hash[key].append(value)

    def putInHash(self, candidates, target):
        for num in candidates:
            self.addToHash(num, [num])
            tempNum = num
            tempArr = [num]
            while(tempNum+num < target):
                tempNum = tempNum + num
                tempArr.append(num)
                self.addToHash(tempNum, tempArr[:])

    def logic(self, candidates, target):
        for num in candidates:
            if(num == target):
                output.append([num])
                continue
            temp = [num]
            targetTemp = target
            while(targetTemp-num > 0):
                if(targetTemp-num in self.hash):
                    print self.hash[targetTemp-num], temp
                temp.append(num)
                targetTemp = targetTemp-num
                
    def combinationSum(self, candidates, target):
        self.putInHash(candidates, target)
        self.logic(candidates, target)
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
class Solution3(object):

    def logic(self, candidates, target, output, finalResult):
        if(sum(output) > target):
            return
        if(sum(output) == target):
            finalResult.append(output)
            return
        for num in candidates:
            if(sum(output)+num <= target):
                #notice output+[num] thats for appending to the list on the fly so we dont need
                #extra line for backtracking
                self.logic(candidates, target, output+[num], finalResult)
    
    def combinationSum(self, candidates, target):
        #notice finalResult ? we do that so we dont need global variable to store output
        finalResult = []
        self.logic(candidates, target, [], finalResult)
        print finalResult

#Main
obj = Solution3()
obj.combinationSum([2,3,5], 8)

obj = Solution3()
#obj.combinationSum([2,3,6,7], 7)

obj = Solution3()
#obj.combinationSum([7,3,2], 18)
