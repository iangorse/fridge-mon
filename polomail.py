import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import base64

class Email():
    def __init__(self, config):
        self.config = config
        self.EMAIL_FROM = self.config["from"]
        self.EMAIL_TO = self.config["to"]
    
    def sendEmail(self, msg, subject):       
        msgText = MIMEText(msg)
        msgText['Subject'] = subject
        msgText['From'] = self.EMAIL_FROM
        msgText['To'] = self.EMAIL_TO    

        s = smtplib.SMTP(self.config['smtp-server'])
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.config["username"], self.config["password"])
        s.sendmail(self.EMAIL_FROM, self.EMAIL_TO, msgText.as_string())
        s.quit()

    

