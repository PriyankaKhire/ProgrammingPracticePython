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

    def decode(self, morse):
        

#Main
o = MorseCode()
o.encode("geeksforgeeks")
