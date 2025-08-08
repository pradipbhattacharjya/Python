#Validate the Quality and Correctness of Email Values
#-Must not be empty
#-Must contain'.' and '@'
#-Must contain exactly oe '@' symbol
#-Must end with '.com','.org',or '.net'
#-Must not be longer then 254 characters
#-Must start and end with a letter or digit

email = 'pradipbhattacharjya1997@gmail.com'
email = email.strip()
if email == "":
    print("Email cannot be empty.")
elif not ("." in email and '@' in email):
    print("Email must contain. and @")
elif email.count('@') != 1:
    print("Email must contain exactly one @.")
elif not email.endswith(('.com','.org','.net')):
    print("Email must end with .com, .org, or .net")
elif len(email) > 245:
    print("Email must not be longer than 245 characters")
elif not (email[0].isalnum and email[-1].isalnum()):
    print("Emailmust strat and with a letter or digit")
else:
    print("Email is valid. ")