my_list = [1,2,"Ansh","Lamba",['aa','bb','cc']]

print(my_list[0])
print(my_list[4])
print(my_list[-3:])
print(my_list[len(my_list)-3 : len(my_list)])

my_list2 = [1,2,"Ansh","Lamba",3,4,5,6]

print(my_list2[:])
print(my_list2[::3])

#lists are mutable
my_list2.append("Hero")
print(my_list2)

my_list2.insert(1,"pradip")
print(my_list2)

# delete
my_list2.pop()
print(my_list2)


