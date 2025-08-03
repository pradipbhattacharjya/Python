#string functions

# len
# max
# min
# sorted

print(len('helli world'))
print(max('helli world'))
print(min('helli world'))
print(sorted('helli world'))
print(sorted('helli world',reverse=True))

s = 'hello world'
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.count('l'))

print('my name is pradip'.find('is'))
print('my name is pradip'.endswith('ip'))
print('my name is pradip'.startswith('my'))


name = 'Pradip'
gender = 'male'

print('Hi my name is {} and I am a {}'.format(name,gender))

print('prdaip123%'.isalnum())
print('nitish'.isalpha())

print('123'.isdigit())

print('hi my name is nitish'.split())

print('-'.join(['hi', 'my', 'name', 'is', 'nitish']))
print('hi my name is nitish'.replace('nitish','pradip'))
print('pradip                 '.strip())