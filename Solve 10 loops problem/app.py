#1>Counting Positive Numbers
#Given a list of numbers, count how many are positive.

numbers = [1, -2,-3,-5, 6, -7,-8,-9,18]
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1
    print("Final count of pOSitive number: ", positive_number_count)
    
 