#8>Function with **kwargs
#Create a function that accepts any number of keyword arguments and prints them in format key: value.
def print_kwargs(**kwargs):
    # print("Name",name, "Power: ", power)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman",power ="lazer")
# print_kwargs(name="Shaktiman"

