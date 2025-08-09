# continue 
names = ['john', 'maria', '', 'Kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        continue
    print(f'Name = {name}')