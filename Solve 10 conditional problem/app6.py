#6>Transportation Mode Selection
#Choose a mode of transportation based on the distance(e.g..<3Km:Walk,3-15km:Bike,>15 km: Car).

distance = int(input("Enter your kilomiter :"))

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"
print("AI recommends you the transport of: ",transport)