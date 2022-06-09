from pickletools import read_string1
import smtplib
from email.mime.text import MIMEText

def send_email(customer,dealer,rating,comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'f2cbb742b8dead'
    password = 'b32653d9b92b2b'
    message = f"<h3>New Feedbacl Submission</h3><ul><li>Customer:{customer}</li><li>Customer:{customer}</li><li>Customer:{dealer}</li><li>Customer:{dealer}</li><li>Customer:{rating}</li><li>Customer:{rating}</li><li>Customer:{comments}</li><li>Customer:{comments}</li></ul>"

    senderemail = 'swapnilvects29@gmail.com'
    receiveremail = 'swapnil.wankhede645@gmail.com'
    msg = MIMEText(message,'html')
    msg['Subject']='Lexus Feedback'
    msg['From'] = senderemail
    msg['To'] = receiveremail

    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(senderemail,receiveremail,msg.as_string())