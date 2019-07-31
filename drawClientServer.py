from Tkinter import *

class Draw(object):
    def __init__(self, canvasWidth, canvasHeight):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=canvasWidth, height=canvasHeight, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.width = canvasWidth
        self.height = canvasHeight

    def drawServer(self):
        #I want the server to be in the middle
        self.canvas.create_rectangle((self.width/2 + self.width/16), (self.height/2 + self.height/2.1), (self.width/2 - self.width/16), (self.height/2 - self.height/2.1), fill="#4E9BE9", outline="#5D6A76")
        self.canvas.create_text(self.width/2, self.height/2, text="Server", font="Times 10 italic bold")

    def drawClient(self):
        self.canvas.create_rectangle((self.width/8 + self.width/16), (self.height/8 + (self.height/16)), (self.width/8 - self.width/16), (self.height/8 - (self.height/16)), fill="#FC8F22", outline="#89633E")
        self.canvas.create_text(self.width/8, self.height/8, text="Client", font="Times 10 italic bold")

    def drawArrow(self):
        self.canvas.create_line((self.width/8 + self.width/16), (self.height/8 + (self.height/16)), (self.width/2 - self.width/16), (self.height/2 - self.height/2.1), arrow=LAST, fill="green")

    def run(self):
        self.root.mainloop()

#Main
d = Draw(500, 500)
d.drawServer()
d.drawClient()
d.drawArrow()
d.run()
