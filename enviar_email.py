import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
from configuracoesEmail import dados_email

def enviaremail():
    to_addr = ['']
    titulo = str(f'Monitoramento Propostas CRED - {date.today()}')
    subject = titulo
    body = 'Bom dia, Segue monitoramento diário de propostas.'

    server = smtplib.SMTP(dados_email()['smtp_server'], dados_email()['smtp_port'])
    server.starttls()
    server.login(dados_email()['acc_addr'], dados_email()['acc_pwd'])

    msg = MIMEMultipart()
    msg["From"] = dados_email()['acc_addr']
    msg["To"] = ", ".join(to_addr)
    msg["Subject"] = subject

    arquivo = str(f'MonitoramentoClientesCred{date.today()}.xlsx')
    attachment = open(arquivo, 'rb')

    xlsxFilename = arquivo

    part = MIMEBase('application', "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={arquivo}')
    msg.attach(part)

    msgText = MIMEText('{}'.format(body))
    msg.attach(msgText)

    server.sendmail(dados_email()['acc_addr'], to_addr, msg.as_string())
    server.quit()