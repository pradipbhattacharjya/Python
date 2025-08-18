chai = "Masala Chai"
first_char = chai[0]
print(first_char)

slice_chai = chai[0:6]
print(slice_chai)

num_list = "0123456789"

print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[:])

print(chai.lower())

chai = "Lemon Chai"
print(chai.replace("Lemon","Ginger"))

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", "))

chai = "Masala Chai"
print(chai.find('Chai'))

chai = "Masala Chai chai chai"  
print(chai.count('Chai'))

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity,chai_type))

chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety)
print(" ".join(chai_variety))

chai ="Masala Chai"
print(len(chai))

for letter in chai:
    print(letter)


chai = "He Said,\"Masala chai is awesome\""
print(chai)

chai = r"c:\\user\\pwd"
print(chai)
print(chai)

chai = "Masala Chai"
print(chai)
print("Masala" in chai)
print("Masalaa" in chai)