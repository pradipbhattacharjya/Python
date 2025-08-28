# if name is less than 3 characterss long
#     name must be at least 3 characters
# otherwise if it's more than 50 characters long
#     name can be a maximum of 50 characters
# otherwise
#     name looks good!

name = "Jqwqqwwfdewfefwfwffdscsfwegwfsfcsege"


if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")