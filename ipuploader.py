from socket import *
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 
import os 
   
myip = gethostbyname(gethostname())
"""gauth = GoogleAuth() 
  
gauth.LocalWebserverAuth()        
drive = GoogleDrive(gauth) 
   
path = r"C:\Games\Battlefield"   
   
for x in os.listdir(path): 
   
    f = drive.CreateFile({'title': x}) 
    f.SetContentFile(os.path.join(path, x)) 
    f.Upload() 
  
    
    
    
    
    
    
    f = None"""
