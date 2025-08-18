chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)

print(chai_types["Masala"])

print(chai_types.get("Ginger"))

chai_types["Ginger"] = "Fresh"
print(chai_types)

for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai,chai_types[chai])

for key, value in chai_types.items():
    print(key,value)


if "Masala" in chai_types:
    print("I have masala chai")


print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"
print(chai_types)

chai_types.pop("Ginger")
print(chai_types)

chai_types.popitem()
print(chai_types)

del chai_types["Green"]
print(chai_types)

chai_types_copy = chai_types.copy()


tea_shop = {
    "chai": {"Masala":"spicy", "Ginger": "zesty"},
    "Tea" : {"Green": "Mild", "Black": "Strong"}
}

print(tea_shop)

print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])


squared_num = {x:x**2 for x in range(6)}
print(squared_num)

squared_num.clear()
print(squared_num)

key = ["Masala","Ginger","Lemon"]
print(key)

default_value = "Delicious"
print(default_value)

new_dict = dict.fromkeys(key,default_value)