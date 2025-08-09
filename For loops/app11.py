#Pass
names = ['john', 'maria', '', 'Kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        pass
    print(f'Name = {name}')