import tkinter as tk
from PIL import ImageTk,Image

REFRESH_TIME = 2

class UserInterface(tk.Tk):
	def __init__(self,width,height,perceptron,perceptron_thread):
		tk.Tk.__init__(self)
		#dimensions
		self.width = width
		self.height = height
		N_COLS_BUTTONS = 3
		BUTTON_WIDTH = 'THIS_WIDTH'

		#perceptron
		self.perceptron = perceptron

		#title
		self.title("Perceptron 2D")

		#canvas
		self.canvas = self.setCanvas(width,height,'black')
		self.canvas.grid(row=0, column=0, columnspan=N_COLS_BUTTONS, rowspan=1,sticky=tk.W + tk.E + tk.N + tk.S)

		#image
		image_directory = "singlelayer_perceptron.png"	
		self.image,self.photo_image_object = self.setImage(0,0,image_directory)

		#buttons
		learn_button = self.createButton('Learn',1,0)
		learn_button.config(width = len(BUTTON_WIDTH), height = 1,bd=4)
		plot_button = self.createButton('Plot',1,1)
		plot_button.config(width = len(BUTTON_WIDTH), height = 1,bd=4)
		reset_button = self.createButton('Reset',1,2)
		reset_button.config(width = len(BUTTON_WIDTH), height = 1,bd=4)

		# handle event on closing
		#self.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.check_for_events()


	def createLabel(self,text,row,col):
		label = tk.Label(text = text,font=("fontsys",8))
		label.grid(row = row, column = col,sticky=tk.W + tk.E + tk.N + tk.S)
		return label 

	def createLabelSmallTitle(self,text,row,col):
		label = tk.Label(text = text,font=("fontsys",9,"bold"))
		label.grid(row = row, column = col,sticky=tk.W + tk.E + tk.N + tk.S)
		return label	

	def createLabelTitle(self,text,row,col):
		label = tk.Label(text = text,font=("fontsys",10,"bold"))
		label.grid(row = row, column = col,sticky=tk.W + tk.E + tk.N + tk.S)
		return label    

	def createButton(self,text,row,col):
		button = tk.Button(text=text)
		button.grid(row=row,column=col)
		return button

	def disableButton(self,button):
		button.config(state=DISABLED)

	def enableButton(self,button):
		button.config(state="normal")

	def setImage(self,row,col,directory):
		photo_image_object = Image.open(directory)
		photo_image_object = photo_image_object.resize((306,166),Image.ANTIALIAS)
		photo_image_object = ImageTk.PhotoImage(photo_image_object)
		image = self.canvas.create_image((row,col),anchor=tk.NW,image = photo_image_object)
		return image,photo_image_object

	def setCanvas(self, width, height, color):
		canvas = tk.Canvas(width = width, height = height, bg = color)
		return canvas

	def draw(self):
		pass

	def clear(self):     
		pass

	def repaint(self):
		self.clear()
		self.draw()

	def learn_button_pressed(self):
		pass

	def reset_button_pressed(self):
		pass

	def plot_button_pressed(self):
		pass

	def check_for_events(self):
		#self.repaint()
		#self.after(REFRESH_TIME,self.run)
		pass

	def on_closing(self):
		pass
