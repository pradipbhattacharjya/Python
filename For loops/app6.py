#Clean first,transform second - always in that order
files = [' Report.csv','DATA.csv', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt','.csv')
    print(f"Processing {file}")