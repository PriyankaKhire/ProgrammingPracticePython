#Given numbers from 1 to 9
#generate string such that either addition or subctraction of the numbers should fetch you
# the total of 100
#example 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
class Approch1(object):
    def __init__(self):
        self.digits = [1,2,3,4,5,6,7,8,9,0]
        self.operations = ['add', 'sub', 'nothing']

    def logic(self, index, number, string, s):
        if( index >= len(self.digits)-1):
            if (s == 10):
                print string, number, s
            return
        for operation in self.operations:
            if(operation == 'add'):
                self.logic(index+1, self.digits[index+1], string+"+"+str(number), s+self.digits[index])
            elif(operation == 'sub'):
                self.logic(index+1, self.digits[index+1], string+"-"+str(number), s-self.digits[index])
            elif(operation == 'nothing'):
                self.logic(index+2, (number*10)+self.digits[index+1], string, s)
                
    def solution(self):
        self.logic(0,1,"",0)

#Main
o = Approch1()
o.solution()
