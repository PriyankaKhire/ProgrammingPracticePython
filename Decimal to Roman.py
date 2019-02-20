#Decimal to Roman
class Approch1(object):
    def __init__(self, num):
        self.num = num
        self.roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

    def constructNumber(self, num, place):
        if(num in self.roman):
            return self.roman[num*(10**place)]
        if(num == 4 or num == 9):
            return self.roman[1*(10**place)] + self.roman[(num+1)*(10**place)]
        if(num < 4):
            return self.roman[1*(10**place)]*num
        if(num < 9):
            return self.roman[5*(10**place)]+(self.roman[1*(10**place)]*(num - 5))
        

    def logic(self):
        if(self.num > 3999):
            return "not compatible"
        n = self.num
        place = 0
        output = ""
        while n > 0:
            remainder = n%10
            n = n/10
            if(remainder == 0):
                place = place+1
                continue
            output = self.constructNumber(remainder, place) + output
            place = place+1
        print output

#Main
obj1 = Approch1(1804)
obj1.logic()

obj2 = Approch1(1890)
obj2.logic()

obj3 = Approch1(1994)
obj3.logic()
