#8> Password Strength Checker
#Check if a password is "Weak","Medium",or "Strong".Criteria: <6 chars(Weak),6-10 chars(Medium),>10chars(strong).
password = "Secure3P@ss"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password stength is : ", strength)