tea_types = ("Black", "Green","Oolong")
print(tea_types)

print(len(tea_types))

more_tea = ("Herbal","Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have green tea")

more_tea = ("Herbal","Earl Grey","Herbal")
print(more_tea.count("Herbal")) 

print(type(tea_types))