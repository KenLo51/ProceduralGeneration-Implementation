import numpy as np
from math import *
import cv2
import typing


# References : 
#   1.https://openhome.cc/Gossip/P5JS/Lsystem.html
#   2.http://paulbourke.net/fractals/lsys/

#    F	         Move forward by line length drawing a line
#    f	         Move forward by line length without drawing a line
#    +	         Turn left by turning angle(ø)
#    -	         Turn right by turning angle(ø)
#    |	         Reverse direction (ie: turn by 180 degrees)
#    [	         Push current drawing state onto stack
#    ]	         Pop current drawing state from the stack
#    #	         Increment the line width by line width increment
#    !	         Decrement the line width by line width increment
#
# Did not implement :
#    @	         Draw a dot with line width radius
#    {	         Open a polygon
#    }	         Close a polygon and fill it with fill colour
#    >	         Multiply the line length by the line length scale factor
#    <	         Divide the line length by the line length scale factor
#    &	         Swap the meaning of + and -
#    (	         Decrement turning angle by turning angle increment
#    )	         Increment turning angle by turning angle increment

Axiom = "F+F+F+F"
Rules = {  "F" : "F+F-F-FF+F+F-F"}
degree = 90
Times = 6

savePath = "Images/LSystem_result_01"

class lsystem():
    def __init__(self, axiom : typing.AnyStr, rules : typing.Dict, rotateDeg, n,
                imgSize=(512, 512), startPos = (256, 256), startOri = (0, -1),
                lineLength = 4, lineWidth = 1, widthIncrement = 1):
        self.n = n
        self.axiom = axiom
        self.rules = rules
        self.TurningDegree = rotateDeg
        self.TurningAngle = self.TurningDegree * pi / 180
        self.board = np.zeros(shape=imgSize, dtype=np.uint8)
        self.currPos = startPos
        self.currOri = startOri
        self.LineLength = lineLength # pixel
        self.LineWidth = lineWidth # pixel
        self.LineWidthIncrement = widthIncrement # pixel

        self.posStack = []
        self.oriStack = []

    def produceOne(self, axiom, n):
        if(n == 0):
            return
        n = n - 1
        while len(axiom)>0:
            command = axiom[0]
            axiom = axiom[1:]

            if(command in self.rules): # use rules
                self.produceOne(self.rules[command], n)

            if(command == "F"): # Move forward drawing
                nextPos = (self.currPos[0]+self.currOri[0]*self.LineLength , self.currPos[1]+self.currOri[1]*self.LineLength)
                cv2.line(self.board, (int(self.currPos[0]), int(self.currPos[1])), (int(nextPos[0]), int(nextPos[1])), (255), self.LineWidth)
                self.currPos = nextPos
            if(command == "f"): # Move forward without drawing
                self.currPos = (self.currPos[0]+self.currOri[0]*self.LineLength , self.currPos[1]+self.currOri[1]*self.LineLength)
            
            if(command == "+"): # Turn left
                self.currOri = ( self.currOri[0]*cos(self.TurningAngle) - self.currOri[1]*sin(self.TurningAngle),
                            self.currOri[0]*sin(self.TurningAngle) + self.currOri[1]*cos(self.TurningAngle))
            if(command == "-"): # Turn right
                self.currOri = ( self.currOri[0]*cos(-self.TurningAngle) - self.currOri[1]*sin(-self.TurningAngle),
                            self.currOri[0]*sin(-self.TurningAngle) + self.currOri[1]*cos(-self.TurningAngle))
            if(command == "|"): # Reverse direction
                self.currOri = ( -self.currOri[0], -self.currOri[1] )

            if(command == "["): # Push current drawing state onto stack
                self.posStack.append(self.currPos)
                self.oriStack.append(self.currOri)
            if(command == "]"): # Pop current drawing state from the stack
                if(len(self.currPos) <= 0 or len(self.currOri) <= 0):
                    raise ValueError
                self.currPos = self.posStack.pop()
                self.currOri = self.oriStack.pop()

            if(command == "#"): # Increment the line width
                self.LineWidth = self.LineWidth + self.LineWidthIncrement
            if(command == "!"): # Decrement the line width
                self.LineWidth = self.LineWidth - self.LineWidthIncrement

    def produceAll(self):
        
        self.produceOne(self.axiom, self.n)

        return self.board

if __name__ == "__main__":

    for i in range(Times):
        board = lsystem(Axiom, Rules, degree, i+1,
            imgSize=(1024, 1024), startPos=(128, 896)).produceAll()

        cv2.imshow("test", board)
        cv2.imwrite(f"{savePath}_{i:02d}.png", board)
        cv2.waitKey(0)
        