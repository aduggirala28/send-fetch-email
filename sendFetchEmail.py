#! /usr/bin/python3
from getpass import getpass
import smtplib
import re
import poplib
import email
import imaplib


def fetchEmailPop(email_id, passwd):
    mailbox = poplib.POP3_SSL(pop_server, '995')
    mailbox.set_debuglevel(True)
    mailbox.user(email_id)
    mailbox.pass_(passwd)
    num = len(mailbox.list()[1])
    print("********** FETCHING THE LATEST MESSAGE FROM THE INBOX USING POP ********** \n %s" % (mailbox.retr(num)[1]))
    mailbox.quit()


def fetchEmailImap(email_id, passwd):
    mailbox = imaplib.IMAP4_SSL(imap_server, 993)
    mailbox.debug
    mailbox.login(email_id, passwd)
    mailbox.select()
    typ, num = mailbox.search(None, 'ALL')
    typ, data = mailbox.fetch(num[0].split()[len(num) - 1], '(RFC822)')
    #2nd argument of fetch message parts can be RFC822 or BODY[]; look up legend in README.
    print('********* FETCHING THE LATEST MESSAGE FROM THE INBOX USING IMAP ********** \n %s\n' % (data[0][1]))
    mailbox.close()
    mailbox.logout()

def sendEmail(email_id, passwd):
    print("Trying to send email  now")
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(True)
    server.login(email_id, passwd)
    msg = email.message.EmailMessage()
    msg.set_payload("Hi there from Python")
    msg['Subject'] = "Just Python saying Hi! "
    server.send_message(msg, email_id, email_id)
    server.quit()

if __name__ == "__main__":
    print("Python Script to send/fetch email.")
    email_id = input("Please enter your Email id: ")
    passwd = getpass()
    if re.search('.*yahoo\.com', email_id):
        print("Yahoo SMTP server")
        smtp_server = 'smtp.mail.yahoo.com'
        pop_server = 'pop.mail.yahoo.com'
        imap_server = 'imap.mail.yahoo.com'
    elif re.search('.*gmail.com', email_id):
        print("Gmail SMTP server")
        smtp_server = 'smtp.gmail.com'
        pop_server = 'pop.gmail.com'
        imap_server = 'imap.gmail.com'
    else:
        smtp_server = input("The domain is not yahoo/gmail \n Enter the SMTP server for domain: ")
        pop_server = input("Enter POP server for domain: ")
        imap_server = input("Enter IMAP server for domain: ")
    sendEmail(email_id, passwd)
    fetchEmailPop(email_id, passwd)
    fetchEmailImap(email_id, passwd)
