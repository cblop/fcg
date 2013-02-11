from pyprocessing import *

""" Lots of repeated code here: have a generic draw function """
XSIZE = 24
YSIZE = 24

class feature():
  def __init__(self):
    pass

def setup():
  size(600,800)
  background(0)

def drawPoints(points, color):
    """docstring for drawPoints"""
    stroke(color[0], color[1], color[2])
    points = [(x[0] * XSIZE, x[1] * YSIZE) for x in points]
    for i in range((len(points) - 1)):
      line(points[i][0], points[i][1], points[i+1][0], points[i+1][1])

def drawCross(points):
    """docstring for drawCross"""
    stroke(0,255,0)
    xfactor = XSIZE / 4
    yfactor = YSIZE / 4
    line(points[0] - xfactor, points[1], points[0] + xfactor, points[1]) 
    line (points[0], points[1] - yfactor, points[0], points[1] + yfactor)

def drawNose():
    """docstring for drawNose"""
    points = [(11,19),(10,20),(11,21),(15,21),(16,20),(15,19)]
    color = (255,255,0)
    drawPoints(points, color)

def drawMouth():
    """docstring for drawMouth"""
    color = (255,0,0)
    # Upper lip first
    upper = [(9,23),(8,25),(9,24),(17,24),(18,25),(17,23),(9,23)]
    # Then lower lip
    lower = [(8,25),(11,28),(15,28),(18,25),(14,27),(12,27),(8,25)]
    drawPoints(upper, color)
    drawPoints(lower, color)

def drawEyes():
    """docstring for drawEyes"""
    color = (255,255,255)
    lefteye = [(7,12),(6,13),(7,14),(9,14),(10,13),(9,12),(7,12)]
    righteye = [(17,12),(16,13),(17,14),(19,14),(20,13),(19,12),(17,12)]
    drawPoints(lefteye, color)
    drawPoints(righteye, color)

def drawPupils():
    stroke(150,255,255)
    fill(150,255,255)
    leftpupil = [8,13]
    leftpupil[0] *= XSIZE
    leftpupil[1] *= YSIZE
    rightpupil = [18,13]
    rightpupil[0] *= XSIZE
    rightpupil[1] *= YSIZE
    ellipse(leftpupil[0],leftpupil[1], XSIZE, YSIZE)
    ellipse(rightpupil[0],rightpupil[1], XSIZE, YSIZE)


def drawHead(tpoints):
    """docstring for drawHead"""
    color = (255,0,255)
    points = [(6,4),(2,7),(2,20),(6,30),(11,32),(15,32),(20,30),(22,25),(23,20),(23,7),(20,4),(6,4)]
    drawPoints(points, color)

def drawEars():
    """docstring for drawEars"""
    color = (255,0,255)
    leftear = [(2,11),(1,11),(0,12),(1,20),(2,20),(2,11)]
    rightear = [(23,11),(24,11),(25,12),(24,20),(23,20),(23,11)]
    drawPoints(leftear, color)
    drawPoints(rightear, color)

def drawHair():
    """docstring for drawHair"""
    color = (255,100,0)
    points = [(6,1),(2,3),(2,7),(6,4),(20,4),(23,7),(23,4),(20,1),(6,1)]
    drawPoints(points, color)

def drawEyebrows():
    """docstring for drawEyebrows"""
    color = (150,100,50)
    leftbrow = [(6,10),(5,12),(7,11),(11,11),(6,10)]
    rightbrow = [(15,11),(19,11),(21,12),(20,10),(15,11)]
    drawPoints(leftbrow, color)
    drawPoints(rightbrow, color)

def refresh():
  trackpoints = {'fore0':(6,6), 'fore1':(20,6), 'lbrow0':(6,10), 'lbrow1':(11,11),
  'rbrow0':(15,11), 'rbrow1':(20,10), 'leye':(4,15), 'reye':(22,15), 'lcheek':(7,21),
  'rcheek':(19,21), 'nose':(13,20), 'tlip':(13,23), 'blip':(13,28), 'chin':(13,31)}
  count = 0
  for key in trackpoints:
    point = (trackpoints[key][0] * XSIZE, trackpoints[key][1] * YSIZE)
    drawCross(point)

  headpoints = [trackpoints['leye'], trackpoints['reye'], trackpoints['lcheek'],
                trackpoints['rcheek'], trackpoints['chin']]
  drawHead(headpoints)
  drawHair()
  drawNose()
  drawMouth()
  drawEyes()
  drawEars()
  drawPupils()
  drawEyebrows()

def draw():
  refresh()

run()
