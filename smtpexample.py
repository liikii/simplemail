# -*- encoding: utf8 -*-
"""
smtp example.
"""
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sent_mail(s, f, t, p):
    """
    :param s: SMTP server host.
    :param f: from.
    :param t: to.
    :param p: password.
    """
    msg = MIMEMultipart('related')

    msg['Subject'] = "thinks"
    msg['From'] = f
    msg['To'] = t
    msg.preamble = 'This is a multi-part message in MIME format.'

    alt_msg = MIMEMultipart('alternative')
    msg.attach(alt_msg)

    msg_plain = MIMEText('This is the alternative plain text message.')
    alt_msg.attach(msg_plain)

    msg_html = MIMEText('<b>Some <i>HTML</i> text</b><a href="http://www.runoob.com">it\'s a link</a>', 'html')
    alt_msg.attach(msg_html)

    m = SMTP_SSL(s)
    m.login(f, p)
    m.sendmail(f, [t], msg.as_string())
    m.quit()
    print('ok')


sent_mail('smtp.afghanistan.com', "mail@afghanistan.com", "tomail@afghanistan.com", 'mail')
