#! /usr/bin/python3
from getpass import getpass
import smtplib
import re
import poplib
import email
import imaplib


def print_fetch(extra_log, from_email, to_email, protocol, message):
    print("**********%s FETCHING THE LATEST MESSAGE FROM USER %s IN THE INBOX %s USING %s ********** \n %s" % (
        extra_log, from_email, to_email, protocol, message))


def fetchEmailPop():
    print("********** BEGIN POP **********")
    mailbox = poplib.POP3_SSL(pop_server, '995')
    mailbox.set_debuglevel(True)
    mailbox.user(email_id_to)
    mailbox.pass_(passwd_to)
    num_list = mailbox.list()
    found = False
    if num_list[1]:
        for each_msg in range(len(num_list[1]), 0, -1):
            msg_list = mailbox.retr(each_msg)[1]
            for each_header in msg_list:
                if re.search("From:\s*.*@.*\.com", each_header.decode("utf-8")):
                    if re.search(".*" + email_id_from + ".*", each_header.decode("utf-8")):
                        print_fetch("", email_id_from, email_id_to, "POP", msg_list)
                        found = True
                    break
            if found:
                break
    else:
        print_fetch("ERROR! NO EMAIL FOUND WHILE", email_id_from, email_id_to, "POP", "")
    mailbox.quit()


def fetchEmailImap():
    print("********** BEGIN IMAP **********")
    mailbox = imaplib.IMAP4_SSL(imap_server, 993)
    mailbox.debug = 1
    mailbox.login(email_id_to, passwd_to)
    mailbox.select("Inbox")
    typ, num = mailbox.search(None, '(FROM "%s")' % email_id_from)
    msg_list = num[0].split()
    if num is not None and msg_list:
        typ, data = mailbox.fetch(msg_list[len(msg_list) - 1], '(RFC822)')
        # 2nd argument of fetch message parts can be RFC822 or BODY[]; look up legend in README.
        print_fetch("", email_id_from, email_id_to, "IMAP", data[0][1])

    else:
        print_fetch("ERROR! NO EMAIL FOUND WHILE", email_id_from, email_id_to, "IMAP", "")
    mailbox.close()
    mailbox.logout()


def sendEmail():
    print("********* BEGIN SMTP - SENDING EMAIL FROM USER %s to USER %s ********** \n" % (email_id_from, email_id_to))
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(True)
    server.login(email_id_from, passwd_from)
    msg = email.message.EmailMessage()
    msg.set_payload("Hi there!!! from Python")
    msg['Subject'] = "Just Python saying Hi! :) :)"
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
