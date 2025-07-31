'''
if name is less than 3 characters long
   name nust be at least 3 characters
otherwise if it's more than 50 characters long
      name can be a maximum of 50 characters
otherwise
   name looks good!
'''

name = "pradip bhattacharjya"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("name must be a  maximum of 50 characters.")
else:
    print("Nmae looks good!")