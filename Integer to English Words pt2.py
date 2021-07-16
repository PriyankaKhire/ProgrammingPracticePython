# Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
class Solution(object):
    def __init__(self):
        self.tensHash = {
            1: 'Ten',
            2: 'Hundred',
            3: 'Thousand',
            6: 'Million',
            9: 'Billion',
            12: 'Trillion',
            15: 'Quadrillion',
            18: 'Quintillion',
            21: 'Sextillion',
            24: 'Septillion',
            27: 'Octillion',
            30: 'Nonillion'
        }
        self.onesHash = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven', 
            8: 'Eight',
            9: 'Nine'
        }
        self.teenHash = {
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        self.endTensHash = {
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }
    
    def twoDigit(self, num):
        # 00
        if (num == 0):
            return 
        # 0 to 9
        if (num in self.onesHash):
            return self.onesHash[num]
        # 10
        if (num == 10):
            return self.tensHash[1]
        # 11 to 19
        if (num in self.teenHash):
            return self.teenHash[num]
        # 20 to 90
        if (num in self.endTensHash):
            return self.endTensHash[num]
        # 21 to 99
        prefix = self.endTensHash[(num/10)*10]
        suffix = self.onesHash[num%10]
        return prefix + " " + suffix
    
    def threeDigit(self, num):
        suffix = self.onesHash[(num/100)]
        suffix = suffix + " " + self.tensHash[2]
        prefix = self.twoDigit(num%100)
        if (prefix == None):
            return suffix
        return suffix + " " + prefix
    
    def divideNumber(self, num, power, answer):
        if(num == 0):
            return
        if (num/10 == 0):
            answer.insert(0, self.onesHash[num])
            return self.divideNumber(num/10, power+1, answer)
        if (num/100 == 0):
            answer.insert(0, self.twoDigit(num))
            return self.divideNumber(num/100, power+1, answer)
        if (num/1000 == 0):
            answer.insert(0, self.threeDigit(num))
            return self.divideNumber(num/1000, power+1, answer)
        # take 3 digits at a time
        suffix = self.tensHash[power+3] + " " + self.threeDigit(num%1000)
        print suffix
        answer.insert(0, suffix)
        return self.divideNumber(num/1000, power+3, answer)
        
    
    def numberToWords(self, num):
        if(num == 0):
            return "Zero"
        stringArray = []
        self.divideNumber(num, 0, stringArray)
        return " ".join(stringArray)
        """
        :type num: int
        :rtype: str
        """
        
