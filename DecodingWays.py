#Decode ways
#https://leetcode.com/problems/decode-ways/description/
class Approch1(object):
    def __init__(self, s):
        self.dict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z' }
        self.output = []
        self.s = s

    def isValid(self, string):
        #Convert string to int
        converted_number = int(string)
        if converted_number == 0:
            print "Error zero encountered"
            exit()
        #Check if its in range of 1 to 26
        if(converted_number > 0 and converted_number <=26):
            return True
        return False
        
    def decode(self, s, index, way):
        print "---"
        print "index is "+str(index)
        if(index == len(s)):
            self.output.append(way)
            print self.output
            return
        #Now there are 2 things you can do here
        #1. use the number at index as is
        #2.add 1 to index and if the 2 digit number is valid then use that
        print "the way string so far is "+way
        if(self.isValid(s[index])):
            print str(s[index])+" is valid "
            print "way = "+str(way+self.dict[int(s[index])])
            #convert it to string and add it to ways
            self.decode(s, index+1, way+self.dict[int(s[index])])
            print "way = "+way
        if(index+1 < len(s) and self.isValid(s[index]+s[index+1])):
            print str(s[index]+s[index+1])+" is valid "
            print "way = "+str(way+self.dict[int(s[index]+s[index+1])])
            self.decode(s, index+2, way+self.dict[int(s[index]+s[index+1])])
            print "way = "+way

    def numWays(self):
        self.decode(self.s, 0, "")
        print "number of ways "+str(len(self.output))

class Approch2(object):
    def __init__(self):
        self.dict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z' }
        self.ways = 0
        
    def isValid(self, number):
        if(int(number) in self.dict):
            return True
        return False

    def decode(self, number, output, index):
        if(index == len(number)):
            print output
            self.ways = self.ways+1
            return
        if(self.isValid(number[index])):
            self.decode(number, output+self.dict[int(number[index])], index+1)
        if(index < len(number)-1 and self.isValid(number[index]+number[index+1])):
           self.decode(number, output+self.dict[int(number[index]+number[index+1])], index+2)
    
    def numDecodings(self, s):
        self.decode(s, "", 0)
        print "Number of ways ", self.ways

class Approch3(object):
    def __init__(self, number):
        self.number = number

    def recurrse(self, number, output, index):
        if(index == len(number)):
            print output
            return
        #1) add single digit indivudially
        output.append(number[index])
        self.recurrse(number, output, index+1)
        output.pop()
        #2) club 2 digits together if they are less than 27
        if(index+1 < len(number) and int(number[index]+number[index+1]) < 27):
            output.append(number[index]+number[index+1])
            self.recurrse(number, output, index+2)
            output.pop()
            
    def logic(self):
        self.recurrse(self.number, [], 0)

#Main Program
print " Approch 1"
o1 = Approch1("1234")
o1.numWays()
print "\n Approch 2"
o2 = Approch2()
o2.numDecodings("1234")
print "\n Approch 3"
o3 = Approch3("1234")
o3.logic()
           
