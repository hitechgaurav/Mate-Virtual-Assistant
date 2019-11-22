import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class _email_:
    __smtp_server="smtp."
    def __init__(self, rec):
        self.port = 587
        self.sender_email =#sender email address
        self.sender_pass = #sender id password
        self.context = ssl.create_default_context()
        self.rec=rec
        x=self.rec.index("@")
        self.header=""
        for i in range(x+1, len(self.rec)):
            self.header+=self.rec[i]
        self.__smtp_server+=self.header
    def send_simple_mail(self,message):
        try:
            server = smtplib.SMTP(self.__smtp_server,self.port)
            server.ehlo() # Can be omitted
            server.starttls(context=self.context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(self.sender_email, self.sender_pass)
            server.sendmail(self.sender_email, self.rec, message)
            print("Message Sent")
            # TODO: Send email here
        except Exception as e:
            print(e)
        finally:
            server.quit()
    def send_complex_mail(self, sub, bdy, file):
        self.subject=sub
        self.body=bdy
        self.message=MIMEMultipart()
        self.message["From"]=self.sender_email
        self.message["To"]=self.rec
        self.message["Subject"]=self.subject
        self.message["Bcc"]=self.rec

        self.message.attach(MIMEText(self.body, 'plain'))

        self.filename=file
        with open(self.filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",
        f"attachment; filename= {self.filename}",)

        self.message.attach(part)
        text = self.message.as_string()
        try:
            with smtplib.SMTP_SSL(self.__smtp_server, 465, context=self.context) as server:
                server.login(self.sender_email, self.sender_pass)
                server.sendmail(self.sender_email, self.rec, text)
        except Exception as e:
            print(e)
