import smtplib
import os

def mail(sendto, subject_, mail_text):

    gmail_user = 'headapp18@gmail.com'
    gmail_password = 'bhuproject'

    sent_from = gmail_user
    to = ['iameshanpandey@gmail.com', sendto]
    subject = subject_
    body = 'I am sending this mail again to check the sepeed of mail delivery\n\n- You'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
        os.system("say 'Email sent!'")
    except:
        print('Something went wrong...')
        os.system("say 'Something went wrong...'")
