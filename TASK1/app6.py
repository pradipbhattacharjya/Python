#Check if the user is either an admin or a moderator, and either they're not banned or they've verified their email
def is_valid_user(role, is_banned, email_verified):
    return role in ["admin", "moderator"] and (not is_banned or email_verified)

# Examples
print(is_valid_user("admin", False, False))   # True
print(is_valid_user("moderator", True, True)) # True
print(is_valid_user("user", False, True))     # False
print(is_valid_user("admin", True, False))    # False
