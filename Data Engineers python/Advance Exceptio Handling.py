#try except 
x = "10"

try:
    if (x>10):
        print("Greater than 10")

    else:
        print("Bla-Bla")

except Exception as e:
    print(e)

print("Hello world")