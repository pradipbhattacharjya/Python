#Check if a user's email is not empty,contains '@',and ends with '.com'

def is_valid_email(email):
    return email.strip() != "" and "@" in email and email.endswith(".com")

print(is_valid_email("user@example.com"))
print(is_valid_email("user@domain.org"))
print(is_valid_email(""))