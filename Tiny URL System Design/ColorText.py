#Color Text
import sys
class ColorText(object):
    def __init__(self, text):
        print text
        colors = {"orange":"KEYWORD",
                  "red":"COMMENT",
                  "green":"STRING"}
        
    def display(self, text, color):
        print text
        color.write(text, self.colors[color])

#Main
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
