#Arithmetic Operators
print(5 + 6)
print(5 - 6)
print(5 * 6)
print(5 / 6)
print(5 // 6)
print(5 % 6)
print(5 ** 2)

#Relational Operators
print(4>5)
print(4<5)
print(4>=5)
print(4<=5)
print(4==5)
print(4!=5)

#Logical Operators
print(1 and 0)
print(1 or 0)
print(not 0)
#Bitwise Operators
#Bitwise and
print(2 & 3)
#Bitwise or
print(2 | 3)
#Bitwise xor
print(2^3)

print(~3)
print(4>> 2)
print(5 << 2)

#Assignment Operators
a = 2
#Membership Operators
#in/not in
print('D' in 'Delhi')
print('D' not in 'Delhi')

#qs-Find the sum of a 3 digit number entered by the user

number = int(input("Enter a 3 digit number "))
a =number % 10

number = number//10

b = number % 10
number = number //10

c = number % 10

print(a + b + c)

