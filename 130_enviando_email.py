from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open("template.html", "r", encoding="utf-8") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.safe_substitute(nome="William Círico", data=data_atual)

msg = MIMEMultipart()
msg['from'] = "William Círico"
msg['to'] = "contato.williamc@gmail.com"
msg['subject'] = "Atenção: este é um e-mail de testes"

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open("imagem.jpg", "rb") as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("contato.williamc@gmail.com", "wiLLam#@")
    smtp.send_message(msg)
    print("E-mail enviado com sucesso")
