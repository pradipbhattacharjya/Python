score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

grade = "A" if score >= 90 else "F"
print(grade)

grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)

