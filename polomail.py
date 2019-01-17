import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import base64
import json

class Email():
    def __init__(self):
        
        with open('config-sample.json') as json_data:
            self.d = json.load(json_data)            

        self.EMAIL_FROM = self.d["from"]
        self.EMAIL_TO = self.d["to"]
    
    def sendEmail(self, msg, subject):       
        msgText = MIMEText(msg)
        msgText['Subject'] = subject
        msgText['From'] = self.EMAIL_FROM
        msgText['To'] = self.EMAIL_TO    

        s = smtplib.SMTP('smtp.outlook.com')
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.d["username"], self.d["password"])
        s.sendmail(self.EMAIL_FROM, self.EMAIL_TO, msgText.as_string())
        s.quit()

    

