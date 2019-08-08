#Salary Adjustment
#https://leetcode.com/discuss/interview-question/351313/Google-or-Phone-Screen-or-Salary-Adjustment
'''
Give an array of salaries.
The total salary has a budget.
At the beginning, the total salary of employees is larger than the budget.
It is required to find the number k, and reduce all the salaries larger than k to k,
such that the total salary is exactly equal to the budget.

Example 1:

Input: salaries = [100, 300, 200, 400], budget = 800
Output: 250
Explanation: k should be 250, so the total salary after the reduction 100 + 250 + 200 + 250 is exactly equal to 800.
You can assume that solution always exists.
'''
class Solution(object):
    
    def setSalaries(self, salaries, k):
        newSalaries = []
        for salary in salaries:
            newSalaries.append(min(k, salary))
        return newSalaries

    def binarySearch(self, salaries, budget, low, high):
        if(low > high):
            return
        mid = (low+high)/2
        newSalaries = self.setSalaries(salaries, mid)
        if(sum(newSalaries) == budget):
            return mid
        if(sum(newSalaries) > budget):
            return self.binarySearch(salaries, budget, low, mid-1)
        else:
            return self.binarySearch(salaries, budget, mid+1, high)
        
    def getK(self, salaries, budget):
        # The problem states that 'find the number k, and reduce all the salaries larger than k to k'
        # so k cannot go higher than the largest number in the salaries array.
        for k in range(1, max(salaries)+1):
            newSalaries = self.setSalaries(salaries, k)
            if(sum(newSalaries) <= budget):
                print newSalaries, sum(newSalaries)
            else:
                print "Salaries out of budget", newSalaries, sum(newSalaries)
        # from this we can conclude that there is a low of 1 and high of max(salaries)
        # from the above output we can say we can use binary search in this problem instead of doing it the above way
        print "the best k is "
        print self.binarySearch(salaries, budget, 0, max(salaries))

# Main
salaries = [100, 300, 200, 400]
budget = 800
obj = Solution()
obj.getK(salaries, budget)
