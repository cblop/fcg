from pyprocessing import *
from tracker import *
import time

class Face:
    def __init__(self, tpoints):

        self.XSIZE = 24
        self.YSIZE = 24

        self.tpoints = tpoints
        self.headpoints = [self.tpoints[6], self.tpoints[7], self.tpoints[8], self.tpoints[10], self.tpoints[13]]
        self.hairpoints = [self.tpoints[0], self.tpoints[1], self.tpoints[6], self.tpoints[7]]
        self.earpoints = [self.tpoints[6], self.tpoints[7]]
        self.eyepoints = self.earpoints
        self.nosepoint = self.tpoints[9]
        self.mouthPoints = [self.tpoints[11], self.tpoints[12], self.tpoints[8], self.tpoints[10]]
        self.browPoints = [self.tpoints[2], self.tpoints[3], self.tpoints[4], self.tpoints[5]]

        '''
        self.headpoints = [self.tpoints['leye'], self.tpoints['reye'], self.tpoints['lcheek'],
                           self.tpoints['rcheek'], self.tpoints['chin']]
        self.hairpoints = [trackpoints['lfore'], trackpoints['rfore'],
                           self.tpoints['leye'], self.tpoints['reye']]
        self.earpoints = [self.tpoints['leye'], self.tpoints['reye']]
        self.eyepoints = self.earpoints
        self.mouthPoints = [self.tpoints['tlip'], self.tpoints['blip'], self.tpoints['lcheek'], self.tpoints['rcheek']]
        self.browPoints = [self.tpoints['lbrow0'], self.tpoints['lbrow1'],
                           self.tpoints['rbrow0'], self.tpoints['rbrow1']]
        '''

    def update(self, tpoints):
        self.tpoints = tpoints
        self.headpoints = [self.tpoints[6], self.tpoints[7], self.tpoints[8], self.tpoints[10], self.tpoints[13]]
        self.hairpoints = [self.tpoints[0], self.tpoints[1], self.tpoints[6], self.tpoints[7]]
        self.earpoints = [self.tpoints[6], self.tpoints[7]]
        self.eyepoints = self.earpoints
        self.nosepoint = self.tpoints[9]
        self.mouthPoints = [self.tpoints[11], self.tpoints[12], self.tpoints[8], self.tpoints[10]]
        self.browPoints = [self.tpoints[2], self.tpoints[3], self.tpoints[4], self.tpoints[5]]


    def drawAll(self):
        count = 0
        for item in self.tpoints:
            point = (item[0] * self.XSIZE, item[1] * self.YSIZE)
            self.drawCross(point)
        self.drawHead(self.headpoints)
        self.drawHair(self.hairpoints)
        self.drawEars(self.earpoints)
        self.drawNose(self.nosepoint)
        self.drawMouth(self.mouthPoints)
        self.drawEyes(self.eyepoints)
        self.drawPupils(self.eyepoints)
        self.drawEyebrows(self.browPoints)


    def drawPoints(self, points, color):
        """docstring for drawPoints"""
        stroke(color[0], color[1], color[2])
        points = [(x[0] * self.XSIZE, x[1] * self.YSIZE) for x in points]
        for i in range((len(points) - 1)):
          line(points[i][0], points[i][1], points[i+1][0], points[i+1][1])

    def drawCross(self, points):
        """docstring for drawCross"""
        stroke(0,255,0)
        xfactor = self.XSIZE / 4
        yfactor = self.YSIZE / 4
        line(points[0] - xfactor, points[1], points[0] + xfactor, points[1]) 
        line (points[0], points[1] - yfactor, points[0], points[1] + yfactor)

    def drawNose(self, tpoints):
        """draws the nose"""
        #points = [(11,19),(10,20),(11,21),(15,21),(16,20),(15,19)]
        nose = tpoints
        points = [(nose[0] - 2, nose[1] - 1), (nose[0] - 3, nose[1]),
                  (nose[0] - 2, nose[1] + 1), (nose[0] + 2, nose[1] + 1),
                  (nose[0] + 3, nose[1]), (nose[0] + 2, nose[1] - 1)]
        color = (255,255,0)
        self.drawPoints(points, color)

    def drawMouth(self, tpoints):
        """docstring for drawMouth"""
        color = (255,0,0)
        tlip = tpoints[0]
        blip = tpoints[1]
        lcheek = tpoints[2]
        rcheek = tpoints[3]
        # Upper lip first
        #upper = [(9,23),(8,25),(9,24),(17,24),(18,25),(17,23),(9,23)]
        upper = [(tlip[0] - 4, tlip[1]), (lcheek[0] + 1, lcheek[1] + 4),
                 (tlip[0] - 4, tlip[1] + 1), (tlip[0] + 4, tlip[1] + 1),
                 (rcheek[0] - 1, rcheek[1] + 4), (tlip[0] + 4, tlip[1]),
                 (tlip[0] - 4, tlip[1])]
        # Then lower lip
        #lower = [(8,25),(11,28),(15,28),(18,25),(14,27),(12,27),(8,25)]
        lower = [(lcheek[0] + 1, lcheek[1] + 4), (blip[0] - 2, blip[1]),
                 (blip[0] + 2, blip[1]), (rcheek[0] - 1, rcheek[1] + 4),
                 (blip[0] + 1, blip[1] - 1), (blip[0] - 1, blip[1] - 1),
                 (lcheek[0] + 1, lcheek[1] + 4)]
        self.drawPoints(upper, color)
        self.drawPoints(lower, color)

    def drawEyes(self, tpoints):
        """tpoints are leye, reye"""
        color = (255,255,255)
        #lefteye = [(7,12),(6,13),(7,14),(9,14),(10,13),(9,12),(7,12)]
        leye = tpoints[0]
        reye = tpoints[1]
        lefteye = []
        lefteye.extend([(leye[0] + 3, leye[1] - 3), (leye[0] + 2, leye[1] - 2),
                        (leye[0] + 3, leye[1] - 1), (leye[0] + 5, leye[1] - 1),
                        (leye[0] + 6, leye[1] - 2), (leye[0] + 5, leye[1] - 3),
                        (leye[0] + 3, leye[1] - 3)])
        righteye = []
        righteye.extend([(reye[0] - 5, reye[1] - 3), (reye[0] - 6, reye[1] - 2),
                         (reye[0] - 5, reye[1] - 1), (reye[0] - 3, reye[1] - 1),
                         (reye[0] - 3, reye[1] - 1), (reye[0] - 2, reye[1] - 2),
                         (reye[0] - 3, reye[1] - 3), (reye[0] - 5, reye[1] - 3)])
        #righteye = [(17,12),(16,13),(17,14),(19,14),(20,13),(19,12),(17,12)]
        self.drawPoints(lefteye, color)
        self.drawPoints(righteye, color)

    def drawPupils(self, tpoints):
        """tpoints are leye, reye"""
        leye = tpoints[0]
        reye = tpoints[1]
        stroke(150,255,255)
        fill(150,255,255)
        #leftpupil = [8,13]
        leftpupil = [leye[0] + 4, leye[1] - 2]
        leftpupil[0] *= self.XSIZE
        leftpupil[1] *= self.YSIZE
        #rightpupil = [18,13]
        rightpupil = [reye[0] - 4, reye[1] - 2]
        rightpupil[0] *= self.XSIZE
        rightpupil[1] *= self.YSIZE
        ellipse(leftpupil[0],leftpupil[1], self.XSIZE, self.YSIZE)
        ellipse(rightpupil[0],rightpupil[1], self.XSIZE, self.YSIZE)


    def drawHead(self, tpoints):
        """tpoints are leye, reye, lcheek, rcheek, chin"""
        color = (255,0,255)
        #points = [(6,4),(2,7),(2,20),(6,30),(11,32),(15,32),(20,30),(22,25),(23,20),(23,7),(20,4),(6,4)]
        leye = tpoints[0]
        reye = tpoints[1]
        lcheek = tpoints[2]
        rcheek = tpoints[3]
        chin = tpoints [4]

        points = []
        points.extend([(leye[0] - 1, leye[1] - 8),(leye[0] - 1, leye[1] + 5)])
        points.extend([(lcheek[0] - 3, lcheek[1] + 4), (lcheek[0] - 1, lcheek[1] + 9)])
        points.extend([(chin[0] - 2, chin[1] + 1), (chin[0] + 2, chin[1] + 1)])
        points.extend([(rcheek[0] + 1, rcheek[1] + 9), (rcheek[0] +3, rcheek[1] + 4)])
        points.extend([(reye[0] + 1, reye[1] + 5), (reye[0] + 1, reye[1] - 8)])

        self.drawPoints(points, color)

    def drawEars(self, tpoints):
        """tpoints: leye, reye"""
        color = (255,0,255)
        #leftear = [(3,11),(2,11),(1,12),(2,20),(3,20),(3,11)]
        #rightear = [(23,11),(24,11),(25,12),(24,20),(23,20),(23,11)]
        leye = tpoints[0]
        reye = tpoints[1]
        leftear = []
        rightear = []
        leftear.extend([(leye[0] - 1, leye[1] - 4), (leye[0] - 2, leye[1] - 4),
                        (leye[0] -3, leye[1] - 3), (leye[0] - 2, leye[1] + 5),
                        (leye[0] - 1, leye[1] + 5), (leye[0] - 1, leye[1] - 4)])
        rightear.extend([(reye[0] + 1, reye[1] - 4), (reye[0] + 2, reye[1] - 4),
                        (reye[0] + 3, reye[1] - 3), (reye[0] + 2, reye[1] + 5),
                        (reye[0] + 1, reye[1] + 5), (reye[0] + 1, reye[1] - 4)])
        self.drawPoints(leftear, color)
        self.drawPoints(rightear, color)

    def drawHair(self, tpoints):
        """tpoints: lfore, rfore, leye, reye"""
        color = (255,100,0)
        lfore = tpoints[0]
        rfore = tpoints[1]
        leye = tpoints[2]
        reye = tpoints[3]

        #points = [(7,1),(3,3),(3,7),(7,4),(20,4),(23,7),(23,4),(20,1),(7,1)]
        points = []
        points.extend([(lfore[0], lfore[1] - 5), (lfore[0] - 3, lfore[1] -3), (leye[0] - 1, leye[1] - 8), (lfore[0], lfore[1] - 2)])
        points.extend([(rfore[0], rfore[1] - 2), (reye[0] + 1, reye[1] - 8), (rfore[0] + 3, rfore[1] - 2), (rfore[0], rfore[1] - 5), (lfore[0], lfore[1] - 5)])
        self.drawPoints(points, color)

    def drawEyebrows(self, tpoints):
        """docstring for drawEyebrows"""
        color = (150,100,50)
        lbrow0 = tpoints[0]
        lbrow1 = tpoints[1]
        rbrow0 = tpoints[2]
        rbrow1 = tpoints[3]

        #leftbrow = [(6,10),(5,12),(7,11),(11,11),(6,10)]
        #rightbrow = [(15,11),(19,11),(21,12),(20,10),(15,11)]

        leftbrow = [(lbrow0[0], lbrow0[1]), (lbrow0[0] - 1, lbrow0[1] + 2),
                    (lbrow1[0] - 4, lbrow1[1]), (lbrow1[0], lbrow1[1]), (lbrow0[0], lbrow0[1])]
        rightbrow = [(rbrow0[0], rbrow0[1]), (rbrow0[0] + 4, rbrow0[1]),
                     (rbrow1[0] + 1, rbrow1[1] + 2), (rbrow1[0], rbrow1[1]), (rbrow0[0], rbrow0[1])]
        self.drawPoints(leftbrow, color)
        self.drawPoints(rightbrow, color)


def readFile(filename):
    f = open(filename, 'r')
    frames = []
    for line in f:
        temp = eval(line.strip('\n'))
        frames.append(list(temp))

    return frames

def transpose(points):
    #base = points[0]
    base = points
    print base
    ref = [(6.,6.),(20.,6.),(6.,10.),(11.,11.),(15.,11.),(20.,10.),(4.,15.),(22.,15.),
           (7.,21.), (13.,20.), (19.,21.), (13.,23.), (13.,27.), (13.,31.)]
    trans = []
    for i in range(len(base)):
        xamount = base[i][0] / ref[i][0]
        yamount = base[i][1] / ref[i][1]
        trans.append((xamount, yamount))

    for i in range(len(points)):
        for j in range(len(points[i])):
            points[i][j]= (points[i][j][0] / trans[j][0], points[i][j][1] / trans[j][1])

    return points


#points = readFile('points6.txt')
tpoints = runTracking()
#tpoints = transpose(points)
face = Face(tpoints)
index = 0

def setup():
    size(600,800)
    background(0)
    #print points[0]

def refresh():
  #tpoints = transpose(points)
  #print tpoints[0]
  global index
  global face
  tpoints = runTracking()
  print tpoints
  face.update(tpoints)
  face.drawAll()

def draw():
    background(0)
    refresh()

run()
