#Color text
import sys
class ColorText(object):
    def __init__(self):
        self.colors = {"orange":"KEYWORD",
                       "green":"STRING",
                       "dark-red":"COMMENT",
                       "black":"SYNC",
                       "purple":"BUILTIN",
                       "brown":"console",
                       "blue":"stdout",
                       "light-red":"stderr",
                       "black-highlight":"hit",
                       "red-highlight":"ERROR",
                       "grey-highlight":"sel"}
    def help(self):
        print "The supported colors are: "
        print "orange"
        print "green"
        print "dark-red"
        print "black"
        print  "purple"
        print  "brown"
        print  "blue"
        print  "black-highlight"
        print   "light-red"
        print   "red-highlight"
        print   "grey-highlight"
        
    def display(self, text, colour):
        try: color = sys.stdout.shell
        except AttributeError: raise RuntimeError("Use IDLE")
        color.write(str(text)+"\n",self.colors[colour.lower()])

