#Check if a username is a string,is not None,and is longer than 5 characters
def is_valid_username(username):
    return isinstance(username,str) and username is not None and len(username)>5

print(is_valid_username('admin12'))
print(is_valid_username("user"))
print(is_valid_username(None))
