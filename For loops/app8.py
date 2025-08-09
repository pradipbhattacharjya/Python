#2-challenge
#print a left-aligned pyramid of stars with 6 rows using a for loop
rows = 6
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()