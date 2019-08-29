from Tkinter import *

class Draw(object):
    def __init__(self, w, h):
        self.canvas = Canvas(width=w, height=h, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.w = w
        self.h = h

    def getOtherCorners(self, upperLeft, bottomRight):
        bottomLeft = [upperLeft[0], bottomRight[1]]
        upperRight = [bottomRight[0], upperLeft[1]]
        return bottomLeft, upperRight

    def getUpperMid(self, upperLeft, upperRight):
        return self.midPoint(upperLeft, upperRight)

    def getBottomMid(self, bottomLeft, bottomRight):
        return self.midPoint(bottomLeft, bottomRight)

    def getLeftMid(self, upperLeft, bottomLeft):
        return self.midPoint(upperLeft, bottomLeft)

    def getRightMid(self, upperRight, bottomRight):
        return self.midPoint(upperRight, bottomRight)

    def getCenterPoint(self, upperLeft, bottomRight):
        return self.midPoint(upperLeft, bottomRight)

    def bottomCurve(self, upperLeft, bottomRight):
        bottomLeft, upperRight = self.getOtherCorners(upperLeft, bottomRight)
        # left vertical line
        lmx, lmy = self.getLeftMid(upperLeft, bottomLeft)
        bmx, bmy = self.getBottomMid(bottomLeft, bottomRight)
        cx, cy = self.getCenterPoint(upperLeft, bottomRight)
        x1, y1 = self.midPoint([lmx, lmy], [bmx, bmy])
        x2, y2 = self.midPoint([cx, cy], upperLeft)        
        self.canvas.create_line(x1, y1,  x2, y2, fill='red')
        # bottom horizontal line
        x3, y3 = self.midPoint([cx, cy], bottomRight)
        self.canvas.create_line(x1, y1,  x3, y3, fill='red')
        # right vertical line
        umx, umy = self.getUpperMid(upperLeft, upperRight)
        rmx, rmy = self.getRightMid(upperRight, bottomRight)
        x4, y4 = self.midPoint([umx, umy], [rmx, rmy])
        self.canvas.create_line(x3, y3, x4, y4, fill='red')

    def topCurve(self, upperLeft, bottomRight):
        bottomLeft, upperRight = self.getOtherCorners(upperLeft, bottomRight)
        # left vertical line
        lmx, lmy = self.getLeftMid(upperLeft, bottomLeft)
        bmx, bmy = self.getBottomMid(bottomLeft, bottomRight)
        cx, cy = self.getCenterPoint(upperLeft, bottomRight)
        x1, y1 = self.midPoint([lmx, lmy], [bmx, bmy])
        x2, y2 = self.midPoint([cx, cy], upperLeft)        
        self.canvas.create_line(x1, y1,  x2, y2, fill='red')
        # top horizontal line
        umx, umy = self.getUpperMid(upperLeft, upperRight)
        rmx, rmy = self.getRightMid(upperRight, bottomRight)
        x3, y3 = self.midPoint([umx, umy], [rmx, rmy])
        self.canvas.create_line(x2, y2, x3, y3, fill='red')
        # right vertical line
        x4, y4 = self.midPoint(bottomRight, [cx, cy])
        self.canvas.create_line(x3, y3, x4, y4, fill='red')

    # --
    #    |
    # --
    def rightCurve(self, upperLeft, bottomRight):
        # we are given a 2X2 grid
        bottomLeft, upperRight = self.getOtherCorners(upperLeft, bottomRight)
        # bottom horizontal line
        lmx, lmy = self.getLeftMid(upperLeft, bottomLeft)
        bmx, bmy = self.getBottomMid(bottomLeft, bottomRight)
        cx, cy = self.getCenterPoint(upperLeft, bottomRight)
        x1, y1 = self.midPoint([lmx, lmy], [bmx, bmy])
        x2, y2 = self.midPoint([cx, cy], bottomRight)
        self.canvas.create_line(x1, y1,  x2, y2, fill='red')
        # vertical line
        umx, umy = self.getUpperMid(upperLeft, upperRight)
        rmx, rmy = self.getRightMid(upperRight, bottomRight)
        x3, y3 = self.midPoint([umx, umy], [rmx, rmy])
        self.canvas.create_line(x2, y2, x3, y3, fill='red')
        # top horizontal line
        x4, y4 = self.midPoint(upperLeft, [cx, cy])
        self.canvas.create_line(x3, y3, x4, y4, fill='red')

    
    #  --
    # |
    #  --
    def leftCurve(self, upperLeft, bottomRight):
        # we are given a 2X2 grid
        bottomLeft, upperRight = self.getOtherCorners(upperLeft, bottomRight)
        # bottom horizontal line
        lmx, lmy = self.getLeftMid(upperLeft, bottomLeft)
        bmx, bmy = self.getBottomMid(bottomLeft, bottomRight)
        cx, cy = self.getCenterPoint(upperLeft, bottomRight)
        x1, y1 = self.midPoint([lmx, lmy], [bmx, bmy])
        x2, y2 = self.midPoint([cx, cy], bottomRight)
        self.canvas.create_line(x1, y1,  x2, y2, fill='red')
        # vertical line
        umx, umy = self.getUpperMid(upperLeft, upperRight)
        lmx, lmy = self.getLeftMid(upperLeft, bottomLeft)
        x3, y3 = self.midPoint([umx, umy], [lmx, lmy])
        self.canvas.create_line(x1, y1, x3, y3, fill='red')
        # top horizontal line
        rmx, rmy = self.getRightMid(upperRight, bottomRight)
        x4, y4 = self.midPoint([umx, umy], [rmx, rmy])
        self.canvas.create_line(x3, y3, x4, y4, fill='red')
        
    def midPoint(self, p1, p2):
        return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2

    def drawCurve(self, iteration, upperLeft, bottomRight, whatSide):
        if(iteration == 1):
            self.bottomCurve(upperLeft, bottomRight)
            return
        bottomLeft, upperRight = self.getOtherCorners(upperLeft, bottomRight)
        w0, h0 = self.getUpperMid(upperLeft, upperRight)
        w1, h1 = self.getBottomMid(bottomLeft, bottomRight)
        w2, h2 = self.getLeftMid(upperLeft, bottomLeft)
        w3, h3 = self.getRightMid(upperRight, bottomRight)
        w4, h4 = self.getCenterPoint(upperLeft, bottomRight)
        # top left
        self.drawCurve(iteration-1, upperLeft, [w4, h4], 'topLeft')
        # bottom left
        self.drawCurve(iteration-1, [w2, h2], [w1, h1], 'bottomLeft')
        # top right
        self.drawCurve(iteration-1, [w0, h0], [w3, h3], 'topRight')
        # bottom right
        self.drawCurve(iteration-1, [w4, h4], bottomRight, 'bottomRight')

    def drawGrid(self, iteration, upperLeft, bottomRight):
        if(iteration == 0):
            return
        bottomLeft, upperRight = self.getOtherCorners(upperLeft, bottomRight)
        #mid points for vertica line
        w0, h0 = self.getUpperMid(upperLeft, upperRight)
        w1, h1 = self.getBottomMid(bottomLeft, bottomRight)
        self.canvas.create_line(w0, h0, w1, h1, fill='gray')
        #mid point for horizontal line
        w2, h2 = self.getLeftMid(upperLeft, bottomLeft)
        w3, h3 = self.getRightMid(upperRight, bottomRight)
        self.canvas.create_line(w2, h2, w3, h3, fill='gray')
        # center point
        w4, h4 = self.getCenterPoint(upperLeft, bottomRight)
        # we just need to know that every iteraiton divides the plane into 4 equal parts
        # the plane is made of upperLeft points and bottomRight points                
        # top left
        self.drawGrid(iteration-1, upperLeft, [w4, h4])
        # bottom left
        self.drawGrid(iteration-1, [w2, h2], [w1, h1])
        # top right
        self.drawGrid(iteration-1, [w0, h0], [w3, h3])
        # bottom right
        self.drawGrid(iteration-1, [w4, h4], bottomRight)

    def run(self, iterations):
        self.drawGrid(iterations, [0, 0], [self.w, self.h])
        self.drawCurve(iterations, [0, 0], [self.w, self.h], '')
        mainloop()

# Main
obj = Draw(350, 350)
obj.run(4)
