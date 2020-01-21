#! /usr/bin/python3
from getpass import getpass
import smtplib
import re
import poplib
import email
import imaplib


def fetchEmailPop():
    mailbox = poplib.POP3_SSL(pop_server, '995')
    mailbox.set_debuglevel(True)
    mailbox.user(email_id_to)
    mailbox.pass_(passwd_to)
    num = len(mailbox.list()[1])
    print("********** FETCHING THE LATEST MESSAGE FROM THE INBOX USING POP ********** \n %s" % (mailbox.retr(num)[1]))
    mailbox.quit()


def fetchEmailImap():
    mailbox = imaplib.IMAP4_SSL(imap_server, 993)
    mailbox.debug
    mailbox.login(email_id_to, passwd_to)
    mailbox.select()
    typ, num = mailbox.search(None, '(FROM "%s")' %(email_id_from))
    typ, data = mailbox.fetch(num[0].split()[len(num) - 1], '(RFC822)')
    # 2nd argument of fetch message parts can be RFC822 or BODY[]; look up legend in README.
    print('********* FETCHING THE LATEST MESSAGE FROM USER %s THE INBOX USING IMAP ********** \n %s\n' % (email_id_from, data[0][1]))
    mailbox.close()
    mailbox.logout()


def sendEmail():
    print("********* SENDING EMAIL FROM USER %s to USER %s ********** \n" % (email_id_from, email_id_to))
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(True)
    server.login(email_id_from, passwd_from)
    msg = email.message.EmailMessage()
    msg.set_payload("Hi there from Python")
    msg['Subject'] = "Just Python saying Hi! "
    server.send_message(msg, email_id_from, email_id_to)
    server.quit()


if __name__ == "__main__":
    print("Python Script to send/fetch email.")
    email_id_from = input("Please enter your Email id you would like to send the email from : ")
    passwd_from = getpass("Password for %s: " % email_id_from)
    email_id_to = input("Please enter the Email id you would like to the email to : ")
    passwd_to = getpass("Password for %s : " % email_id_to)

    if re.search('.*yahoo\.com', email_id_from):
        print("Yahoo SMTP server")
        smtp_server = 'smtp.mail.yahoo.com'
    elif re.search('.*gmail.com', email_id_from):
        print("Gmail SMTP server")
        smtp_server = 'smtp.gmail.com'
    else:
        smtp_server = input("The domain is not yahoo/gmail \n Enter the SMTP server for domain: ")

    if re.search('.*yahoo\.com', email_id_to):
        print("Yahoo POP and IMAP server")
        pop_server = 'pop.mail.yahoo.com'
        imap_server = 'imap.mail.yahoo.com'
    elif re.search('.*gmail.com', email_id_to):
        print("Gmail POP and IMAP server")
        pop_server = 'pop.gmail.com'
        imap_server = 'imap.gmail.com'
    else:
        pop_server = input("The domain is not yahoo/gmail \n Enter POP server for domain: ")
        imap_server = input("Enter IMAP server for domain: ")
    sendEmail()
    fetchEmailPop()
    fetchEmailImap()