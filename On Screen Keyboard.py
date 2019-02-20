#Given an on-screen key board such that there are letters A-Z placed in the following order
# A B C D E F G
# H I J K L M N
# O P Q R S T U
# V W X Y Z
#Now to type a word there is a highlight box that starts always at letter A
# you can move that box with the help of arrow keys up, down, left, right
#and once you highlight the letter you want to type you press enter.
# Now given a word you need to come up with up down left right sequence on the key board to type that word
# for example if the word is AOZ then the sequence would be
# Enter, Down, Down, Enter, Down, Right, Right, Right, Right, Enter
#so the first enter is coz you are already at A
#then you move from A to O by pressing down key twice and enter to enter the letter O
# then you move down and 3 x right to get to key Z and press enter to enter it.
class Approch1(object):
    def __init__(self, word):
        self.word = word

    def findPos(self, letter):
        #get ASCII
        ascii = ord(letter)-ord('a')
        #get row
        row = 0
        # if between 0-6 row 0
        if(ascii >= 0 and ascii <= 6):
            row = 0
        if(ascii >=7 and ascii <=13):
            row = 1
        if(ascii >= 14 and ascii <= 20):
            row = 2
        if(ascii >= 21 and ascii <= 25):
            row = 3
        #find col
        col = ascii%7
        return [row, col]

    def moveRow(self, prevRow, row):
        #if difference is -ve then move down else move up
        diff = prevRow - row
        if(diff > 0):
            #Move up
            return abs(diff) * " Up"
        return abs(diff) * " Down"

    def moveCol(self, prevCol, col):
        #if difference is -ve then move right else move left
        diff = prevCol - col
        if (diff > 0):
            return abs(diff) * " Left"
        return abs(diff) * " Right"
            

    def logic(self):
        prevPos = [0,0]
        output = ""
        for letter in self.word:
            pos = self.findPos(letter.lower())
            #if previous pos == currPos
            if(prevPos == pos):
                output = output + 'Enter'
                continue
            #tackle the row first
            #if either of the rows are 4th row we wanna avoid the 2 end spaces
            if(prevPos[0] == 4):
                output = output + self.moveRow(prevPos[0] , pos[0]) + self.moveCol(prevPos[1], pos[1]) + ' Enter'
            else:
                output = output + self.moveCol(prevPos[1], pos[1]) + self.moveRow(prevPos[0] , pos[0]) + ' Enter'
            prevPos = pos
        print output
            

#Main
obj1 = Approch1("AOZ")
obj1.logic()
