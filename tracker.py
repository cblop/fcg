
import cv
def getthresholdedimg(im):
	'''this function take RGB image.Then convert it into HSV for easy colour detection and threshold it with yellow part as white and all other regions as black.Then return that image'''
	imghsv=cv.CreateImage(cv.GetSize(im),8,3)
	cv.CvtColor(im,imghsv,cv.CV_BGR2HSV)				# Convert image from RGB to HSV
		
	# A little change here. Creates images for green,blue and yellow (or whatever color you like).
	imgyellow=cv.CreateImage(cv.GetSize(im),8,1)
	imgblue=cv.CreateImage(cv.GetSize(im),8,1)
	
	imgthreshold=cv.CreateImage(cv.GetSize(im),8,1)
	
	cv.InRangeS(imghsv,cv.Scalar(20,100,100),cv.Scalar(40,255,255),imgyellow)	# Select a range of yellow color
	cv.InRangeS(imghsv,cv.Scalar(100,100,100),cv.Scalar(120,255,255),imgblue)	# Select a range of blue color
	#cv.InRangeS(imghsv,cv.Scalar(100,135,135),cv.Scalar(140,255,255),imgblue)	# Select a range of blue color
#	Add everything
	#cv.Add(imgyellow,imgblue,imgthreshold)
	#return imgthreshold
	return imgyellow, imgblue

def captureVid():
	capture=cv.CaptureFromCAM(0)
	frame = cv.QueryFrame(capture)
	return capture, frame

def getContours(capture, frame):
	#frame_size = cv.GetSize(frame)
	#grey_image = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, 1)
	#test=cv.CreateImage(cv.GetSize(frame),8,3)
	#img2=cv.CreateImage(cv.GetSize(frame),8,3)

	color_image = cv.QueryFrame(capture)
	imdraw=cv.CreateImage(cv.GetSize(frame),8,3)
	cv.SetZero(imdraw)
	cv.Flip(color_image,color_image,1)
	cv.Smooth(color_image, color_image, cv.CV_GAUSSIAN, 3, 0)
	imgyellowthresh, imgbluethresh = getthresholdedimg(color_image)
	cv.Erode(imgyellowthresh,imgyellowthresh,None,3)
	cv.Dilate(imgyellowthresh,imgyellowthresh,None,10)
	cv.Erode(imgbluethresh,imgbluethresh,None,3)
	cv.Dilate(imgbluethresh,imgbluethresh,None,10)
	#img2=cv.CloneImage(imgyellowthresh)
	storage = cv.CreateMemStorage(0)
	storage2 = cv.CreateMemStorage(0)
	ycontours = cv.FindContours(imgyellowthresh, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
	bcontours = cv.FindContours(imgbluethresh, storage2, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)

	return ycontours, bcontours

def getPoints(ycontours, bcontours):
	ypoints = []	
	bpoints = []	
	i = 0
	for contours in [ycontours, bcontours]:
		while contours:
			# Draw bounding rectangles
			bound_rect = cv.BoundingRect(list(contours))
			contours = contours.h_next()
			pt1 = (bound_rect[0] + (bound_rect[2] / 2), bound_rect[1] + (bound_rect[3] / 2))

			# for more details about cv.BoundingRect,see documentation
			#pt1 = (bound_rect[0], bound_rect[1])
			#pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
			if i == 0:
				ypoints.append(pt1)
			else:
				bpoints.append(pt1)
			#points.append(pt2)
			#cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255,0,0), 2)
		i += 1

	return ypoints, bpoints

def sortPoints(ypoints, bpoints):
	tpoints = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
			   (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

	if len(ypoints) > 6 and len(bpoints) > 6:
		ypoints = sorted(ypoints, key=lambda x: x[1])
		if ypoints[1][0] < ypoints[2][0]:
			ypoints[1], ypoints[2] = ypoints[2], ypoints[1]

		if ypoints[5][0] < ypoints[4][0]:
			ypoints[4], ypoints[5] = ypoints[5], ypoints[4]

		bpoints = sorted(bpoints, key=lambda x: x[1])
		if bpoints[1][0] < bpoints[2][0]:
			bpoints[1], bpoints[2] = bpoints[2], bpoints[1]

		tpoints = [ypoints[0], bpoints[0], bpoints[1], ypoints[1],
				   bpoints[2], ypoints[2], ypoints[3], bpoints[3],
				   bpoints[4], ypoints[4], ypoints[5], bpoints[5],
				   ypoints[6], bpoints[6]]

	return tpoints

def runTracking():
	capture, frame = captureVid()
	ycontours, bcontours = getContours(capture, frame)
	ypoints, bpoints = getPoints(ycontours, bcontours)
    #print "Y: " + `ypoints` + "  B: " + `bpoints`

	tpoints = sortPoints(ypoints, bpoints)
	return tpoints

if __name__ == "__main__":
	runTracking()
