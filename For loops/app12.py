#Break vs Continue Real-World Applications

#Loop through a list of days and print only the working days, skipping the weekends

days = ['Mon', 'Sun', 'Wed', 'Tue']
weekends = ['Sat', 'Sun']
for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')