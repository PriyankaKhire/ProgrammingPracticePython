#Given numbers from 1 to 9
#generate string such that either addition or subctraction of the numbers should fetch you
# the total of 100
#example 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
class Approch1(object):
    def __init__(self):
        self.digits = [1,2,3,0]
        self.operations = ['add', 'sub', 'nothing']

    def logic(self, index, number, array, s):
        if(index == len(self.digits)-1):
            print array, s
            return
        #for every index we have 3 operations
        for operation in self.operations:
            if(operation == "add"):
                array.append(number)
                self.logic(index+1, self.digits[index+1], array, s+number)
                array.pop()
            elif(operation == "sub"):
                array.append(-number)
                self.logic(index+1, self.digits[index+1], array, s-number)
                array.pop()
            else:
                if array:
                    top = array.pop()
                    array.append((top*10)+number)
                    self.logic(index+1, self.digits[index+1], array, s+((top*10)+number))
                    array.pop()
                    array.append(-((top*10)+number))
                    self.logic(index+1, self.digits[index+1], array, s-((top*10)+number))
                    array.pop()
                
                    
    def solution(self):
        self.logic(0, self.digits[0], [], 0)

#Main
o = Approch1()
o.solution()
