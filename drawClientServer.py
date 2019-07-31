from Tkinter import *

class Server(object):
    def __init__(self, width, height):
        self.x1 = (width/2 + width/16)
        self.y1 = (height/2 + height/2.1)
        self.x2 = (width/2 - width/16)
        self.y2 = (height/2 - height/2.1)
        self.textX1 = width/2
        self.textY1 = height/2

class Client(object):
    def __init__(self, width, height):
        self.x1 = (3*width/12)
        self.y1 = (3*height/12)
        self.x2 = (width/12)
        self.y2 = (height/12)
        self.textX1 = None
        self.textY1 = None
        self.arrowX1 = None
        self.arrowY1 = None
        self.arrowX2 = None
        self.arrowY2 = None

    def calculateTextCoordinates(self):
        self.textX1 = (self.x1+self.x2)/2
        self.textY1 = (self.y1+self.y2)/2

    def assignArrowCoordinates(self, x1, y1, x2, y2):
        self.arrowX1 = x1
        self.arrowY1 = y1
        self.arrowX2 = x2
        self.arrowY2 = y2

class Draw(object):
    def __init__(self, canvasWidth, canvasHeight):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=canvasWidth, height=canvasHeight, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.width = canvasWidth
        self.height = canvasHeight
        self.client1 = None
        self.client2 = None
        self.server = None

    def drawServer(self):
        #I want the server to be in the middle
        s = Server(self.width, self.height)
        self.canvas.create_rectangle(s.x1, s.y1, s.x2, s.y2, fill="#4E9BE9", outline="#5D6A76")
        self.canvas.create_text(s.textX1, s.textY1, text="Server", font="Times 10 italic bold")
        self.server = s

    def drawClient(self, c, name):
        self.canvas.create_rectangle(c.x1, c.y1, c.x2, c.y2, fill="#FC8F22", outline="#89633E")
        self.canvas.create_text(c.textX1, c.textY1, text=name, font="Times 10 italic bold")

    def addClientVertically(self, y, name):
        c = Client(self.width, self.height)
        c.y1 = c.y1 + y
        c.y2 = c.y2 + y
        c.calculateTextCoordinates()
        self.drawClient(c, name)
        return c

    def drawArrowFromServer(self, x1, y1, x2, y2, string, color):
        self.canvas.create_line(x1, y1, x2, y2, arrow=FIRST, fill=color)
        self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=string, font="Times 10 italic bold")

    def drawArrowFromClient(self, x1, y1, x2, y2, string, color):
        self.canvas.create_line(x1, y1, x2, y2, arrow=LAST, fill=color)
        self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=string, font="Times 10 italic bold")

    def drawClient1(self):
        self.client1 = self.addClientVertically(0, "Client 1")
        self.client1.assignArrowCoordinates(self.client1.x1, self.client1.y2, self.server.x2, self.server.y2+20)
        #Ack
        self.drawArrowFromClient(self.client1.arrowX1, self.client1.arrowY1, self.client1.arrowX2, self.client1.arrowY2, "Message", "red")
        self.drawArrowFromServer(self.client1.arrowX1, self.client1.arrowY1+30, self.client1.arrowX2, self.client1.arrowY2+30, "Ack", "green")
        self.drawArrowFromServer(self.client1.arrowX1, self.client1.arrowY1+60, self.client1.arrowX2, self.client1.arrowY2+60, "Delivered", "blue")

    def drawClient2(self):
        self.client2 = self.addClientVertically(8*self.height/12, "Client 2")
        self.client2.assignArrowCoordinates(self.client2.x1, self.client2.y1, self.server.x2, self.server.y1-20)
        self.drawArrowFromClient(self.client2.arrowX1, self.client2.arrowY1, self.client2.arrowX2, self.client2.arrowY2, "Message", "red")
        self.drawArrowFromServer(self.client2.arrowX1, self.client2.arrowY1-30, self.client2.arrowX2, self.client2.arrowY2-30, "Ack", "green")
        self.drawArrowFromServer(self.client2.arrowX1, self.client2.arrowY1-60, self.client2.arrowX2, self.client2.arrowY2-60, "Delivered", "blue")


    def run(self):
        self.root.mainloop()

#Main
d = Draw(500, 500)
d.drawServer()
d.drawClient1()
d.drawClient2()
d.run()
