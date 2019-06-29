from Tkinter import *
import math
import os, os.path
class Draw(object):
    def __init__(self, canvasWidth, canvasHeight):
        self.canvas = Canvas(width=canvasWidth, height=canvasHeight, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

    def drawCircle(self, x, y, radius):
        x0 = x - radius
        y0 = y - radius
        x1 = x + radius
        y1 = y + radius
        self.canvas.create_oval(x0, y0, x1, y1, width=2, fill='white')

    def findPosBasedOnAngle(self, x, y, radius, angle):
        x3 = (x + (radius * math.cos(math.radians(-angle))  ))
        y3 = (y + (radius * math.sin(math.radians(-angle))   ))
        self.drawOnCircumference(x3, y3, 'yellow', str(angle))

    def drawOnCircumference(self, x1, y1, color, string):
        self.canvas.create_oval(x1-10, y1-10, x1+10, y1+10, width=2, fill=color)
        self.canvas.create_text(x1, y1, text=string)

    def run(self):
        mainloop()

#Main
h = 350
w = 350
obj = Draw(w, h)
obj.drawCircle(w/2, h/2, 100)
obj.findPosBasedOnAngle(w/2, h/2, 100, 180)
obj.run()
