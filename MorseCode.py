#Morse conversion

class MorseCode(object):
    def __init__(self):
        self.alphabet = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        self.morse = {".-":'a',"-...":'b',"-.-.":'c',"-..":'d',".":'e',"..-.":'f',"--.":'g',"....":'h',"..":'i',".---":'j',"-.-":'k',".-..":'l',"--":'m',"-.":'n',"---":'o',".--.":'p',"--.-":'q',".-.":'r',"...":'s',"-":'t',"..-":'u',"...-":'v',".--":'w',"-..-":'x',"-.--":'y',"--..":'z'}
        
    def encode(self, string):
        morse = ""
        for char in string:
            morse = morse+self.alphabet[char]
        print morse

    def decode_logic(self, morse, currIndex, output):
        if currIndex == len(morse):
            print output
            return
        #We add 1 to 4 to index to see if it forms morse character or not
        for i in range(1, 5):
            if(currIndex+i > len(morse)):
                break
            morseCharacter = morse[currIndex:currIndex+i]
            if(morseCharacter in self.morse):
                self.decode_logic(morse, currIndex+i, output + self.morse[morseCharacter])

            
                

                
    def decode(self, morse):
        #The min number of characters used in morse code is 1 and max is 4
        self.decode_logic(morse, 0, "")
        
        

#Main
o = MorseCode()
o.encode("an")
o.decode(".--.")
