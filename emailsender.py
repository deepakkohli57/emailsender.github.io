#we are making software of email sender

import smtplib,webbrowser,getpass

def get_mail():
    serviceProvider=['gmail','yahoo','hotmail','outlook']
    while True:
            mail=input("Enter your valid email address")
            if ('@' in mail and '.com' in mail):
                    symbol_pos = mail.find('@')
                    dotcom_pos = mail.find('.com')
                    sp = mail[symbol_pos+1 : dotcom_pos]

                    if sp in serviceProvider:
                        return mail,sp
                        break

                    else:
                        print("Sorry! We are not provide a service for " + sp)
                        print("We are only provide a service for gmail,yahoo,hotmail,outlook")
                        continue
                
            else:
                print("You are not entered a valid email address")
                print("\n please again enter email id")
                continue
            

def set_domain_email(serviceProvider):
    if serviceProvider =='gmail':
     return 'smtp.gmail.com'
    elif serviceProvider == 'yahoo':
     return 'smtp.mail.yahoo.com'
    elif serviceProvider == 'hotmail' and serviceProvider == 'outlook':
     return 'smtp-mail.outlook.com'

print('Welcome you can send email through this programme')
print('Enter your email id and password')
email,serviceProvider=get_mail()
password=getpass.getpass("Enter your password:")



while True:

    try:
        smtpDomain = set_domain_email(serviceProvider)
        connection = smtplib.SMTP(smtpDomain ,587)
        connection.ehlo()
        connection.starttls()
        connection.login(email,password)


    except:
        if serviceProvider=='gmail':
                print("There are basically two reason to unable login your id and password :")
                print("You are typed invalid id and password")
                print("Your less secure account is unable if you want to enable your less secure account :")
                answer=input("Yes or No")
                if answer=='yes':
                    webbrowser.open('https://myaccount.google.com/lesssecureapps')
                  
                else:
                    print("we wont't open webpage for you,you can go to https://myaccount.google.com/lesssecureapps")
                    print("Enter your id and password")
                    email,sp = get_mail()
                    password=getpass.getpass("password:")
                    continue
        else:
                    print("Login Unsuccessfull,")
                    print("Enter your valid id and password")
                    email,sp = get_mail()
                    password=getpass.getpass("password:")
                    continue       
                
    else:
        print("You login successfully")
        break

print("Enter your Reciever email address ")
recieverEmail,recieverSP = get_mail()
Subject=input("Enter your Subject")
Message=input("Enter your Message")
connection.sendmail(email,recieverEmail,str(Subject) + "\n \n" + str(Message))
print("Email send successfully")
connection.quit()    
    

            











