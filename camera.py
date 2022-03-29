import numpy as np
import socket
import cv2 as cv
import imutils
import time
import base64 

BUFF_SIZE = 65536

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
    """cv.imshow('frame', grey)
    if cv.waitKey(1) == ord('q'):
        break"""
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()