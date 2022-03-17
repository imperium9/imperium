# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
import tkinter.font
#from tkinter.ttk import *
#from turtle import bgcolor

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.title("Imperium")
master.geometry("720x480")
master.minsize(480,360)
master.iconbitmap("spyware-icon-3.ico")
master.config(background="black")


#style = Style()
 
#style.configure('TButton', font=('American typewriter', 14), background='black', foreground='green')
#style.map('TButton', background=[('active', 'black')])
# function to open a new window
# on a button click
def openPositionWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Imperium Position")
	newWindow.iconbitmap("spyware-icon-3.ico")
	newWindow.config(background="black")
	# sets the geometry of toplevel
	newWindow.geometry("480x480")

	# A Label widget to show in toplevel
	Label(newWindow,text ="Target's position :",font=("System", 17), bg='black',fg='green').pack()

def openKeysWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Imperium Keys")
	newWindow.config(background="black")
	newWindow.iconbitmap("spyware-icon-3.ico")

	# sets the geometry of toplevel
	newWindow.geometry("480x480")

	# A Label widget to show in toplevel
	Label(newWindow,text ="Target's keys received !",font=("System", 17), bg='black',fg='green').pack()

def openCameraWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Imperium Webcam")
	newWindow.config(background="black")
	newWindow.iconbitmap("spyware-icon-3.ico")

	# sets the geometry of toplevel
	newWindow.geometry("480x480")

	# A Label widget to show in toplevel
	Label(newWindow,text ="Target's webcam:",font=("System", 17), bg='black',fg='green').pack()

def openPhotoWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Imperium Photo")
	newWindow.config(background="black")
	newWindow.iconbitmap("spyware-icon-3.ico")

	# sets the geometry of toplevel
	newWindow.geometry("480x480")

	# A Label widget to show in toplevel
	Label(newWindow,text ="Target's Photo:",font=("System", 17), bg='black',fg='green').pack()



label = Label(master,text ="Target :",font=("System", 22), bg='black',fg='green')

label.grid(ipadx=100 ,padx = 60,pady=20,row=0,column=0,sticky = N)

# a button widget which will open a
# new window on button click
posbtn = Button(master, 
			text ="Get Target Position",font=("System", 15), bg='black',fg='green',
			#style = 'W.TButton',
			command = openPositionWindow)
posbtn.grid(padx=60,pady=20,row=1,column=1,sticky = N)

keysbtn = Button(master,
			text ="Get Target Keys",font=("System", 15), bg='black',fg='green',
			#style = 'W.TButton',
			command = openKeysWindow)
keysbtn.grid(pady=20,row=2,column=1,sticky = N)

camerabtn = Button(master,
			text ="Get Target Webcam", font=("System", 15), bg='black',fg='green',
			#style = 'W.TButton',
			command = openCameraWindow)
camerabtn.grid(pady=20,row=3,column=1,sticky=N)

photobtn = Button(master,
			text ="Get Target Photo", font=("System", 15), bg='black',fg='green',
			#style = 'W.TButton',
			command = openPhotoWindow)
photobtn.grid(pady=20,row=4,column=1,sticky = N)

label2 = Label(master,text ="Target's Cmd :",font=("System", 17), bg='black',fg='green')
label2.grid(row=5,column=0,sticky=W)
textfromshell= ""
distantshell = Entry(master,font=("System", 17), bg='#021D09',fg='green')
distantshell.grid(pady=20,row=6,column=0,sticky = W)
distantshell.insert(0,">>>")
# mainloop, runs infinitely
mainloop()
