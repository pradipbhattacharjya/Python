# using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print({key:value*0.62 for (key,value) in distances.items()})