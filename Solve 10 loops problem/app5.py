#5> Find the First Non-Repeated Character
#Given a string,find the First Non-Repeated Character.

input_str = "teeter"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break