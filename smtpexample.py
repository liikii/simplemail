# -*- encoding: utf8 -*-
"""
smtp example.
-------------------
reference:
https://en.wikipedia.org/wiki/Email
"""
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def sent_mail(s, f, t, p, sbj, txt_msg, html_msg, cc=None):
    """
    :param s: SMTP server host.
    :param f: from mail.
    :param t: to mail address list.
    :param p: password.
    :param cc: Carbon copy;
    :param sbj: subject.
    :param txt_msg: plain text message.
    :param html_msg: html message.
    """
    msg = MIMEMultipart('related')

    msg['Subject'] = Header(sbj, 'utf8', header_name='Subject').encode()
    msg['From'] = f
    msg['To'] = ','.join(t)
    if cc:
        msg['Cc'] = ','.join(cc)
    msg.preamble = 'This is a multi-part message in MIME format.'

    alt_msg = MIMEMultipart('alternative')
    msg.attach(alt_msg)

    msg_plain = MIMEText(txt_msg, _charset='utf-8')
    alt_msg.attach(msg_plain)
    msg_html = MIMEText(html_msg, 'html', 'utf-8')
    alt_msg.attach(msg_html)

    m = SMTP_SSL(s)
    m.login(f, p)
    ts = t + cc if cc else t
    m.sendmail(f, ts, msg.as_string())
    m.quit()
    print('ok')


sent_mail('smtp.guanajuato.com',
          "from@guanajuato.com", 
          ["to0@guanajuato.com", "to1@guanajuato.net"],
          'guanajuato_password', 'hello guanajuato subject',
          'hello guanajuato text',
          '<a href="http://www.guanajuato.com">it\'s a link</a>')
