try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age connot be 0.')
except ValueError:
    print('Invalid value')

