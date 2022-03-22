from tkinter import *

def gettargetpos():
    pass
def gettargetkeys():
    pass
def gettargetwebcam():
    pass
def gettargetphoto():
    pass

window = Tk()
window.title("Spyware Serveur")
window.geometry("720x480")
window.minsize(480,360)
window.iconbitmap("spyware-icon-3.ico")
window.config(background="#DA3131")

framebutton1 = Frame(window,bg="#DA3131")
gettarget_pos_button = Button(framebutton1, text="Get target's position",font =("Courrier",12) ,bg ="black",fg="white",command=gettargetpos())
gettarget_pos_button.pack(pady=20,padx=5)
framebutton1.grid(row = 0,column = 0, sticky=W)

framebutton2 = Frame(window,bg="#DA3131")
gettarget_keys_button = Button(framebutton2, text="Get target's keys",font =("Courrier",12) ,bg ="black",fg="white")
gettarget_keys_button.pack(pady=20,padx=5)
framebutton2.grid(row = 0,column = 1, sticky=W)

framebutton3 = Frame(window,bg="#DA3131")
gettarget_webcam_button = Button(framebutton3, text="Get target's webcam",font =("Courrier",12) ,bg ="black",fg="white")
gettarget_webcam_button.pack(pady=20,padx=5)
framebutton3.grid(row = 0,column = 2, sticky=W)

framebutton4 = Frame(window,bg="#DA3131")
gettarget_photo_button = Button(framebutton4, text="Get target's photo",font =("Courrier",12) ,bg ="black",fg="white")
gettarget_photo_button.pack(pady=20,padx=5)
framebutton4.grid(row = 0,column = 3, sticky=W)




#framebutton1.pack(expand=YES)
#framebutton2.pack(expand=YES)
window.mainloop()
