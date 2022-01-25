import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Message:

    def __init__(self, email, password, sms_gateway, smtp, port):
        self.email = email
        self.password = password
        self.sms_gateway = sms_gateway
        self.smtp = smtp
        self.port = port
        self.server = ''
    
    # Starts up SMTP server
    def start(self):
        self.server = smtplib.SMTP(self.smtp, self.port)
        self.server.starttls()
        try:
            self.server.login(self.email, self.password)
            print('SMTP server started')
        except:
            print('Issue connecting to server, make sure email and password are correct')
        
    # Prepares and sends message
    def send_message(self, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.sms_gateway
        msg['Subject'] = 'Product In-Stock Alert'
        msg.attach(MIMEText(message, 'plain'))

        sms = msg.as_string()

        self.server.sendmail(self.email, self.sms_gateway, sms)
    

        