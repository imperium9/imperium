import numpy as np
import socket
import cv2 as cv
import imutils
import time
import base64 

BUFF_SIZE = 65536
myname = socket.gethostname()
myip = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
port=9999
socket_adress =  (myip,port)
server.bind(socket_adress)
print("listening at :",socket_adress)
vid = cv.VideoCapture(0)
fps,st,frames_to_count,cnt = (0,0,20,0)

while True :
    msg,client_addr = server_socket.recvfrom(BUFF_SIZE)