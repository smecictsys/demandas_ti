import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr
from unidecode import unidecode


class Msender:
        def send_email(self, data):
            link = "http://192.168.100.111:5000/ti/demandas/listar_todas"
            email = "thyezoliveiramonteiro@smec.saquarema.rj.gov.br"
            subjet = "Notificação - Nova demanda de TI"
            
            html = f"""
            <html>
            <head></head>
            <body>
                <h1>Nova demanda {data['tipo']}</h1>
                <p>Este email, veio do sistema de demandas.</p>

                <P><strong>Data:</strong> {data['entrada']}</p>
                <p><strong>Solicitante:</strong> {data['solicitante']} (Nome/Sala)</p>
                <p><strong>Descrição:</strong> {data['desc']}</p>

                <h2>Acessa a lista completa no link abaixo</h2>
                <a href={link}>Listar todas as demandas</a>
            </body>
            </html>
            """
            self.enviar_email(email, subjet, html)

        def enviar_email(self, destinatario, assunto, mensagem):
            try:
                remetente_nome = "Sistema de demandas"
                remetente_email = 'sisdemandasinterno@smec.saquarema.rj.gov.br'
                senha = 'ysqe moju iohw mjtw'
                remetente = formataddr((remetente_nome, remetente_email))
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                servidor = smtplib.SMTP(smtp_server, smtp_port)
                servidor.starttls()
                servidor.login(remetente_email, senha)
                mensagem_email = MIMEMultipart()
                mensagem_email['From'] = remetente
                mensagem_email['To'] = destinatario
                mensagem_email['Subject'] = assunto
                corpo_da_mensagem = mensagem
                mensagem_email.attach(MIMEText(corpo_da_mensagem, 'html'))

                servidor.sendmail(remetente_email, destinatario, mensagem_email.as_string())
                servidor.quit()
            except Exception as e:
                print("erro: ", e)
