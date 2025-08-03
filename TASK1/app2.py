#Check if a user's name is not empty and the age is greater than or equal to 18
def is_valid_user(name, age):
    return bool(name.strip()) and age >= 18

# Example usage
print(is_valid_user("Alice", 20))  # True
print(is_valid_user("   ", 25))    # False
print(is_valid_user("Bob", 17))    # False