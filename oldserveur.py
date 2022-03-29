from tkinter import *
from tkinter.ttk import *

mainwindow = Tk()
mainwindow.title("Spyware Serveur")
mainwindow.geometry("620x480")
mainwindow.minsize(480,360)
mainwindow.iconbitmap("spyware-icon-3.ico")
mainwindow.config(background="#DA3131")

def gettargetpos():
    poswindow = Toplevel(mainwindow)
    poswindow.title("Spyware position")
    poswindow.geometry("360x360")
    pass
def gettargetkeys():
    keyswindow = Toplevel(mainwindow)
    keyswindow.title("Spyware keylogger")
    keyswindow.geometry("360x360")
    Label(keyswindow,text ="Target's keys received !").pack()
    pass
def gettargetwebcam():
    webcamwindow = Toplevel(mainwindow)
    webcamwindow.title("Spyware Webcam")
    webcamwindow.geometry("360x360")
    
    pass
def gettargetphoto():
    photowindow = Toplevel(mainwindow)
    photowindow.title("Spyware Photo")
    photowindow.geometry("360x360")
    pass

framebutton1 = Frame(mainwindow,bg="#DA3131")
gettarget_pos_button = Button(framebutton1, text="Get target's position",font =("Linux Biolinum G",12) ,bg ="black",fg="white",command=gettargetpos)
gettarget_pos_button.pack(pady=20,padx=5)
framebutton1.grid(row = 0,column = 0, sticky=W)

framebutton2 = Frame(mainwindow,bg="#DA3131")
gettarget_keys_button = Button(framebutton2, text="Get target's keys",font =("Courrier",12) ,bg ="black",fg="white",command=gettargetkeys)
gettarget_keys_button.pack(pady=20,padx=5)
framebutton2.grid(row = 0,column = 1, sticky=W)

framebutton3 = Frame(mainwindow,bg="#DA3131")
gettarget_webcam_button = Button(framebutton3, text="Get target's webcam",font =("Courrier",12) ,bg ="black",fg="white",command=gettargetwebcam)
gettarget_webcam_button.pack(pady=20,padx=5)
framebutton3.grid(row = 0,column = 2, sticky=W)

framebutton4 = Frame(mainwindow,bg="#DA3131")
gettarget_photo_button = Button(framebutton4, text="Get target's photo",font =("Courrier",12) ,bg ="black",fg="white",command=gettargetpos)
gettarget_photo_button.pack(pady=20,padx=5)
framebutton4.grid(row = 0,column = 3, sticky=W)




#framebutton1.pack(expand=YES)
#framebutton2.pack(expand=YES)
mainloop()