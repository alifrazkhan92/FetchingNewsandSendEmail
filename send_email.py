import smtplib, ssl

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'my_email@gmail.com'
    password = '<PASSWORD>'


    receiver = '<EMAIL>'
    conntext = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=conntext) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email("Hello, this is a test email sent from Python!")

