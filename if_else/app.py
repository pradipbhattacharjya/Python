#login program and indentation
#email - pradipbhattacharjya1997@gmail.com
#Password - 123

email = input('enter email ')
password = input('enter password ')

if email == 'pradipbhattacharjya1997@gmail.com' and password == '123':
    print('Welcome')
elif email == 'pradipbhattacharjya1997@gmail.com' and password != '123':
    print('Incorrect password')
    password = input('Entar password')
    if password == '123':
        print('Welcome,finally!')
    else:
        print('bata tumse na ho paayega!')
else:
    print('Not Correct')