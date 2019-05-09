#Tiny URL
from Server import Server
from ColorText import ColorText
class Program(object):

    def logic(self):
        ColorText.display("Tiny URL", "orange")
        longURL = raw_input("Enter a long URL to make tiny:\n")
        server = Server(longURL)
        
#Main
obj = Program()
obj.logic()
