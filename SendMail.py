import smtplib

def sentmail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')


gmail_user = 'example@gmail.com'
gmail_password = 'password'

sent_from = gmail_user
to = ['example2@gmail.com']
subject = 'Switch IS AVAILABLE!!'
body = 'GO GET IT NOW!!!'
# body = test.body
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

if __name__ == "__main__":
    sentmail()
