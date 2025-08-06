#Email must not be empty
#Email must contain a '.' and '@'
#Email must contain exactly one '@' symbol
#Email must end with '.com','.org',or '.net'
#Email must not be longer than 254 characters
#Email must start and end with a letter or digit


email = ""
# Clean the String
email = email.strip()
if email == "":
    print("Email cannot be empty. ")
else:
    print("Email is valid.")