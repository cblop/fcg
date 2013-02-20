import Tkinter as tk
from PIL import Image, ImageTk


class App:
	def __init__(self, root, images):
		self.index = 0
		self.images = images
		self.points = []

		for i in range(len(self.images)):
			self.images[i] = ImageTk.PhotoImage(self.images[i])


		w = images[0].width()
		h = images[0].height()

		x = 0
		y = 0

		self.panel1 = tk.Canvas(root, width=w, height=h)
		self.panel1.pack(side='top', fill='both', expand='yes')

		self.panel1.bind("<1>", self.onMouseDown)

		self.showImage()

		self.donebutton = tk.Button(self.panel1, text='done')
		self.donebutton.bind("<Button-1>", self.doneButtonClicked)
		self.donebutton.pack(side='bottom')

		#self.undobutton = tk.Button(self.panel1, text='undo')
		#self.undobutton.bind("<Button-2>", self.undoButtonClicked)
		#self.undobutton.pack(side='top')

		self.panel1.image = images[0]

		root.geometry("%dx%d+%d+%d" % (w, h, x, y))

	def onMouseDown(self, event):
		print "frame coordinates: %s/%s" % (event.x, event.y)
		print "root coordinates: %s/%s" % (event.x_root, event.y_root)
		self.points.append((event.x, event.y))
		self.panel1.create_line(event.x - 5, event.y, event.x + 5, event.y, fill='yellow')
		self.panel1.create_line(event.x, event.y - 5, event.x, event.y + 5, fill='yellow')

	def doneButtonClicked(self, event):
		print 'button clicked'
		self.index += 1
		self.showImage()
		writeFile('points.txt', self.points)
		self.points = []

	#def undoButtonClicked(self, event):
	#	print 'undo clicked'

	def showImage(self):
		self.panel1.create_image(0, 0, image=self.images[self.index], anchor='nw')

def writeFile(filename, strings):
	f = open(filename, 'a')
	f.write(str(strings).strip('[]') + '\n')

	f.close()

def clearFile(filename):
	f = open(filename, 'w')
	f.close()

def main():
	clearFile('points.txt')
	images = []
	imageFile = "images/cap-001.jpeg"

	for i in range(1, 253):
		if i < 10:
			imageFile = "images/cap-00" + `i` + ".jpeg"
		elif i < 100:
			imageFile = "images/cap-0" + `i` + ".jpeg"
		else:
			imageFile = "images/cap-" + `i` + ".jpeg"

		#image1 = ImageTk.PhotoImage(Image.open(imageFile))
		image1 = Image.open(imageFile)
		images.append(image1)

	root = tk.Tk()
	root.title("background image")
	app = App(root, images)
	root.mainloop()

if __name__ == "__main__":
	main()
