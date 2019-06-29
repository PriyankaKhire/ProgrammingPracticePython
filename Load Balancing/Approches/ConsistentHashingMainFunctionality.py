#Consistent Hashing Main Functionality
from Tkinter import *
import math
import os, os.path
class Draw(object):
    def __init__(self, canvasWidth, canvasHeight):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=canvasWidth, height=canvasHeight, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)       

    def drawCircle(self, x, y, radius):
        x0 = x - radius
        y0 = y - radius
        x1 = x + radius
        y1 = y + radius
        self.canvas.create_oval(x0, y0, x1, y1, width=2, fill='white')

    def drawOnCircumference(self, x1, y1, color, string):
        self.canvas.create_oval(x1-10, y1-10, x1+10, y1+10, width=2, fill=color)
        self.canvas.create_text(x1, y1, text=string)

    def run(self):
        self.root.mainloop()
    
class MainFunctionality(object):
    def __init__(self):
        self.ringRadius = 100
        self.canvasWidth = 350
        self.canvasHeight = 350
        self.d = Draw(self.canvasWidth, self.canvasHeight)
        self.d.drawCircle(self.canvasWidth/2, self.canvasHeight/2, self.ringRadius)
        self.servers = {}
        self.request = {}
    
    def getNumberOfServers(self):
        return len(os.listdir('../Servers'))

    def hashFunctionToGiveAngle(self, number):
        return number%360

    def positionOnCircumference(self, angle):
        #parametric equation for a circle in clock wise direction
        #if you want in anti clockwise direction then just change angle to negative
        x = self.canvasWidth/2
        y = self.canvasHeight/2
        x1 = (x + (self.ringRadius * math.cos(math.radians(angle))))
        y1 = (y + (self.ringRadius * math.sin(math.radians(angle))))
        return [x1, y1]

    def fillServersHash(self):
        totalServers = self.getNumberOfServers()
        #Clean servers hash, this is to tackle problem of adding new or removing servers.
        #we do this by flushing out old values 
        #self.servers = {}
        #since we are destroying and creating this object every time in Consistant Hashing getServerNumber function
        # we dont need to do this step.
        print "Total number of servers is ",totalServers
        for i in range(totalServers):
            angle = self.hashFunctionToGiveAngle(i)*90
            posOnCircumference = self.positionOnCircumference(angle)
            self.servers[i] = [angle, posOnCircumference]
            self.d.drawOnCircumference(posOnCircumference[0], posOnCircumference[1], '#FF4B63', str(i+1))

    def drawOldRequests(self):
        for key in self.request:
            angle = self.request[key][0]
            posOnCircumference = self.request[key][1]
            self.d.drawOnCircumference(posOnCircumference[0], posOnCircumference[1], '#FFFF54', str(key))

    def fillRequestHash(self, requestId):
        self.drawOldRequests()
        angle = self.hashFunctionToGiveAngle(requestId)
        posOnCircumference = self.positionOnCircumference(angle)
        self.request[requestId] = [angle, posOnCircumference]
        self.d.drawOnCircumference(posOnCircumference[0], posOnCircumference[1], '#57DEFF', str(requestId))

    def findAngleOfArcClockWiseDirecton(self, p1, p2):
        x0 = self.canvasWidth/2
        y0 = self.canvasHeight/2
        theta1 = math.degrees(math.atan2(p1[1]-y0, p1[0]-x0))
        theta2 = math.degrees(math.atan2(p2[1]-y0, p2[0]-x0))
        return theta2-theta1
        
    def selectServerForRequest(self, requestId):
        output = {}
        for server in self.servers:
            angle = self.findAngleOfArcClockWiseDirecton(self.request[requestId][1], self.servers[server][1])
            if(angle > 0):
                output[angle] = server
        return output[min(output, key=output.get)]
    
        
    def logic(self, requestId, request):
        #repopulate the request hash
        self.request = request
        #give each of those servers angle
        self.fillServersHash()
        #put the request on the ring
        self.fillRequestHash(requestId)
        #select the nearest server in clockwise direction
        server = self.selectServerForRequest(requestId)
        print "Server", server+1, " is closest to request in Clockwise direction"
        self.d.run()
        return server, self.request
