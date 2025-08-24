x = 10

try:
    if (x>10):
        print("Greater than 10")

    else:
        print("Bla-Bla")

except Exception as e:
    print(f"Hey, you got this error -{e}")

finally:
    print("I will alwasys run")

print("Hello world")



name = "pradip"

my_string = f"Hello My name is {name}.How are you?"

print(my_string)