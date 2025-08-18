tea_varities = ["Black","Green", "Oolong","White"]
print(tea_varities)
print(tea_varities[1])
print(tea_varities[:2])
tea_varities[3] = "Herbal"
print(tea_varities)

tea_varities = ["Black","Green", "Oolong","White"]
tea_varities[1:2] = ["Lemon"]
print(tea_varities)

print(tea_varities[1:3])
tea_varities[1:3] = ["green", "Masala"]
print(tea_varities)


# print(tea_varities[1:1])

for tea in tea_varities:
    print(tea)

for tea in tea_varities:
    print(tea, end="-")


if "Oolong" in tea_varities:
    print("I have Ooling tea")

tea_varities.append("Oolong")
print(tea_varities)

if "Oolong" in tea_varities:
    print("I have Ooling tea")

tea_varities.pop()
print(tea_varities)

tea_varities.remove("green")
print(tea_varities)

tea_varities.insert(1, "green")
print(tea_varities)

tea_varities_copy = tea_varities.copy()

tea_varities_copy.append("Lemon")
print(tea_varities_copy)

squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_num = [y**3 for y in range (5)]
print(cube_num)

