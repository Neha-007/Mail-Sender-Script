#In order for this script to work, you must also enable "less secure apps" to access your Gmail account.
#As a warning, this is not ideal, and Google does indeed warn against enabling this feature. Be forewarned! 
#https://myaccount.google.com/u/2/lesssecureapps?pageId=none

import smtplib
def send():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    EMAIL_ADDRESS=str(input('Sender Email ID:'))
    PASSWORD=str(input('Enter Password:'))
    server.login(EMAIL_ADDRESS,PASSWORD)
    address=str(input('Sender Address:'))
    message=str(input('Message:'))
    server.sendmail(EMAIL_ADDRESS,address,message)
    server.quit()
    print('Mail was sent Sucessfully!!!')
send()
