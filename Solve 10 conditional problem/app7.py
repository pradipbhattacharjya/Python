#7> Coffee Customization
#Customize a coffee order:"Small",or "Large" With an option for "Extra shot" of espresso.

Order_size = "Medium"
extra_shot = True

if extra_shot:
    coffee = Order_size + " coffee with an extra shot"
else:
    coffee = Order_size + " coffee"

print("Order: ",coffee)