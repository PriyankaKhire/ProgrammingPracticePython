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


#Main
o = Approch1(1234567891)
o.solution()

