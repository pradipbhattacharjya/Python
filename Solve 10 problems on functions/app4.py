#5>Default  Parameter Value
#Write a function that greets a user.if no name is provided, it should  greet with a default name.

def greet(name = "User"):
    return "Hello," + name + " !"


print(greet("chai"))
print(greet())