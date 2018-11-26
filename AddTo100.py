#Given numbers from 1 to 9
#generate string such that either addition or subctraction of the numbers should fetch you
# the total of 100
#example 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
class Approch1(object):
    def __init__(self):
        self.digits = [1,2,3,4,5,6,7,8,9]

    def logic2(self, index, output, s):
        if(index == len(self.digits)):
            if(s==100):
                print output, s
            return
        #add
        output.append(self.digits[index])
        self.logic2(index+1, output, s+self.digits[index])
        output.pop()
        #subctract
        output.append(-self.digits[index])
        self.logic2(index+1, output, s-self.digits[index])
        output.pop()
        #multiply
        if(output):
            top = output.pop()
            #*********************************************
            #this is where I went wrong in previous approches  #*
            n = 0                                                                       #*
            if(top > 0):                                                              #*
                n = (top*10)+self.digits[index]                            #*
            else:                                                                      #*
                n = (top*10)-self.digits[index]                           #*
            #*********************************************
            output.append(n)                                                
            self.logic2(index+1, output, (s-top)+n)
            #output.pop() <- add this line back and see how it changes in memory, and thats why I went wrong previously too. because I put this in for loop
            #lesson learnt, dont use for loop when you have less instances and when its not actually required.    
                    
    def solution(self):
        self.logic2(0, [], 0)

#Main
o = Approch1()
o.solution()
