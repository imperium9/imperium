import cv2, imutils, socket
import numpy as np
import time
import base64
import threading
global opconnect
opconnect = False

def threadconnectioncheck():
	checker = threading.Thread(target=connectionchecker)
	checker.start()

def connectionchecker():
	opconnect = True
	bind_ip = "127.0.0.1"
	bind_port = 9998

	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	server.bind((bind_ip, bind_port))

	print("[*] Ready for data at %s:%d" % (bind_ip, bind_port))

	while opconnect==True:
	
		data, addr = server.recvfrom(1024)

		print("[*] Got data from %s:%d: %s" % (addr[0], addr[1], data))
		if data==b'closing video':
			print("closing everything...")
			opconnect = False
			break
		print("thread still running")
	
BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '127.0.0.1'
print(host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
print('Listening at:',socket_address)
opconnect = True
vid = cv2.VideoCapture(0) #  replace 'rocket.mp4' with 0 for webcam
fps,st,frames_to_count,cnt = (0,0,20,0)
msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
print('GOT connection from ',client_addr)
opconnect=True
threadconnectioncheck()
WIDTH=400
while(vid.isOpened() and opconnect==True):
	_,frame = vid.read()
	frame = imutils.resize(frame,width=WIDTH)
	encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
	message = base64.b64encode(buffer)
	server_socket.sendto(message,client_addr)#l'erreur vient surement de là
	"""if connectionchecker.is_alive()==False:
		break"""