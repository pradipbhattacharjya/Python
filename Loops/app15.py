#nested if
score = 95
Submitted_project = True
if score >= 90:
    if Submitted_project:
        print("A+")
    else:
     print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")