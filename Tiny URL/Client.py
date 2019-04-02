#Tiny URL Client
import sys
sys.path.append("..")
from ColorText import ColorText
import random

class Client(object):
    def __init__(self):
        self.id = random.randint(1, 300)
        self.longURL = None

    def displayPage(self):
        ct = ColorText()
        ct.display(4*"\t"+"Tiny URL", "red-highlight")

    def run(self):
        self.displayPage()
        self.longURL = raw_input("Enter a long URL to make tiny:\n")
        
