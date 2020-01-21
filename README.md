# SMTP, POP and IMAP send/fetch email using Python

Python script to send email using SMTP and fetch the latest email in the inbox using POP3 and IMAP4. 
Script contains smtp, pop and imap servers for Yahoo and Gmail mail, alternatively user will be prompted to enter in those respective server names in case of other domains.

For yahoo, generate a one time password from account settings of your yahoo email account (account info --> Privacy --> generate one time password), instead of the regular password used from the web-UI.

For gmail, less secure app access has to be allowed for email to go through from this script.
https://myaccount.google.com/lesssecureapps

For IMAP, the fetch command takes message parts as the string argument which can be looked up from here 
https://tools.ietf.org/html/rfc3501 -- IMAP 

Doc for POP - https://tools.ietf.org/html/rfc1939
Doc for SMTP - https://tools.ietf.org/html/rfc821