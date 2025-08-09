#Scan emails to block unsafe date from entering your system

emails = [
    'data@gmail.com',
    'baraa@outlook.de',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack')
        break
    print(f'Processing Email : {email}')