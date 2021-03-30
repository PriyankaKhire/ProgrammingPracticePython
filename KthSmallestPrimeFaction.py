# K-th Smallest Prime Fraction
# https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Fraction(object):
    def __init__(self, val, numerator, denominator):
        self.val = val
        self.numerator = numerator
        self.denominator = denominator
        
class Solution(object):
    def getAllFractions(self, array):
        fractions = []
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                # create Fraction object
                obj = Fraction(array[i]/float(array[j]), array[i], array[j])
                fractions.append(obj)
        # sort the objects based on their val
        fractions.sort(key=lambda x: x.val)
        return fractions
        
        
    def kthSmallestPrimeFraction(self, arr, k):
        if k == 0:
            return []
        fractions = self.getAllFractions(arr)
        return [fractions[k-1].numerator, fractions[k-1].denominator]
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        
