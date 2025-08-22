#Iterations

my_list =["Order","Products","Customers"]


for i in my_list:
    print(i)


# range function
# for i in range(1,101):
#     print(i)


for i in my_list:

    if(i.lower() == "order"):
        print("My Order")
    else:
        print("Not My Order")