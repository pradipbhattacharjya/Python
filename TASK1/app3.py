#Check if the password is at least 8 characters long and does not contain spaces

def is_valid_password(password):
    return len(password) >= 8 and ' ' not in password

# Examples
print(is_valid_password("StrongPass"))   # True
print(is_valid_password("short"))        # False
print(is_valid_password("pass word123")) # False