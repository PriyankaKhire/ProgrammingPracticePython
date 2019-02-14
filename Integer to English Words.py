#Integer to English Words
#https://leetcode.com/problems/integer-to-english-words/description/

class Approch1(object):
    def __init__(self, integer):
        self. integer = integer
        self.queue = []
        self.ones = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
        self.teen = {'11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen','16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}
        self.tens = {'1': 'Ten', '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
        self.hundred = "Hundred"
        self.thousand = "Thousand"
        self.million = "Million"
        self.billion = "Billion"

    def enqueue(self):
        while self.integer:
            number = self.integer%10
            self.integer = self.integer/10
            self.queue.append(str(number))

    def switch(self, count, number):
        case = { 1: self.ones[number],
                 2: self.tens[number],
                 3: self.ones[number] + self.hundred,
                 4: self.ones[number] + self.thousand,
                 5: self.tens[number],
                 6: self.ones[number] + self.hundred,
                 7: self.ones[number] + self.million,
                 8: self.tens[number],
                 9: self.ones[number] + self.hundred,
                 10: self.ones[number] + self.billion,
                 11: self.tens[number],
                 12: self.ones[number] + self.hundred}
        return case[count]

    def count(self):
        placeCount = 0
        string = ""
        while self.queue:
            placeCount = placeCount + 1
            digit = self.queue.pop(0)
            # we need to check if top of queue is 1 if so then the combined digit falls in teens
            if(self.queue and self.queue[0] == "1" and (placeCount == 1 or placeCount == 4 or placeCount == 7 or placeCount == 10)):
                #We got a teen
                digit = self.queue.pop(0)+digit
                filler = ""
                if(placeCount == 4):
                    filler = self.thousand
                elif(placeCount == 7):
                    filler = self.million
                elif(placeCount == 10):
                    filler = self.billion
                string = self.teen[digit]+filler+string
                continue
            string = self.switch(placeCount, digit) + string
        print string
            

    def solution(self):
        self.enqueue()
        self.count()

class Approch2(object):
    def __init__(self, number):
        self.number = number
        self.output = ""
        self.ones = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        self.tens = {1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
        self.teens = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
        self.hundred = " Hundred"
        self.thousand = " Thousand"
        self.million = " Million"
        self.billion = " Billion"

    def switch(self, number, place):
        case = {
            0: self.ones[number],
            1: self.tens[number],
            2: self.ones[number]+self.hundred,
            3: self.ones[number]+self.thousand,
            4: self.tens[number],
            5: self.ones[number]+self.hundred,
            6: self.ones[number]+self.million,
            7: self.tens[number],
            8: self.ones[number]+self.hundred,
            9: self.ones[number]+self.billion
            }
        return case[place]
        
    def recurrse(self, number, place, output):
        if(number == 0):
            print output
            return
        remainder = number%10
        number = number/10
        if(number > 0 and (place == 0 or place ==3 or place == 6) and number%10 == 1):
            #we got a teen
            self.recurrse(number/10, place+2, self.teens[((number%10)*10)+remainder]+" "+output)
        else:
            output = self.switch(remainder, place)+" "+output
            self.recurrse(number, place+1, output)
                
    def logic(self):
        self.recurrse(self.number, 0, "")
        
        

#Main
#o = Approch1(1234567891)
#o.solution()

obj1 = Approch2(1234567891)
obj1.logic()
