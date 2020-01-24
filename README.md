# SMTP, POP and IMAP send/fetch email using Python

Python script to send email using SMTP and fetch the latest email in the inbox using POP3 and IMAP4. 
Script contains smtp, pop and imap servers for Yahoo and Gmail mail, alternatively user will be prompted to enter in those respective server names in case of other domains.

The debug levels are commented out in the script for pop, imap and smtp.

` Note: Setting the debug level true for a poplib instance displays the password in std out in plaintext. 
Setting debug level true for an smtplib instance displays the Base64 encoded email+password string in std out. Debug levels print the protocol handshakes and other commands to std out which are helpful in debugging; use caution when using this output elsewhere.  `

For yahoo, generate a one time password from account settings of your yahoo email account (account info --> Privacy --> generate one time password), instead of the regular password used from the web-UI.

For gmail, you can either generate one time app password using these instructions here https://support.google.com/accounts/answer/185833?hl=en or alternatively "less secure app access" has to be allowed for email to go through from this script.
https://myaccount.google.com/lesssecureapps

For IMAP, the search command takes the sender's email id as parameter and for filtering and the fetch command takes message parts as the string argument which can be looked up from here 
Doc for IMAP - https://tools.ietf.org/html/rfc3501 

For POP, the script iterates through the inbox messages and searches for latest message from the sender's email id, by doing a regex search on the 'From' header.

Doc for POP - https://tools.ietf.org/html/rfc1939

Doc for SMTP - https://tools.ietf.org/html/rfc821