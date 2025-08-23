my_list =[1,2,3,4,5,6]
new_list = []

print(my_list[::-1])

#permanent list reverse
my_list.reverse()
print(my_list)

# Temporary list reverse 
for i in reversed(my_list):
    print(i)




for i in my_list:
    new_list.append(i*i)

print(new_list)