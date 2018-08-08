#Roman to Integer
#https://leetcode.com/problems/roman-to-integer/description/

class Approch1(object):
    def __init__(self):
        self.q = []
        self.roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    def enqueue(self, s):
        for letter in s:
            self.q.append(letter)

    def convert(self):
        num = 0
        while self.q:
            curr = self.q.pop(0)
            if (self.q and self.roman[self.q[0]] > self.roman[curr]):
                num = num + (self.roman[self.q[0]] - self.roman[curr])
                self.q.pop(0)
            else:
                num = num + self.roman[curr]
        return num

    def romanToInt(self, s):
        self.enqueue(s)
        print self.convert()
        """
        :type s: str
        :rtype: int
        """
#Main Program
o = Approch1()
o.romanToInt("MCMXCIV")
