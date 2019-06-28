from Tkinter import *
import math

class Draw(object):
    def __init__(self):
        self.canvas = Canvas(width=350, height=350, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

    def drawCircleWithRadiusAndCenterPoint(self, x, y, radius):
        x0 = x - radius
        y0 = y - radius
        x1 = x + radius
        y1 = y + radius
        self.canvas.create_oval(x0, y0, x1, y1, width=2, fill='white')

    def drawOnCircumference2(self, x, y, radius, angle):
        x1 = (radius*math.cos(angle)) + x
        y1 = (radius*math.sin(angle)) + y
        self.canvas.create_oval(x1-10, y1-10, x1+10, y1+10, width=2, fill='red')
        self.canvas.create_text(x1, y1, text=angle)

    def drawOnCircumference(self, x, y, radius, angle):
        #parametric equation for a circle
        x1 = (x + (radius * math.cos(angle)))
        y1 = (y + (radius * math.sin(angle)))
        self.canvas.create_oval(x1-10, y1-10, x1+10, y1+10, width=2, fill='yellow')
        self.canvas.create_text(x1, y1, text=angle)

    def drawCircle(self, x1, y1, x2, y2):
        #the 4 points are
        #x1, y1 <- top left corner
        #x2, y1 <- top right corner
        #x1, y2 <- bottom left corner
        #x2, y2 <- bottom right corner
        self.canvas.create_oval(x1, y1, x2, y2, width=2, fill='white')

    def originOfCircle(self, x1, y1, x2, y2):
        x = (x1+x2)/2
        y = (y1+y2)/2
        self.canvas.create_oval(x-5, y-5, x+5, y+5, width=3, fill='blue')


    def drawOn4CornersOfCircle(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1, y1, x1+3, y1+3, width=3, fill='yellow')
        self.canvas.create_oval(x2, y1, x2+3, y1+3, width=3, fill='yellow')
        self.canvas.create_oval(x1, y2, x1+3, y2+3, width=3, fill='yellow')
        self.canvas.create_oval(x2, y2, x2+3, y2+3, width=3, fill='yellow')

    def drawOn4CircumferencePointsOfCircle(self, x1, y1, x2, y2):
        #top = (x1+x2)/2, y1
        #bottom = (x1+x2)/2, y2
        #left = x1, (y1+y2)/2
        #right = x2, (y1+y2)/2
        x3 = (x1+x2)/2
        y3 = (y1+y2)/2
        self.canvas.create_oval(x3-10, y1-10, x3+10, y1+10, width=3, fill='red')
        self.canvas.create_oval(x3-10, y2-10, x3+10, y2+10, width=3, fill='red')
        self.canvas.create_oval(x1-10, y3-10, x1+10, y3+10, width=3, fill='red')
        self.canvas.create_oval(x2-10, y3-10, x2+10, y3+10, width=3, fill='red')
        
        

    def run(self):
        x1 = 15
        y1 = 15
        x2 = 300
        y2 = 300
        #self.drawCircle(x1, y1, x2, y2)
        #self.drawOn4CornersOfCircle(x1, y1, x2, y2)
        #self.drawOn4CircumferencePointsOfCircle(x1, y1, x2, y2)
        #self.originOfCircle(x1, y1, x2, y2)
        self.drawCircleWithRadiusAndCenterPoint(175, 175, 100)
        self.drawOnCircumference(175, 175, 100, 0)
        self.drawOnCircumference(175, 175, 100, 11)
        self.drawOnCircumference(175, 175, 100, 22)
        self.drawOnCircumference(175, 175, 100, 33)    
        mainloop()

#Main
obj = Draw()
obj.run()
